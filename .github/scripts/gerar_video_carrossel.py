"""
TEC Solar — Gerador de Vídeo Carrossel MP4 v2.0
Resolução: 1080x1920 (9:16) | 4 slides | Voiceover ElevenLabs
"""

import os
import re
import sys
import math
import random
import tempfile
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageFont

try:
    from moviepy import (VideoClip, concatenate_videoclips, AudioFileClip,
                         CompositeAudioClip, concatenate_audioclips)
except ImportError:
    from moviepy.editor import (VideoClip, concatenate_videoclips, AudioFileClip,
                                CompositeAudioClip, concatenate_audioclips)

print("Script versão 2.0 — com efeitos 3D e animações")
print("numpy:", np.__version__)

# Flags de efeitos visuais — usados no diagnóstico de log
EFEITO_3D_ATIVO = True   # draw_text_3d: sombra 4 camadas no título
ANIMACAO_ATIVA  = True   # subtítulo aparece linha por linha
RAIOS_ATIVOS    = True   # draw_lightning_arcs nos 4 cantos da capa
print("=== EFEITOS ATIVOS: 3D={}, ANIMACAO={}, RAIOS={}".format(
      EFEITO_3D_ATIVO, ANIMACAO_ATIVA, RAIOS_ATIVOS))

# ════════════════════════════════════════════════════════════
# CAMINHOS E CONSTANTES
# ════════════════════════════════════════════════════════════

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.dirname(os.path.dirname(SCRIPT_DIR))
IMG_DIR    = os.path.join(REPO_ROOT, "imagens-padrao")

W, H          = 1080, 1920
FPS           = 24
DUR_S1 = 8.0    # capa
DUR_S2 = 10.0   # causa
DUR_S3 = 10.0   # diagnóstico
DUR_S4    = 8.0    # CTA (base; estende com áudio)
FADE_DUR  = 0.5    # fade entre slides
PAUSE_DUR = 3.0    # pausa estática após última linha

NAVY       = (13,  31,  60)
NAVY_DARK  = (5,   13,  26)
CIANO      = (0,  180, 216)
DOURADO    = (245, 166,  35)
BRANCO     = (255, 255, 255)
CINZA_FOOT = (190, 190, 190)

OVERLAY_ALPHA = int(255 * 0.82)   # rgba(5,13,26, 0.82)

# ════════════════════════════════════════════════════════════
# MAPAS DE IMAGENS POR SLIDE
# ════════════════════════════════════════════════════════════

# Slide 1 — Capa: imagem da marca do post
IMAGENS_MARCA = {
    "canadian": ["Inversor-Canadian-Bancada.webp",
                 "Inversor-Canadian-Bancada (2).webp"],
    "fronius":  ["Inversor-Fronius-Bancada.webp",
                 "Inversor-Fronius-Bancada (2).webp",
                 "Inversor-Fronius-Bancada (3).webp"],
    "growatt":  ["Inversor-Growatt-Bancada.webp",
                 "Inversor-Growatt-Bancada (2).webp"],
    "deye":     ["Inversor-Deye-Bancada.webp",
                 "Inversor-Deye-Bancada (2).webp",
                 "Inversor-Deye-Bancada (3).webp"],
    "sma":      ["Inversor-SMA-Bancada.webp",
                 "Inversor-SMA-Bancada (2).webp"],
    "sungrow":  ["Inversor-Sungrow-Bancada.webp"],
    "weg":      ["Inversor-WEG-Bancada.webp"],
    "hoymiles": ["Inversor-Hoymiles-Bancada.webp",
                 "Inversor-Hoymiles-Bancada (2).webp"],
    "drive":    ["Drive-Solar-Bancada.webp",
                 "Drive-Solar-Bancada (2).webp",
                 "Drive-Solar-Bancada (3).webp"],
}

# Slide 2 — Causa: placas eletrônicas
IMAGENS_CAUSA = [
    "Placa-Eletrônica-Bancada.webp",
    "Placa-Eletrônica-Bancada (2).webp",
    "Placa-Eletrônica-Bancada (3).webp",
    "Placa-Eletrônica-Bancada (4).webp",
    "Placa-Eletrônica-Bancada (5).webp",
    "Placa-Eletrônica-Bancada (6).webp",
    "Placa-Eletrônica-Bancada (7).webp",
    "Placa-Eletrônica-Bancada (8).webp",
]

# Slide 3 — Diagnóstico: inversor aberto / bancada
IMAGENS_DIAG = [
    "Inversor-Placa-Eletrônica-Bancada.webp",
    "Inversor-Placa-Eletrônica-Bancada (2).webp",
    "Inversor-Placa-Eletrônica-Bancada (3).webp",
    "Inversor-Placa-Eletrõnica-Bancada.webp",
]

# Slide 4 — CTA: múltiplos inversores
IMAGENS_CTA = [
    "Multi-Inversores-Bancada.webp",
    "Multi-Inversores-Bancada (2).webp",
    "Multi-Inversores-Bancada (3).webp",
]

NOMES_MARCA = {
    "canadian": "Canadian Solar",
    "fronius":  "Fronius",
    "growatt":  "Growatt",
    "deye":     "Deye",
    "sma":      "SMA",
    "sungrow":  "Sungrow",
    "weg":      "WEG",
    "hoymiles": "Hoymiles",
    "drive":    "Drive Solar",
}


def sel(lista, num):
    return lista[num % len(lista)]


def selecionar_imagens(marca, numero_post):
    """Seleciona 4 imagens únicas por slide, priorizando por marca e tipo."""
    try:
        todos = sorted([f for f in os.listdir(IMG_DIR) if f.lower().endswith(".webp")])
    except FileNotFoundError:
        return None, None, None, None

    marca_low = (marca or "").lower()
    usadas    = set()

    def candidatos(keywords):
        kw = [k.lower() for k in keywords]
        return [f for f in todos if any(k in f.lower() for k in kw)]

    def escolher(cands):
        livres = [f for f in cands if f not in usadas]
        if not livres:
            livres = [f for f in todos if f not in usadas]
        if not livres:
            livres = todos
        escolha = livres[numero_post % len(livres)]
        usadas.add(escolha)
        return escolha

    # Slide 1 (capa): brand-specific → fallback Inversor
    capa_cands = candidatos([marca_low]) if marca_low else []
    if not capa_cands:
        capa_cands = candidatos(["inversor"])
    img_capa = escolher(capa_cands or todos)

    # Slide 4 (CTA): brand-specific (arquivo diferente da capa) → Multi-Inversores → Inversor
    cta_cands = candidatos([marca_low]) if marca_low else []
    if not cta_cands:
        cta_cands = candidatos(["multi-inversores", "inversor"])
    img_cta = escolher(cta_cands or todos)

    # Slide 2 (causa): Placa ou Bancada
    causa_cands = candidatos(["placa", "bancada"])
    img_causa = escolher(causa_cands or todos)

    # Slide 3 (diag): Placa ou Bancada (diferente do slide 2)
    diag_cands = candidatos(["placa", "bancada"])
    img_diag = escolher(diag_cands or todos)

    return img_capa, img_causa, img_diag, img_cta


