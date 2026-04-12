"""
TEC Solar — Gerador de Carrossel Instagram
Versão 3.0 — Imagens reais de inversores + Python Pillow
"""

import os
import sys
import requests
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from io import BytesIO
import textwrap

# ============================================================
# BANCO DE IMAGENS REAIS — POSTIMG.CC
# ============================================================

FUNDOS = {
    "falha":      "https://i.postimg.cc/Ty2GJZMC/fundo-raios-falha-png.png",
    "diagnostico":"https://i.postimg.cc/qtB0x9Vc/fundo-bancada-tech-png.png",
    "componente": "https://i.postimg.cc/Z9YZx1tH/fundo-circuitos-ciano-png.png",
    "cta":        "https://i.postimg.cc/Y42kzJK8/fundo-energia-restaurada-png.png",
}

INVERSORES = {
    "fronius":   [
        "https://i.postimg.cc/XZN3kT6S/Inversor-Fronius.png",
        "https://i.postimg.cc/XZ2WHQnY/Inversor-Fronius-(2).png",
        "https://i.postimg.cc/FfPvWDhK/Inversor-Fronius-(3).png",
    ],
    "growatt":   [
        "https://i.postimg.cc/f3WZf6QM/Inversor-Growatt.png",
        "https://i.postimg.cc/wtWzf097/Inversor-Growatt-(2).png",
    ],
    "deye":      [
        "https://i.postimg.cc/B8ZsBdfs/Inversor-Deye.png",
        "https://i.postimg.cc/Z9fm7VJR/Inversor-Deye-(2).png",
    ],
    "sma":       [
        "https://i.postimg.cc/Y42kzJBM/Inversor-SMA.png",
        "https://i.postimg.cc/WDpjwQc2/Inversor-SMA-(2).png",
    ],
    "sungrow":   [
        "https://i.postimg.cc/Lq4R3rF9/Inversor-Sungrow.png",
        "https://i.postimg.cc/v1Pyq3bJ/Inversor-Sungrow-(2).png",
    ],
    "weg":       [
        "https://i.postimg.cc/gwcdHfbk/Inversor-Weg.png",
        "https://i.postimg.cc/hJCnypKW/inversor-Weg-(2).png",
    ],
    "canadian":  [
        "https://i.postimg.cc/p90vGqPN/Inversor-Canadian.png",
        "https://i.postimg.cc/NyNtJpQv/Inversor-Canadian-(2).png",
        "https://i.postimg.cc/8FyGKtTG/Inversor-Canadian-(3).png",
    ],
    "hoymiles":  [
        "https://i.postimg.cc/FfPvWDhm/Inversor-hoymiles.png",
        "https://i.postimg.cc/Tykx7CTT/Inversor-hoymiles-(2).png",
    ],
    "abb":       [
        "https://i.postimg.cc/NyNtJpQg/Inversor-ABB.png",
        "https://i.postimg.cc/xksQxt9T/Inversor-ABB-(2).png",
        "https://i.postimg.cc/WD9VWXsp/Inversor-ABB-(3).png",
    ],
}

PLACAS = [
    "https://i.postimg.cc/McZxmhJk/Placa-Eletronica.png",
    "https://i.postimg.cc/mcZRy0fv/Placa-eletronica-(2).png",
    "https://i.postimg.cc/qtB0x9VW/Placa-eletronica-(3).png",
    "https://i.postimg.cc/5H91SZdG/Placa-eletronica-(4).png",
    "https://i.postimg.cc/4K4ZQrkW/Placa-eletronica-(5).png",
]

# ============================================================
# CORES TEC SOLAR
# ============================================================

COR_FUNDO      = (13, 31, 60)
COR_DOURADO    = (245, 166, 35)
COR_CIANO      = (0, 180, 216)
COR_BRANCO     = (255, 255, 255)
COR_VERMELHO   = (255, 107, 107)
COR_OVERLAY    = (13, 31, 60, 120)

LARGURA  = 1080
ALTURA   = 1350

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

def montar_fundo(url_fundo, url_inversor=None, posicao="centro-baixo"):
    fundo = baixar_imagem(url_fundo).resize((LARGURA, ALTURA), Image.LANCZOS)
    canvas = Image.new("RGBA", (LARGURA, ALTURA))
    canvas.paste(fundo, (0, 0))

    overlay = Image.new("RGBA", (LARGURA, ALTURA), COR_OVERLAY)
    canvas = Image.alpha_composite(canvas, overlay)

    if url_inversor:
        inversor = baixar_imagem(url_inversor)
        max_h = 580
        ratio = max_h / inversor.height
        novo_w = int(inversor.width * ratio)
        inversor = inversor.resize((novo_w, max_h), Image.LANCZOS)

        if inversor.mode != "RGBA":
            inversor = inversor.convert("RGBA")
        r, g, b, a = inversor.split()

        if posicao == "centro-baixo":
            x = (LARGURA - novo_w) // 2
            y = ALTURA - max_h - 80
        elif posicao == "centro":
            x = (LARGURA - novo_w) // 2
            y = (ALTURA - max_h) // 2

        canvas.paste(inversor, (x, y), a)

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
# DETECTAR MARCA DO POST
# ============================================================

def detectar_marca(titulo):
    titulo_lower = titulo.lower()
    for marca in INVERSORES.keys():
        if marca in titulo_lower:
            return marca
    return None

# ============================================================
# SLIDE 1 — CAPA
# ============================================================

