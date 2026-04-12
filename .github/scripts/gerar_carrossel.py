"""
TEC Solar — Gerador de Carrossel Instagram
Versão 4.0 — GitHub Assets + Mix de imagens por contexto
"""

import os
import sys
import requests
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from io import BytesIO

# ============================================================
# BASE URL — GitHub Raw
# ============================================================

BASE = "https://raw.githubusercontent.com/rhuanfmav-code/tec-solar-blog/main/"

# ============================================================
# BANCO DE IMAGENS — GitHub
# ============================================================

FUNDOS = {
    "falha":       BASE + "fundo-raios-falha.png.png",
    "diagnostico": BASE + "fundo-bancada-tech.png.png",
    "componente":  BASE + "fundo-circuitos-ciano.png.png",
    "cta":         BASE + "fundo-energia-restaurada.png.png",
}

# Inversores FECHADOS — capa, CTA, comparativo
INVERSORES_FECHADOS = {
    "fronius":  [
        BASE + "inversor-fronius.png.png",
        BASE + "inversor-fronius.png (2).png",
    ],
    "growatt":  [
        BASE + "inversor-growatt.png.png",
        BASE + "inversor-growatt.png (2).png",
        BASE + "inversor-growatt.png (3).png",
    ],
    "deye":     [
        BASE + "inversor-deye.png.png",
        BASE + "inversor-deye.png (2).png",
    ],
    "sma":      [
        BASE + "inversor-sma.png.png",
        BASE + "inversor-sma.png (2).png",
        BASE + "inversor-sma.png (3).png",
    ],
    "sungrow":  [
        BASE + "inversor-sungrow.png.png",
        BASE + "inversor-sungrow.png (2).png",
        BASE + "inversor-sungrow.png (3).png",
    ],
    "weg":      [
        BASE + "inversor-weg.png.png",
        BASE + "inversor-weg.png (2).png",
    ],
    "canadian": [
        BASE + "inversor-canadian.png.png",
        BASE + "inversor-canadian.png (2).png",
    ],
    "hoymiles": [
        BASE + "inversor-hpymiles.png.png",
        BASE + "inversor-hpymiles.png (2).png",
        BASE + "inversor-hpymiles.png (3).png",
    ],
    "drive":    [
        BASE + "inversor-drive.png.png",
        BASE + "inversor-drive.png (2).png",
    ],
}

# Inversores ABERTOS — slides técnicos (bancada, diagnóstico)
INVERSORES_ABERTOS = {
    "fronius":  [BASE + "inversor-aberto-fronius.png.png"],
    "growatt":  [BASE + "inversor-aberto-growatt.png.png"],
    "deye":     [BASE + "inversor-aberto-deye.png.png"],
    "sma":      [BASE + "inversor-aberto-sma.png.png"],
    "sungrow":  [BASE + "inversor-aberto-sungrow.png.png"],
    "weg":      [BASE + "inversor-aberto-weg.png.png"],
}

# Placas eletrônicas — slide causa raiz
PLACAS = [
    BASE + "placa-eletronica.png.png",
    BASE + "placa-eletronica.png (2).png",
    BASE + "placa-eletronica.png (3).png",
    BASE + "placa-eletronica.png (4).png",
    BASE + "placa-eletronica.png (5).png",
]

# ============================================================
# LÓGICA DE IMAGEM POR SLIDE
# Slide 1 — Capa:       inversor FECHADO
# Slide 2 — Causa raiz: PLACA eletrônica
# Slide 3 — Bancada:    inversor ABERTO
# Slide 4 — Mercado:    inversor FECHADO
# Slide 5 — CTA:        inversor FECHADO
# ============================================================

def get_inversor_fechado(marca, indice=0):
    lista = INVERSORES_FECHADOS.get(marca, INVERSORES_FECHADOS["fronius"])
    return lista[indice % len(lista)]

def get_inversor_aberto(marca):
    lista = INVERSORES_ABERTOS.get(marca)
    if lista:
        return lista[0]
    return get_inversor_fechado(marca, 1)

def get_placa(numero_post):
    return PLACAS[numero_post % len(PLACAS)]

# ============================================================
# CORES TEC SOLAR
# ============================================================