# ════════════════════════════════════════════════════════════
# FONTES
# ════════════════════════════════════════════════════════════

def get_font(size, bold=False):
    caminhos_bold = [
        "/usr/share/fonts/truetype/montserrat/Montserrat-Black.ttf",
        "/usr/share/fonts/truetype/montserrat/Montserrat-ExtraBold.ttf",
        "/usr/share/fonts/truetype/montserrat/Montserrat-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    caminhos_reg = [
        "/usr/share/fonts/truetype/montserrat/Montserrat-Bold.ttf",
        "/usr/share/fonts/truetype/montserrat/Montserrat-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for c in (caminhos_bold if bold else caminhos_reg):
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


# ════════════════════════════════════════════════════════════
# PARSE DO POST MARKDOWN
# ════════════════════════════════════════════════════════════

def parse_post(md_path):
    with open(md_path, encoding="utf-8") as f:
        texto = f.read()

    def campo(label):
        m = re.search(rf'\[{re.escape(label)}\]\s*\n+\s*\n+(.+?)(?:\n|$)', texto)
        return m.group(1).strip() if m else ""

    titulo_seo = campo("TÍTULO SEO — Title Tag")
    categoria  = campo("CATEGORIA")

    m = re.search(
        r'(Falha\s+\d+|Erro\s+\d+|[EF]\d{2,4}|Arc\s+Fault|Grid\s+Lost|GFCI\s+Fault)',
        titulo_seo, re.IGNORECASE
    )
    if m:
        codigo_erro = m.group(0).upper()
    else:
        # Extrai o texto antes do "—" na parte após o primeiro ":"
        # Ex: "Drive Solar: Driver de IGBT — descrição" → "DRIVER DE IGBT"
        parte_apos_dois_pontos = titulo_seo.split(":", 1)[-1].strip()
        codigo_bruto = parte_apos_dois_pontos.split("—", 1)[0].strip()
        # Trunca à última palavra completa dentro de 25 caracteres
        if len(codigo_bruto) > 25:
            palavras_cod, acumulado = codigo_bruto.split(), ""
            for p in palavras_cod:
                candidato = (acumulado + " " + p).strip()
                if len(candidato) <= 25:
                    acumulado = candidato
                else:
                    break
            codigo_bruto = acumulado or palavras_cod[0]
        codigo_erro = codigo_bruto.upper()

    partes = titulo_seo.split(":", 1)
    subtitulo = partes[1].strip() if len(partes) > 1 else titulo_seo

    marcas = ["canadian", "fronius", "growatt", "deye", "sma",
              "sungrow", "weg", "hoymiles", "drive"]
    marca = next((mk for mk in marcas if mk in titulo_seo.lower()), None)

    m_causa = re.search(
        r'## [^\n]*[Cc]aus[^\n]*\n(.*?)(?=\n## |\Z)', texto, re.DOTALL
    )
    causas = []
    if m_causa:
        itens = re.findall(
            r'(?m)^\d+\. +(.+?)(?=\n\d+\.|\n\n|\Z)', m_causa.group(1), re.DOTALL
        )
        for item in itens[:3]:
            parte = item.split("—", 1)[0].strip()
            causas.append(re.sub(r'\s+', ' ', parte)[:75])
    while len(causas) < 3:
        causas.append("")

    m_diag = re.search(
        r'## [^\n]*[Ii]dentificar[^\n]*\n(.*?)(?=\n## |\Z)', texto, re.DOTALL
    )
    passos = []
    if m_diag:
        itens = re.findall(
            r'(?m)^\d+\. +(.+?)(?=\n\d+\.|\n\n|\Z)', m_diag.group(1), re.DOTALL
        )
        for item in itens[:2]:
            passos.append(re.sub(r'\s+', ' ', item.strip())[:100])
    while len(passos) < 2:
        passos.append("")

    # ── Coletar H2/H3 do corpo para fallback de posts educacionais ──
    h2_h3_all = [h.strip() for h in re.findall(r'^#{2,3}\s+(.+)', texto, re.MULTILINE)
                 if not h.strip().startswith('[')]

    # Fallback causas: primeiros 3 H2/H3, depois frases do corpo
    if all(c == "" for c in causas):
        fallback_c = h2_h3_all[:3]
        if not fallback_c:
            m_c = re.search(
                r'\[TEXTO DO POST[^\]]*\]\s*\n+[-─]+\s*\n+(.*)', texto, re.DOTALL
            )
            if m_c:
                corpo = re.sub(r'\*\*(.+?)\*\*', r'\1', m_c.group(1))
                sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', corpo)
                         if len(s.strip()) > 20 and not s.strip().startswith('#')]
                fallback_c = [s[:75] for s in sents[:3]]
        causas = (fallback_c + ["", "", ""])[:3]

    # Fallback passos: próximos 2 H2/H3 (diferentes dos usados em causas)
    if all(p == "" for p in passos):
        fallback_p = h2_h3_all[3:5]
        if not fallback_p:
            fallback_p = h2_h3_all[:2]
        if not fallback_p:
            m_p = re.search(
                r'\[TEXTO DO POST[^\]]*\]\s*\n+[-─]+\s*\n+(.*)', texto, re.DOTALL
            )
            if m_p:
                corpo = re.sub(r'\*\*(.+?)\*\*', r'\1', m_p.group(1))
                sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', corpo)
                         if len(s.strip()) > 20 and not s.strip().startswith('#')]
                fallback_p = [s[:100] for s in sents[3:5]]
        passos = (fallback_p + ["", ""])[:2]

    # Extrair problema dos 2 primeiros parágrafos do corpo
    m_intro = re.search(
        r'\[TEXTO DO POST[^\]]*\]\s*\n+[-─]+\s*\n+(.*?)(?=\n---|\n##|\Z)',
        texto, re.DOTALL
    )
    problema = ""
    if m_intro:
        paragrafos = [p.strip() for p in m_intro.group(1).split("\n\n") if p.strip()]
        if paragrafos:
            # Pega as primeiras 120 chars do primeiro parágrafo (sem negrito)
            raw = re.sub(r'\*\*(.+?)\*\*', r'\1', paragrafos[0])
            problema = raw[:120].rstrip(".,;: ")

    return {
        "titulo_seo":  titulo_seo,
        "codigo_erro": codigo_erro,
        "subtitulo":   subtitulo,
        "categoria":   categoria.upper(),
        "causas":      causas,
        "passos":      passos,
        "marca":       marca,
        "problema":    problema,
    }


