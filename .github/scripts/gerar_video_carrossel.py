"""
TEC Solar — Gerador de Vídeo Carrossel MP4
4 slides x 5s = 20s | 1080x1350px | H.264
"""

import os
import re
import sys
import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont

try:
    from moviepy import VideoClip, concatenate_videoclips
except ImportError:
    from moviepy.editor import VideoClip, concatenate_videoclips

# ── Caminhos ────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# ── Dimensões e timing ──────────────────────────────────────
W, H            = 1080, 1350
FPS             = 24
DURACAO_SLIDE   = 5.0

# ── Cores TEC Solar ─────────────────────────────────────────
NAVY       = (13,  31,  60)
NAVY_DARK  = (5,   13,  26)
CIANO      = (0,  180, 216)
DOURADO    = (245, 166,  35)
BRANCO     = (255, 255, 255)
CINZA_FOOT = (190, 190, 190)

# ── Mapeamento marca → imagem de fundo ─────────────────────
IMAGENS_MARCA = {
    "canadian": "Inversor-Canadian-Bancada.webp",
    "fronius":  "Inversor-Fronius-Bancada.webp",
    "growatt":  "Inversor-Growatt-Bancada.webp",
    "deye":     "Inversor-Deye-Bancada.webp",
    "sma":      "Inversor-SMA-Bancada.webp",
    "sungrow":  "Inversor-Sungrow-Bancada.webp",
    "weg":      "Inversor-WEG-Bancada.webp",
    "hoymiles": "Inversor-Hoymiles-Bancada.webp",
    "drive":    "Drive-Solar-Bancada.webp",
    "placa":    "Placa-Eletrônica-Bancada.webp",
    "multi":    "Multi-Inversores-Bancada.webp",
}


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
    lista = caminhos_bold if bold else caminhos_reg
    for c in lista:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


# ════════════════════════════════════════════════════════════
# PARSE DO POST MARKDOWN
# ════════════════════════════════════════════════════════════

def parse_post(caminho_md):
    with open(caminho_md, encoding="utf-8") as f:
        texto = f.read()

    # Título SEO
    m = re.search(r'\[TÍTULO SEO[^\]]*\]\s*\n+\s*\n+(.+?)(?:\n|$)', texto)
    titulo_seo = m.group(1).strip() if m else ""

    # Categoria
    m = re.search(r'\[CATEGORIA\]\s*\n+\s*\n+(.+?)(?:\n|$)', texto)
    categoria = m.group(1).strip() if m else "CÓDIGO DE ERRO"

    # Código do erro
    m = re.search(
        r'(Falha\s+\d+|Erro\s+\d+|[EF]\d{2,4}|Arc\s+Fault|Grid\s+Lost|GFCI\s+Fault)',
        titulo_seo, re.IGNORECASE
    )
    codigo_erro = m.group(0).upper() if m else titulo_seo[:20].upper()

    # Subtítulo = depois dos dois pontos no título SEO
    partes = titulo_seo.split(":", 1)
    subtitulo = partes[1].strip() if len(partes) > 1 else titulo_seo

    # Detectar marca
    marcas = ["canadian", "fronius", "growatt", "deye", "sma",
              "sungrow", "weg", "hoymiles", "drive"]
    marca = next((mk for mk in marcas if mk in titulo_seo.lower()), None)

    # Causas (primeiros 3 itens numerados da seção de causa)
    m_sec = re.search(
        r'## [^\n]*[Cc]aus[^\n]*\n(.*?)(?=\n## |\Z)', texto, re.DOTALL
    )
    causas = []
    if m_sec:
        itens = re.findall(
            r'(?m)^\d+\. +(.+?)(?=\n\d+\.|\n\n|\Z)', m_sec.group(1), re.DOTALL
        )
        for item in itens[:3]:
            parte = item.split("—", 1)[0].strip()
            causas.append(re.sub(r'\s+', ' ', parte)[:75])
    while len(causas) < 3:
        causas.append("")

    # Passos de diagnóstico (primeiros 2 itens numerados)
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

    return {
        "titulo_seo": titulo_seo,
        "codigo_erro": codigo_erro,
        "subtitulo":   subtitulo,
        "categoria":   categoria.upper(),
        "causas":      causas,
        "passos":      passos,
        "marca":       marca,
    }


# ════════════════════════════════════════════════════════════
# FUNDO E ELEMENTOS VISUAIS
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


