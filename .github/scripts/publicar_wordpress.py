"""
TEC Solar — Publicador Automático WordPress
Versão 2.0 — Imagens locais por marca e tema (sem Unsplash)
"""

import os
import sys
import re
import json
import requests
from pathlib import Path

WP_URL           = os.environ.get("WP_URL", "https://blogtecsolar.com.br")
WP_USER          = os.environ.get("WP_USER", "")
WP_PASSWORD      = os.environ.get("WP_APP_PASSWORD", "")

API_BASE = f"{WP_URL.rstrip('/')}/wp-json/wp/v2"
AUTH     = (WP_USER, WP_PASSWORD)

# ============================================================
# CTA HTML — bloco fixo injetado ao final de todo post
# ============================================================

NEW_CTA_SENTINEL = "background:#25D366"  # exclusivo dos botões novos
OLD_CTA_MARKERS  = ["Condenaram seu inversor", "Antes de comprar equipamento novo"]

CTA_HTML = (
    "<hr>\n"
    "<h2>Envie seu inversor para diagnóstico</h2>\n"
    "<p>Antes de comprar equipamento novo, envie para a nossa bancada. "
    "A TEC Solar realiza diagnóstico eletrônico completo em nível de componente "
    "— abrimos o inversor, medimos a placa, identificamos a causa raiz e "
    "entregamos um laudo técnico detalhado.</p>\n"
    "<p>Se o reparo for viável, você recebe o equipamento funcionando por uma "
    "fração do custo de substituição. Se não for, o laudo serve de base para "
    "qualquer decisão.</p>\n"
    "<p>Atendemos todo o Brasil via logística reversa.</p>\n"
    '<div style="display:flex; flex-direction:column; gap:12px; margin-top:20px;">\n'
    "<a href=\"https://wa.me/5538998891587?text=Ol%C3%A1%2C%20vim%20pelo%20blog%20e%20quero%20enviar%20meu%20inversor%20para%20diagn%C3%B3stico\" "
    'target="_blank" style="background:#25D366; color:white; padding:14px 24px; '
    'border-radius:8px; text-decoration:none; font-weight:bold; text-align:center;">'
    "👉 Falar no WhatsApp agora</a>\n"
    "<a href=\"https://www.instagram.com/tec_solar_moc?igsh=MWl2djYzeXk2Zm51dQ%3D%3D&utm_source=qr\" "
    'target="_blank" style="background:#E1306C; color:white; padding:14px 24px; '
    'border-radius:8px; text-decoration:none; font-weight:bold; text-align:center;">'
    "📸 Seguir no Instagram</a>\n"
    "<a href=\"https://youtube.com/@tecsolar-reparodeinversores?si=kG3Njqipg8QRbZSD\" "
    'target="_blank" style="background:#FF0000; color:white; padding:14px 24px; '
    'border-radius:8px; text-decoration:none; font-weight:bold; text-align:center;">'
    "▶️ Ver vídeos no YouTube</a>\n"
    "</div>"
)


def injetar_cta(html):
    """Remove CTA antigo (qualquer variante) e insere o novo ao final.
    Detecta novo CTA pela presença exclusiva de background:#25D366.
    """
    if NEW_CTA_SENTINEL in html:
        return html

    idx_old = -1
    for marker in OLD_CTA_MARKERS:
        pos = html.find(marker)
        if pos != -1:
            idx_old = pos
            break

    if idx_old != -1:
        idx_hr = html.rfind("<hr>", 0, idx_old)
        html   = html[: idx_hr if idx_hr != -1 else idx_old].rstrip()

    return html + "\n" + CTA_HTML

# Pasta de imagens: três níveis acima do script (.github/scripts/ → raiz)
PASTA_IMAGENS = Path(__file__).resolve().parent.parent.parent / "imagens-padrao"

# ============================================================
# MAPAS DE IMAGENS
# ============================================================

