# Post 103 — Capacitor de barramento CC: degradação, ESR alto e quando trocar

---

[PALAVRA-CHAVE FOCO]
capacitor de barramento CC inversor solar

---

[TÍTULO SEO — Title Tag]
Capacitor de barramento CC: ESR alto e quando trocar

---

[SLUG — URL do Post]
capacitor-barramento-cc-inversor-solar-esr-degradacao

---

[META DESCRIPTION]
ESR alto no capacitor de barramento CC causa falhas intermitentes no inversor. Aprenda a diagnosticar, medir e decidir quando o reparo compensa.

---

[CATEGORIA]
Análise Técnica de Componentes

---

[TAGS]
capacitor de barramento CC, ESR alto inversor solar, degradação de capacitor, reparo de inversor solar, diagnóstico eletrônico inversor

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **capacitor de barramento CC** não tem código de erro próprio. Quando ele começa a falhar, o inversor avisa em outros termos: "bus voltage fault", "DC overvoltage", "overcurrent protection" — mensagens que apontam para outra direção e deixam a causa real escondida.

Na nossa bancada, esse padrão chega com uma história quase sempre igual: o equipamento funcionava bem no inverno, começou a dar trip esporádico no verão e voltou ao normal depois de resfriar. Técnicos que não reconhecem esse comportamento tendem a trocar o inversor inteiro — ou, pior, devolver o equipamento ao cliente sem chegar à causa real. Já recebemos inversores condenados por essa falha onde o custo do reparo ficou abaixo de R$ 500. O aparelho novo teria saído por R$ 5.000.

## O que causa esse problema

O capacitor de barramento CC fica posicionado entre o estágio de entrada e as pontes de IGBTs. Sua função é dupla: suavizar o ripple de corrente que vem dos painéis fotovoltaicos e estabilizar a tensão do barramento durante as comutações de alta frequência.

O principal mecanismo de degradação é o **aumento do ESR** (resistência série equivalente). Em capacitores eletrolíticos de alumínio — os mais comuns em inversores de geração mais antiga — o eletrólito interno vai secando com o tempo e com o calor. À medida que o eletrólito perde volume, a resistência interna sobe. Com ESR elevado, o capacitor passa a dissipar mais calor durante a operação, e esse calor acelera ainda mais o envelhecimento. É uma degradação que se retroalimenta.

Junto com o ESR, a capacitância efetiva cai. Quando desce abaixo de 80% do valor nominal, o filtro não faz mais o que deveria. O ripple de tensão no barramento aumenta, e o inversor começa a ver variações que os algoritmos de controle interpretam como falha de rede ou sobretensão.

Quatro fatores aceleram esse processo no contexto brasileiro:
- Temperatura ambiente elevada, principalmente nas regiões do Cerrado, Semiárido e Norte — onde o inversor opera próximo ao limite térmico durante boa parte do ano
- Instalações sem ventilação adequada: caixas metálicas fechadas, paredes expostas ao sol, locais sem circulação de ar
- Ciclos térmicos diários intensos: o capacitor aquece quando o sol nasce, resfria à noite — todos os dias, por anos a fio
- Qualidade de rede ruim, com variações de tensão que elevam o ripple de corrente e estressam o dielétrico

A vida útil nominal de um capacitor eletrolítico de 85 °C é de 10.000 a 15.000 horas em temperatura máxima. Nas condições de campo que a gente vê no interior do Brasil, essa expectativa cai.

## Como identificar

A inspeção visual é o ponto de partida. Um capacitor em processo de falha pode mostrar o topo levemente abaulado, resíduo de eletrólito ao redor da base ou marcas de calor no corpo. Nem sempre é visível. Por isso a medição é insubstituível.

1. **Medidor de ESR dedicado** — conecta nos terminais do capacitor sem dessoldá-lo em modelos que operam in-circuit. Valor de ESR acima de 3 a 5 vezes o nominal indica degradação significativa. É o passo mais rápido e mais barato.
2. **LCR meter** — mede capacitância e ESR com precisão. Capacitância abaixo de 80% do valor de plaqueta é critério objetivo de substituição, independente do visual.
3. **Osciloscópio no barramento CC** — ripple de tensão acima de 2 a 3% da tensão nominal, com carga aplicada, indica que a capacitância efetiva não está cumprindo a função de filtro.
4. **Câmera termográfica** — identifica ponto quente localizado na região dos capacitores durante operação. Não fecha o diagnóstico sozinha, mas direciona a busca.
5. **Histórico de comportamento** — trip em dias quentes, melhora depois de resfriar, piora gradual ao longo dos meses. Esse dado vale mais do que qualquer leitura isolada.
6. **Medição de resistência de isolamento** — descarta painel ou cabeamento CC como causa antes de abrir o equipamento.