COR_DOURADO  = (245, 166, 35)
COR_CIANO    = (0, 180, 216)
COR_BRANCO   = (255, 255, 255)
COR_VERMELHO = (255, 107, 107)
COR_OVERLAY  = (13, 31, 60, 120)

LARGURA = 1080
ALTURA  = 1350

# ============================================================
# UTILITÁRIOS
# ============================================================

def baixar_imagem(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, timeout=15, headers=headers)
    resp.raise_for_status()
    return Image.open(BytesIO(resp.content)).convert("RGBA")

def get_font(tamanho, bold=False):
    fontes_bold = [
        "/usr/share/fonts/truetype/montserrat/Montserrat-ExtraBold.ttf",
        "/usr/share/fonts/truetype/montserrat/Montserrat-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    fontes_regular = [
        "/usr/share/fonts/truetype/montserrat/Montserrat-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    lista = fontes_bold if bold else fontes_regular
    for caminho in lista:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, tamanho)
    return ImageFont.load_default()

def montar_fundo(url_fundo, url_imagem=None, posicao="centro-baixo"):
    fundo = baixar_imagem(url_fundo).resize((LARGURA, ALTURA), Image.LANCZOS)
    canvas = Image.new("RGBA", (LARGURA, ALTURA))
    canvas.paste(fundo, (0, 0))

    overlay = Image.new("RGBA", (LARGURA, ALTURA), COR_OVERLAY)
    canvas = Image.alpha_composite(canvas, overlay)

    if url_imagem:
        img_item = baixar_imagem(url_imagem)
        max_h = 580
        ratio = max_h / img_item.height
        novo_w = int(img_item.width * ratio)
        img_item = img_item.resize((novo_w, max_h), Image.LANCZOS)

        if img_item.mode != "RGBA":
            img_item = img_item.convert("RGBA")
        r, g, b, a = img_item.split()

        if posicao == "centro-baixo":
            x = (LARGURA - novo_w) // 2
            y = ALTURA - max_h - 80
        elif posicao == "centro":
            x = (LARGURA - novo_w) // 2
            y = (ALTURA - max_h) // 2

        canvas.paste(img_item, (x, y), a)

    return canvas.convert("RGB")

def desenhar_linha(draw, y, cor=None, largura_pct=0.6):
    cor = cor or COR_CIANO
    x1 = int(LARGURA * (1 - largura_pct) / 2)
    x2 = int(LARGURA * (1 - (1 - largura_pct) / 2))
    draw.rectangle([x1, y, x2, y + 2], fill=cor)

def desenhar_texto_wrap(draw, texto, x, y, font, cor, max_largura, alinhamento="left"):
    palavras = texto.split()
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        teste = linha_atual + " " + palavra if linha_atual else palavra
        bbox = draw.textbbox((0, 0), teste, font=font)
        if bbox[2] <= max_largura:
            linha_atual = teste
        else:
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra
    if linha_atual:
        linhas.append(linha_atual)

    y_atual = y
    for linha in linhas:
        if alinhamento == "center":
            bbox = draw.textbbox((0, 0), linha, font=font)
            x_linha = (LARGURA - bbox[2]) // 2
        else:
            x_linha = x
        draw.text((x_linha, y_atual), linha, font=font, fill=cor)
        bbox = draw.textbbox((0, 0), linha, font=font)
        y_atual += bbox[3] + 8
    return y_atual

def rodape(draw):
    font = get_font(24)
    texto = "REPARO  ·  DIAGNÓSTICO  ·  MANUTENÇÃO"
    bbox = draw.textbbox((0, 0), texto, font=font)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, ALTURA - 60), texto, font=font, fill=(255, 255, 255, 90))

def salvar(img, numero_post, numero_slide):
    pasta = f"carrossel/post-{numero_post:02d}"
    os.makedirs(pasta, exist_ok=True)
    caminho = f"{pasta}/slide-{numero_slide}.png"
    img.save(caminho, "PNG")
    print(f"✅ Salvo: {caminho}")
    return caminho

# ============================================================
# DETECTAR MARCA
# ============================================================

def detectar_marca(titulo):
    titulo_lower = titulo.lower()
    for marca in INVERSORES_FECHADOS.keys():
        if marca in titulo_lower:
            return marca
    return None

# ============================================================
# SLIDE 1 — CAPA (inversor fechado)
# ============================================================

