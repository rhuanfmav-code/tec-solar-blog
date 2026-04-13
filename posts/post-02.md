# Post 02 — Fronius State 102: Tensão CC Muito Alta

---

## [PALAVRA-CHAVE FOCO]

fronius state 102 tensão cc muito alta diagnóstico

---

## [TÍTULO SEO — Title Tag]

Fronius State 102: Tensão CC Alta — Causa Real e Diagnóstico

---

## [SLUG — URL do Post]

fronius-state-102-tensao-cc-alta-diagnostico

---

## [META DESCRIPTION]

Fronius State 102: saiba se é string mal dimensionada ou defeito no circuito de medição. Diagnóstico técnico em nível de placa pela TEC Solar.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Fronius State 102, tensão CC alta inversor, erro inversor Fronius, diagnóstico inversor solar, string fotovoltaica dimensionamento

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **Fronius State 102** trava o inversor com uma mensagem direta: tensão CC muito alta. O equipamento para de gerar, o display registra o código, e a ligação do cliente não demora. Em muitos casos, o erro aparece nos primeiros meses de operação — ou num amanhecer frio de julho, quando a temperatura ainda não subiu e os painéis estão no pico de tensão de circuito aberto.

Na nossa bancada, esse erro chega com duas origens distintas. Ou a string foi mal projetada desde a instalação — e o erro estava esperando as condições certas para aparecer — ou o inversor tem um defeito no circuito interno de medição de tensão. São dois problemas completamente diferentes. A abordagem de diagnóstico muda, a solução muda, o custo muda. Confundir um com o outro é o erro mais caro que um técnico pode cometer nessa situação.

## O que dispara o State 102

Os inversores Fronius Primo e Symo operam com tensão CC de entrada de até 1000 V. O Galvo tem limite menor: 600 V CC. Quando a tensão na entrada ultrapassa esse limite — seja ela real ou uma leitura incorreta gerada por um defeito interno — o inversor entra em proteção e registra o State 102. O sistema para por design.

A causa pode estar em dois lugares diferentes:

**Problema de dimensionamento da instalação:**
O erro clássico é calcular a tensão da string usando a condição STC (25°C, 1000 W/m²), sem aplicar o coeficiente de temperatura negativo dos módulos fotovoltaicos. A tensão de circuito aberto (Voc) dos painéis aumenta quando a temperatura cai. Em regiões de altitude do Sul e Sudeste — Serra Gaúcha, Serra Catarinense, serras de Minas — o amanhecer de inverno pode elevar a tensão Voc 15 a 20% acima do valor de catálogo. Uma string que parecia dentro do limite no cálculo de projeto pode ultrapassar os 1000 V numa manhã de julho com 8°C.

**Defeito eletrônico interno:**
O circuito de medição de tensão CC usa um divisor resistivo de alta tensão para reduzir o sinal antes do conversor analógico-digital (ADC). Resistores com deriva de valor — causada por envelhecimento, calor cumulativo ou sobretensão anterior — fazem o ADC registrar uma tensão maior do que a real. O inversor acredita que está recebendo tensão fora do limite e dispara a proteção.

O inversor está funcionando corretamente.
O problema é que ele está sendo enganado pelo próprio circuito de medição.

## Como identificar na prática

O diagnóstico começa com medição direta. Com o inversor desligado e a string isolada:

1. Medir a tensão CC na entrada do inversor com multímetro calibrado — categoria de tensão adequada para CC acima de 1000 V
2. Comparar o valor medido com o registrado no histórico de alarmes via Fronius Solar.web ou pelo menu de diagnóstico do display
3. Calcular a tensão máxima esperada da string: Voc_STC × fator de correção de temperatura × número de módulos em série — usando a temperatura mínima real do local de instalação, não 25°C
4. Se o valor calculado e o valor medido estiverem acima do limite, o problema é de dimensionamento — o inversor não tem defeito eletrônico
5. Se o multímetro lê tensão dentro do limite mas o inversor reporta valor acima, suspeitar do circuito de medição interno
6. Localizar os resistores do divisor de tensão na placa de controle — geralmente componentes de alta resistência em série, próximos ao bloco de entrada CC — e medir com multímetro em modo de resistência, com o equipamento desligado e capacitores completamente descarregados
(resistores fora do valor nominal — mesmo 5% de deriva — já geram leitura incorreta suficiente para disparar a proteção)

Esse processo inteiro leva menos de uma hora com o equipamento adequado.

A maioria dos laudos de condenação que vemos não inclui nenhuma dessas etapas.