# Imagem principal: selecionada pela marca do inversor
MAPA_PRINCIPAL = {
    "growatt":      ["Inversor-Growatt-Bancada.webp",
                     "Inversor-Growatt-Bancada (2).webp"],
    "fronius":      ["Inversor-Fronius-Bancada.webp",
                     "Inversor-Fronius-Bancada (2).webp",
                     "Inversor-Fronius-Bancada (3).webp"],
    "deye":         ["Inversor-Deye-Bancada.webp",
                     "Inversor-Deye-Bancada (2).webp",
                     "Inversor-Deye-Bancada (3).webp"],
    "sma":          ["Inversor-SMA-Bancada.webp",
                     "Inversor-SMA-Bancada (2).webp"],
    "sungrow":      ["Inversor-Sungrow-Bancada.webp"],
    "weg":          ["Inversor-WEG-Bancada.webp"],
    "canadian":     ["Inversor-Canadian-Bancada.webp",
                     "Inversor-Canadian-Bancada (2).webp"],
    "hoymiles":     ["Inversor-Hoymiles-Bancada.webp",
                     "Inversor-Hoymiles-Bancada (2).webp"],
    "huawei":       ["Inversor-Huawey-Bancada.webp"],
    "sofar":        ["Inversor-Sofar-Bancada.webp"],
    "drive":        ["Drive-Solar-Bancada.webp",
                     "Drive-Solar-Bancada (2).webp",
                     "Drive-Solar-Bancada (3).webp"],
    "bomba":        ["Drive-Solar-Bancada.webp",
                     "Drive-Solar-Bancada (2).webp",
                     "Drive-Solar-Bancada (3).webp"],
    "bombeamento":  ["Drive-Solar-Bancada.webp",
                     "Drive-Solar-Bancada (2).webp",
                     "Drive-Solar-Bancada (3).webp"],
    "default":      ["Multi-Inversores-Bancada.webp",
                     "Multi-Inversores-Bancada (2).webp",
                     "Multi-Inversores-Bancada (3).webp"],
}

# Imagem secundária: selecionada pelo tema do post
# Cada entrada: ([keywords], [arquivos disponíveis])
# Usa a primeira linha cuja keyword apareça no título/slug
MAPA_SECUNDARIA = [
    (
        ["isolamento", "aterramento", "fuga à terra", "leakage", "string leakage"],
        ["Inversor-Placa-Eletrônica-Bancada.webp"],
    ),
    (
        ["tensão cc", "mppt", "string", "sobretensão cc", "subtensão cc", "tensão alta", "tensão baixa"],
        ["Placa-Eletrônica-Bancada (2).webp",
         "Placa-Eletrônica-Bancada (3).webp"],
    ),
    (
        ["rede", "grid lost", "grid", "ca ", " ca ", "frequência", "ac lost", "perda de rede"],
        ["Inversor-Placa-Eletrônica-Bancada (2).webp"],
    ),
    (
        ["igbt", "capacitor", "driver", "componente", "mosfet", "transistor", "varistor"],
        ["Placa-Eletrônica-Bancada (4).webp",
         "Placa-Eletrônica-Bancada (5).webp",
         "Placa-Eletrônica-Bancada (6).webp",
         "Placa-Eletrônica-Bancada (7).webp",
         "Placa-Eletrônica-Bancada (8).webp"],
    ),
    (
        ["diagnóstico", "bancada", "processo", "reparo", "laudo", "checklist"],
        ["Inversor-Placa-Eletrônica-Bancada (3).webp"],
    ),
    (
        ["múltiplos", "comparativo", " vs ", "on-grid", "off-grid", "híbrido"],
        ["Multi-Inversores-Bancada (2).webp",
         "Multi-Inversores-Bancada (3).webp"],
    ),
]

DEFAULT_SECUNDARIA = [
    "Placa-Eletrônica-Bancada (2).webp",
    "Placa-Eletrônica-Bancada (3).webp",
]

# ============================================================
# SELEÇÃO DE IMAGENS
# ============================================================

def extrair_numero_post(caminho):
    """Extrai o número do post do nome do arquivo (posts/post-06.md → 6)."""
    match = re.search(r'post-0*(\d+)', str(caminho))
    return int(match.group(1)) if match else 1

def detectar_marca(titulo, slug):
    """Detecta a marca do inversor pelo título e slug."""
    texto = (titulo + " " + slug).lower()
    for marca in ["growatt", "fronius", "deye", "sma", "sungrow", "weg",
                   "canadian", "hoymiles", "huawei", "sofar",
                   "bombeamento", "bomba", "drive"]:
        if marca in texto:
            return marca
    return "default"

def rotacionar(lista, numero_post):
    """Seleciona item da lista por módulo do número do post."""
    return lista[numero_post % len(lista)]

def resolver_imagem_principal(titulo, slug, numero_post):
    """Retorna (caminho, alt_text, legenda) para a imagem principal."""
    marca = detectar_marca(titulo, slug)
    nome  = rotacionar(MAPA_PRINCIPAL[marca], numero_post)
    caminho = PASTA_IMAGENS / nome

    marca_display = marca.replace("default", "solar").upper()
    alt_text = (
        f"Inversor {marca_display} em bancada técnica para diagnóstico eletrônico — TEC Solar"
    )[:125]
    legenda = f"Fig. 1 — Inversor {marca_display} em diagnóstico na bancada da TEC Solar"

    return caminho, alt_text, legenda

