"""
TEC Solar — Publicador Automático WordPress
Versão 1.3 — Unsplash API para imagens relevantes por contexto
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

WP_URL           = os.environ.get("WP_URL", "https://blogtecsolar.com.br")
WP_USER          = os.environ.get("WP_USER", "")
WP_PASSWORD      = os.environ.get("WP_APP_PASSWORD", "")
UNSPLASH_KEY     = os.environ.get("UNSPLASH_ACCESS_KEY", "")

API_BASE = f"{WP_URL.rstrip('/')}/wp-json/wp/v2"
AUTH     = (WP_USER, WP_PASSWORD)

# ============================================================
# QUERIES UNSPLASH POR CONTEXTO
# ============================================================

QUERIES_UNSPLASH = {
    "falha de isolamento":     "solar inverter electronics repair",
    "isolamento":              "solar inverter electronics repair",
    "tensão de rede":          "solar panel technician maintenance",
    "sobretensão":             "electrical engineer solar panel",
    "subtensão":               "solar energy technician",
    "placa de controle":       "electronics circuit board repair",
    "igbt":                    "power electronics circuit board",
    "capacitor":               "electronics components circuit board",
    "string":                  "solar panel installation rooftop",
    "fronius":                 "solar inverter technician repair",
    "growatt":                 "solar energy system maintenance",
    "deye":                    "solar inverter installation",
    "sma":                     "solar power inverter electronics",
    "sungrow":                 "solar energy technician equipment",
    "weg":                     "industrial solar inverter",
    "drive":                   "solar pump irrigation system",
    "bombeamento":             "solar pump water irrigation",
    "default":                 "solar inverter technician repair electronics",
}

def buscar_imagem_unsplash(titulo_post, palavra_chave):
    """Busca imagem relevante no Unsplash baseado no contexto do post."""
    if not UNSPLASH_KEY:
        return None

    texto = (titulo_post + " " + palavra_chave).lower()
    query = QUERIES_UNSPLASH["default"]
    for chave, q in QUERIES_UNSPLASH.items():
        if chave in texto:
            query = q
            break

    print(f"   Buscando Unsplash: '{query}'")
    resp = requests.get(
        "https://api.unsplash.com/search/photos",
        headers={"Authorization": f"Client-ID {UNSPLASH_KEY}"},
        params={
            "query": query,
            "per_page": 5,
            "orientation": "landscape",
            "content_filter": "high",
        },
        timeout=15
    )

    if resp.status_code != 200:
        print(f"   AVISO Unsplash: {resp.status_code}")
        return None

    resultados = resp.json().get("results", [])
    if not resultados:
        return None

    # Pega a primeira imagem de alta qualidade
    foto = resultados[0]
    url = foto["urls"]["regular"]  # 1080px largura
    print(f"   Imagem encontrada: {foto['alt_description'] or query}")
    return url

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
    }

    match_h1 = re.search(r"^#\s+(.+)$", conteudo, re.MULTILINE)
    dados["titulo"] = match_h1.group(1).strip() if match_h1 else dados["titulo_seo"]
    return dados

# ============================================================
# IMAGENS
# ============================================================

def fazer_upload_imagem(url_imagem, alt_text, legenda, titulo_post):
    """Baixa imagem da URL, converte para JPEG e faz upload no WordPress."""
    print(f"   Baixando: {url_imagem}")
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url_imagem, timeout=30, headers=headers)
    resp.raise_for_status()

    nome_arquivo = "tec-solar-post.jpg"
    mime_type = "image/jpeg"

    if PIL_OK:
        img = Image.open(BytesIO(resp.content)).convert("RGB")
        if img.width > 1200 or img.height > 1200:
            img.thumbnail((1200, 1200), Image.LANCZOS)
        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=85, optimize=True)
        conteudo = buffer.getvalue()
        print(f"   Convertida: {len(conteudo)//1024}KB")
    else:
        conteudo = resp.content

    resp_up = requests.post(
        f"{API_BASE}/media",
        auth=AUTH,
        headers={
            "Content-Disposition": f'attachment; filename="{nome_arquivo}"',
            "Content-Type": mime_type,
        },
        data=conteudo
    )
    resp_up.raise_for_status()
    media = resp_up.json()
    media_id = media["id"]

    requests.post(f"{API_BASE}/media/{media_id}", auth=AUTH, json={
        "alt_text":    alt_text[:125],
        "caption":     legenda,
        "title":       titulo_post,
        "description": alt_text,
    })

    print(f"   Upload OK: ID {media_id}")
    return media_id, media.get("source_url", "")

# ============================================================
# CATEGORIA E TAGS
# ============================================================

def obter_categoria():
    return 52

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
            fechar_p(); fechar_lista(); continue
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
                fechar_lista(); html.append("<ul>"); em_ul = True
            html.append(f"<li>{formatar(s[2:])}</li>")
        elif re.match(r'^\d+\.\s', s):
            fechar_p()
            if not em_ol:
                fechar_lista(); html.append("<ol>"); em_ol = True
            item = re.sub(r'^\d+\.\s', '', s)
            html.append(f"<li>{formatar(item)}</li>")
        else:
            fechar_lista()
            if not em_p:
                html.append("<p>"); em_p = True
            else:
                html.append(" ")
            html.append(formatar(s))

    fechar_p(); fechar_lista()
    return "\n".join(html)

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

    # Busca imagem relevante no Unsplash
    id_imagem = None
    print("\n📷 Buscando imagem...")
    url_img = buscar_imagem_unsplash(dados["titulo"], dados["palavra_chave"])

    if not url_img:
        # Fallback: imagem padrão do GitHub
        print("   Usando imagem padrão TEC Solar")
        url_img = "https://raw.githubusercontent.com/rhuanfmav-code/tec-solar-blog/main/fundo-bancada-tech.png.png"

    try:
        alt_text = f"Diagnóstico técnico de inversor solar — {dados['titulo']}"
        id_imagem, _ = fazer_upload_imagem(url_img, alt_text, dados["titulo"], dados["titulo"])
    except Exception as e:
        print(f"   AVISO imagem: {e}")

    # Conteúdo
    print("\n📝 Processando conteúdo...")
    conteudo_html = converter_markdown_para_html(dados["conteudo"])
    conteudo_html = processar_links(conteudo_html, dados["links_internos"], dados["links_externos"])

    # Categoria e tags
    print("\n🏷 Categorias e tags...")
    categoria_id = obter_categoria()
    tag_ids = obter_ou_criar_tags(dados["tags"]) if dados["tags"] else []
    print(f"   Categoria ID: {categoria_id} | Tags: {tag_ids}")

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
    if id_imagem:
        payload["featured_media"] = id_imagem

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
