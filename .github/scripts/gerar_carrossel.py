"""
Script de geração de carrossel Instagram via DALL-E 3
TEC Solar — Centro Técnico de Inversores Solares

Uso: python3 gerar_carrossel.py <numero_post>
Exemplo: python3 gerar_carrossel.py 02
"""

import requests
import os
import sys
import time

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("ERRO: variável OPENAI_API_KEY não encontrada.")
    sys.exit(1)

# ──────────────────────────────────────────────
# PROMPTS POR POST
# ──────────────────────────────────────────────

POSTS = {
    "02": {
        "titulo": "Fronius State 102 — Tensão CC Muito Alta",
        "prompts": [
            # SLIDE 1 — CAPA
            """Generate a single standalone vertical Instagram post image.
Format: 1080x1350 pixels, 4:5 ratio, PNG.
This is image 1 of 5 — deliver as individual file only, never merged.
BACKGROUND: Very dark navy blue exactly #0D1F3C covering entire image.
Dense glowing PCB circuit board traces in cyan #00B4D8 and golden #F5A623
covering the entire background like a giant motherboard — thin traces with
bright connection nodes, exactly like @tec_solar_moc Instagram posts.
Bright scattered light dots as tech stars across the background.
MAIN VISUAL CENTER-BOTTOM (occupying 55% image height, lower half):
Fronius Symo on-grid solar inverter — white/gray metallic casing, LCD display on front panel, DC connection terminals at bottom — floating in dramatic 3/4 perspective above glowing PCB surface.
Cyan electric arcs and fault sparks radiating from both sides of inverter.
Golden energy sparks exploding around it.
Intense cyan glow halo behind the inverter.
Top 40% of image is clear space for text.
TEXT OVERLAY — top area, left-aligned, 60px left margin:
Row 1 small tag inside rounded rectangle with cyan border:
lightning bolt emoji + 'CÓDIGO DE ERRO'
Montserrat Bold uppercase, cyan #00B4D8, small, wide letter-spacing.
Row 2-3 main title very large impactful (2 lines):
'STATE 102' — Montserrat Black uppercase, golden #F5A623, ~90px
'FRONIUS' — Montserrat Black uppercase, golden #F5A623, ~90px
Thin horizontal cyan #00B4D8 line separator, 60% image width.
Row 4-5 subtitle (2 lines):
'Tensão CC Alta —'
'String ou Sensor com Defeito?'
Montserrat SemiBold, white #FFFFFF, medium size.
BOTTOM FOOTER centered:
'REPARO · DIAGNÓSTICO · MANUTENÇÃO'
Montserrat Regular, white 35% opacity, very wide letter-spacing.
BOTTOM-RIGHT CORNER: Completely empty clean space 120x120px.
No star, no ornament, no symbol — just empty space for logo.
Ultra HD photorealistic cinematic tech premium.
DO NOT merge with other images. Single file only.""",

            # SLIDE 2 — CAUSA RAIZ
            """Generate a single standalone vertical Instagram post image.
Format: 1080x1350 pixels, 4:5 ratio, PNG.
This is image 2 of 5 — deliver as individual file only, never merged.
BACKGROUND: Very dark navy blue exactly #0D1F3C covering entire image.
Dense glowing PCB circuit board traces in cyan #00B4D8 and golden #F5A623
covering entire background like giant motherboard with bright connection nodes.
MAIN VISUAL CENTER-BOTTOM (60% image height, lower half):
Extreme close-up of solar inverter power circuit board opened and exposed,
isometric perspective slightly tilted for depth.
Visible components in high detail: cylindrical electrolytic capacitors,
IGBT transistors in TO-247 package, toroidal transformer,
central DSP microchip, SMD resistors and capacitors.
High-value resistors near DC input connectors with subtle amber/orange glow
indicating thermal drift degradation.
PCB traces illuminated in cyan showing current path.
Thin cyan light threads leaking between components — visual effect of false voltage reading signal.
Top 40% clear for text overlay.
TEXT OVERLAY — top, left-aligned:
Small counter inside rounded rectangle with cyan border:
'02 / 05' — Montserrat Bold, cyan #00B4D8, small size.
Title 2 lines large:
'A CAUSA' — Montserrat Black uppercase, white #FFFFFF, large
'RAIZ' — Montserrat Black uppercase, golden #F5A623, large
Thin cyan separator line.
3 bullet points stacked:
● cyan filled circle 'String dimensionada sem coeficiente de temperatura — Voc elevada no frio'
● cyan filled circle 'Inversor opera fora do limite por meses sem que o erro seja percebido'
● golden filled circle 'Resistores do divisor de tensão com deriva — leitura falsa no ADC'
Montserrat Medium, white, medium size.
Third bullet uses golden circle — it is the most critical cause.
BOTTOM FOOTER: 'REPARO · DIAGNÓSTICO · MANUTENÇÃO'
Montserrat Regular, white 35% opacity, very wide letter-spacing.
BOTTOM-RIGHT CORNER: Completely empty clean 120x120px space. No logo. No ornament.
Ultra HD photorealistic cinematic tech premium.
DO NOT merge with other images. Single file only.""",

            # SLIDE 3 — COMO IDENTIFICAR NA PRÁTICA
            """Generate a single standalone vertical Instagram post image.
Format: 1080x1350 pixels, 4:5 ratio, PNG.
This is image 3 of 5 — deliver as individual file only, never merged.
BACKGROUND: Very dark navy blue exactly #0D1F3C with dense glowing
cyan and golden PCB circuit traces covering entire background.
MAIN VISUAL CENTER-BOTTOM (lower half of image):
Electronics technician hands wearing dark gray work gloves holding
a professional yellow or red digital multimeter
(high voltage rated, digital display, black test probes)
pressed against DC input terminals of an open Fronius solar inverter
circuit board on professional electronics lab workbench.
Background softly blurred: oscilloscope with glowing waveform screen,
professional soldering iron, LED illuminated magnifying glass.
Cyan diagnostic light beam shooting from multimeter probes
scanning components like a diagnostic scanner.
Subtle golden sparks at measurement point.
Top clear for text overlay.
TEXT OVERLAY — top, left-aligned:
Counter inside cyan border rectangle:
'03 / 05' — Montserrat Bold, cyan #00B4D8, small.
Title 2 lines:
'NA' — Montserrat Black uppercase, white #FFFFFF, large
'BANCADA' — Montserrat Black uppercase, golden #F5A623, large
Thin cyan separator line.
3 stacked information boxes with left border accent:
BOX 1 — 3px cyan left border, very subtle cyan transparent background:
Label: 'PASSO 1' Montserrat Bold cyan uppercase small wide letter-spacing
Text: 'Medir tensão CC na entrada com multímetro calibrado e comparar com o histórico do display'
Montserrat Regular, white, medium size.
BOX 2 — 3px cyan left border, subtle cyan transparent background:
Label: 'PASSO 2' Montserrat Bold cyan uppercase small
Text: 'Localizar resistores do divisor de tensão na placa de controle e medir em modo de resistência'
Montserrat Regular, white, medium size.
BOX 3 — 3px golden left border, very subtle golden transparent background:
Label: '⚠ SINAL FÍSICO' Montserrat Bold golden uppercase small
Text: 'Multímetro lê tensão dentro do limite, mas inversor reporta valor acima — defeito no circuito de medição'
Montserrat Regular, white, medium size.
BOTTOM FOOTER: 'REPARO · DIAGNÓSTICO · MANUTENÇÃO'
Montserrat Regular, white 35% opacity, very wide letter-spacing.
BOTTOM-RIGHT CORNER: Completely empty clean 120x120px. No logo. No ornament.
Ultra HD photorealistic cinematic tech premium.
DO NOT merge with other images. Single file only.""",

            # SLIDE 4 — O ERRO DO MERCADO
            """Generate a single standalone vertical Instagram post image.
Format: 1080x1350 pixels, 4:5 ratio, PNG.
This is image 4 of 5 — deliver as individual file only, never merged.
BACKGROUND: Very dark navy blue exactly #0D1F3C with dense glowing
cyan and golden PCB circuit traces covering entire background.
MAIN VISUAL CENTER (central portion of image):
Two Fronius solar inverters side by side,
divided by vertical white/cyan light beam in exact center of image.
LEFT inverter: dead, cold gray color, no energy, dark shadows,
deteriorated look, subtle red X symbol above it.
RIGHT inverter: vibrant, cyan energy explosion bursting from inside,
golden glow radiating outward, illuminated display,
light rays expanding outward in all directions.
Upper and lower image areas free for text overlay.
TEXT OVERLAY:
Top centered:
Counter '04 / 05' — cyan border tag same style.
Title 2 lines centered:
'O MERCADO CONDENA.' — Montserrat Black uppercase, white #FFFFFF, large
'A TEC SOLAR REPARA.' — Montserrat Black uppercase, golden #F5A623, large
Golden centered separator line.
Dark translucent box with subtle white border centered:
'Técnico mede tensão acima do limite, condena o inversor e troca por novo — sem verificar se é medição falsa ou string mal dimensionada. O problema se repete.'
Montserrat Regular, white 85% opacity, medium size.
Two comparison blocks side by side bottom area:
LEFT block — red #ff6b6b border, subtle red transparent background:
Label 'TROCA' Montserrat Regular white small uppercase
Value 'R$ 7.000' Montserrat ExtraBold #ff6b6b large
Sub 'inversor novo' Montserrat Regular white small
RIGHT block — cyan #00B4D8 border, subtle cyan transparent background:
Label 'REPARO' Montserrat Regular white small uppercase
Value 'R$ 600' Montserrat ExtraBold cyan #00B4D8 large
Sub 'TEC Solar' Montserrat Regular white small
BOTTOM FOOTER: 'REPARO · DIAGNÓSTICO · MANUTENÇÃO'
Montserrat Regular, white 35% opacity, very wide letter-spacing.
BOTTOM-RIGHT CORNER: Completely empty clean 120x120px. No logo. No ornament.
Ultra HD photorealistic cinematic tech premium.
DO NOT merge with other images. Single file only.""",

            # SLIDE 5 — CTA FINAL
            """Generate a single standalone vertical Instagram post image.
Format: 1080x1350 pixels, 4:5 ratio, PNG.
This is image 5 of 5 — deliver as individual file only, never merged.
BACKGROUND: Very dark navy blue exactly #0D1F3C with MAXIMUM INTENSITY
dense glowing cyan #00B4D8 and golden #F5A623 PCB circuit traces
covering every area of the background at full brightness.
MAIN VISUAL CENTER:
Fronius Symo on-grid solar inverter — white/gray metallic casing, LCD display on front panel
Centered and slightly elevated, presented like a technical trophy.
MAXIMUM energy explosion: cyan and golden light bursting from
inverter center in all directions simultaneously,
very long light rays reaching all four image edges,
floating golden and cyan energy particles everywhere around the inverter,
premium tech lens flare effects at corners and image edges.
Clear space in top and bottom areas for text overlay.
TEXT OVERLAY:
Top centered:
Small spaced text: 'ANTES DE CONDENAR,'
Montserrat Bold uppercase, white 40% opacity, very wide letter-spacing, small.
Main title 1 line very large impactful:
'DIAGNOSTIQUE.'
Montserrat Black uppercase, golden #F5A623, very large size,
subtle golden glow shadow effect around letters.
Thin cyan centered separator line below title.
Support text 2 lines centered:
'Laudo técnico completo em nível de placa.'
'Atendemos todo o Brasil via logística reversa.'
Montserrat Regular, white 75% opacity, medium size, generous line-height.
Rounded rectangle box centered with cyan #00B4D8 border,
very subtle cyan transparent background:
Inside top label: 'WHATSAPP'
Montserrat Regular, white 40% opacity, small, very wide letter-spacing
Main number centered: '(38) 99889-1587'
Montserrat ExtraBold, white #FFFFFF, large bold size
Text below the box:
'@tec_solar_moc'
Montserrat Regular, white 30% opacity, small size.
BOTTOM FOOTER: 'REPARO · DIAGNÓSTICO · MANUTENÇÃO'
Montserrat Regular, white 35% opacity, very wide letter-spacing, centered.
BOTTOM-RIGHT CORNER: Completely empty clean 120x120px space.
No star, no ornament, no symbol — just empty space for manual logo insertion.
Ultra HD photorealistic cinematic tech premium.
DO NOT merge with other images. Single file only.""",
        ]
    }
}