Um único dado isolado pode enganar. O conjunto fecha o diagnóstico.

## Quando é falha eletrônica interna

Nem toda instabilidade no barramento CC vem do capacitor. Antes de concluir, é preciso descartar outras causas:

- Sobretensão de string — painel ou conjunto fora do dimensionamento adequado
- Falha no circuito de pré-carga, que não limita adequadamente a corrente de inrush
- IGBT com falha parcial, gerando ondulação assimétrica no barramento

A diferença está no padrão de comportamento. Se o inversor dispara em temperatura normal e irradiância baixa, o capacitor provavelmente não é o culpado. Se a falha surge progressivamente com calor e carga alta, e desaparece ao resfriar, o capacitor entra como principal candidato.

Na bancada, a medição direta fecha o diagnóstico. Sem ela, qualquer conclusão é suposição.

## Vale a pena consertar?

Na maioria dos casos, sim. Com folga.

Um capacitor de barramento de 1000 µF / 450 V — tamanho comum em inversores de 3 a 5 kW — custa entre R$ 40 e R$ 90 por unidade, dependendo do fabricante e especificação. Um inversor típico tem de 2 a 6 capacitores de barramento. O custo de componentes fica na faixa de R$ 150 a R$ 450.

Com mão de obra especializada — dessoldagem de componentes de grande porte, verificação do circuito de pré-carga antes da energização, teste de carga após substituição — o reparo total fica entre R$ 400 e R$ 1.000.

Um inversor de 5 kW novo sai por R$ 3.500 a R$ 6.000. A diferença se paga sozinha.

Um ponto técnico que define a viabilidade do reparo: ao substituir, troque todos os capacitores do barramento de uma vez, não só o que está com ESR mais alto. Capacitores do mesmo lote envelhecem juntos — se um chegou ao limite, os outros estão chegando. Substituir somente o pior é adiar o problema por alguns meses.

---

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

[LINKS INTERNOS SUGERIDOS]

- Âncora: 'capacitores eletrolíticos em inversores' → URL: /capacitores-eletrolíticos-inversores-vida-util-degradacao → Contexto: introdução ou seção "O que causa esse problema", ao mencionar o tipo de componente
- Âncora: 'pasta térmica em inversores' → URL: /pasta-termica-inversores-igbt-vida-util → Contexto: seção "O que causa esse problema", ao tratar de fatores que afetam a vida útil térmica
- Âncora: 'diagnóstico em nível de placa' → URL: /o-que-e-diagnostico-nivel-placa-reparo-inversor → Contexto: seção "Como identificar", ao descrever a metodologia de bancada
- Âncora: 'inversores condenados pelo mercado ainda têm conserto' → URL: /por-que-maioria-inversores-condenados-ainda-tem-conserto → Contexto: seção "Vale a pena consertar?", ao tratar de equipamentos que chegam à bancada desnecessariamente
- Âncora: 'inversor fora de garantia' → URL: /inversor-fora-de-garantia-trocar-ou-reparar → Contexto: seção "Vale a pena consertar?", ao comparar custo de reparo com custo de substituição

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "resistência série equivalente" → URL: https://www.abnt.org.br → Fonte: ABNT — parâmetro técnico definido nas normas de qualidade de componentes passivos aplicadas em eletrônica de potência
- Texto âncora: "10.000 a 15.000 horas" → URL: https://www.iec.ch → Fonte: IEC 60068 — norma internacional de testes de vida útil e estresse térmico para capacitores eletrolíticos em equipamentos eletrônicos

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: placa eletrônica com capacitores eletrolíticos cilíndricos visíveis — representa diretamente o componente analisado no post
→ Nome do arquivo: capacitor-barramento-cc-inversor-solar-placa.webp
→ Alt Text (máx. 125 caracteres): Capacitores eletrolíticos em placa de inversor solar — diagnóstico de ESR alto e degradação do barramento CC
→ Legenda: Fig. 1 — Capacitores de barramento CC são componentes críticos do estágio de potência do inversor solar
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1200
→ Por que foi escolhida: técnico com multímetro medindo componente eletrônico em bancada — representa o processo de medição de ESR e capacitância descrito na seção de identificação
→ Nome do arquivo: medicao-esr-capacitor-bancada-inversor.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo ESR de capacitor em bancada eletrônica — diagnóstico de degradação em inversor solar
→ Legenda: Fig. 2 — A medição de ESR in-circuit ou com componente dessoldado define o diagnóstico antes de qualquer substituição
→ Onde inserir: Após H2 "Como identificar"
