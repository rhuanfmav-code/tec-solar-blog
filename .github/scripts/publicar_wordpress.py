"""
TEC Solar — Publicador Automático WordPress
Versão 1.0 — API REST + Yoast SEO + Imagens WebP

Lê post-XX.md do repositório e publica tudo automaticamente:
- Upload de imagens (WebP, <150KB, alt text, legenda)
- Título, slug, conteúdo, categoria, tags
- Imagem destaque
- Yoast SEO (palavra-chave, título SEO, meta description)
- Links internos e externos no conteúdo
"""

import os
import sys
import re
import json
import requests
from pathlib import Path
from io import BytesIO

try:
    from PIL import Image
    PIL_OK = True
except ImportError:
    PIL_OK = False

# ============================================================
# CONFIGURAÇÃO — via secrets do GitHub Actions
# ============================================================

WP_URL      = os.environ.get("WP_URL", "https://blogtecsolar.com.br")
WP_USER     = os.environ.get("WP_USER", "")
WP_PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

API_BASE = f"{WP_URL.rstrip('/')}/wp-json/wp/v2"
AUTH     = (WP_USER, WP_PASSWORD)

# ============================================================
# PARSER DO POST .md
# ============================================================

def extrair_secao(conteudo, marcador_inicio, marcador_fim=None):
    """Extrai o texto entre dois marcadores ## [...]"""
    pattern = rf"##\s*\[{re.escape(marcador_inicio)}\]\s*\n(.*?)\n(?=##|\Z)"
    match = re.search(pattern, conteudo, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def parsear_post(caminho_arquivo):
    """Lê o arquivo .md e extrai todos os campos."""
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

    # Título do post (primeira linha H1)
    match_h1 = re.search(r"^#\s+(.+)$", conteudo, re.MULTILINE)
    dados["titulo"] = match_h1.group(1).strip() if match_h1 else dados["titulo_seo"]

    return dados

def extrair_dados_imagem(conteudo, tipo):
    """Extrai URL, nome, alt text e legenda de uma seção de imagem."""
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
# IMAGENS — Download, conversão WebP, upload WordPress
# ============================================================

def baixar_e_converter_webp(url, nome_arquivo, max_kb=150):
    """Baixa imagem, converte para WebP, reduz até <150KB."""
    print(f"   Baixando imagem: {url}")
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, timeout=30, headers=headers)
    resp.raise_for_status()

    if not PIL_OK:
        print("   AVISO: Pillow não disponível. Usando imagem original.")
        return resp.content, nome_arquivo.replace(".webp", ".jpg"), "image/jpeg"

    img = Image.open(BytesIO(resp.content)).convert("RGB")

    # Redimensiona se muito grande
    max_dim = 1200
    if img.width > max_dim or img.height > max_dim:
        img.thumbnail((max_dim, max_dim), Image.LANCZOS)

    # Converte para WebP com qualidade ajustada até ficar < max_kb
    qualidade = 85
    while qualidade >= 40:
        buffer = BytesIO()
        img.save(buffer, format="WEBP", quality=qualidade, method=6)
        tamanho_kb = buffer.tell() / 1024
        if tamanho_kb <= max_kb:
            break
        qualidade -= 10

    print(f"   Imagem convertida: {tamanho_kb:.0f}KB (qualidade {qualidade})")
    return buffer.getvalue(), nome_arquivo, "image/webp"

def fazer_upload_imagem(dados_imagem, alt_text, legenda, titulo_post):
    """Faz upload da imagem para a biblioteca do WordPress."""
    conteudo, nome_arquivo, mime_type = baixar_e_converter_webp(
        dados_imagem["url"],
        dados_imagem.get("nome", "imagem-tec-solar.webp")
    )

    headers = {
        "Content-Disposition": f'attachment; filename="{nome_arquivo}"',
        "Content-Type": mime_type,
    }

    resp = requests.post(
        f"{API_BASE}/media",
        auth=AUTH,
        headers=headers,
        data=conteudo
    )
    resp.raise_for_status()
    media = resp.json()
    media_id = media["id"]

    # Atualiza alt text, legenda e título
    requests.post(
        f"{API_BASE}/media/{media_id}",
        auth=AUTH,
        json={
            "alt_text":    alt_text[:125],
            "caption":     legenda,
            "title":       titulo_post,
            "description": alt_text,
        }
    )

    print(f"   Upload OK: ID {media_id} — {nome_arquivo}")
    return media_id, media.get("source_url", "")

# ============================================================
# CATEGORIAS E TAGS
# ============================================================

def obter_ou_criar_categoria(nome):
    # Categoria fixa — Inversores Solares (ID 52)
    return 52
def obter_ou_criar_tags(tags_str):
    """Retorna lista de IDs de tags, criando as que não existem."""
    tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    ids = []
    for tag in tags:
        resp = requests.get(f"{API_BASE}/tags", auth=AUTH, params={"search": tag})
        existentes = resp.json()
        encontrado = False
        for t in existentes:
            if t["name"].lower() == tag.lower():
                ids.append(t["id"])
                encontrado = True
                break
        if not encontrado:
            resp = requests.post(f"{API_BASE}/tags", auth=AUTH, json={"name": tag})
            if resp.status_code in [200, 201]:
                ids.append(resp.json()["id"])
    return ids