# ──────────────────────────────────────────────
# FUNÇÃO DE GERAÇÃO
# ──────────────────────────────────────────────

def gerar_imagem(prompt, numero_slide, numero_post):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    payload = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1792",
        "quality": "hd",
        "response_format": "url"
    }

    print(f"  Gerando slide {numero_slide}/5...")
    for tentativa in range(3):
        try:
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers=headers,
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            data = response.json()
            image_url = data["data"][0]["url"]

            img_response = requests.get(image_url, timeout=60)
            img_response.raise_for_status()

            pasta = f"carrossel/post-{numero_post}"
            os.makedirs(pasta, exist_ok=True)
            filename = f"{pasta}/slide-{numero_slide}.png"

            with open(filename, "wb") as f:
                f.write(img_response.content)

            tamanho_kb = os.path.getsize(filename) / 1024
            print(f"  slide-{numero_slide}.png salvo ({tamanho_kb:.0f} KB)")
            return filename

        except Exception as e:
            print(f"  Tentativa {tentativa + 1} falhou: {e}")
            if tentativa < 2:
                time.sleep(5 * (tentativa + 1))

    print(f"  ERRO: slide {numero_slide} não foi gerado após 3 tentativas.")
    return None


# ──────────────────────────────────────────────
# EXECUÇÃO
# ──────────────────────────────────────────────

