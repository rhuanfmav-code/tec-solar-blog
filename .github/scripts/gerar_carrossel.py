"""
Script de geração de carrossel Instagram via DALL-E 3
TEC Solar — Centro Técnico de Inversores Solares

Uso: python3 gerar_carrossel.py <numero_post>
Exemplo: python3 gerar_carrossel.py 02

FILOSOFIA DOS PROMPTS:
- Texto é o elemento PRIMÁRIO — deve ser legível e renderizado com precisão
- Visuais são FOTORREALISTAS: fotografias de produto, macro de PCB, bancada real
- Inversores descritos fisicamente (sem marca) mas compatíveis com o modelo do post
- Cada slide é um carousel card completo com hierarquia visual clara
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

            # ─────────────────────────────────
            # SLIDE 1 — CAPA
            # ─────────────────────────────────
            """Vertical Instagram carousel slide, 1080x1350px, 4:5 ratio, single image, do not merge with other images.

CRITICAL — RENDER ALL TEXT BELOW CLEARLY AND LEGIBLY. Text is the primary element.

LAYOUT: Top 45% = text zone. Bottom 55% = product photo zone.

TEXT ZONE (top 45%, dark navy #0D1F3C background, left-aligned, 60px left margin):
Line 1 — small pill badge with cyan #00B4D8 border, rounded corners:
  Text inside badge: "⚡ CÓDIGO DE ERRO" — Montserrat Bold, all caps, cyan #00B4D8, 24px, wide letter-spacing
Line 2 — main title, very large, bold:
  "STATE 102" — Montserrat Black, all caps, golden yellow #F5A623, 88px, visible and sharp
Line 3 — subtitle line, same weight:
  "FRONIUS" — Montserrat Black, all caps, white #FFFFFF, 88px
Horizontal rule: thin cyan #00B4D8 line, 65% of image width, 3px thick
Line 4 — supporting text:
  "Tensão CC Alta —" — Montserrat SemiBold, white #FFFFFF, 32px
Line 5:
  "String ou defeito no sensor?" — Montserrat SemiBold, white #FFFFFF, 32px

BOTTOM FOOTER (last 80px of image):
  Text: "REPARO · DIAGNÓSTICO · MANUTENÇÃO" — Montserrat Regular, white 40% opacity, all caps, very wide letter-spacing, centered

BOTTOM-RIGHT: empty 120x120px space reserved for logo

PRODUCT PHOTO ZONE (bottom 55%):
Ultra-high resolution product photograph of a wall-mounted solar string inverter:
- Rectangular white and light gray metallic enclosure, approximately 60cm tall × 45cm wide × 20cm deep
- Front panel features a blue-backlit LCD numeric display showing "State 102" error code
- Ventilation grilles on both sides, aluminum heat sink fins visible on edges
- Professional DC/AC wiring terminals at the bottom with colored cables
- Mounted on dark wall, dramatic side lighting casting sharp shadows
- Cyan electric arc faults glowing at the DC input terminals
- Golden light halo emanating from behind the unit
- Background: very dark navy blue #0D1F3C with glowing circuit board trace patterns in cyan and gold

STYLE: ultra-detailed product photography, Canon EOS R5 quality, cinematic studio lighting, photorealistic, no cartoons, no 3D renders.""",

            # ─────────────────────────────────
            # SLIDE 2 — A CAUSA RAIZ
            # ─────────────────────────────────
            """Vertical Instagram carousel slide, 1080x1350px, 4:5 ratio, single image, do not merge with other images.

CRITICAL — RENDER ALL TEXT BELOW CLEARLY AND LEGIBLE. Text is the primary element of this image.

LAYOUT: Top 50% = text zone on dark background. Bottom 50% = macro PCB photo zone.

TEXT ZONE (top 50%, solid dark navy #0D1F3C, left-aligned, 60px margins):
Line 1 — counter badge, small, cyan border rounded rectangle:
  "02 / 05" — Montserrat Bold, cyan #00B4D8, 22px, wide letter-spacing
Line 2 — title, very large:
  "A CAUSA" — Montserrat Black, all caps, white #FFFFFF, 82px
Line 3 — title accent:
  "RAIZ" — Montserrat Black, all caps, golden #F5A623, 82px
Horizontal rule: thin cyan line, 60% width
Bullet list, left-aligned, 32px Montserrat Medium, white, line-height 1.6:
  "●  String dimensionada sem coeficiente de temperatura"
  "●  Voc dos painéis sobe 15–20% em dias frios"
  "●  Resistores do divisor de tensão com deriva de valor"
The third bullet uses a golden ● circle and golden text — it is the most critical point.

BOTTOM FOOTER: "REPARO · DIAGNÓSTICO · MANUTENÇÃO" — Montserrat Regular, white 40% opacity, all caps, centered, wide letter-spacing

BOTTOM-RIGHT: empty 120x120px space

PHOTO ZONE (bottom 50%):
Extreme macro photography of a real solar inverter power electronics circuit board, opened and exposed on a lab bench:
- Large cylindrical aluminum electrolytic capacitors (35mm tall, blue and black sleeves) arranged in rows
- IGBT power transistors in TO-247 packages with silver metallic body and three leads
- Toroidal ferrite transformer wrapped in yellow tape
- DSP/FPGA control microchip in LQFP package at center
- SMD ceramic capacitors and metal film resistors densely packed
- One area near DC input shows capacitors with bulging tops and slight amber burn marks — indicating thermal degradation
- PCB traces lit in cyan, faint glow effect at component joints
- Background: dark navy, glowing PCB patterns

STYLE: Nikon Z9 macro lens, 1:1 magnification, professional electronics photography, no 3D render, photorealistic.""",

            # ─────────────────────────────────
            # SLIDE 3 — NA BANCADA
            # ─────────────────────────────────
            """Vertical Instagram carousel slide, 1080x1350px, 4:5 ratio, single image, do not merge with other images.

CRITICAL — RENDER ALL TEXT BELOW CLEARLY AND LEGIBLY. Text cards must be sharp and readable.

LAYOUT: Top 42% = text zone. Bottom 58% = workbench photo zone.

TEXT ZONE (top 42%, dark navy #0D1F3C background, left-aligned, 60px margins):
Line 1 — counter badge:
  "03 / 05" — Montserrat Bold, cyan #00B4D8, 22px, rounded rectangle badge with cyan border
Line 2 — title:
  "NA" — Montserrat Black, all caps, white #FFFFFF, 82px
Line 3 — title accent:
  "BANCADA" — Montserrat Black, all caps, golden #F5A623, 82px
Horizontal rule: thin cyan line, 60% width

Three text boxes stacked vertically, each with a left border accent:

BOX 1 — 4px solid cyan left border, very subtle cyan transparent background:
  Label: "PASSO 1" — Montserrat Bold, cyan #00B4D8, 18px, all caps, wide spacing
  Text: "Medir tensão CC na entrada com multímetro e comparar com o histórico do display"
  — Montserrat Regular, white, 26px

BOX 2 — 4px solid cyan left border:
  Label: "PASSO 2" — Montserrat Bold, cyan #00B4D8, 18px
  Text: "Localizar resistores do divisor de tensão na placa e testar em modo ohm"
  — Montserrat Regular, white, 26px

BOX 3 — 4px solid golden #F5A623 left border, subtle golden background:
  Label: "⚠ SINAL FÍSICO" — Montserrat Bold, golden #F5A623, 18px
  Text: "Multímetro dentro do limite — display lê acima. Defeito no circuito de medição"
  — Montserrat Regular, white, 26px

BOTTOM FOOTER: "REPARO · DIAGNÓSTICO · MANUTENÇÃO" — Montserrat Regular, white 40% opacity, centered, wide letter-spacing

BOTTOM-RIGHT: empty 120x120px space

PHOTO ZONE (bottom 58%):
Professional electronics repair workbench, photographed from slightly above at 45-degree angle:
- Technician hands in dark gray anti-static work gloves
- Holding a yellow FLUKE or BRYMEN digital multimeter with red and black probes
- Probes placed on DC bus capacitor terminals of an open inverter circuit board
- Multimeter display showing DC voltage reading: "987 V DC"
- Circuit board clearly visible: green PCB, large IGBT transistors, cylindrical capacitors
- Workbench tools softly blurred in background: oscilloscope with green waveform, soldering station, magnifying lamp
- Cyan diagnostic light beam from probes scanning circuit
- Professional laboratory ambient lighting
- Background: very dark navy blue with subtle glowing PCB trace patterns

STYLE: Canon EOS 5D Mark IV, 50mm lens, professional product photography, photorealistic, not illustrated, not 3D rendered.""",

            # ─────────────────────────────────
            # SLIDE 4 — O ERRO DO MERCADO
            # ─────────────────────────────────
            """Vertical Instagram carousel slide, 1080x1350px, 4:5 ratio, single image, do not merge with other images.

CRITICAL — RENDER ALL TEXT AND NUMBERS BELOW CLEARLY AND LEGIBLY. Numbers must be sharp and readable.

LAYOUT:
- Top 35%: title text zone on dark navy background
- Middle 30%: two inverter photos side by side, divided by center light beam
- Bottom 35%: comparison price boxes + quote + footer

TEXT ZONE (top 35%, dark navy #0D1F3C):
Counter: "04 / 05" — Montserrat Bold, cyan, small badge
Title line 1, centered, very large:
  "O MERCADO CONDENA." — Montserrat Black, all caps, white #FFFFFF, 64px
Title line 2, centered:
  "A TEC SOLAR REPARA." — Montserrat Black, all caps, golden #F5A623, 64px
Thin golden horizontal rule, centered, 50% width

MIDDLE PHOTO ZONE (30%):
Split composition — two identical white rectangular wall-mounted solar inverters side by side, divided by a vertical white/cyan energy beam:
LEFT inverter: dead unit — gray desaturated photo, no display light, dust on surface, drooping cables, red X symbol above it in a red circle
RIGHT inverter: active repaired unit — display lit and showing "Normal", cyan light radiating from ventilation grilles, golden warm glow, crisp clean cables

BOTTOM COMPARISON ZONE (35%):
Centered quote box, dark background with white subtle border:
  Text: "Sem checar o circuito de medição, o inversor bom vira sucata."
  — Montserrat Italic, white 85% opacity, 26px, centered

Two side-by-side comparison cards:
LEFT CARD — red border #FF4444, dark red transparent background:
  Top label: "TROCA" — Montserrat Regular, white, 18px, all caps, wide spacing
  Big number: "R$ 7.000" — Montserrat ExtraBold, red #FF4444, 58px — MUST BE CLEARLY VISIBLE AND LEGIBLE
  Sub-label: "inversor novo" — Montserrat Regular, white, 18px

RIGHT CARD — cyan border #00B4D8, dark cyan transparent background:
  Top label: "REPARO" — Montserrat Regular, white, 18px, all caps, wide spacing
  Big number: "R$ 600" — Montserrat ExtraBold, cyan #00B4D8, 58px — MUST BE CLEARLY VISIBLE AND LEGIBLE
  Sub-label: "TEC Solar" — Montserrat Regular, white, 18px

FOOTER: "REPARO · DIAGNÓSTICO · MANUTENÇÃO" — Montserrat Regular, white 40% opacity, centered
BOTTOM-RIGHT: empty 120x120px space""",

            # ─────────────────────────────────
            # SLIDE 5 — CTA FINAL
            # ─────────────────────────────────
            """Vertical Instagram carousel slide, 1080x1350px, 4:5 ratio, single image, do not merge with other images.

CRITICAL — ALL TEXT MUST BE RENDERED SHARPLY AND LEGIBLY. This is a call-to-action card — text is everything.

BACKGROUND: Very dark navy blue #0D1F3C, maximum intensity dense glowing circuit board traces in cyan #00B4D8 and golden #F5A623 covering the entire background like a giant glowing motherboard — ultra-bright connection nodes, light bursts at junctions, scattered bright tech star dots everywhere.

CENTRAL PRODUCT PHOTO:
Ultra-high resolution photograph of a wall-mounted solar string inverter in REPAIRED and OPERATIONAL state:
- White and light gray metallic rectangular enclosure, professional grade
- Blue LCD display illuminated showing "NORMAL" or "OK" status — no error code
- Clean professional cabling at terminals
- Positioned at center of image, slightly elevated, like a trophy
- Maximum energy explosion effect: intense cyan and golden light rays bursting outward from the inverter in all directions, reaching all four image edges
- Long golden light streaks radiating outward like solar flares
- Floating golden and cyan energy particles surrounding the inverter
- Premium lens flare effects at image corners

TEXT OVERLAY — render all text clearly:

Top of image, centered, small spaced text:
  "ANTES DE CONDENAR," — Montserrat Bold, all caps, white 45% opacity, 24px, very wide letter-spacing

Main title, centered, very large:
  "DIAGNOSTIQUE." — Montserrat Black, all caps, golden #F5A623, 96px
  Golden glow shadow effect behind each letter — text must be large, bold, unmistakably readable

Thin cyan horizontal rule, centered, 55% width

Supporting text, 2 lines, centered:
  "Laudo técnico completo em nível de placa." — Montserrat Regular, white 80% opacity, 28px
  "Atendemos todo o Brasil via logística reversa." — Montserrat Regular, white 80% opacity, 28px

Contact box — rounded rectangle, cyan #00B4D8 border, 3px, dark subtle cyan fill:
  Top label inside box: "WHATSAPP" — Montserrat Regular, white 45% opacity, 16px, all caps, wide spacing
  Main number — MUST BE LEGIBLE AND LARGE:
  "(38) 99889-1587" — Montserrat ExtraBold, white #FFFFFF, 52px, centered inside box
  Below box, small:
  "@tec_solar_moc" — Montserrat Regular, white 35% opacity, 20px, centered

FOOTER: "REPARO · DIAGNÓSTICO · MANUTENÇÃO" — Montserrat Regular, white 35% opacity, all caps, wide letter-spacing, centered
BOTTOM-RIGHT: completely empty clean 120x120px space, no ornament, no logo, just empty space

STYLE: ultra HD photorealistic cinematic, premium tech dark aesthetic, product photography quality, photorealistic inverter — not illustrated, not 3D cartoon rendered.""",
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
            time.sleep(2)

    print("\n" + "=" * 60)
    print(f"Carrossel Post {numero_post} concluído:")
    nomes_slide = ["Capa", "Causa Raiz", "Como Identificar na Prática", "Erro do Mercado", "CTA Final"]
    for i, (arq, nome) in enumerate(zip(arquivos, nomes_slide), 1):
        status = arq if arq else "FALHOU"
        print(f"  slide-{i}.png — {nome}: {status}")
    print("\nAdicione a logo manualmente no Canva antes de postar.")


if __name__ == "__main__":
    main()