def gerar_slide_1(dados, numero_post, marca):
    url_inv = get_inversor_fechado(marca, 0) if marca else None
    img = montar_fundo(FUNDOS["falha"], url_inv, "centro-baixo")
    draw = ImageDraw.Draw(img)

    font_tag = get_font(26, bold=True)
    tag_texto = f"⚡  {dados.get('categoria', 'CÓDIGO DE ERRO').upper()}"
    bbox = draw.textbbox((0, 0), tag_texto, font=font_tag)
    tag_w = bbox[2] + 40
    tag_h = bbox[3] + 20
    tag_x, tag_y = 60, 70
    draw.rounded_rectangle([tag_x, tag_y, tag_x + tag_w, tag_y + tag_h],
                            radius=20, outline=COR_CIANO, width=2)
    draw.text((tag_x + 20, tag_y + 10), tag_texto, font=font_tag, fill=COR_CIANO)

    y = tag_y + tag_h + 28
    font_titulo = get_font(88, bold=True)
    for linha_key in ["titulo_linha1", "titulo_linha2"]:
        linha = dados.get(linha_key, "").upper()
        bbox = draw.textbbox((0, 0), linha, font=font_titulo)
        x = (LARGURA - bbox[2]) // 2
        draw.text((x, y), linha, font=font_titulo, fill=COR_DOURADO)
        y += bbox[3] + 10

    y += 14
    desenhar_linha(draw, y)
    y += 28

    font_sub = get_font(34, bold=True)
    for sub_key in ["subtitulo1", "subtitulo2"]:
        sub = dados.get(sub_key, "")
        bbox = draw.textbbox((0, 0), sub, font=font_sub)
        x = (LARGURA - bbox[2]) // 2
        draw.text((x, y), sub, font=font_sub, fill=COR_BRANCO)
        y += bbox[3] + 10

    rodape(draw)
    return salvar(img, numero_post, 1)

# ============================================================
# SLIDE 2 — CAUSA RAIZ (placa eletrônica)
# ============================================================

def gerar_slide_2(dados, numero_post, marca):
    img = montar_fundo(FUNDOS["componente"], get_placa(numero_post), "centro-baixo")
    draw = ImageDraw.Draw(img)

    font_cont = get_font(26, bold=True)
    draw.rounded_rectangle([LARGURA - 140, 50, LARGURA - 50, 90],
                            radius=8, outline=COR_CIANO, width=2)
    draw.text((LARGURA - 130, 56), "02 / 05", font=font_cont, fill=COR_CIANO)

    y = 90
    font_titulo = get_font(72, bold=True)
    draw.text((60, y), "A CAUSA", font=font_titulo, fill=COR_BRANCO)
    y += 85
    draw.text((60, y), "RAIZ", font=font_titulo, fill=COR_DOURADO)
    y += 90

    desenhar_linha(draw, y, largura_pct=0.4)
    y += 30

    font_bullet = get_font(30)
    causas = [
        (dados.get("causa1", ""), COR_CIANO),
        (dados.get("causa2", ""), COR_CIANO),
        (dados.get("causa_principal", ""), COR_DOURADO),
    ]
    for texto, cor_bullet in causas:
        draw.ellipse([60, y + 8, 82, y + 30], fill=cor_bullet)
        y = desenhar_texto_wrap(draw, texto, 100, y, font_bullet, COR_BRANCO, 880)
        y += 16

    rodape(draw)
    return salvar(img, numero_post, 2)

# ============================================================
# SLIDE 3 — BANCADA (inversor aberto)
# ============================================================

