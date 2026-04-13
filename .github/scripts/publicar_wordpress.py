"""
TEC Solar — Publicador Automático WordPress
Versão 1.1 — Corrigido categoria + upload imagem
"""

import os
import sys
import re
import requests
from pathlib import Path
from io import BytesIO

try:
    from PIL import Image
    PIL_OK = True
except ImportError:
    PIL_OK = False

WP_URL      = os.environ.get("WP_URL", "https://blogtecsolar.com.br")
WP_USER     = os.environ.get("WP_USER", "")
WP_PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

API_BASE = f"{WP_URL.rstrip('/')}/wp-json/wp/v2"
AUTH     = (WP_USER, WP_PASSWORD)

# ============================================================
# PARSER
# ============================================================

def extrair_secao(conteudo, marcador):
    pattern = rf"##\s*\[{re.escape(marcador)}\]\s*\n(.*?)\n(?=##|\Z)"
    match = re.search(pattern, conteudo, re.DOTALL)
    return match.group(1).strip() if match else ""

def parsear_post(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    dados = {
        "palavra_chave":     extrair_secao(conteudo, "PALAVRA-CHAVE FOCO"),
        "titulo_seo":        extrair_secao(conteudo, "TÍTULO SEO — Title Tag"),
        "slug":              extrair_secao(conteudo, "SLUG — URL do Post"),
        "meta_description":  extrair_secao(conteudo, "META DESCRIPTION"),
        "categoria":         extrair_secao(conteudo, "CATEGORIA"),
        "tags":              extrair_secao(conteudo, "TAGS"),
        "conteudo":          extrair_secao(conteudo, "TEXTO DO POST — VERSÃO HUMANIZADA FINAL"),
        "links_internos":    extrair_secao(conteudo, "LINKS INTERNOS SUGERIDOS"),
        "links_externos":    extrair_secao(conteudo, "LINKS EXTERNOS SUGERIDOS"),
        "imagem_principal":  extrair_dados_imagem(conteudo, "IMAGEM PRINCIPAL"),
        "imagem_secundaria": extrair_dados_imagem(conteudo, "IMAGEM SECUNDÁRIA"),
    }

    match_h1 = re.search(r"^#\s+(.+)$", conteudo, re.MULTILINE)
    dados["titulo"] = match_h1.group(1).strip() if match_h1 else dados["titulo_seo"]
    return dados

def extrair_dados_imagem(conteudo, tipo):
    secao = extrair_secao(conteudo, tipo + " — USE ESTA") or extrair_secao(conteudo, tipo + " — USE NO MEIO DO POST")
    if not secao:
        return None
    dados = {}
    for linha in secao.split("\n"):
        linha = linha.strip().lstrip("→").strip()
        if linha.startswith("URL para download:"):
            dados["url"] = linha.split(":", 1)[1].strip()
        elif linha.startswith("Nome do arquivo:"):
            dados["nome"] = linha.split(":", 1)[1].strip()
        elif linha.startswith("Alt Text"):
            dados["alt"] = re.sub(r"\(.*?\)", "", linha.split(":", 1)[1]).strip()
        elif linha.startswith("Legenda:"):
            dados["legenda"] = linha.split(":", 1)[1].strip()
        elif linha.startswith("Onde inserir:"):
            dados["posicao"] = linha.split(":", 1)[1].strip()
    return dados if "url" in dados else None

# ============================================================
# IMAGENS
# ============================================================

def baixar_e_converter_jpeg(url, nome_arquivo, max_kb=150):
    """Baixa imagem e converte para JPEG (mais compatível que WebP)."""
    print(f"   Baixando imagem: {url}")
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, timeout=30, headers=headers)
    resp.raise_for_status()

    if not PIL_OK:
        nome_jpg = nome_arquivo.replace(".webp", ".jpg")
        return resp.content, nome_jpg, "image/jpeg"

    img = Image.open(BytesIO(resp.content)).convert("RGB")
    if img.width > 1200 or img.height > 1200:
        img.thumbnail((1200, 1200), Image.LANCZOS)

    qualidade = 85
    while qualidade >= 40:
        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=qualidade, optimize=True)
        if buffer.tell() / 1024 <= max_kb:
            break
        qualidade -= 10

    nome_jpg = nome_arquivo.replace(".webp", ".jpg").replace(".png", ".jpg")
    if not nome_jpg.endswith(".jpg"):
        nome_jpg += ".jpg"

    print(f"   Convertida: {buffer.tell()//1024}KB (qualidade {qualidade})")
    return buffer.getvalue(), nome_jpg, "image/jpeg"

