# Post 33 — Capacitores eletrolíticos em inversores solares: vida útil, degradação e quando trocar

---

## [PALAVRA-CHAVE FOCO]

capacitores eletrolíticos em inversores solares

---

## [TÍTULO SEO — Title Tag]

Capacitor eletrolítico em inversor solar: quando trocar

---

## [SLUG — URL do Post]

capacitor-eletrolitico-inversor-solar-vida-util-degradacao

---

## [META DESCRIPTION]

Capacitores eletrolíticos degradam em silêncio e causam falhas em IGBTs. Saiba medir ESR, identificar sinais e quando substituir.

---

## [CATEGORIA]

Análise Técnica de Componentes

---

## [TAGS]

capacitor eletrolítico inversor solar, degradação ESR capacitor, vida útil capacitor inversor, barramento CC inversor, reparo capacitor inversor

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Capacitores eletrolíticos** são os componentes com maior taxa de degradação em inversores solares. Não por defeito de fabricação — por física. Eles contêm eletrólito líquido que evapora lentamente ao longo do tempo, e cada grau a mais de temperatura acelera esse processo de forma mensurável.

Na nossa bancada, capacitores degradados aparecem como causa raiz em mais da metade dos inversores que chegam com erros de tensão de barramento ou instabilidade sem explicação aparente. O equipamento foi descartado, o laudo dizia "defeito na eletrônica de potência", e o problema era um banco de capacitores com ESR elevado que não filtrava mais o barramento adequadamente. Problema de componente passivo, não de estágio de potência.

## O que causa esse problema

O capacitor eletrolítico de alumínio armazena energia no campo elétrico entre duas folhas de alumínio separadas por um óxido dielétrico e embebidas em eletrólito. O eletrólito é o componente ativo — sem ele, o capacitor perde capacitância e o ESR (resistência série equivalente) sobe. O problema é que o eletrólito evapora.

A velocidade de evaporação depende de temperatura e corrente de ripple. A cada 10°C de aumento na temperatura de operação, a taxa de degradação dobra. Um capacitor especificado para 5.000 horas a 85°C roda em torno de 65°C num inversor típico em ambiente controlado. Parece folga. Mas em inversores instalados no Nordeste e no Centro-Oeste, com ventilação comprometida ou exposição ao sol direto na carcaça, a temperatura interna pode passar de 75°C — e a conta muda completamente.

Dentro do inversor, os capacitores de barramento CC são os que suportam maior estresse. São os maiores fisicamente — normalmente 450V a 500V de tensão nominal com capacitância entre 470µF e 2200µF — e são eles que absorvem a corrente de ripple mais alta do sistema. Essa corrente aquece o eletrólito pelo efeito Joule no próprio ESR interno. Quanto mais envelhecido o capacitor, maior o ESR; quanto maior o ESR, mais calor gerado pela corrente de ripple; quanto mais calor, mais rápida a evaporação.

É um ciclo de degradação que se autoalimenta.

Os capacitores do filtro de entrada e do filtro de saída também envelhecem, mas geralmente são os de barramento que falham primeiro por operarem sob maior estresse elétrico e térmico contínuo.

## Como identificar

A degradação não tem sintoma único. Ela aparece de formas diferentes conforme o estágio de deterioração:

1. Erros de sobretensão ou subtensão no barramento CC que somem após reinício e voltam sem causa externa identificável
2. Tensão CC oscilando no display durante geração mesmo com irradiância estável
3. Ruído audível de alta frequência no inversor que não existia antes, causado por ripple de barramento fora de controle
4. Capacitor com topo abaulado ou com vestígio de eletrólito ressecado ao redor da base — sinal de degradação avançada, mas ausente na maioria dos casos de falha
5. ESR elevado na medição direta: capacitor de 1000µF saudável tem ESR abaixo de 0,1Ω; acima de 0,5Ω já causa instabilidade mensurável; acima de 2Ω, o barramento está comprometido
6. Capacitância abaixo de 80% do valor nominal — limiar de fim de vida definido pela IEC 60384-4

Para medir ESR, é necessário um capacímetro com função específica ou um LCR meter. Multímetro comum não detecta capacitor degradado — mede capacitância dentro da faixa nominal e não indica ESR. Esse é o erro de diagnóstico mais frequente nessa situação: o técnico mede com multímetro, o capacitor "passa no teste", e o problema permanece sem explicação.

## Quando é falha eletrônica interna

Capacitor degradado que não é identificado a tempo causa falhas secundárias. O barramento CC mal filtrado gera picos de tensão que excedem o VCES máximo dos IGBTs — 600V ou 1200V dependendo da configuração do equipamento. Um único pico acima desse limite perfura o óxido de gate e o componente falha em curto.

Quando o inversor chega com IGBT queimado e capacitor com ESR elevado no mesmo evento, a sequência mais provável é: capacitor falhou primeiro, pico de barramento destruiu o IGBT. Trocar o IGBT sem trocar os capacitores garante repetição do problema em poucos meses.

Identificar qual componente falhou primeiro muda o escopo do reparo. Capacitor degradado com IGBT íntegro: substituição dos capacitores e verificação do circuito de gate drive, inversor volta à operação. Capacitor degradado mais IGBT queimado: reparo mais extenso, mas ainda dentro da janela de viabilidade econômica para a maioria dos inversores acima de 5 kW.