# ════════════════════════════════════════════════════════════
# VOICEOVER — ElevenLabs
# ════════════════════════════════════════════════════════════

def gerar_script_voz(dados):
    nome_marca = NOMES_MARCA.get(dados["marca"], dados["titulo_seo"].split()[0])
    codigo     = dados["codigo_erro"]
    causa      = dados["causas"][0] if dados["causas"][0] else "a causa raiz está na placa"
    return (
        f"Seu inversor {nome_marca}... exibindo {codigo}? "
        f"A maioria dos técnicos reseta, e fecha o chamado. "
        f"O erro volta. O equipamento continua com defeito. "
        f"Na nossa bancada... a causa real quase nunca é o que parece. "
        f"{causa}. "
        f"Antes de condenar o equipamento... ou pedir um novo, "
        f"você precisa de um diagnóstico em nível de placa. "
        f"A TEC Solar atende todo o Brasil, via logística reversa. "
        f"Acesse nosso perfil... link na bio... "
        f"e envie seu inversor para diagnóstico."
    )


def gerar_voiceover(script, api_key):
    if not api_key:
        print("⚠️  ELEVENLABS_API_KEY não configurado — vídeo sem áudio")
        return None

    voice_id = os.environ.get("ELEVENLABS_VOICE_ID", "").strip() or "pNInz6obpgDQGcFmaJgB"
    print(f"🎤  Voice ID: {voice_id}")

    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        print(f"📡  POST {url}")
        resp = requests.post(
            url,
            headers={
                "xi-api-key": api_key,
                "Content-Type": "application/json",
                "Accept": "audio/mpeg",
            },
            json={
                "text": script,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.75,
                    "similarity_boost": 0.75,
                    "style": 0.30,
                    "use_speaker_boost": True,
                },
            },
            timeout=60,
        )
        print(f"📶  HTTP {resp.status_code} | Content-Type: {resp.headers.get('Content-Type','?')} | {len(resp.content)} bytes")
        if not resp.ok:
            try:
                print(f"❌  Erro API ElevenLabs: {resp.json()}")
            except Exception:
                print(f"❌  Resposta bruta: {resp.text[:500]}")
            resp.raise_for_status()
        tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        tmp.write(resp.content)
        tmp.close()
        print(f"✅  Voiceover gerado: {tmp.name} ({len(resp.content)} bytes)")
        return tmp.name
    except Exception as exc:
        print(f"⚠️  ElevenLabs falhou: {exc} — vídeo sem áudio")
        return None


# ════════════════════════════════════════════════════════════
# FUNDO — CROP FILL + OVERLAY
# ════════════════════════════════════════════════════════════

def fundo_gradiente():
    arr = np.zeros((H, W, 3), dtype=np.uint8)
    for y in range(H):
        t = y / H
        arr[y, :] = [
            int(NAVY[0] * (1 - t) + NAVY_DARK[0] * t),
            int(NAVY[1] * (1 - t) + NAVY_DARK[1] * t),
            int(NAVY[2] * (1 - t) + NAVY_DARK[2] * t),
        ]
    return Image.fromarray(arr, "RGB").convert("RGBA")


def crop_fill(img, tw, th):
    """Scale + center-crop para preencher tw×th sem bordas pretas."""
    sw, sh = img.size
    scale  = max(tw / sw, th / sh)
    nw     = max(tw, int(sw * scale))
    nh     = max(th, int(sh * scale))
    img    = img.resize((nw, nh), Image.LANCZOS)
    x      = (nw - tw) // 2
    y      = (nh - th) // 2
    return img.crop((x, y, x + tw, y + th))


def load_bg(nome_arquivo):
    path = os.path.join(IMG_DIR, nome_arquivo)
    if os.path.exists(path):
        return Image.open(path).convert("RGBA")
    # Fallback: qualquer multi-inversores
    for fb in IMAGENS_CTA:
        fb_path = os.path.join(IMG_DIR, fb)
        if os.path.exists(fb_path):
            return Image.open(fb_path).convert("RGBA")
    return None


# Segmentos de circuito PCB (coordenadas para 1080×1920)
_SEGS = [
    (100, 284, 400, 284), (400, 284, 400, 497),
    (400, 497, 700, 497), (700, 497, 700, 711),
    (700, 711, 920, 711), (200, 881, 500, 881),
    (500, 881, 500, 1165), (500, 1165, 820, 1165),
    (140, 1422, 600, 1422), (600, 1422, 600, 1677),
    (820, 1023, 1040, 1023), (1040, 1023, 1040, 1279),
    (50,  597,  50,  1023), (50,  1023, 220, 1023),
]


def linhas_circuito(draw, progresso=1.0):
    visivel = max(1, int(len(_SEGS) * progresso))
    for i in range(visivel):
        x1, y1, x2, y2 = _SEGS[i]
        draw.line([(x1, y1), (x2, y2)], fill=(*CIANO, 50), width=1)
        draw.ellipse([x2 - 3, y2 - 3, x2 + 3, y2 + 3], fill=(*CIANO, 70))


def particulas_cantos(draw, seed):
    random.seed(seed)
    for _ in range(12):
        side = random.choice(["tl", "tr", "bl", "br"])
        if side == "tl":   x, y = random.randint(0, 180), random.randint(0, 280)
        elif side == "tr": x, y = random.randint(W - 180, W), random.randint(0, 280)
        elif side == "bl": x, y = random.randint(0, 180), random.randint(H - 280, H)
        else:              x, y = random.randint(W - 180, W), random.randint(H - 280, H)
        cor  = CIANO if random.random() > 0.3 else DOURADO
        r    = random.randint(2, 5)
        alph = random.randint(25, 80)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(*cor, alph))