def fazer_upload_imagem(dados_imagem, alt_text, legenda, titulo_post):
    conteudo, nome_arquivo, mime_type = baixar_e_converter_jpeg(
        dados_imagem["url"],
        dados_imagem.get("nome", "imagem-tec-solar.jpg")
    )

    resp = requests.post(
        f"{API_BASE}/media",
        auth=AUTH,
        headers={
            "Content-Disposition": f'attachment; filename="{nome_arquivo}"',
            "Content-Type": mime_type,
        },
        data=conteudo
    )
    resp.raise_for_status()
    media = resp.json()
    media_id = media["id"]

    requests.post(f"{API_BASE}/media/{media_id}", auth=AUTH, json={
        "alt_text":    alt_text[:125],
        "caption":     legenda,
        "title":       titulo_post,
        "description": alt_text,
    })

    print(f"   Upload OK: ID {media_id} — {nome_arquivo}")
    return media_id, media.get("source_url", "")

# ============================================================
# CATEGORIA — fixa Inversores Solares (ID 52)
# ============================================================

def obter_categoria():
    return 52

# ============================================================
# TAGS
# ============================================================

def obter_ou_criar_tags(tags_str):
    tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    ids = []
    for tag in tags:
        try:
            resp = requests.get(f"{API_BASE}/tags", auth=AUTH, params={"search": tag})
            if resp.status_code == 200 and resp.text.strip():
                existentes = resp.json()
                encontrado = False
                for t in existentes:
                    if t["name"].lower() == tag.lower():
                        ids.append(t["id"])
                        encontrado = True
                        break
                if not encontrado:
                    resp2 = requests.post(f"{API_BASE}/tags", auth=AUTH, json={"name": tag})
                    if resp2.status_code in [200, 201] and resp2.text.strip():
                        ids.append(resp2.json()["id"])
        except Exception as e:
            print(f"   AVISO tag '{tag}': {e}")
    return ids

# ============================================================
# CONTEÚDO
# ============================================================

def processar_links(conteudo, links_internos_str, links_externos_str):
    for linha in links_externos_str.split("\n"):
        match = re.search(r'[Tt]exto\s+â[n]?cora:\s*["\'](.+?)["\'].*?(https?://\S+)', linha)
        if match:
            ancora, url = match.group(1), match.group(2).rstrip(")")
            conteudo = conteudo.replace(ancora, f'<a href="{url}" target="_blank" rel="noopener noreferrer">{ancora}</a>', 1)
    for linha in links_internos_str.split("\n"):
        match = re.search(r'[Â]ncora:\s*["\'](.+?)["\']', linha)
        if match:
            ancora = match.group(1)
            conteudo = conteudo.replace(ancora, f'<a href="#" title="Link interno pendente">{ancora}</a>', 1)
    return conteudo

def converter_markdown_para_html(texto):
    linhas = texto.split("\n")
    html = []
    em_p = False
    em_ul = False
    em_ol = False

    def fechar_p():
        nonlocal em_p
        if em_p:
            html.append("</p>")
            em_p = False

    def fechar_lista():
        nonlocal em_ul, em_ol
        if em_ul:
            html.append("</ul>")
            em_ul = False
        if em_ol:
            html.append("</ol>")
            em_ol = False

    def formatar(t):
        t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
        t = re.sub(r'\[(.+?)\]\((https?://[^\)]+)\)', r'<a href="\2">\1</a>', t)
        return t

    for linha in linhas:
        s = linha.strip()
        if not s:
            fechar_p()
            fechar_lista()
            continue
        if s.startswith("### "):
            fechar_p(); fechar_lista()
            html.append(f"<h3>{formatar(s[4:])}</h3>")
        elif s.startswith("## "):
            fechar_p(); fechar_lista()
            html.append(f"<h2>{formatar(s[3:])}</h2>")
        elif s.startswith("# "):
            fechar_p(); fechar_lista()
            html.append(f"<h1>{formatar(s[2:])}</h1>")
        elif s.startswith("> "):
            fechar_p(); fechar_lista()
            html.append(f"<blockquote><p>{formatar(s[2:])}</p></blockquote>")
        elif s.startswith("- ") or s.startswith("* "):
            fechar_p()
            if not em_ul:
                fechar_lista()
                html.append("<ul>")
                em_ul = True
            html.append(f"<li>{formatar(s[2:])}</li>")
        elif re.match(r'^\d+\.\s', s):
            fechar_p()
            if not em_ol:
                fechar_lista()
                html.append("<ol>")
                em_ol = True
            item_ol = re.sub(r'^\d+\.\s', '', s)
            html.append(f"<li>{formatar(item_ol)}</li>")
        else:
            fechar_lista()
            if not em_p:
                html.append("<p>")
                em_p = True
            else:
                html.append(" ")
            html.append(formatar(s))

    fechar_p()
    fechar_lista()
    return "\n".join(html)

def inserir_imagem_no_conteudo(conteudo_html, url_imagem, alt_text, legenda, marcador_h2):
    img_html = f'\n<figure class="wp-block-image size-large"><img src="{url_imagem}" alt="{alt_text}" /><figcaption>{legenda}</figcaption></figure>\n'
    match = re.search(rf'(<h2>{re.escape(marcador_h2)}.*?</h2>)', conteudo_html, re.IGNORECASE)
    if match:
        pos = match.end()
        return conteudo_html[:pos] + img_html + conteudo_html[pos:]
    meio = len(conteudo_html) // 2
    return conteudo_html[:meio] + img_html + conteudo_html[meio:]