def resolver_imagem_secundaria(titulo, slug, numero_post):
    """Retorna (caminho, alt_text, legenda) para a imagem secundária."""
    texto = (titulo + " " + slug).lower()
    nome  = None

    for keywords, opcoes in MAPA_SECUNDARIA:
        if any(k in texto for k in keywords):
            nome = rotacionar(opcoes, numero_post)
            break

    if not nome:
        nome = rotacionar(DEFAULT_SECUNDARIA, numero_post)

    caminho = PASTA_IMAGENS / nome
    alt_text = (
        f"Placa eletrônica de inversor solar em diagnóstico técnico na bancada da TEC Solar"
    )[:125]
    legenda = "Fig. 2 — Detalhe da placa eletrônica durante diagnóstico em nível de componente"

    return caminho, alt_text, legenda

# ============================================================
# UPLOAD DE IMAGEM LOCAL
# ============================================================

def _upload_bytes(conteudo, nome_arquivo, mime_type):
    """Envia bytes brutos para a API de mídia do WordPress. Retorna response."""
    return requests.post(
        f"{API_BASE}/media",
        auth=AUTH,
        headers={
            "Content-Disposition": f'attachment; filename="{nome_arquivo}"',
            "Content-Type":        mime_type,
            "Content-Length":      str(len(conteudo)),
        },
        data=conteudo,
    )

def fazer_upload_imagem_local(caminho, alt_text, legenda, titulo_post):
    """Lê imagem local WebP e faz upload no WordPress.
    Se o upload WebP falhar (ex.: MIME não permitido no servidor),
    converte automaticamente para JPEG via Pillow e tenta novamente.
    """
    from PIL import Image
    import io

    caminho = Path(caminho)
    if not caminho.exists():
        raise FileNotFoundError(f"Imagem não encontrada: {caminho}")

    conteudo = caminho.read_bytes()
    print(f"   Lendo: {caminho.name} ({len(conteudo) // 1024} KB)")

    # Nome seguro para Content-Disposition (sem parênteses, espaços ou acentos)
    nome_seguro = re.sub(r'[^\w\-.]', '-', caminho.stem) + caminho.suffix

    # --- Tentativa 1: WebP original ---
    resp_up = _upload_bytes(conteudo, nome_seguro, "image/webp")

    if not resp_up.ok:
        print(f"   Erro upload WebP: HTTP {resp_up.status_code}")
        print(f"   Detalhe: {resp_up.text[:400]}")
        # --- Tentativa 2: fallback JPEG via Pillow ---
        print("   Convertendo para JPEG e tentando novamente...")
        img = Image.open(caminho).convert("RGB")
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=88)
        buf.seek(0)
        nome_jpeg = re.sub(r'[^\w\-.]', '-', caminho.stem) + '.jpg'
        resp_up   = _upload_bytes(buf.getvalue(), nome_jpeg, "image/jpeg")

        if not resp_up.ok:
            print(f"   Erro upload JPEG: HTTP {resp_up.status_code}")
            print(f"   Detalhe: {resp_up.text[:400]}")
            resp_up.raise_for_status()

    media    = resp_up.json()
    media_id = media["id"]
    url      = media.get("source_url", "")

    # Atualizar metadados da mídia (alt text, legenda, título)
    resp_meta = requests.post(
        f"{API_BASE}/media/{media_id}",
        auth=AUTH,
        headers={"Content-Type": "application/json; charset=utf-8"},
        data=json.dumps({
            "alt_text":    alt_text[:125],
            "caption":     legenda,
            "title":       titulo_post,
            "description": alt_text,
        }, ensure_ascii=False).encode("utf-8"),
    )
    if not resp_meta.ok:
        print(f"   AVISO metadados mídia: HTTP {resp_meta.status_code}")

    print(f"   Upload OK: ID {media_id} — {url}")
    return media_id, url

# ============================================================
# INSERÇÃO DA IMAGEM SECUNDÁRIA NO CORPO HTML
# ============================================================