def montar_base(nome_img, alpha_fundo=1.0, seed=0, prog_circ=1.0, t=0.0, dur=1.0):
    """Fundo: Ken Burns 1.0→1.15 + overlay preto 65% + circuito + partículas."""
    img = load_bg(nome_img)
    if img:
        # Ken Burns: zoom lento de 1.0 → 1.15 ao longo do slide
        base   = crop_fill(img, W, H)
        scale  = 1.0 + 0.15 * (t / max(dur, 0.01))
        new_w  = int(W * scale)
        new_h  = int(H * scale)
        zoomed = base.resize((new_w, new_h), Image.LANCZOS)
        ox     = (new_w - W) // 2
        oy     = (new_h - H) // 2
        img_crop = zoomed.crop((ox, oy, ox + W, oy + H))
        # Overlay preto 65% sobre a imagem com Ken Burns
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * 0.65)))
        canvas  = Image.alpha_composite(img_crop.convert("RGBA"), overlay)
    else:
        canvas = fundo_gradiente()

    circ = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    linhas_circuito(ImageDraw.Draw(circ), prog_circ)
    canvas = Image.alpha_composite(canvas, circ)

    part = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    particulas_cantos(ImageDraw.Draw(part), seed)
    canvas = Image.alpha_composite(canvas, part)

    if alpha_fundo < 1.0:
        dark = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * (1 - alpha_fundo))))
        canvas = Image.alpha_composite(canvas, dark)

    return canvas


# ════════════════════════════════════════════════════════════
# UTILITÁRIOS DE TEXTO E DECORAÇÃO
# ════════════════════════════════════════════════════════════

def wrap_text(draw, texto, font, max_w):
    palavras = texto.split()
    linhas, linha = [], ""
    for p in palavras:
        teste = (linha + " " + p).strip()
        if draw.textbbox((0, 0), teste, font=font)[2] <= max_w:
            linha = teste
        else:
            if linha:
                linhas.append(linha)
            linha = p
    if linha:
        linhas.append(linha)
    return linhas or [texto]


def quebrar_titulo(texto, font, largura_max, draw):
    palavras = texto.split()
    linhas, linha_atual = [], ""
    for palavra in palavras:
        teste = (linha_atual + " " + palavra).strip()
        bbox  = draw.textbbox((0, 0), teste, font=font)
        if bbox[2] - bbox[0] <= largura_max:
            linha_atual = teste
        else:
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra
    if linha_atual:
        linhas.append(linha_atual)
    return linhas or [texto]


def draw_lines(draw, linhas, x, y, font, cor, align="left", alpha=255):
    rgba  = (*cor[:3], alpha)
    y_cur = y
    for linha in linhas:
        bb = draw.textbbox((0, 0), linha, font=font)
        xp = (W - bb[2]) // 2 if align == "center" else x
        draw.text((xp, y_cur), linha, font=font, fill=rgba)
        y_cur += bb[3] + 10
    return y_cur


def add_rodape(canvas):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw  = ImageDraw.Draw(layer)
    font  = get_font(24)
    txt   = "REPARO  ·  DIAGNÓSTICO  ·  MANUTENÇÃO"
    bb    = draw.textbbox((0, 0), txt, font=font)
    draw.text(((W - bb[2]) // 2, H - 65), txt, font=font,
              fill=(*CINZA_FOOT, 90))
    return Image.alpha_composite(canvas, layer)


def add_logo(canvas):
    path = os.path.join(REPO_ROOT, "Design sem nome (21).png")
    if not os.path.exists(path):
        return canvas
    logo = Image.open(path).convert("RGBA")
    lw   = 140
    lh   = int(logo.height * (lw / logo.width))
    logo = logo.resize((lw, lh), Image.LANCZOS)
    canvas.paste(logo, (W - lw - 24, H - lh - 84), logo.split()[3])
    return canvas


# ════════════════════════════════════════════════════════════
# HELPERS DE ANIMAÇÃO
# ════════════════════════════════════════════════════════════

def eio(v):
    v = max(0.0, min(1.0, v))
    return v * v * (3 - 2 * v)


def prog(t, s, e):
    if e <= s:
        return 1.0
    return max(0.0, min(1.0, (t - s) / (e - s)))


def fade_out(canvas, p_fadeout):
    if p_fadeout >= 1.0:
        return canvas
    blk = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * (1 - p_fadeout))))
    return Image.alpha_composite(canvas, blk)


def draw_text_3d(draw, text, font, y, alpha=255):
    """Título com 4 camadas de sombra deslocada criando ilusão 3D."""
    bb = draw.textbbox((0, 0), text, font=font)
    x  = (W - bb[2]) // 2
    for ox, oy, a_frac in [(6, 6, 0.25), (4, 4, 0.35), (2, 3, 0.50), (1, 1, 0.65)]:
        draw.text((x + ox, y + oy), text, font=font,
                  fill=(*NAVY_DARK, int(alpha * a_frac)))
    draw.text((x, y), text, font=font, fill=(*DOURADO, alpha))
    return bb[3]


def draw_glow_text(draw, text, font, y, glow_alpha):
    """Halo difuso ao redor do texto simulando brilho."""
    if glow_alpha <= 0:
        return
    bb = draw.textbbox((0, 0), text, font=font)
    x  = (W - bb[2]) // 2
    for ox, oy in [(-5,0),(5,0),(0,-5),(0,5),(-4,-4),(4,4),(-4,4),(4,-4),
                   (-7,0),(7,0),(0,-7),(0,7)]:
        draw.text((x + ox, y + oy), text, font=font,
                  fill=(*DOURADO, glow_alpha))


def desenhar_titulo_capa(draw, texto, font, W, y_inicio, cor):
    """Desenha título com quebra automática de linha e sombra simples."""
    palavras = texto.split()
    linhas, linha_atual = [], ""
    for palavra in palavras:
        teste = (linha_atual + " " + palavra).strip()
        bbox  = draw.textbbox((0, 0), teste, font=font)
        if bbox[2] - bbox[0] <= W - 120:
            linha_atual = teste
        else:
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra
    if linha_atual:
        linhas.append(linha_atual)

    y = y_inicio
    for linha in linhas:
        bbox = draw.textbbox((0, 0), linha, font=font)
        x    = (W - (bbox[2] - bbox[0])) // 2
        draw.text((x + 2, y + 2), linha, font=font, fill=(0, 0, 0, 180))
        draw.text((x, y), linha, font=font, fill=cor)
        y += (bbox[3] - bbox[1]) + 8
    return y


def draw_lightning_arcs(draw, t, alpha):
    """Raios elétricos irregulares nos quatro cantos."""
    if alpha <= 0:
        return
    random.seed(int(t * 10))
    zones = [
        (20,  20,  220, 320),
        (W - 220, 20,  W - 20, 320),
        (20,  H - 320, 220, H - 20),
        (W - 220, H - 320, W - 20, H - 20),
    ]
    for (x1, y1, x2, y2) in zones:
        for _ in range(random.randint(1, 3)):
            pts = [(random.randint(x1, x2), random.randint(y1, y2))]
            for _ in range(random.randint(3, 6)):
                nx = max(x1, min(x2, pts[-1][0] + random.randint(-35, 35)))
                ny = max(y1, min(y2, pts[-1][1] + random.randint(-35, 35)))
                pts.append((nx, ny))
            draw.line(pts, fill=(*CIANO, alpha), width=1)