Ainda existe um terceiro cenário que complica o diagnóstico: capacitor em fase inicial de degradação — ESR entre 0,2Ω e 0,5Ω — que já instabiliza o barramento mas não gera erro registrado. O inversor apresenta comportamento errático, desliga sem código de falha claro, e reinicia normalmente. Não existe forma de identificar esse estágio sem medir. Aparência do capacitor não ajuda — externamente, está normal.

## Vale a pena consertar?

Quase sempre.

A substituição de capacitores de barramento é um reparo direto em bancada. Os componentes custam entre R$ 15 e R$ 80 por unidade dependendo da capacitância, tensão e fabricante — Panasonic, Nichicon, Rubycon e Nippon Chemi-Con são as referências para essa aplicação em inversores. Um banco completo de capacitores de barramento raramente passa de R$ 300 a R$ 500 em componentes para inversores de 5 a 15 kW.

A hora de bancada entra no custo porque não é um reparo que se faz sem medir. É preciso identificar quais capacitores falharam, verificar se há dano secundário nos componentes adjacentes e substituir por componentes de especificação idêntica ou superior. Mesma tensão nominal, mesma capacitância, mesma temperatura máxima de operação — 105°C é preferível a 85°C em qualquer reparo de campo.

Quando um capacitor do banco falha, a boa prática é trocar o banco inteiro. Os outros capacitores têm o mesmo tempo de operação e passaram pelo mesmo estresse. Trocar só o que falhou significa que os vizinhos vão falhar nos próximos meses.

O que não faz sentido é condenar o inversor por "defeito de potência" sem medir os capacitores primeiro. O ESR é uma medição de três segundos com o equipamento certo. O resultado dessa medição muda completamente a decisão que vem depois.

## Envie seu inversor para diagnóstico

Antes de comprar equipamento novo, envie para a nossa bancada. A TEC Solar realiza diagnóstico eletrônico completo em nível de componente — abrimos o inversor, medimos a placa, identificamos a causa raiz e entregamos um laudo técnico detalhado.

Se o reparo for viável, você recebe o equipamento funcionando por uma fração do custo de substituição. Se não for, o laudo serve de base para qualquer decisão.

Atendemos todo o Brasil via logística reversa.

<div style="display:flex; flex-direction:column; gap:12px; margin-top:20px;">

<a href="https://wa.me/5538998891587?text=Ol%C3%A1%2C%20vim%20pelo%20blog%20e%20quero%20enviar%20meu%20inversor%20para%20diagn%C3%B3stico" target="_blank" style="background:#25D366; color:white; padding:14px 24px; border-radius:8px; text-decoration:none; font-weight:bold; text-align:center;">
👉 Falar no WhatsApp agora
</a>

<a href="https://www.instagram.com/tec_solar_moc?igsh=MWl2djYzeXk2Zm51dQ%3D%3D&utm_source=qr" target="_blank" style="background:#E1306C; color:white; padding:14px 24px; border-radius:8px; text-decoration:none; font-weight:bold; text-align:center;">
📸 Seguir no Instagram
</a>

<a href="https://youtube.com/@tecsolar-reparodeinversores?si=kG3Njqipg8QRbZSD" target="_blank" style="background:#FF0000; color:white; padding:14px 24px; border-radius:8px; text-decoration:none; font-weight:bold; text-align:center;">
▶️ Ver vídeos no YouTube
</a>

</div>

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "picos de tensão que excedem o VCES máximo dos IGBTs" → Link para: Por que os IGBTs queimam em inversores solares: as 6 causas reais (Post 10)
- Âncora: "circuito de gate drive" → Link para: O que é o driver de IGBT e por que sua falha destrói o estágio de potência (Post 21)
- Âncora: "ciclos térmicos" → Link para: Por que inversores solares falham mais no verão: calor, poeira e ciclos térmicos (Post 32)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 60384-4" → Fonte: IEC — Fixed capacitors for use in electronic equipment (iec.ch)
- Texto âncora: "ESR do capacitor" → Fonte: Nichicon — Technical Notes on Aluminum Electrolytic Capacitors (nichicon.com)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Placa de circuito eletrônico com capacitores visíveis, contexto direto do tema
→ Nome do arquivo: capacitor-eletrolitico-inversor-solar-bancada.webp
→ Alt Text (máx. 125 caracteres): Capacitores eletrolíticos em placa de inversor solar — degradação de ESR e vida útil em bancada TEC Solar
→ Legenda: Fig. 1 — Capacitores eletrolíticos de barramento CC: os componentes com maior taxa de degradação em inversores solares
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200
→ Por que foi escolhida: Técnico com equipamento de medição, representando diagnóstico de ESR em bancada
→ Nome do arquivo: medicao-esr-capacitor-inversor-solar-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo ESR de capacitor eletrolítico em bancada de reparo de inversor solar
→ Legenda: Fig. 2 — Medição de ESR identifica capacitor degradado sem sinal visual — multímetro comum não detecta essa falha
→ Onde inserir: Após H2 "Como identificar"