_SEGMENTOS_CIRC = [
    (100, 200, 400, 200), (400, 200, 400, 350), (400, 350, 700, 350),
    (700, 350, 700, 500), (700, 500, 920, 500),
    (200, 620, 500, 620), (500, 620, 500, 820), (500, 820, 820, 820),
    (140, 1000, 600, 1000), (600, 1000, 600, 1180),
    (820, 720, 1040, 720), (1040, 720, 1040, 900),
    (50,  420, 50,  720), (50,  720, 220, 720),
]


def linhas_circuito(draw, progresso=1.0):
    total    = len(_SEGMENTOS_CIRC)
    visivel  = max(1, int(total * progresso))
    cor_line = (*CIANO, 50)
    cor_no   = (*CIANO, 70)
    for i in range(visivel):
        x1, y1, x2, y2 = _SEGMENTOS_CIRC[i]
        draw.line([(x1, y1), (x2, y2)], fill=cor_line, width=1)
        draw.ellipse([x2 - 3, y2 - 3, x2 + 3, y2 + 3], fill=cor_no)


def particulas_cantos(draw, seed):
    random.seed(seed)
    for _ in range(10):
        side = random.choice(["tl", "tr", "bl", "br"])
        if side == "tl":
            x, y = random.randint(0, 160), random.randint(0, 220)
        elif side == "tr":
            x, y = random.randint(W - 160, W), random.randint(0, 220)
        elif side == "bl":
            x, y = random.randint(0, 160), random.randint(H - 220, H)
        else:
            x, y = random.randint(W - 160, W), random.randint(H - 220, H)
        cor  = CIANO if random.random() > 0.3 else DOURADO
        r    = random.randint(2, 5)
        alph = random.randint(25, 80)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(*cor, alph))


def carregar_imagem_marca(marca):
    pasta = os.path.join(REPO_ROOT, "imagens-padrao")
    candidatos = []
    if marca and marca in IMAGENS_MARCA:
        candidatos.append(IMAGENS_MARCA[marca])
    candidatos += ["Multi-Inversores-Bancada.webp",
                   "Placa-Eletrônica-Bancada.webp"]
    for nome in candidatos:
        c = os.path.join(pasta, nome)
        if os.path.exists(c):
            return Image.open(c).convert("RGBA")
    return None


def montar_base(marca, alpha_fundo=1.0, seed=0, prog_circ=1.0):
    canvas = fundo_gradiente()

    # Imagem de marca com overlay escuro rgba(5,13,26,0.75)
    img = carregar_imagem_marca(marca)
    if img:
        ratio = min(W / img.width, H / img.height)
        nw, nh = int(img.width * ratio), int(img.height * ratio)
        img = img.resize((nw, nh), Image.LANCZOS)
        ov  = Image.new("RGBA", (nw, nh), (5, 13, 26, int(255 * 0.75)))
        img = Image.alpha_composite(img, ov)
        canvas.paste(img, ((W - nw) // 2, (H - nh) // 2), img.split()[3])

    # Linhas de circuito
    circ = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    linhas_circuito(ImageDraw.Draw(circ), prog_circ)
    canvas = Image.alpha_composite(canvas, circ)

    # Partículas
    part = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    particulas_cantos(ImageDraw.Draw(part), seed)
    canvas = Image.alpha_composite(canvas, part)

    # Fade in do fundo
    if alpha_fundo < 1.0:
        dark = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * (1 - alpha_fundo))))
        canvas = Image.alpha_composite(canvas, dark)

    return canvas


# ════════════════════════════════════════════════════════════
# UTILITÁRIOS DE TEXTO
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


def draw_text_lines(draw, linhas, x, y, font, cor, align="left", alpha=255):
    rgba = (*cor[:3], alpha)
    y0   = y
    for linha in linhas:
        bb = draw.textbbox((0, 0), linha, font=font)
        xp = (W - bb[2]) // 2 if align == "center" else x
        draw.text((xp, y0), linha, font=font, fill=rgba)
        y0 += bb[3] + 8
    return y0