def fade_in(canvas, t):
    """Fade in nos primeiros FADE_DUR segundos de cada slide."""
    if t >= FADE_DUR:
        return canvas
    dark = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * (1.0 - t / FADE_DUR))))
    return Image.alpha_composite(canvas, dark)


def pause_progress(t, anim_end, slide_dur):
    """Progresso da barra de pausa (0→1): começa em anim_end, termina em slide_dur-FADE_DUR."""
    pause_end = slide_dur - FADE_DUR
    if t <= anim_end:
        return 0.0
    return min(1.0, (t - anim_end) / max(0.01, pause_end - anim_end))


def draw_progress_bar_fill(draw, progress):
    """Linha ciano fina na base do slide se preenchendo durante a pausa."""
    if progress <= 0:
        return
    bar_w = int(W * min(1.0, progress))
    draw.rectangle([0, H - 8, bar_w, H - 4], fill=(*CIANO, 180))


def draw_palavras_animadas(draw, texto, font, x_start, y_start, t, t_inicio, cor, max_w):
    """Revela palavras uma a uma: 0.25s por palavra, fade-in de 0.1s cada.
    Retorna o tempo logo após a última palavra (para encadear próximo bloco).
    """
    palavras = texto.split()
    x, y     = x_start, y_start
    t_p      = t_inicio
    for palavra in palavras:
        bb_p = draw.textbbox((0, 0), palavra + " ", font=font)
        w_p  = bb_p[2]
        if x + w_p > x_start + max_w and x > x_start:
            x  = x_start
            y += bb_p[3] + 8
        alpha = int(255 * eio(prog(t, t_p, t_p + 0.1)))
        draw.text((x, y), palavra, font=font, fill=(*cor[:3], alpha))
        x  += w_p
        t_p += 0.25
    return t_p


def transicao_lateral(clip1, clip2, duracao=0.4):
    """Transição slide lateral direita→esquerda entre dois VideoClips."""
    def make_frame(t):
        if t < duracao:
            progresso = t / duracao
            frame1 = clip1.get_frame(clip1.duration - max(duracao - t, 0.001))
            frame2 = clip2.get_frame(0)
            offset = int(W * progresso)
            frame  = np.zeros((H, W, 3), dtype=np.uint8)
            if offset < W:
                frame[:, :W - offset] = frame1[:, offset:]
                frame[:, W - offset:] = frame2[:, :offset]
            else:
                frame = frame2
            return frame
        return clip2.get_frame(t - duracao)
    return VideoClip(make_frame, duration=clip2.duration + duracao)


# ════════════════════════════════════════════════════════════
# SLIDE 1 — CAPA  (imagem da marca, 1080x1920)
# ════════════════════════════════════════════════════════════