def inserir_imagem_secundaria_no_html(html, src_url, alt_text, legenda):
    """Insere <figure> após o 2º H2 (ou 1º se não houver 2º)."""
    figura = (
        f'\n<figure class="wp-block-image size-large aligncenter">'
        f'<img src="{src_url}" alt="{alt_text}" />'
        f'<figcaption>{legenda}</figcaption>'
        f'</figure>\n'
    )
    partes = html.split("</h2>")
    if len(partes) >= 3:
        partes[2] = figura + partes[2]   # após o 2º H2
    elif len(partes) >= 2:
        partes[1] = figura + partes[1]   # após o 1º H2 se só houver um
    return "</h2>".join(partes)

# ============================================================
# PARSER
# ============================================================

def extrair_secao(conteudo, marcador):
    # Usa "## [" como delimitador de fim para não cortar H2s internos do post
    pattern = rf"##\s*\[{re.escape(marcador)}\]\s*\n(.*?)\n(?=##\s*\[|\Z)"
    match = re.search(pattern, conteudo, re.DOTALL)
    return match.group(1).strip() if match else ""

def parsear_post(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    dados = {
        "palavra_chave":    extrair_secao(conteudo, "PALAVRA-CHAVE FOCO"),
        "titulo_seo":       extrair_secao(conteudo, "TÍTULO SEO — Title Tag"),
        "slug":             extrair_secao(conteudo, "SLUG — URL do Post"),
        "meta_description": extrair_secao(conteudo, "META DESCRIPTION"),
        "categoria":        extrair_secao(conteudo, "CATEGORIA"),
        "tags":             extrair_secao(conteudo, "TAGS"),
        "conteudo":         extrair_secao(conteudo, "TEXTO DO POST — VERSÃO HUMANIZADA FINAL"),
        "links_internos":   extrair_secao(conteudo, "LINKS INTERNOS SUGERIDOS"),
        "links_externos":   extrair_secao(conteudo, "LINKS EXTERNOS SUGERIDOS"),
    }

    match_h1 = re.search(r"^#\s+(.+)$", conteudo, re.MULTILINE)
    titulo_raw = match_h1.group(1).strip() if match_h1 else dados["titulo_seo"]
    # Remove prefixo "Post XX —", "Post XX -" ou "Post XX:"
    dados["titulo"] = re.sub(r'^Post\s+\d+\s*[—\-:]+\s*', '', titulo_raw).strip()
    return dados

# ============================================================
# CONTEÚDO
# ============================================================

def processar_links(conteudo, links_internos_str, links_externos_str):
    for linha in links_externos_str.split("\n"):
        match = re.search(r'[Tt]exto\s+â[n]?cora:\s*["\'](.+?)["\'].*?(https?://\S+)', linha)
        if match:
            ancora, url = match.group(1), match.group(2).rstrip(")")
            conteudo = conteudo.replace(
                ancora,
                f'<a href="{url}" target="_blank" rel="noopener noreferrer">{ancora}</a>',
                1,
            )
    # Links internos: NÃO inserir href se o post de destino ainda não existe
    # O texto corre normalmente sem âncora
    return conteudo

def renumerar_listas_ordenadas(texto):
    """Renumera itens de listas ordenadas sequencialmente dentro de cada seção.
    Reseta o contador apenas ao encontrar um heading (##) ou separador (---),
    garantindo que itens separados por linhas em branco ou texto de continuação
    mantenham numeração contínua em vez de reiniciar em 1.
    """
    linhas    = texto.split('\n')
    resultado = []
    contador  = 0

    for linha in linhas:
        s = linha.strip()
        if re.match(r'^\d+\.\s', s):
            contador += 1
            linha = re.sub(r'^\d+\.', f'{contador}.', linha, count=1)
        elif re.match(r'^#{1,6}\s', s) or re.match(r'^-{3,}$', s):
            contador = 0
        resultado.append(linha)

    return '\n'.join(resultado)


def corrigir_numeracao_ol(html):
    """Pós-processa o HTML para garantir numeração sequencial em listas
    ordenadas que foram fragmentadas em múltiplos <ol> pelo conversor
    (ocorre quando parágrafos de continuação separam os itens).

    Estratégia: tokeniza o HTML em marcadores relevantes e, sempre que
    um <ol> aparece após um </ol> anterior sem que um heading ou <hr>
    tenha redefinido a seção, adiciona start=N para continuar a contagem.
    """
    # Tokeniza preservando os delimitadores como grupos capturados
    partes = re.split(
        r'(<ol[^>]*>|</ol>|<h[1-6][^>]*>|<hr[^>]*>|<li[^>]*>)',
        html,
    )

    resultado = []
    li_count  = 0      # total de <li> emitidos na cadeia atual
    em_cadeia = False  # True após o primeiro <ol> da seção atual

    for parte in partes:
        if re.match(r'<ol', parte):
            if em_cadeia:
                # Continuação: injeta start= para prosseguir a contagem
                resultado.append(f'<ol start="{li_count + 1}">')
            else:
                resultado.append('<ol>')
                em_cadeia = True
        elif parte == '</ol>':
            resultado.append('</ol>')
            # Não reseta em_cadeia — próximo <ol> sem heading = continuação
        elif re.match(r'<h[1-6]', parte) or re.match(r'<hr', parte):
            # Quebra de seção: reseta tudo
            resultado.append(parte)
            li_count  = 0
            em_cadeia = False
        elif re.match(r'<li', parte):
            li_count += 1
            resultado.append(parte)
        else:
            resultado.append(parte)

    return ''.join(resultado)

def converter_markdown_para_html(texto):
    linhas = texto.split("\n")
    html   = []
    em_p   = False
    em_ul  = False
    em_ol  = False

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
        t = re.sub(r'\*(.+?)\*',     r'<em>\1</em>', t)
        t = re.sub(r'\[(.+?)\]\((https?://[^\)]+)\)', r'<a href="\2">\1</a>', t)
        return t

    for linha in linhas:
        s = linha.strip()
        if not s:
            fechar_p(); fechar_lista(); continue
        if re.match(r'^-{3,}$', s):
            fechar_p(); fechar_lista()
            html.append("<hr>")
        elif s.startswith("### "):
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
# HELPER — POST JSON COM ENCODING UTF-8 EXPLÍCITO
# ============================================================

def post_json(url, auth, payload, extra_headers=None):
    """Envia POST JSON com encoding UTF-8 explícito no payload."""
    headers = {"Content-Type": "application/json; charset=utf-8"}
    if extra_headers:
        headers.update(extra_headers)
    return requests.post(
        url,
        auth=auth,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=headers,
    )

# ============================================================
# CATEGORIA E TAGS
# ============================================================

def obter_categoria():
    return 52

def limpar_tag(tag):
    """Remove lixo de início e fim da tag: ---, —, –, hífens, espaços e símbolos."""
    tag = tag.strip()
    tag = re.sub(r'[\s\-—–_]+$', '', tag)   # limpeza do final
    tag = re.sub(r'^[\s\-—–_]+', '', tag)   # limpeza do início
    tag = re.sub(r'-{2,}', '-', tag)         # múltiplos hífens consecutivos → um só
    return tag.strip()

def obter_ou_criar_tags(tags_str):
    tags = [limpar_tag(t) for t in tags_str.split(",")]
    tags = [t for t in tags if t]
    ids  = []
    for tag in tags:
        try:
            resp = requests.get(f"{API_BASE}/tags", auth=AUTH, params={"search": tag})
            if resp.status_code == 200 and resp.text.strip():
                existentes  = resp.json()
                encontrado  = False
                for t in existentes:
                    if t["name"].lower() == tag.lower():
                        ids.append(t["id"])
                        encontrado = True
                        break
                if not encontrado:
                    resp2 = post_json(f"{API_BASE}/tags", AUTH, {"name": tag})
                    if resp2.status_code in [200, 201] and resp2.text.strip():
                        ids.append(resp2.json()["id"])
        except Exception as e:
            print(f"   AVISO tag '{tag}': {e}")
    return ids

# ============================================================
# YOAST SEO
# ============================================================

def configurar_yoast(post_id, palavra_chave, titulo_seo, meta_description):
    resp = post_json(f"{API_BASE}/posts/{post_id}", AUTH, {"meta": {
        "_yoast_wpseo_focuskw":  palavra_chave,
        "_yoast_wpseo_title":    titulo_seo,
        "_yoast_wpseo_metadesc": meta_description,
    }})
    if resp.status_code in [200, 201]:
        print("   Yoast SEO configurado")
    else:
        print(f"   AVISO Yoast: {resp.status_code}")

# ============================================================
# PUBLICAÇÃO PRINCIPAL
# ============================================================

MINIMO_PALAVRAS_CORPO = 800


def contar_palavras_corpo(texto):
    """Conta palavras do corpo removendo tags HTML e marcação Markdown."""
    texto = re.sub(r'<[^>]+>', ' ', texto)
    return len(re.findall(r'\b\w+\b', texto))


def publicar_post(caminho_arquivo):
    print(f"\n Publicando: {caminho_arquivo}")
    dados        = parsear_post(caminho_arquivo)
    numero_post  = extrair_numero_post(caminho_arquivo)
    titulo       = dados["titulo"]
    slug         = dados["slug"]

    print(f"   Título : {titulo}")
    print(f"   Slug   : {slug}")
    print(f"   Post # : {numero_post}")

    # ── Validação de tamanho mínimo do corpo ──────────────────
    n_palavras = contar_palavras_corpo(dados["conteudo"])
    print(f"   Palavras no corpo: {n_palavras}")
    if n_palavras < MINIMO_PALAVRAS_CORPO:
        print(
            f"\n ERRO: corpo com {n_palavras} palavras — mínimo exigido: "
            f"{MINIMO_PALAVRAS_CORPO}. Post não publicado."
        )
        sys.exit(1)

    # ── Imagem principal ──────────────────────────────────────
    print("\n Imagem principal...")
    id_principal = None
    try:
        caminho_p, alt_p, leg_p = resolver_imagem_principal(titulo, slug, numero_post)
        id_principal, _ = fazer_upload_imagem_local(caminho_p, alt_p, leg_p, titulo)
    except Exception as e:
        print(f"   AVISO imagem principal: {e}")

    # ── Imagem secundária ─────────────────────────────────────
    print("\n Imagem secundária...")
    url_secundaria = ""
    alt_secundaria = ""
    leg_secundaria = ""
    try:
        caminho_s, alt_s, leg_s = resolver_imagem_secundaria(titulo, slug, numero_post)
        _, url_secundaria = fazer_upload_imagem_local(caminho_s, alt_s, leg_s, titulo)
        alt_secundaria = alt_s
        leg_secundaria = leg_s
    except Exception as e:
        print(f"   AVISO imagem secundária: {e}")

    # ── Conteúdo ──────────────────────────────────────────────
    print("\n Processando conteúdo...")
    conteudo_md   = renumerar_listas_ordenadas(dados["conteudo"])
    conteudo_html = converter_markdown_para_html(conteudo_md)
    conteudo_html = corrigir_numeracao_ol(conteudo_html)
    conteudo_html = processar_links(conteudo_html, dados["links_internos"], dados["links_externos"])
    conteudo_html = injetar_cta(conteudo_html)

    if url_secundaria:
        conteudo_html = inserir_imagem_secundaria_no_html(
            conteudo_html, url_secundaria, alt_secundaria, leg_secundaria
        )

    # ── Categoria e tags ──────────────────────────────────────
    print("\n Categorias e tags...")
    categoria_id = obter_categoria()
    tag_ids      = obter_ou_criar_tags(dados["tags"]) if dados["tags"] else []
    print(f"   Categoria ID: {categoria_id} | Tags: {tag_ids}")

    # ── Criar post ────────────────────────────────────────────
    print("\n Criando post no WordPress...")
    payload = {
        "title":      titulo,
        "slug":       slug,
        "content":    conteudo_html,
        "status":     "publish",
        "categories": [categoria_id],
        "meta": {
            "_yoast_wpseo_focuskw":  dados["palavra_chave"],
            "_yoast_wpseo_title":    dados["titulo_seo"],
            "_yoast_wpseo_metadesc": dados["meta_description"],
        },
    }
    if tag_ids:
        payload["tags"] = tag_ids
    if id_principal:
        payload["featured_media"] = id_principal

    resp = post_json(f"{API_BASE}/posts", AUTH, payload)
    if resp.status_code not in [200, 201]:
        print(f" Erro ao criar post: {resp.status_code}")
        print(resp.text[:500])
        sys.exit(1)

    post    = resp.json()
    post_id = post["id"]
    post_url = post.get("link", "")
    print(f"   Post criado: ID {post_id}")
    print(f"   URL: {post_url}")

    print("\n Configurando Yoast SEO...")
    configurar_yoast(post_id, dados["palavra_chave"], dados["titulo_seo"], dados["meta_description"])

    print(f"\n Post publicado com sucesso!")
    print(f"   {post_url}")
    return post_id, post_url

# ============================================================
# ENTRADA
# ============================================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        posts = sorted(Path("posts").glob("post-*.md"))
        if not posts:
            print(" Nenhum arquivo post-XX.md encontrado em /posts/")
            sys.exit(1)
        caminho = str(posts[-1])
    else:
        caminho = sys.argv[1]

    if not os.path.exists(caminho):
        print(f" Arquivo não encontrado: {caminho}")
        sys.exit(1)

    publicar_post(caminho)