# ============================================================
# CONTEÚDO — Processar links e inserir imagem secundária
# ============================================================

def processar_links(conteudo, links_internos_str, links_externos_str):
    """Insere links internos e externos no conteúdo."""

    # Links externos — âncora → URL
    for linha in links_externos_str.split("\n"):
        match = re.search(r'[Tt]exto â[n]?cora:\s*["\'](.+?)["\'].*?→.*?Fonte:.*?(https?://\S+)', linha)
        if not match:
            match = re.search(r'[Tt]exto â[n]?cora:\s*"(.+?)".*?→.*?(https?://\S+)', linha)
        if match:
            ancora, url = match.group(1), match.group(2).rstrip(")")
            link_html = f'<a href="{url}" target="_blank" rel="noopener noreferrer">{ancora}</a>'
            conteudo = conteudo.replace(ancora, link_html, 1)

    # Links internos — âncora → placeholder (URL será preenchida depois)
    for linha in links_internos_str.split("\n"):
        match = re.search(r'[Â]ncora:\s*["\'](.+?)["\']', linha)
        if match:
            ancora = match.group(1)
            # Cria link com placeholder — será atualizado quando post de destino existir
            link_html = f'<a href="#" title="Link interno — atualizar quando post for publicado">{ancora}</a>'
            conteudo = conteudo.replace(ancora, link_html, 1)

    return conteudo

def converter_markdown_para_html(texto):
    """Conversão básica de Markdown para HTML (sem dependências externas)."""
    linhas = texto.split("\n")
    html_linhas = []
    em_paragrafo = False
    em_lista = False

    for linha in linhas:
        linha_stripped = linha.strip()

        if not linha_stripped:
            if em_paragrafo:
                html_linhas.append("</p>")
                em_paragrafo = False
            if em_lista:
                html_linhas.append("</ul>")
                em_lista = False
            continue

        # Headings
        if linha_stripped.startswith("### "):
            if em_paragrafo: html_linhas.append("</p>"); em_paragrafo = False
            html_linhas.append(f"<h3>{linha_stripped[4:]}</h3>")
        elif linha_stripped.startswith("## "):
            if em_paragrafo: html_linhas.append("</p>"); em_paragrafo = False
            html_linhas.append(f"<h2>{linha_stripped[3:]}</h2>")
        elif linha_stripped.startswith("# "):
            if em_paragrafo: html_linhas.append("</p>"); em_paragrafo = False
            html_linhas.append(f"<h1>{linha_stripped[2:]}</h1>")

        # Lista
        elif linha_stripped.startswith("- ") or linha_stripped.startswith("* "):
            if em_paragrafo: html_linhas.append("</p>"); em_paragrafo = False
            if not em_lista:
                html_linhas.append("<ul>")
                em_lista = True
            item = linha_stripped[2:]
            item = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item)
            html_linhas.append(f"<li>{item}</li>")

        # Numerada
        elif re.match(r'^\d+\.\s', linha_stripped):
            if em_paragrafo: html_linhas.append("</p>"); em_paragrafo = False
            if not em_lista:
                html_linhas.append("<ol>")
                em_lista = True
            item = re.sub(r'^\d+\.\s', '', linha_stripped)
            item = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', item)
            html_linhas.append(f"<li>{item}</li>")

        # Blockquote
        elif linha_stripped.startswith("> "):
            if em_paragrafo: html_linhas.append("</p>"); em_paragrafo = False
            texto_bq = linha_stripped[2:]
            texto_bq = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', texto_bq)
            html_linhas.append(f"<blockquote><p>{texto_bq}</p></blockquote>")

        # Parágrafo normal
        else:
            if em_lista:
                tag_fecha = "</ul>" if any("<ul>" in l for l in html_linhas[-10:]) else "</ol>"
                html_linhas.append(tag_fecha)
                em_lista = False
            if not em_paragrafo:
                html_linhas.append("<p>")
                em_paragrafo = True
            else:
                html_linhas.append(" ")
            # Inline formatting
            linha_fmt = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', linha_stripped)
            linha_fmt = re.sub(r'\*(.+?)\*', r'<em>\1</em>', linha_fmt)
            linha_fmt = re.sub(r'\[(.+?)\]\((https?://[^\)]+)\)', r'<a href="\2">\1</a>', linha_fmt)
            html_linhas.append(linha_fmt)

    if em_paragrafo:
        html_linhas.append("</p>")
    if em_lista:
        html_linhas.append("</ul>")

    return "\n".join(html_linhas)