def add_rodape(canvas):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw  = ImageDraw.Draw(layer)
    font  = get_font(22)
    txt   = "REPARO  ·  DIAGNÓSTICO  ·  MANUTENÇÃO"
    bb    = draw.textbbox((0, 0), txt, font=font)
    draw.text(((W - bb[2]) // 2, H - 52), txt, font=font,
              fill=(*CINZA_FOOT, 90))
    return Image.alpha_composite(canvas, layer)


def add_logo(canvas):
    logo_path = os.path.join(REPO_ROOT, "Design sem nome (21).png")
    if not os.path.exists(logo_path):
        return canvas
    logo  = Image.open(logo_path).convert("RGBA")
    lw    = 130
    lh    = int(logo.height * (lw / logo.width))
    logo  = logo.resize((lw, lh), Image.LANCZOS)
    canvas.paste(logo, (W - lw - 22, H - lh - 68), logo.split()[3])
    return canvas


# ════════════════════════════════════════════════════════════
# ANIMAÇÕES (easing + progress helpers)
# ════════════════════════════════════════════════════════════

def eio(v):
    v = max(0.0, min(1.0, v))
    return v * v * (3 - 2 * v)


def prog(t, s, e):
    if e <= s:
        return 1.0
    return max(0.0, min(1.0, (t - s) / (e - s)))


def fade_overlay(canvas, alpha_multiplier):
    if alpha_multiplier >= 1.0:
        return canvas
    black = Image.new("RGBA", (W, H), (0, 0, 0, int(255 * (1 - alpha_multiplier))))
    return Image.alpha_composite(canvas, black)


# ════════════════════════════════════════════════════════════
# SLIDE 1 — CAPA
# ════════════════════════════════════════════════════════════

def frame_s1(t, dados):
    pf  = eio(prog(t, 0.0, 0.30))
    pc  = eio(prog(t, 0.3, 0.80))
    pe  = eio(prog(t, 0.8, 1.50))
    pt  = eio(prog(t, 1.5, 2.50))
    ps  = eio(prog(t, 2.5, 3.50))
    pfo = 1.0 - eio(prog(t, 4.5, 5.00))

    canvas = montar_base(dados["marca"], pf, int(t * 8), pc)
    layer  = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw   = ImageDraw.Draw(layer)

    # Eyebrow — desliza de baixo
    font_e = get_font(28, bold=True)
    txt_e  = f"⚡  {dados['categoria']}"
    ey     = 80 + int((1 - pe) * 60)
    bb     = draw.textbbox((0, 0), txt_e, font=font_e)
    bw, bh = bb[2] + 44, bb[3] + 20
    draw.rounded_rectangle([60, ey, 60 + bw, ey + bh],
                            radius=20, outline=(*CIANO, int(255 * pe)), width=2)
    draw.text((80, ey + 10), txt_e, font=font_e, fill=(*CIANO, int(255 * pe)))

    # Título principal palavra a palavra
    font_t  = get_font(96, bold=True)
    palavras = dados["codigo_erro"].split()
    y       = 180
    vis     = max(1, round(len(palavras) * pt))
    for i, p in enumerate(palavras[:vis]):
        a  = int(255 * pt)
        bb = draw.textbbox((0, 0), p, font=font_t)
        draw.text(((W - bb[2]) // 2, y), p, font=font_t, fill=(*DOURADO, a))
        y += bb[3] + 10

    # Linha separadora
    if pt > 0.4:
        ly = y + 18
        draw.rectangle([int(W * 0.18), ly, int(W * 0.82), ly + 2],
                       fill=(*CIANO, int(200 * pt)))
        y = ly + 28

    # Subtítulo
    font_s  = get_font(34, bold=True)
    linhas  = wrap_text(draw, dados["subtitulo"], font_s, W - 120)
    draw_text_lines(draw, linhas, 60, y, font_s, BRANCO, "center", int(255 * ps))

    canvas = Image.alpha_composite(canvas, layer)
    canvas = add_rodape(canvas)
    canvas = add_logo(canvas)
    canvas = fade_overlay(canvas, pfo)
    return np.array(canvas.convert("RGB"))


# ════════════════════════════════════════════════════════════
# SLIDE 2 — CAUSA RAIZ
# ════════════════════════════════════════════════════════════

def frame_s2(t, dados):
    pf  = eio(prog(t, 0.0, 0.30))
    pc  = eio(prog(t, 0.3, 0.80))
    pe  = eio(prog(t, 0.8, 1.50))
    pt  = eio(prog(t, 1.5, 2.50))
    pfo = 1.0 - eio(prog(t, 4.5, 5.00))

    canvas = montar_base("placa", pf, int(t * 8) + 100, pc)
    layer  = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw   = ImageDraw.Draw(layer)

    # Contador
    font_c = get_font(26, bold=True)
    a_c    = int(255 * pe)
    draw.rounded_rectangle([W - 140, 50, W - 50, 92],
                            radius=8, outline=(*CIANO, a_c), width=2)
    draw.text((W - 130, 58), "02 / 04", font=font_c, fill=(*CIANO, a_c))

    # Eyebrow
    ey = 80 + int((1 - pe) * 50)
    draw.text((60, ey), "⚡  CAUSA REAL", font=get_font(28, bold=True),
              fill=(*CIANO, a_c))

    # Título
    font_t = get_font(88, bold=True)
    a_t    = int(255 * pt)
    draw.text((60, 155), "A CAUSA", font=font_t, fill=(*BRANCO, a_t))
    draw.text((60, 255), "RAIZ",    font=font_t, fill=(*DOURADO, a_t))
    if pt > 0.3:
        draw.rectangle([60, 360, 400, 362], fill=(*CIANO, int(200 * pt)))

    # Bullets com aparecimento progressivo
    font_b = get_font(30)
    for i, causa in enumerate(dados["causas"]):
        ps_b = eio(prog(t, 2.5 + i * 0.65, 3.15 + i * 0.65))
        ab   = int(255 * ps_b)
        by   = 390 + i * 135
        cor  = CIANO if i < 2 else DOURADO
        draw.ellipse([60, by + 10, 84, by + 34], fill=(*cor, ab))
        linhas = wrap_text(draw, causa, font_b, W - 140)
        draw_text_lines(draw, linhas, 100, by, font_b, BRANCO, "left", ab)

    canvas = Image.alpha_composite(canvas, layer)
    canvas = add_rodape(canvas)
    canvas = add_logo(canvas)
    canvas = fade_overlay(canvas, pfo)
    return np.array(canvas.convert("RGB"))


# ════════════════════════════════════════════════════════════
# SLIDE 3 — DIAGNÓSTICO
# ════════════════════════════════════════════════════════════

def frame_s3(t, dados):
    pf  = eio(prog(t, 0.0, 0.30))
    pc  = eio(prog(t, 0.3, 0.80))
    pe  = eio(prog(t, 0.8, 1.50))
    pt  = eio(prog(t, 1.5, 2.50))
    pfo = 1.0 - eio(prog(t, 4.5, 5.00))

    canvas = montar_base(dados["marca"], pf, int(t * 8) + 200, pc)
    layer  = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw   = ImageDraw.Draw(layer)

    # Contador
    a_c    = int(255 * pe)
    font_c = get_font(26, bold=True)
    draw.rounded_rectangle([W - 140, 50, W - 50, 92],
                            radius=8, outline=(*CIANO, a_c), width=2)
    draw.text((W - 130, 58), "03 / 04", font=font_c, fill=(*CIANO, a_c))

    # Eyebrow
    ey = 80 + int((1 - pe) * 50)
    draw.text((60, ey), "⚡  DIAGNÓSTICO", font=get_font(28, bold=True),
              fill=(*CIANO, a_c))

    # Título
    font_t = get_font(80, bold=True)
    a_t    = int(255 * pt)
    draw.text((60, 155), "CHECKLIST",  font=font_t, fill=(*BRANCO, a_t))
    draw.text((60, 247), "NA PRÁTICA", font=font_t, fill=(*DOURADO, a_t))
    if pt > 0.3:
        draw.rectangle([60, 342, 440, 344], fill=(*CIANO, int(200 * pt)))

    # Passos
    font_l = get_font(24, bold=True)
    font_p = get_font(28)
    for i, passo in enumerate(dados["passos"]):
        ps_p  = eio(prog(t, 2.5 + i * 0.9, 3.2 + i * 0.9))
        ap    = int(255 * ps_p)
        py    = 365 + i * 220
        draw.rectangle([60, py, 65, py + 88], fill=(*CIANO, ap))
        draw.text((80, py), f"PASSO {i + 1}", font=font_l, fill=(*CIANO, ap))
        linhas = wrap_text(draw, passo, font_p, W - 140)
        draw_text_lines(draw, linhas, 80, py + 36, font_p, BRANCO, "left", ap)

    canvas = Image.alpha_composite(canvas, layer)
    canvas = add_rodape(canvas)
    canvas = add_logo(canvas)
    canvas = fade_overlay(canvas, pfo)
    return np.array(canvas.convert("RGB"))


# ════════════════════════════════════════════════════════════
# SLIDE 4 — CTA
# ════════════════════════════════════════════════════════════

def frame_s4(t, dados):
    pf    = eio(prog(t, 0.0, 0.30))
    pc    = eio(prog(t, 0.3, 0.80))
    pt    = eio(prog(t, 0.8, 1.80))
    psrv  = eio(prog(t, 1.8, 2.80))
    pcta  = eio(prog(t, 2.8, 3.80))

    canvas = montar_base(dados["marca"], pf, int(t * 8) + 300, pc)
    layer  = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw   = ImageDraw.Draw(layer)

    # Acima
    font_a = get_font(30)
    txt_a  = "ANTES DE CONDENAR,"
    bb     = draw.textbbox((0, 0), txt_a, font=font_a)
    draw.text(((W - bb[2]) // 2, 90), txt_a, font=font_a,
              fill=(*BRANCO, int(180 * pt)))

    # DIAGNOSTIQUE.
    font_d = get_font(92, bold=True)
    txt_d  = "DIAGNOSTIQUE."
    bb     = draw.textbbox((0, 0), txt_d, font=font_d)
    draw.text(((W - bb[2]) // 2, 138), txt_d, font=font_d,
              fill=(*DOURADO, int(255 * pt)))

    if pt > 0.5:
        draw.rectangle([int(W * 0.14), 258, int(W * 0.86), 260],
                       fill=(*CIANO, int(200 * pt)))

    # Linhas de serviço
    font_s  = get_font(30)
    servicos = [
        "Diagnóstico eletrônico em nível de componente.",
        "Laudo técnico detalhado — mesmo sem reparo.",
        "Atendemos todo o Brasil via logística reversa.",
    ]
    for i, srv in enumerate(servicos):
        ps_i = eio(prog(t, 1.8 + i * 0.32, 2.3 + i * 0.32))
        bb   = draw.textbbox((0, 0), srv, font=font_s)
        draw.text(((W - bb[2]) // 2, 280 + i * 50), srv, font=font_s,
                  fill=(*BRANCO, int(200 * ps_i)))

    # Caixa CTA
    cta_y = H - 370
    a_cta = int(255 * pcta)
    draw.rounded_rectangle([80, cta_y, W - 80, cta_y + 185],
                            radius=16, outline=(*CIANO, a_cta), width=2)

    font_wl = get_font(24)
    bb      = draw.textbbox((0, 0), "WHATSAPP", font=font_wl)
    draw.text(((W - bb[2]) // 2, cta_y + 18), "WHATSAPP",
              font=font_wl, fill=(*BRANCO, int(140 * pcta)))

    font_wn = get_font(58, bold=True)
    numero  = "(38) 99912-4889"
    bb      = draw.textbbox((0, 0), numero, font=font_wn)
    draw.text(((W - bb[2]) // 2, cta_y + 58), numero,
              font=font_wn, fill=(*BRANCO, a_cta))

    font_ig = get_font(28)
    bb      = draw.textbbox((0, 0), "@tec_solar_moc", font=font_ig)
    draw.text(((W - bb[2]) // 2, cta_y + 133), "@tec_solar_moc",
              font=font_ig, fill=(*CIANO, int(200 * pcta)))

    canvas = Image.alpha_composite(canvas, layer)
    canvas = add_rodape(canvas)
    canvas = add_logo(canvas)
    return np.array(canvas.convert("RGB"))


# ════════════════════════════════════════════════════════════
# GERAÇÃO DO VÍDEO
# ════════════════════════════════════════════════════════════

def gerar_video(numero_post, caminho_md):
    dados = parse_post(caminho_md)
    print(f"Post {numero_post:02d} — {dados['titulo_seo']}")
    print(f"Marca: {dados['marca']} | Código: {dados['codigo_erro']}")
    print(f"Causas: {dados['causas']}")
    print(f"Passos: {dados['passos']}")

    clips = [
        VideoClip(lambda t, d=dados: frame_s1(t, d), duration=DURACAO_SLIDE),
        VideoClip(lambda t, d=dados: frame_s2(t, d), duration=DURACAO_SLIDE),
        VideoClip(lambda t, d=dados: frame_s3(t, d), duration=DURACAO_SLIDE),
        VideoClip(lambda t, d=dados: frame_s4(t, d), duration=DURACAO_SLIDE),
    ]

    video = concatenate_videoclips(clips)

    pasta = os.path.join(REPO_ROOT, f"carrossel/post-{numero_post:02d}")
    os.makedirs(pasta, exist_ok=True)
    saida = os.path.join(pasta, "video-carrossel.mp4")

    video.write_videofile(
        saida,
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="fast",
        pixel_format="yuv420p",
        ffmpeg_params=["-crf", "28"],
        logger=None,
    )
    print(f"✅  Vídeo salvo: {saida}")
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