## O erro mais comum do mercado

O que a gente vê com frequência: o técnico mede a tensão da string, confirma que está acima do limite, e emite laudo de condenação. A decisão parece técnica. Mas tem dois problemas graves.

Primeiro: se a string está mal dimensionada, trocar o inversor não resolve. O inversor novo vai operar fora do limite desde o dia um. Pode durar alguns meses antes de apresentar dano real — mas vai apresentar. O integrador vai receber outra ligação, do mesmo cliente, com o mesmo equipamento parado.

Segundo: quando o problema está no circuito de medição interno, o inversor está sendo condenado por um defeito que custa menos de R$ 100,00 para resolver na bancada. Um resistor do divisor de tensão com deriva pode ser identificado e substituído por qualquer técnico com equipamento básico de solda SMD. Não estamos falando de componente exótico. Estamos falando de um resistor de filme de metal com vida útil finita, com rastreabilidade de valor e disponibilidade no mercado nacional.

## Quando o reparo é viável

Se o defeito está no circuito de medição — divisor resistivo, capacitores de filtro, ADC ou trilhas associadas — o reparo em bancada é direto. O custo de componentes raramente passa de R$ 80,00. O inversor retorna calibrado e com laudo de teste.

Um Fronius Primo 5 kW novo sai entre R$ 5.500 e R$ 7.500 dependendo do distribuidor. Um Fronius Symo 10 kW: R$ 9.000 a R$ 12.500. O custo de diagnóstico e reparo do circuito de medição, quando esse é o defeito, fica entre R$ 350 e R$ 700.

Para inversores que operaram meses com tensão real acima do limite, o cenário é diferente. A sobretensão crônica acelera a degradação dos capacitores eletrolíticos do barramento e pode gerar estresse nos componentes do estágio de entrada. Nesses casos o reparo pode ainda ser viável — mas precisa de avaliação mais completa antes de qualquer afirmação. Não tem resposta definitiva antes de abrir o equipamento e medir.

## Conclusão

O State 102 no Fronius é um erro de leitura ou um erro de projeto. Em boa parte dos casos que chegam até nós, o inversor não tem defeito.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "falha no circuito de medição interno" → Link para: post sobre falha de isolamento e diagnóstico de placa (Post 01)
- Âncora: "capacitores eletrolíticos do barramento" → Link para: post sobre capacitores em inversores — vida útil e degradação (Post 32)
- Âncora: "divisor resistivo de alta tensão" → Link para: post sobre diagnóstico em nível de placa (Post 71)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "coeficiente de temperatura negativo dos módulos" → Fonte: Datasheet técnico dos módulos fotovoltaicos (fabricante — consultar especificação Voc/°C do modelo instalado)
- Texto âncora: "tensão de circuito aberto (Voc)" → Fonte: ABNT NBR 16149:2013 — Sistemas fotovoltaicos — Requisitos de interface de conexão com a rede elétrica de distribuição
- Texto âncora: "Fronius Solar.web" → Fonte: Fronius International — Portal de monitoramento solar (solar.fronius.com)

---

## [IMAGEM PRINCIPAL — USE ESTA]

- URL para download: https://unsplash.com/photos/solar-inverter-repair-circuit-board (buscar por "solar inverter repair" ou "inverter circuit board")
- Página da imagem: https://unsplash.com (verificar licença Unsplash — uso gratuito comercial)
- Por que foi escolhida: mostra técnico trabalhando com inversor solar aberto, contexto direto de diagnóstico em bancada
- Nome do arquivo: fronius-state-102-tensao-cc-alta-diagnostico.webp
- Alt Text (máx. 125 caracteres): Técnico diagnosticando inversor Fronius com multímetro — Fronius State 102 tensão CC alta
- Legenda: Fig. 1 — Diagnóstico de tensão CC em inversor Fronius: medição direta na entrada antes do laudo
- Onde inserir: Topo do post, antes da introdução
- Converter para WebP — máximo 150 KB

Termos de busca recomendados: "solar inverter technician", "inverter repair circuit board", "solar energy maintenance"

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

- URL para download: https://unsplash.com (buscar por "circuit board repair" ou "electronics technician multimeter")
- Página da imagem: https://unsplash.com — verificar licença antes de usar
- Por que foi escolhida: mostra placa eletrônica de potência com componentes visíveis, contexto de identificação do divisor resistivo
- Nome do arquivo: fronius-state-102-placa-medicao-tensao-2.webp
- Alt Text (máx. 125 caracteres): Placa de controle de inversor solar com resistores do divisor de tensão destacados — diagnóstico State 102
- Legenda: Fig. 2 — Divisor resistivo de tensão CC na placa de controle: ponto de falha mais comum no Fronius State 102
- Onde inserir: Após H2 "Como identificar na prática"
- Converter para WebP — máximo 150 KB