def inserir_imagem_no_conteudo(conteudo_html, url_imagem, alt_text, legenda, marcador_h2):
    """Insere imagem secundária após o H2 indicado."""
    img_html = f'''
<figure class="wp-block-image size-large">
  <img src="{url_imagem}" alt="{alt_text}" />
  <figcaption>{legenda}</figcaption>
</figure>
'''
    # Tenta inserir após o H2 indicado
    padrao = rf'(<h2>{re.escape(marcador_h2)}.*?</h2>)'
    match = re.search(padrao, conteudo_html, re.IGNORECASE)
    if match:
        pos = match.end()
        return conteudo_html[:pos] + img_html + conteudo_html[pos:]

    # Fallback: insere no meio do conteúdo
    meio = len(conteudo_html) // 2
    return conteudo_html[:meio] + img_html + conteudo_html[meio:]

# ============================================================
# YOAST SEO
# ============================================================

def configurar_yoast(post_id, palavra_chave, titulo_seo, meta_description):
    """Configura campos do Yoast SEO via meta fields."""
    meta = {
        "_yoast_wpseo_focuskw":         palavra_chave,
        "_yoast_wpseo_title":           titulo_seo,
        "_yoast_wpseo_metadesc":        meta_description,
        "_yoast_wpseo_meta-robots-noindex": "0",
        "_yoast_wpseo_meta-robots-nofollow": "0",
    }

    resp = requests.post(
        f"{API_BASE}/posts/{post_id}",
        auth=AUTH,
        json={"meta": meta}
    )

    if resp.status_code in [200, 201]:
        print(f"   Yoast SEO configurado ✅")
    else:
        print(f"   AVISO Yoast: {resp.status_code} — tentando método alternativo")
        # Método alternativo via campos diretos
        for chave, valor in meta.items():
            requests.post(
                f"{WP_URL.rstrip('/')}/wp-json/yoast/v1/meta",
                auth=AUTH,
                json={"post_id": post_id, "key": chave, "value": valor}
            )

# ============================================================
# PUBLICAÇÃO PRINCIPAL
# ============================================================

def publicar_post(caminho_arquivo):
    print(f"\n🚀 Publicando: {caminho_arquivo}")
    print(f"   WordPress: {WP_URL}")

    # 1. Parsear o arquivo
    dados = parsear_post(caminho_arquivo)
    print(f"   Título: {dados['titulo']}")
    print(f"   Slug: {dados['slug']}")

    # 2. Upload imagem principal
    id_imagem_principal = None
    url_imagem_principal = ""
    if dados["imagem_principal"]:
        print("\n📷 Imagem principal...")
        try:
            id_imagem_principal, url_imagem_principal = fazer_upload_imagem(
                dados["imagem_principal"],
                dados["imagem_principal"].get("alt", ""),
                dados["imagem_principal"].get("legenda", ""),
                dados["titulo"]
            )
        except Exception as e:
            print(f"   AVISO: Falha no upload da imagem principal — {e}")

    # 3. Upload imagem secundária
    url_imagem_secundaria = ""
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
            print(f"   AVISO: Falha no upload da imagem secundária — {e}")

    # 4. Converter conteúdo Markdown → HTML
    print("\n📝 Processando conteúdo...")
    conteudo_html = converter_markdown_para_html(dados["conteudo"])

    # 5. Inserir imagem secundária no conteúdo
    if url_imagem_secundaria and dados["imagem_secundaria"]:
        posicao = dados["imagem_secundaria"].get("posicao", "")
        # Extrai o H2 de referência da instrução "Após H2"
        match_h2 = re.search(r'[Aa]pós\s+H2\s+["\'](.+?)["\']', posicao)
        marcador = match_h2.group(1) if match_h2 else "Como identificar na prática"
        conteudo_html = inserir_imagem_no_conteudo(
            conteudo_html,
            url_imagem_secundaria,
            dados["imagem_secundaria"].get("alt", ""),
            dados["imagem_secundaria"].get("legenda", ""),
            marcador
        )

    # 6. Processar links
    conteudo_html = processar_links(
        conteudo_html,
        dados["links_internos"],
        dados["links_externos"]
    )

    # 7. Obter IDs de categoria e tags
    print("\n🏷 Categorias e tags...")
    categoria_id = obter_ou_criar_categoria(dados["categoria"]) if dados["categoria"] else None
    tag_ids = obter_ou_criar_tags(dados["tags"]) if dados["tags"] else []
    print(f"   Categoria ID: {categoria_id}")
    print(f"   Tags IDs: {tag_ids}")

    # 8. Criar o post
    print("\n📤 Criando post no WordPress...")
    payload = {
        "title":   dados["titulo"],
        "slug":    dados["slug"],
        "content": conteudo_html,
        "status":  "publish",
        "meta": {
            "_yoast_wpseo_focuskw":  dados["palavra_chave"],
            "_yoast_wpseo_title":    dados["titulo_seo"],
            "_yoast_wpseo_metadesc": dados["meta_description"],
        }
    }

    if categoria_id:
        payload["categories"] = [categoria_id]
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

    # 9. Configurar Yoast SEO (segunda passagem para garantir)
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
        # Detecta automaticamente o post mais recente
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