# ============================================================
# YOAST SEO
# ============================================================

def configurar_yoast(post_id, palavra_chave, titulo_seo, meta_description):
    resp = requests.post(f"{API_BASE}/posts/{post_id}", auth=AUTH, json={"meta": {
        "_yoast_wpseo_focuskw":  palavra_chave,
        "_yoast_wpseo_title":    titulo_seo,
        "_yoast_wpseo_metadesc": meta_description,
    }})
    if resp.status_code in [200, 201]:
        print("   Yoast SEO configurado ✅")
    else:
        print(f"   AVISO Yoast: {resp.status_code}")

# ============================================================
# PUBLICAÇÃO PRINCIPAL
# ============================================================

def publicar_post(caminho_arquivo):
    print(f"\n🚀 Publicando: {caminho_arquivo}")
    dados = parsear_post(caminho_arquivo)
    print(f"   Título: {dados['titulo']}")
    print(f"   Slug: {dados['slug']}")

    # Upload imagens
    id_imagem_principal = None
    url_imagem_secundaria = ""

    if dados["imagem_principal"]:
        print("\n📷 Imagem principal...")
        try:
            id_imagem_principal, _ = fazer_upload_imagem(
                dados["imagem_principal"],
                dados["imagem_principal"].get("alt", ""),
                dados["imagem_principal"].get("legenda", ""),
                dados["titulo"]
            )
        except Exception as e:
            print(f"   AVISO imagem principal: {e}")

    if dados["imagem_secundaria"]:
        print("\n📷 Imagem secundária...")
        try:
            _, url_imagem_secundaria = fazer_upload_imagem(
                dados["imagem_secundaria"],
                dados["imagem_secundaria"].get("alt", ""),
                dados["imagem_secundaria"].get("legenda", ""),
                dados["titulo"]
            )
        except Exception as e:
            print(f"   AVISO imagem secundária: {e}")

    # Conteúdo
    print("\n📝 Processando conteúdo...")
    conteudo_html = converter_markdown_para_html(dados["conteudo"])

    if url_imagem_secundaria and dados["imagem_secundaria"]:
        posicao = dados["imagem_secundaria"].get("posicao", "")
        match_h2 = re.search(r'[Aa]pós\s+H2\s+["\'](.+?)["\']', posicao)
        marcador = match_h2.group(1) if match_h2 else "Como identificar na prática"
        conteudo_html = inserir_imagem_no_conteudo(conteudo_html, url_imagem_secundaria,
            dados["imagem_secundaria"].get("alt", ""), dados["imagem_secundaria"].get("legenda", ""), marcador)

    conteudo_html = processar_links(conteudo_html, dados["links_internos"], dados["links_externos"])

    # Categoria e tags
    print("\n🏷 Categorias e tags...")
    categoria_id = obter_categoria()
    tag_ids = obter_ou_criar_tags(dados["tags"]) if dados["tags"] else []
    print(f"   Categoria ID: {categoria_id}")
    print(f"   Tags IDs: {tag_ids}")

    # Criar post
    print("\n📤 Criando post no WordPress...")
    payload = {
        "title":      dados["titulo"],
        "slug":       dados["slug"],
        "content":    conteudo_html,
        "status":     "publish",
        "categories": [categoria_id],
        "meta": {
            "_yoast_wpseo_focuskw":  dados["palavra_chave"],
            "_yoast_wpseo_title":    dados["titulo_seo"],
            "_yoast_wpseo_metadesc": dados["meta_description"],
        }
    }
    if tag_ids:
        payload["tags"] = tag_ids
    if id_imagem_principal:
        payload["featured_media"] = id_imagem_principal

    resp = requests.post(f"{API_BASE}/posts", auth=AUTH, json=payload)
    if resp.status_code not in [200, 201]:
        print(f"❌ Erro ao criar post: {resp.status_code}")
        print(resp.text[:500])
        sys.exit(1)

    post = resp.json()
    post_id = post["id"]
    post_url = post.get("link", "")
    print(f"   Post criado: ID {post_id}")
    print(f"   URL: {post_url}")

    print("\n🔍 Configurando Yoast SEO...")
    configurar_yoast(post_id, dados["palavra_chave"], dados["titulo_seo"], dados["meta_description"])

    print(f"\n✅ Post publicado com sucesso!")
    print(f"   {post_url}")
    return post_id, post_url

# ============================================================
# ENTRADA
# ============================================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        posts = sorted(Path("posts").glob("post-*.md"))
        if not posts:
            print("❌ Nenhum arquivo post-XX.md encontrado em /posts/")
            sys.exit(1)
        caminho = str(posts[-1])
    else:
        caminho = sys.argv[1]

    if not os.path.exists(caminho):
        print(f"❌ Arquivo não encontrado: {caminho}")
        sys.exit(1)

    publicar_post(caminho)