def main():
    numero_post = sys.argv[1] if len(sys.argv) > 1 else "02"
    numero_post = numero_post.zfill(2)

    if numero_post not in POSTS:
        print(f"ERRO: Post {numero_post} não encontrado no script.")
        print(f"Posts disponíveis: {list(POSTS.keys())}")
        sys.exit(1)

    post = POSTS[numero_post]
    print(f"\nGerando carrossel: Post {numero_post} — {post['titulo']}")
    print("=" * 60)

    nomes = ["Capa", "Causa Raiz", "Na Bancada", "Erro do Mercado", "CTA Final"]
    arquivos = []

    for i, (prompt, nome) in enumerate(zip(post["prompts"], nomes), 1):
        print(f"\n[{i}/5] {nome}")
        arquivo = gerar_imagem(prompt, i, numero_post)
        arquivos.append(arquivo)
        if i < 5:
            time.sleep(2)  # pausa entre chamadas

    print("\n" + "=" * 60)
    print(f"Carrossel Post {numero_post} concluído:")
    nomes_slide = ["Capa", "Causa Raiz", "Como Identificar na Prática", "Erro do Mercado", "CTA Final"]
    for i, (arq, nome) in enumerate(zip(arquivos, nomes_slide), 1):
        status = arq if arq else "FALHOU"
        print(f"  slide-{i}.png — {nome}: {status}")
    print("\nAdicione a logo manualmente no Canva antes de postar.")


if __name__ == "__main__":
    main()