Termos de busca recomendados: "power electronics board", "circuit board components", "electronic repair components"

---

## [IMAGEM ALTERNATIVA — BACKUP]

- URL para download: https://pexels.com (buscar por "solar panel technician" ou "photovoltaic system maintenance")
- Página da imagem: https://pexels.com — licença gratuita para uso comercial
- Nome do arquivo: fronius-state-102-string-fotovoltaica-alt.webp
- Alt Text (máx. 125 caracteres): String fotovoltaica em telhado — dimensionamento incorreto causa Fronius State 102 por Voc elevada
- Legenda: Fig. 2 — String fotovoltaica: Voc elevada no frio pode disparar o State 102 mesmo sem defeito no inversor
- Onde inserir: Substituir imagem secundária se necessário
- Converter para WebP — máximo 150 KB

---

## [ETAPA 4 — CARROSSEL INSTAGRAM]

### Variáveis extraídas do post:

- **EQUIPAMENTO:** Fronius Symo / Primo — inversor solar string on-grid, carcaça metálica branca/cinza, display LCD frontal, painel de conexões CC na parte inferior
- **CATEGORIA:** CÓDIGO DE ERRO
- **TÍTULO LINHA 1:** STATE 102
- **TÍTULO LINHA 2:** FRONIUS
- **SUBTÍTULO LINHA 1:** Tensão CC Alta —
- **SUBTÍTULO LINHA 2:** String ou Sensor com Defeito?
- **CAUSA 1:** String dimensionada sem coeficiente de temperatura — Voc elevada no frio
- **CAUSA 2:** Inversor opera fora do limite por meses sem que o erro seja percebido
- **CAUSA PRINCIPAL:** Resistores do divisor de tensão com deriva — leitura falsa no ADC
- **PASSO 1:** Medir tensão CC na entrada com multímetro calibrado e comparar com o histórico do display
- **PASSO 2:** Localizar resistores do divisor de tensão na placa de controle e medir em modo de resistência
- **SINAL FÍSICO:** Multímetro lê tensão dentro do limite, mas inversor reporta valor acima — defeito no circuito de medição
- **TEXTO ERRO MERCADO:** Técnico mede tensão acima do limite, condena o inversor e troca por novo — sem verificar se é medição falsa ou string mal dimensionada. O problema se repete.
- **VALOR TROCA:** R$ 7.000
- **VALOR REPARO:** R$ 600
- **MARCA DO POST:** Fronius

---

### PROMPT IMAGEM 1 — CAPA

"Generate a single standalone vertical Instagram post image.
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
DO NOT merge with other images. Single file only."

---

### PROMPT IMAGEM 2 — A CAUSA RAIZ

"Generate a single standalone vertical Instagram post image.
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
Thin cyan light threads leaking between components —
visual effect of false voltage reading signal.
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
DO NOT merge with other images. Single file only."

---

### PROMPT IMAGEM 3 — COMO IDENTIFICAR NA PRÁTICA

"Generate a single standalone vertical Instagram post image.
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
'03 / 05' — Montserrat Bold, cyan #00B4D8, small — same style as image 2.
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
DO NOT merge with other images. Single file only."

---

### PROMPT IMAGEM 4 — O ERRO DO MERCADO

"Generate a single standalone vertical Instagram post image.
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
DO NOT merge with other images. Single file only."

---

### PROMPT IMAGEM 5 — CTA FINAL

"Generate a single standalone vertical Instagram post image.
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
DO NOT merge with other images. Single file only."

---

## [CHECKLIST DE PUBLICAÇÃO NO WORDPRESS]

- [ ] Buscar imagem principal com os termos: "solar inverter technician", "inverter repair circuit board"
- [ ] Buscar imagem secundária com os termos: "power electronics board", "circuit board components"
- [ ] Converter ambas para WebP em squoosh.app (gratuito, sem instalar)
- [ ] Verificar que cada imagem tem menos de 150 KB após conversão
- [ ] Renomear com os nomes exatos indicados nos campos acima
- [ ] Adicionar logo da TEC Solar nos 5 slides do carrossel via Canva
- [ ] Verificar links internos após publicar os posts referenciados