def gerar_slide_3(dados, numero_post, marca):
    url_inv = get_inversor_aberto(marca) if marca else None
    img = montar_fundo(FUNDOS["diagnostico"], url_inv, "centro-baixo")
    draw = ImageDraw.Draw(img)

    font_cont = get_font(26, bold=True)
    draw.rounded_rectangle([LARGURA - 140, 50, LARGURA - 50, 90],
                            radius=8, outline=COR_CIANO, width=2)
    draw.text((LARGURA - 130, 56), "03 / 05", font=font_cont, fill=COR_CIANO)

    y = 90
    font_titulo = get_font(72, bold=True)
    draw.text((60, y), "NA", font=font_titulo, fill=COR_BRANCO)
    y += 85
    draw.text((60, y), "BANCADA", font=font_titulo, fill=COR_DOURADO)
    y += 90

    desenhar_linha(draw, y, largura_pct=0.4)
    y += 30

    font_label = get_font(24, bold=True)
    font_texto = get_font(28)
    passos = [
        ("PASSO 1", dados.get("passo1", ""), COR_CIANO),
        ("PASSO 2", dados.get("passo2", ""), COR_CIANO),
        ("⚠ SINAL FÍSICO", dados.get("sinal_fisico", ""), COR_DOURADO),
    ]
    for label, texto, cor in passos:
        draw.rectangle([60, y, 65, y + 90], fill=cor)
        draw.text((80, y + 5), label, font=font_label, fill=cor)
        y_fim = desenhar_texto_wrap(draw, texto, 80, y + 38, font_texto, COR_BRANCO, 900)
        y = max(y_fim, y + 95) + 16

    rodape(draw)
    return salvar(img, numero_post, 3)

# ============================================================
# SLIDE 4 — MERCADO (inversor fechado)
# ============================================================

def gerar_slide_4(dados, numero_post, marca):
    url_inv = get_inversor_fechado(marca, 0) if marca else None
    img = montar_fundo(FUNDOS["falha"], url_inv, "centro-baixo")
    draw = ImageDraw.Draw(img)

    font_cont = get_font(26, bold=True)
    draw.rounded_rectangle([LARGURA - 140, 50, LARGURA - 50, 90],
                            radius=8, outline=COR_CIANO, width=2)
    draw.text((LARGURA - 130, 56), "04 / 05", font=font_cont, fill=COR_CIANO)

    y = 90
    font_titulo = get_font(60, bold=True)
    draw.text((60, y), "O MERCADO CONDENA.", font=font_titulo, fill=COR_BRANCO)
    y += 72
    draw.text((60, y), "A TEC SOLAR REPARA.", font=font_titulo, fill=COR_DOURADO)
    y += 80

    desenhar_linha(draw, y, cor=COR_DOURADO, largura_pct=0.4)
    y += 30

    font_texto = get_font(28)
    erro = dados.get("texto_erro_mercado", "")
    draw.rounded_rectangle([55, y, LARGURA - 55, y + 140],
                            radius=10, fill=(255, 255, 255, 20))
    y_fim = desenhar_texto_wrap(draw, erro, 80, y + 20, font_texto, COR_BRANCO, 900)
    y = max(y_fim, y + 145) + 30

    font_label = get_font(24)
    font_valor = get_font(56, bold=True)
    font_sub   = get_font(22)
    bloco_w, bloco_h, gap = 440, 160, 20
    x_esq = 55
    x_dir = x_esq + bloco_w + gap

    draw.rounded_rectangle([x_esq, y, x_esq + bloco_w, y + bloco_h],
                            radius=10, outline=COR_VERMELHO, width=2)
    draw.text((x_esq + 20, y + 16), "TROCA", font=font_label, fill=COR_BRANCO)
    draw.text((x_esq + 20, y + 50), dados.get("valor_troca", "R$ 4.500"),
              font=font_valor, fill=COR_VERMELHO)
    draw.text((x_esq + 20, y + 120), "inversor novo", font=font_sub, fill=COR_BRANCO)

    draw.rounded_rectangle([x_dir, y, x_dir + bloco_w, y + bloco_h],
                            radius=10, outline=COR_CIANO, width=2)
    draw.text((x_dir + 20, y + 16), "REPARO", font=font_label, fill=COR_BRANCO)
    draw.text((x_dir + 20, y + 50), dados.get("valor_reparo", "R$ 600"),
              font=font_valor, fill=COR_CIANO)
    draw.text((x_dir + 20, y + 120), "TEC Solar", font=font_sub, fill=COR_BRANCO)

    rodape(draw)
    return salvar(img, numero_post, 4)

# ============================================================
# SLIDE 5 — CTA (inversor fechado)
# ============================================================