def gerar_slide_1(dados, numero_post, marca):
    url_fundo = FUNDOS["falha"]
    url_inversor = INVERSORES.get(marca, INVERSORES["fronius"])[0] if marca else None

    img = montar_fundo(url_fundo, url_inversor, "centro-baixo")
    draw = ImageDraw.Draw(img)

    font_tag = get_font(26, bold=True)
    tag_texto = f"⚡  {dados.get('categoria', 'CÓDIGO DE ERRO').upper()}"
    bbox = draw.textbbox((0, 0), tag_texto, font=font_tag)
    tag_w = bbox[2] + 40
    tag_h = bbox[3] + 20
    tag_x = 60
    tag_y = 70
    draw.rounded_rectangle([tag_x, tag_y, tag_x + tag_w, tag_y + tag_h],
                            radius=20, outline=COR_CIANO, width=2)
    draw.text((tag_x + 20, tag_y + 10), tag_texto, font=font_tag, fill=COR_CIANO)

    y = tag_y + tag_h + 28
    font_titulo = get_font(88, bold=True)
    linha1 = dados.get("titulo_linha1", "").upper()
    bbox = draw.textbbox((0, 0), linha1, font=font_titulo)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, y), linha1, font=font_titulo, fill=COR_DOURADO)
    y += bbox[3] + 10

    linha2 = dados.get("titulo_linha2", "").upper()
    bbox = draw.textbbox((0, 0), linha2, font=font_titulo)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, y), linha2, font=font_titulo, fill=COR_DOURADO)
    y += bbox[3] + 24

    desenhar_linha(draw, y)
    y += 28

    font_sub = get_font(34, bold=True)
    sub1 = dados.get("subtitulo1", "")
    sub2 = dados.get("subtitulo2", "")
    bbox = draw.textbbox((0, 0), sub1, font=font_sub)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, y), sub1, font=font_sub, fill=COR_BRANCO)
    y += bbox[3] + 10
    bbox = draw.textbbox((0, 0), sub2, font=font_sub)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, y), sub2, font=font_sub, fill=COR_BRANCO)

    rodape(draw)
    return salvar(img, numero_post, 1)

# ============================================================
# SLIDE 2 — CAUSA RAIZ
# ============================================================

def gerar_slide_2(dados, numero_post, marca):
    url_fundo = FUNDOS["componente"]
    url_placa = PLACAS[numero_post % len(PLACAS)]

    img = montar_fundo(url_fundo, url_placa, "centro-baixo")
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
# SLIDE 3 — COMO IDENTIFICAR NA PRÁTICA
# ============================================================

def gerar_slide_3(dados, numero_post, marca):
    url_fundo = FUNDOS["diagnostico"]
    url_inversor = INVERSORES.get(marca, INVERSORES["fronius"])[
        min(1, len(INVERSORES.get(marca, [])) - 1)
    ] if marca else None

    img = montar_fundo(url_fundo, url_inversor, "centro-baixo")
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
# SLIDE 4 — ERRO DO MERCADO
# ============================================================

def gerar_slide_4(dados, numero_post, marca):
    url_fundo = FUNDOS["falha"]
    url_inversor = INVERSORES.get(marca, INVERSORES["fronius"])[0] if marca else None

    img = montar_fundo(url_fundo, url_inversor, "centro-baixo")
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

    font_label  = get_font(24)
    font_valor  = get_font(56, bold=True)
    font_sub    = get_font(22)
    bloco_w     = 440
    bloco_h     = 160
    gap         = 20
    x_esq       = 55
    x_dir       = x_esq + bloco_w + gap

    draw.rounded_rectangle([x_esq, y, x_esq + bloco_w, y + bloco_h],
                            radius=10, outline=COR_VERMELHO, width=2)
    draw.text((x_esq + 20, y + 16), "TROCA", font=font_label, fill=COR_BRANCO)
    draw.text((x_esq + 20, y + 50), dados.get("valor_troca", "R$4.500"),
              font=font_valor, fill=COR_VERMELHO)
    draw.text((x_esq + 20, y + 120), "inversor novo", font=font_sub, fill=COR_BRANCO)

    draw.rounded_rectangle([x_dir, y, x_dir + bloco_w, y + bloco_h],
                            radius=10, outline=COR_CIANO, width=2)
    draw.text((x_dir + 20, y + 16), "REPARO", font=font_label, fill=COR_BRANCO)
    draw.text((x_dir + 20, y + 50), dados.get("valor_reparo", "R$600"),
              font=font_valor, fill=COR_CIANO)
    draw.text((x_dir + 20, y + 120), "TEC Solar", font=font_sub, fill=COR_BRANCO)

    rodape(draw)
    return salvar(img, numero_post, 4)

# ============================================================
# SLIDE 5 — CTA FINAL
# ============================================================

def gerar_slide_5(dados, numero_post, marca):
    url_fundo = FUNDOS["cta"]
    url_inversor = INVERSORES.get(marca, INVERSORES["fronius"])[-1] if marca else None

    img = montar_fundo(url_fundo, url_inversor, "centro")
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
    apoio1 = "Laudo técnico completo em nível de placa."
    apoio2 = "Atendemos todo o Brasil via logística reversa."
    bbox = draw.textbbox((0, 0), apoio1, font=font_apoio)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, 270), apoio1, font=font_apoio, fill=(255, 255, 255, 190))
    bbox = draw.textbbox((0, 0), apoio2, font=font_apoio)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, 314), apoio2, font=font_apoio, fill=(255, 255, 255, 190))

    caixa_y = ALTURA - 340
    draw.rounded_rectangle([100, caixa_y, LARGURA - 100, caixa_y + 160],
                            radius=16, outline=COR_CIANO, width=2)

    font_wlabel = get_font(24)
    texto_wl = "WHATSAPP"
    bbox = draw.textbbox((0, 0), texto_wl, font=font_wlabel)
    x = (LARGURA - bbox[2]) // 2
    draw.text((x, caixa_y + 18), texto_wl, font=font_wlabel, fill=(255, 255, 255, 100))

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