def frame_s1(t, dados):
    pf  = eio(prog(t, 0.0, 0.30))
    pc  = eio(prog(t, 0.3, 0.80))
    pe  = eio(prog(t, 0.8, 1.50))
    pt  = eio(prog(t, 1.5, 2.50))   # zoom + 3D do título
    pfo = 1.0 - eio(prog(t, 7.5, 8.00))
    pp  = pause_progress(t, 4.5, DUR_S1)
    # Glow pulsa continuamente; arcos flickeiam
    pgl   = 0.5 + 0.5 * math.sin(t * 3.0)
    arc_a = int((35 + 45 * pgl) * pt)

    canvas = montar_base(dados["img_capa"], pf, int(t * 8), pc, t=t, dur=DUR_S1)

    # ── Raios elétricos nos cantos ──────────────────────────
    arc_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_lightning_arcs(ImageDraw.Draw(arc_layer), t, arc_a)
    canvas = Image.alpha_composite(canvas, arc_layer)

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw  = ImageDraw.Draw(layer)

    # ── Eyebrow — desliza de baixo para cima ───────────────
    font_e   = get_font(30, bold=True)
    txt_e    = f"⚡  {dados['categoria']}"
    ey_final = 60
    ey_y     = ey_final + int((1 - pe) * 60)
    bb       = draw.textbbox((0, 0), txt_e, font=font_e)
    bw, bh   = bb[2] + 48, bb[3] + 22
    a_e      = int(255 * pe)
    draw.rounded_rectangle([60, ey_y, 60 + bw, ey_y + bh],
                            radius=22, outline=(*CIANO, a_e), width=2)
    draw.text((84, ey_y + 11), txt_e, font=font_e, fill=(*CIANO, a_e))

    a_t    = int(255 * pt)

    # ── Linha 1: "ANTES DE CONDENAR," (ciano, 36px) ───────
    font_l1 = get_font(36)
    txt_l1  = "ANTES DE CONDENAR,"
    bb_l1   = draw.textbbox((0, 0), txt_l1, font=font_l1)
    draw.text(((W - bb_l1[2]) // 2, 115), txt_l1, font=font_l1,
              fill=(*CIANO, int(255 * pe)))

    # ── MODO CAPA: falha/erro vs educacional ──────────────
    modo_falha = bool(dados.get("marca")) and bool(dados.get("codigo_erro"))
    if modo_falha:
        linha2 = f"INVERSOR {NOMES_MARCA.get(dados['marca'], (dados['marca'] or '').upper()).upper()}".strip()
        linha3 = dados["codigo_erro"].upper()
    else:
        titulo = dados["titulo_seo"]
        sep_match = re.search(r'[:—]', titulo)
        if sep_match:
            linha2 = titulo[:sep_match.start()].strip()
            linha3 = dados["subtitulo"]   # subtitulo já é a parte após ":" — não re-extrair
        else:
            linha2 = titulo
            linha3 = ""

    print(f"MODO CAPA: {'falha' if modo_falha else 'educacional'} | linha2='{linha2}' | linha3='{linha3}'")

    y_cur = 168

    if modo_falha:
        # Linha 2: "INVERSOR MARCA" — ciano, 48px
        font_l2   = get_font(48, bold=True)
        linhas_l2 = quebrar_titulo(linha2, font_l2, W - 80, draw)
        for lh in linhas_l2:
            bb_lh = draw.textbbox((0, 0), lh, font=font_l2)
            draw.text(((W - bb_lh[2]) // 2, y_cur), lh, font=font_l2,
                      fill=(*CIANO, a_t))
            y_cur += bb_lh[3] + 8
        y_cur += 10
        # Linha 3: código — dourado, 72px (54 se >15 chars)
        fs_l3   = 54 if len(linha3) > 15 else 72
        font_l3 = get_font(fs_l3, bold=True)
        linhas_l3 = quebrar_titulo(linha3, font_l3, W - 80, draw)
        for lh in linhas_l3:
            bb_lh = draw.textbbox((0, 0), lh, font=font_l3)
            draw.text(((W - bb_lh[2]) // 2, y_cur), lh, font=font_l3,
                      fill=(*DOURADO, a_t))
            y_cur += bb_lh[3] + 8
    else:
        if linha3:
            # Parte antes do separador — dourado, 58px
            font_l2   = get_font(58, bold=True)
            linhas_l2 = quebrar_titulo(linha2, font_l2, W - 80, draw)
            for lh in linhas_l2:
                bb_lh = draw.textbbox((0, 0), lh, font=font_l2)
                draw.text(((W - bb_lh[2]) // 2, y_cur), lh, font=font_l2,
                          fill=(*DOURADO, a_t))
                y_cur += bb_lh[3] + 8
            y_cur += 6
            # Parte depois do separador — branco, 42px
            font_l3   = get_font(42, bold=True)
            linhas_l3 = quebrar_titulo(linha3, font_l3, W - 80, draw)
            for lh in linhas_l3:
                bb_lh = draw.textbbox((0, 0), lh, font=font_l3)
                draw.text(((W - bb_lh[2]) // 2, y_cur), lh, font=font_l3,
                          fill=(*BRANCO, a_t))
                y_cur += bb_lh[3] + 8
        else:
            # Sem separador: título inteiro em dourado, 52px
            font_l2   = get_font(52, bold=True)
            linhas_l2 = quebrar_titulo(linha2, font_l2, W - 80, draw)
            for lh in linhas_l2:
                bb_lh = draw.textbbox((0, 0), lh, font=font_l2)
                draw.text(((W - bb_lh[2]) // 2, y_cur), lh, font=font_l2,
                          fill=(*DOURADO, a_t))
                y_cur += bb_lh[3] + 8

    y3f = y_cur

    # ── Separador ─────────────────────────────────────────
    y_sep = y3f + 12
    if pt > 0.4:
        draw.rectangle([int(W * 0.18), y_sep, int(W * 0.82), y_sep + 2],
                       fill=(*CIANO, int(200 * pt)))

    # ── Linha 4: subtítulo — apenas no modo falha/erro (educacional já mostra em linha3) ──
    if modo_falha:
        font_l4 = get_font(42, bold=True)
        linhas  = quebrar_titulo(dados["subtitulo"], font_l4, W - 80, draw)[:2]
        y4      = y_sep + 18
        for i, linha in enumerate(linhas):
            ps_i = eio(prog(t, 2.5 + i * 0.8, 3.0 + i * 0.8))
            bb_l = draw.textbbox((0, 0), linha, font=font_l4)
            draw.text(((W - bb_l[2]) // 2, y4), linha, font=font_l4,
                      fill=(*BRANCO, int(255 * ps_i)))
            y4 += bb_l[3] + 10

    # ── Barra de progresso durante pausa ──────────────────
    draw_progress_bar_fill(draw, pp)

    canvas = Image.alpha_composite(canvas, layer)
    canvas = add_rodape(canvas)
    canvas = add_logo(canvas)
    canvas = fade_in(canvas, t)
    canvas = fade_out(canvas, pfo)
    return np.array(canvas.convert("RGB"))


# ════════════════════════════════════════════════════════════
# SLIDE 2 — CAUSA RAIZ  (placa eletrônica)
# ════════════════════════════════════════════════════════════

def frame_s2(t, dados):
    pf  = eio(prog(t, 0.0, 0.30))
    pc  = eio(prog(t, 0.3, 0.80))
    pe  = eio(prog(t, 0.8, 1.50))
    pt  = eio(prog(t, 1.5, 2.50))
    pfo = 1.0 - eio(prog(t, 9.5, 10.00))
    pp  = pause_progress(t, 6.5, DUR_S2)

    canvas = montar_base(dados["img_causa"], pf, int(t * 8) + 100, pc, t=t, dur=DUR_S2)
    layer  = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw   = ImageDraw.Draw(layer)

    a_e = int(255 * pe)

    # Contador canto superior direito
    font_c = get_font(26, bold=True)
    draw.rounded_rectangle([W - 148, 58, W - 52, 102],
                            radius=8, outline=(*CIANO, a_e), width=2)
    draw.text((W - 138, 66), "02 / 04", font=font_c, fill=(*CIANO, a_e))

    # Eyebrow
    ey_y = 128 + int((1 - pe) * 60)
    draw.text((60, ey_y), "⚡  CAUSA REAL",
              font=get_font(30, bold=True), fill=(*CIANO, a_e))

    # Título
    font_t = get_font(90, bold=True)
    a_t    = int(255 * pt)
    draw.text((60, 260), "A CAUSA", font=font_t, fill=(*BRANCO, a_t))
    draw.text((60, 362), "RAIZ",    font=font_t, fill=(*DOURADO, a_t))

    if pt > 0.3:
        draw.rectangle([60, 470, 420, 472],
                       fill=(*CIANO, int(200 * pt)))

    # Bullets palavra por palavra
    font_b = get_font(32)
    t_now  = 2.5
    for i, causa in enumerate(dados["causas"]):
        by  = 510 + i * 200
        cor = CIANO if i < 2 else DOURADO
        ab0 = int(255 * eio(prog(t, t_now, t_now + 0.15)))
        draw.ellipse([60, by + 10, 86, by + 36], fill=(*cor, ab0))
        t_now = draw_palavras_animadas(draw, causa, font_b, 104, by, t, t_now, BRANCO, W - 148)
        t_now += 0.3

    draw_progress_bar_fill(draw, pp)

    canvas = Image.alpha_composite(canvas, layer)
    canvas = add_rodape(canvas)
    canvas = add_logo(canvas)
    canvas = fade_in(canvas, t)
    canvas = fade_out(canvas, pfo)
    return np.array(canvas.convert("RGB"))


# ════════════════════════════════════════════════════════════
# SLIDE 3 — DIAGNÓSTICO  (bancada com multímetro)
# ════════════════════════════════════════════════════════════

def frame_s3(t, dados):
    pf  = eio(prog(t, 0.0, 0.30))
    pc  = eio(prog(t, 0.3, 0.80))
    pe  = eio(prog(t, 0.8, 1.50))
    pt  = eio(prog(t, 1.5, 2.50))
    pfo = 1.0 - eio(prog(t, 9.5, 10.00))
    pp  = pause_progress(t, 6.5, DUR_S3)

    canvas = montar_base(dados["img_diag"], pf, int(t * 8) + 200, pc, t=t, dur=DUR_S3)
    layer  = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw   = ImageDraw.Draw(layer)

    a_e = int(255 * pe)

    # Contador
    font_c = get_font(26, bold=True)
    draw.rounded_rectangle([W - 148, 58, W - 52, 102],
                            radius=8, outline=(*CIANO, a_e), width=2)
    draw.text((W - 138, 66), "03 / 04", font=font_c, fill=(*CIANO, a_e))

    # Eyebrow
    ey_y = 128 + int((1 - pe) * 60)
    draw.text((60, ey_y), "⚡  DIAGNÓSTICO",
              font=get_font(30, bold=True), fill=(*CIANO, a_e))

    # Título
    font_t = get_font(82, bold=True)
    a_t    = int(255 * pt)
    draw.text((60, 260), "CHECKLIST",  font=font_t, fill=(*BRANCO, a_t))
    draw.text((60, 354), "NA PRÁTICA", font=font_t, fill=(*DOURADO, a_t))

    if pt > 0.3:
        draw.rectangle([60, 458, 450, 460],
                       fill=(*CIANO, int(200 * pt)))

    # Passos palavra por palavra
    font_l = get_font(26, bold=True)
    font_p = get_font(30)
    t_now  = 2.5
    for i, passo in enumerate(dados["passos"]):
        py  = 490 + i * 300
        ap0 = int(255 * eio(prog(t, t_now, t_now + 0.15)))
        draw.rectangle([60, py, 66, py + 90], fill=(*CIANO, ap0))
        draw.text((82, py), f"PASSO {i + 1}", font=font_l, fill=(*CIANO, ap0))
        t_now = draw_palavras_animadas(draw, passo, font_p, 82, py + 38, t, t_now, BRANCO, W - 148)
        t_now += 0.3

    draw_progress_bar_fill(draw, pp)

    canvas = Image.alpha_composite(canvas, layer)
    canvas = add_rodape(canvas)
    canvas = add_logo(canvas)
    canvas = fade_in(canvas, t)
    canvas = fade_out(canvas, pfo)
    return np.array(canvas.convert("RGB"))


# ════════════════════════════════════════════════════════════
# SLIDE 4 — CTA  (multi-inversores, duração dinâmica)
# ════════════════════════════════════════════════════════════

def frame_s4(t, dados):
    dur  = dados.get("dur_s4", DUR_S4)
    pf   = eio(prog(t, 0.0, 0.30))
    pc   = eio(prog(t, 0.3, 0.80))
    pt   = eio(prog(t, 0.8, 1.80))
    psrv = eio(prog(t, 1.8, 2.80))
    pcta = eio(prog(t, 2.8, 3.80))
    pfo  = 1.0 - eio(prog(t, dur - 0.5, dur))
    pp   = pause_progress(t, dur - PAUSE_DUR - FADE_DUR, dur)

    canvas = montar_base(dados["img_cta"], pf, int(t * 8) + 300, pc, t=t, dur=dados.get("dur_s4", DUR_S4))
    layer  = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw   = ImageDraw.Draw(layer)

    # Acima
    font_a = get_font(32)
    txt_a  = "ANTES DE CONDENAR,"
    bb     = draw.textbbox((0, 0), txt_a, font=font_a)
    draw.text(((W - bb[2]) // 2, 200), txt_a, font=font_a,
              fill=(*BRANCO, int(180 * pt)))

    # DIAGNOSTIQUE.
    font_d = get_font(96, bold=True)
    txt_d  = "DIAGNOSTIQUE."
    bb     = draw.textbbox((0, 0), txt_d, font=font_d)
    draw.text(((W - bb[2]) // 2, 258), txt_d, font=font_d,
              fill=(*DOURADO, int(255 * pt)))

    if pt > 0.5:
        draw.rectangle([int(W * 0.12), 410, int(W * 0.88), 412],
                       fill=(*CIANO, int(200 * pt)))

    # Linhas de serviço
    font_s   = get_font(32)
    servicos = [
        "Diagnóstico eletrônico em nível de componente.",
        "Laudo técnico detalhado — mesmo sem reparo.",
        "Atendemos todo o Brasil via logística reversa.",
    ]
    for i, srv in enumerate(servicos):
        ps_i = eio(prog(t, 1.8 + i * 0.8, 2.4 + i * 0.8))
        bb   = draw.textbbox((0, 0), srv, font=font_s)
        draw.text(((W - bb[2]) // 2, 440 + i * 65), srv, font=font_s,
                  fill=(*BRANCO, int(200 * ps_i)))

    # Caixa WhatsApp
    cta_y = H - 500
    a_cta = int(255 * pcta)
    draw.rounded_rectangle([80, cta_y, W - 80, cta_y + 200],
                            radius=18, outline=(*CIANO, a_cta), width=2)

    font_wl = get_font(26)
    bb      = draw.textbbox((0, 0), "WHATSAPP", font=font_wl)
    draw.text(((W - bb[2]) // 2, cta_y + 20), "WHATSAPP",
              font=font_wl, fill=(*BRANCO, int(140 * pcta)))

    font_wn   = get_font(74, bold=True)
    numero    = "(38) 99889-1587"
    bb        = draw.textbbox((0, 0), numero, font=font_wn)
    xn        = (W - bb[2]) // 2
    yn        = cta_y + 64
    # Desenhar número em camada temporária para aplicar pulse
    num_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    num_draw  = ImageDraw.Draw(num_layer)
    for bx, by_b in [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (2, -2), (-2, 2), (2, 2)]:
        num_draw.text((xn + bx, yn + by_b), numero, font=font_wn, fill=(*BRANCO, a_cta))
    num_draw.text((xn, yn), numero, font=font_wn, fill=(*DOURADO, a_cta))
    # Pulse senoidal: 1.5 Hz, ±5% de escala
    pulse = 1.0 + 0.05 * math.sin(t * 2 * math.pi * 1.5)
    pad   = 20
    rx0   = max(0, xn - pad)
    ry0   = max(0, yn - pad)
    rx1   = min(W, xn + bb[2] + pad)
    ry1   = min(H, yn + bb[3] + pad)
    rw, rh = rx1 - rx0, ry1 - ry0
    if rw > 0 and rh > 0 and a_cta > 0:
        region = num_layer.crop((rx0, ry0, rx1, ry1))
        nw     = max(1, int(rw * pulse))
        nh     = max(1, int(rh * pulse))
        scaled = region.resize((nw, nh), Image.LANCZOS)
        ox     = rx0 + (rw - nw) // 2
        oy     = ry0 + (rh - nh) // 2
        layer.alpha_composite(scaled, (max(0, ox), max(0, oy)))
    else:
        layer.alpha_composite(num_layer)

    font_ig = get_font(30)
    bb      = draw.textbbox((0, 0), "@tec_solar_moc", font=font_ig)
    draw.text(((W - bb[2]) // 2, cta_y + 148), "@tec_solar_moc",
              font=font_ig, fill=(*CIANO, int(200 * pcta)))

    draw_progress_bar_fill(draw, pp)

    canvas = Image.alpha_composite(canvas, layer)
    canvas = add_rodape(canvas)
    canvas = add_logo(canvas)
    canvas = fade_in(canvas, t)
    canvas = fade_out(canvas, pfo)
    return np.array(canvas.convert("RGB"))


# ════════════════════════════════════════════════════════════
# GERAÇÃO DO VÍDEO COMPLETO
# ════════════════════════════════════════════════════════════

def gerar_video(numero_post, md_path):
    dados = parse_post(md_path)
    print(f"=== DEBUG TITULO ===")
    print(f"titulo_completo: '{dados.get('titulo', '')}'")
    print(f"marca: '{dados.get('marca', '')}'")
    print(f"codigo: '{dados.get('codigo', '')}'")
    print(f"subtitulo_capa: '{dados.get('subtitulo', '')}'")
    print(f"===================")
    print(f"Post {numero_post:02d} — {dados['titulo_seo']}")
    print(f"Marca: {dados['marca']} | Código: {dados['codigo_erro']}")

    # Selecionar imagens por slide (brand-aware, sem duplicatas)
    img_capa, img_causa, img_diag, img_cta = selecionar_imagens(dados["marca"], numero_post)
    dados["img_capa"]  = img_capa
    dados["img_causa"] = img_causa
    dados["img_diag"]  = img_diag
    dados["img_cta"]   = img_cta

    print(f"Causas: {dados['causas']}")
    print(f"Passos: {dados['passos']}")
    print(f"Imagens: capa={dados['img_capa']} | causa={dados['img_causa']}")

    # ── Voiceover ElevenLabs ─────────────────────────────────
    api_key    = os.environ.get("ELEVENLABS_API_KEY")
    script_voz = gerar_script_voz(dados)
    print(f"Script voz ({len(script_voz.split())} palavras):\n{script_voz[:120]}...")
    audio_path = gerar_voiceover(script_voz, api_key)

    audio_clip      = None
    slide4_duration = DUR_S4

    if audio_path:
        try:
            audio_clip = AudioFileClip(audio_path).volumex(7.5)
            total_base = DUR_S1 + DUR_S2 + DUR_S3   # 28s
            if audio_clip.duration > total_base + DUR_S4:
                slide4_duration = audio_clip.duration - total_base
                print(f"⏱  Slide 4 estendido para {slide4_duration:.1f}s")
            elif audio_clip.duration < total_base:
                slide4_duration = DUR_S4
            else:
                slide4_duration = max(DUR_S4, audio_clip.duration - total_base)
        except Exception as exc:
            print(f"⚠️  Erro ao carregar áudio: {exc}")
            audio_clip = None

    dados["dur_s4"] = slide4_duration

    # ── Clips ────────────────────────────────────────────────
    c1 = VideoClip(lambda t, d=dados: frame_s1(t, d), duration=DUR_S1)
    c2 = VideoClip(lambda t, d=dados: frame_s2(t, d), duration=DUR_S2)
    c3 = VideoClip(lambda t, d=dados: frame_s3(t, d), duration=DUR_S3)
    c4 = VideoClip(lambda t, d=dados: frame_s4(t, d), duration=slide4_duration)
    # Transições laterais entre slides (direita → esquerda, 0.4s)
    video = concatenate_videoclips([
        c1,
        transicao_lateral(c1, c2),
        transicao_lateral(c2, c3),
        transicao_lateral(c3, c4),
    ])

    # ── Cortar voiceover se exceder duração do vídeo ────────
    if audio_clip:
        try:
            if audio_clip.duration > video.duration:
                try:
                    audio_clip = audio_clip.subclipped(0, video.duration)
                except AttributeError:
                    audio_clip = audio_clip.subclip(0, video.duration)
        except Exception as exc:
            print(f"⚠️  Erro ao cortar voiceover: {exc}")
            audio_clip = None

    # ── Música de fundo + mixagem ───────────────────────────
    bg_path       = os.path.join(REPO_ROOT, "audio-fundo.mp3")
    duracao_total = video.duration
    voiceover     = audio_clip

    if os.path.exists(bg_path):
        try:
            bg_raw    = AudioFileClip(bg_path).subclip(0, duracao_total)
            bg_music  = bg_raw.audio_fadeout(2)
            bg_music  = bg_music.volumex(0.07)
            if voiceover:
                audio_final = CompositeAudioClip([voiceover, bg_music])
            else:
                audio_final = bg_music
            print("Música de fundo aplicada com sucesso")
        except Exception as e:
            print(f"Música de fundo ignorada: {e}")
            audio_final = voiceover
    else:
        audio_final = voiceover

    if audio_final:
        video = video.set_audio(audio_final)
        print(f"🔊  Áudio final aplicado ao vídeo")

    # ── Exportar MP4 ─────────────────────────────────────────
    pasta = os.path.join(REPO_ROOT, f"carrossel/post-{numero_post:02d}")
    os.makedirs(pasta, exist_ok=True)
    saida = os.path.join(pasta, "video-carrossel.mp4")

    video.write_videofile(
        saida,
        fps=30,
        codec="libx264",
        audio_codec="aac",
        threads=4,
        logger=None,
    )
    print(f"✅  Vídeo salvo: {saida}")

    # Limpar temp
    if audio_path and os.path.exists(audio_path):
        os.unlink(audio_path)

    return saida


# ════════════════════════════════════════════════════════════
# ENTRADA
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python gerar_video_carrossel.py <numero_post>")
        sys.exit(1)

    num     = int(sys.argv[1])
    md_path = os.path.join(REPO_ROOT, f"posts/post-{num:02d}.md")

    if not os.path.exists(md_path):
        print(f"Arquivo não encontrado: {md_path}")
        sys.exit(1)

    gerar_video(num, md_path)