def gerar_slide_5(dados, numero_post, marca):
    url_inv = get_inversor_fechado(marca, -1) if marca else None
    img = montar_fundo(FUNDOS["cta"], url_inv, "centro")
    draw = ImageDraw.Draw(img)

    font_acima = get_font(28)
    texto_acima = "ANTES DE CONDENAR,"
    bbox = draw.textbbox((0, 0), texto_acima, font=font_acima)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, 80), texto_acima, font=font_acima, fill=(255, 255, 255, 100))

    font_diag = get_font(88, bold=True)
    texto_diag = "DIAGNOSTIQUE."
    bbox = draw.textbbox((0, 0), texto_diag, font=font_diag)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, 130), texto_diag, font=font_diag, fill=COR_DOURADO)

    desenhar_linha(draw, 240)

    font_apoio = get_font(30)
    for i, apoio in enumerate([
        "Laudo técnico completo em nível de placa.",
        "Atendemos todo o Brasil via logística reversa."
    ]):
        bbox = draw.textbbox((0, 0), apoio, font=font_apoio)
        x = (LARGURA - bbox[2]) // 2
        draw.text((x, 270 + i * 44), apoio, font=font_apoio, fill=(255, 255, 255, 190))

    caixa_y = ALTURA - 340
    draw.rounded_rectangle([100, caixa_y, LARGURA - 100, caixa_y + 160],
                            radius=16, outline=COR_CIANO, width=2)

    font_wlabel = get_font(24)
    bbox = draw.textbbox((0, 0), "WHATSAPP", font=font_wlabel)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, caixa_y + 18), "WHATSAPP", font=font_wlabel, fill=(255, 255, 255, 100))

    font_wnum = get_font(56, bold=True)
    numero = dados.get("whatsapp", "(38) 99889-1587")
    bbox = draw.textbbox((0, 0), numero, font=font_wnum)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, caixa_y + 60), numero, font=font_wnum, fill=COR_BRANCO)

    font_ig = get_font(26)
    ig = "@tec_solar_moc"
    bbox = draw.textbbox((0, 0), ig, font=font_ig)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, caixa_y + 178), ig, font=font_ig, fill=(255, 255, 255, 80))

    rodape(draw)
    return salvar(img, numero_post, 5)

# ============================================================
# FUNÇÃO PRINCIPAL
# ============================================================

def gerar_carrossel(numero_post, dados):
    print(f"\n🚀 Gerando carrossel — Post {numero_post:02d}")
    marca = detectar_marca(
        dados.get("titulo_linha1", "") + " " + dados.get("titulo_linha2", "")
    )
    print(f"   Marca detectada: {marca or 'genérico'}")

    gerar_slide_1(dados, numero_post, marca)
    gerar_slide_2(dados, numero_post, marca)
    gerar_slide_3(dados, numero_post, marca)
    gerar_slide_4(dados, numero_post, marca)
    gerar_slide_5(dados, numero_post, marca)

    print(f"\n✅ Carrossel completo: carrossel/post-{numero_post:02d}/")

# ============================================================
# ENTRADA
# ============================================================

if __name__ == "__main__":
    numero_post = int(sys.argv[1]) if len(sys.argv) > 1 else 2

    dados = {
        "titulo_linha1":      os.environ.get("TITULO_L1", "FRONIUS"),
        "titulo_linha2":      os.environ.get("TITULO_L2", "STATE 102"),
        "categoria":          os.environ.get("CATEGORIA", "CÓDIGO DE ERRO"),
        "subtitulo1":         os.environ.get("SUBTITULO1", "Tensão CC Alta:"),
        "subtitulo2":         os.environ.get("SUBTITULO2", "causa real e diagnóstico"),
        "causa1":             os.environ.get("CAUSA1", "String mal dimensionada"),
        "causa2":             os.environ.get("CAUSA2", "Temperatura baixa elevando o Voc"),
        "causa_principal":    os.environ.get("CAUSA_PRINCIPAL", "Deriva do ADC no divisor resistivo"),
        "passo1":             os.environ.get("PASSO1", "Meça a tensão CC com string fria"),
        "passo2":             os.environ.get("PASSO2", "Meça resistência do divisor"),
        "sinal_fisico":       os.environ.get("SINAL_FISICO", "Resistores SMD escurecidos"),
        "texto_erro_mercado": os.environ.get("TEXTO_ERRO", "Técnico troca o inversor sem diagnosticar a causa real."),
        "valor_troca":        os.environ.get("VALOR_TROCA", "R$ 7.000"),
        "valor_reparo":       os.environ.get("VALOR_REPARO", "R$ 600"),
        "whatsapp":           "(38) 99889-1587",
    }

    gerar_carrossel(numero_post, dados)
