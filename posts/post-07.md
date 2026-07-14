# Post 07 — Canadian Solar Falha 101: Tensão CC Elevada — String ou Sensor com Defeito?

---

## [PALAVRA-CHAVE FOCO]

canadian solar falha 101 tensão cc elevada diagnóstico inversor solar

---

## [TÍTULO SEO — Title Tag]

Canadian Solar Falha 101: String ou Sensor com Defeito?

---

## [SLUG — URL do Post]

canadian-solar-falha-101-tensao-cc-elevada-diagnostico

---

## [META DESCRIPTION]

Canadian Solar com Falha 101? Saiba se é string mal dimensionada ou falha no circuito de medição CC — diagnóstico em nível de placa. TEC Solar.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Canadian Solar Falha 101, tensão CC elevada inversor solar, Voc string temperatura, diagnóstico Canadian Solar CSI, sobretensão CC fotovoltaico

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

A **Falha 101 no inversor Canadian Solar** aparece no display, o equipamento desliga da rede e o técnico no campo não sabe se o problema está na string ou dentro da caixa. O inversor registrou sobretensão CC na entrada e entrou em proteção. A questão é: essa sobretensão é real ou o circuito de medição está lendo errado?

Na nossa bancada, esse código chega com dois perfis completamente diferentes. O primeiro vem de instalações no Sul do Brasil — Paraná, Santa Catarina, Rio Grande do Sul — onde as manhãs de inverno derrubam a temperatura para perto de zero grau e o Voc da string sobe além do que o projeto calculou para 25°C. O segundo vem de sistemas que funcionaram sem problema por dois ou três anos e começaram a dar Falha 101 de forma aleatória, sem relação com temperatura ou horário. Esse segundo grupo é circuito de medição. O tratamento para um não resolve o outro.

Distinguir os dois é o que separa um diagnóstico de uma substituição desnecessária.

---

## O que causa a Falha 101 no Canadian Solar

A Falha 101 é disparada nos inversores da linha CSI (monofásico de 1,5 a 6 kW e trifásico de 3 a 25 kW) quando a tensão nos terminais CC de entrada ultrapassa o limite máximo do modelo. Nas versões CSI-GHH e CSI-T esse limite está entre 1000 V e 1100 V, especificado na placa de características do equipamento e no manual técnico da Canadian Solar.

A tensão CC é lida por um divisor resistivo de alta impedância na placa de controle — resistores SMD em série no lado de alta tensão que escalam o nível para o ADC do microcontrolador. Qualquer alteração nessa cadeia, por degradação de componente ou por surto, muda a relação de divisão e produz uma leitura diferente da realidade.

Causas externas — a string:

1. **String calculada para 25°C sem aplicar o coeficiente de temperatura negativo do Voc** — cada painel de silício cristalino tem αVoc entre −0,26%/°C e −0,35%/°C no datasheet. Numa string de 18 módulos com Voc de 44 V a 25°C, a diferença entre calcular para 25°C e para −5°C ultrapassa 85 V. Em projetos próximos ao limite de 1000 V, esse número é suficiente para derrubar o sistema nas primeiras manhãs de inverno.
   — É o tipo de falha que passa despercebida no comissionamento porque a instalação quase sempre acontece num dia de calor.

2. **Painel substituído por modelo com Voc mais alto sem recalcular a string** — mesma potência no papel, mas Voc diferente. O projeto original passa a estar fora dos limites sem que ninguém perceba.

3. **String com número de módulos em série incompatível com o limite do inversor** — erro de projeto ou ampliação não documentada do array.

4. **Conexões MC4 mal crimpadas gerando resistência de contato variável** — tensão flutuante nos bornes que, em determinadas condições de irradiância, dispara a proteção.

Causas internas — circuito de medição:

1. **Resistores SMD do divisor de alta tensão CC com deriva de resistência** — degradação por calor acumulado, envelhecimento ou umidade nos terminais. A relação de divisão muda e o inversor passa a reportar tensão acima da real.

2. **Op-amp de condicionamento com offset deslocado** — amplificador que processa o sinal do divisor desenvolve deriva por envelhecimento ou por surto. Resultado: tensão reportada consistentemente acima da real.

3. **Capacitor de filtro na entrada CC com ESR elevado** — gera picos transitórios no barramento que o circuito de amostragem do microcontrolador registra como sobretensão pontual.

4. **MOV de proteção com degradação parcial** — varistor envelhecido injeta ruído no ponto de amostragem durante transitórios de irradiância e aciona a proteção fora de condição real de falha.

A IEC 62109-2 define os requisitos de proteção de sobretensão CC em inversores conectados à rede. O Canadian Solar CSI está correto ao disparar a proteção. A questão é se o disparo é legítimo.

---

## Como identificar na prática

Não reseta, não troca, não reconfigura — mede primeiro.

1. Registre o horário exato das ocorrências: Falha 101 nas manhãs frias com céu limpo aponta para problema de string; ocorrências distribuídas ao longo do dia, sem padrão térmico, apontam para circuito de medição interno
2. Meça a tensão CC real nos bornes de entrada do inversor com multímetro calibrado, categoria III mínimo 1000 V — o dado do datalogger ou do monitoramento web não é referência primária aqui
3. Calcule o Voc teórico da string para a temperatura ambiente no momento do fault: **Voc(T) = Voc_STC × [1 + (αVoc ÷ 100) × (T − 25)]**, usando o coeficiente do datasheet do módulo
4. Compare o Voc calculado com o limite de entrada do modelo CSI utilizado
5. Se o Voc calculado está dentro do limite e o inversor reportou sobretensão: o problema é interno — o circuito de medição está lendo acima da realidade
6. Em bancada, aplique tensão CC controlada de valor conhecido na entrada do inversor e compare com o valor que o display ou a interface serial reporta — divergência consistente acima de 30 V confirma deriva no divisor
7. Com o inversor desenergizado e os strings desconectados, meça individualmente os resistores do divisor de alta tensão no PCB e compare com o valor nominal — desvio acima de 1% em componentes de precisão já justifica substituição

Resistores escurecidos próximos às trilhas, verniz com microfissuras na região dos terminais ou oxidação visível na solda são indicativos diretos de degradação térmica acumulada.

---

## O erro mais comum do mercado

O instalador faz a visita, o sol já está alto, a temperatura subiu e o inversor reiniciou sozinho. Não há falha visível. O chamado é encerrado como transitório.

A Falha 101 volta na semana seguinte. Novo reset. Novo fechamento sem medição.

Depois de quatro ou cinco ocorrências, a conclusão é que o inversor tem defeito de fábrica e começa a pressão por substituição em garantia. O Canadian Solar novo sobe ao telhado. A string continua com os mesmos módulos, calculada para 25°C, no mesmo local com temperatura mínima de −3°C. Na próxima manhã fria: Falha 101. O ciclo reinicia com equipamento novo.

O que ficou sem contabilizar: cada ciclo de fault por sobretensão real estressou progressivamente os capacitores do barramento CC e os IGBTs do estágio de potência. Componentes com vida útil medida em horas de operação dentro da especificação. O erro de projeto gerou desgaste eletrônico real no inversor trocado.

---

## Quando o reparo é viável

Se a causa for dimensionamento de string, a solução está em campo — sem abrir o inversor:

- Reduzir o número de módulos em série para trazer o Voc para dentro do limite com margem
- Substituir por módulos com Voc compatível com a temperatura mínima histórica do local
- Corrigir o projeto com o coeficiente de temperatura aplicado na conta

Se a causa for eletrônica interna, o cenário muda por componente:

- Resistores do divisor CC degradados: troca direta com estação de solda SMD; custo de componente entre R$ 5 e R$ 20 por resistor; resultado previsível após calibração de bancada
- Op-amp com offset: substituição do CI; entre R$ 10 e R$ 50 dependendo do encapsulamento e da especificação de offset máximo
- Capacitor de filtro com ESR alto: viável, desde que o estágio de potência não tenha acumulado ciclos de estresse real por sobretensão repetida
- PCB de entrada com dano extenso por corrosão ou surto: substituição do conjunto; R$ 280 a R$ 550 incluindo mão de obra

Inversor Canadian Solar CSI de 5 kW novo: a partir de R$ 3.800. Séries de maior potência: R$ 6.000 a R$ 12.000. Reparo de circuito de medição: R$ 350 a R$ 800. Quando o estágio de potência está intacto, a conta raramente justifica troca.

Ainda não existe resposta definitiva sobre viabilidade sem abrir e medir. Depende do que você vai encontrar na placa.

---

## Conclusão

A Falha 101 no Canadian Solar tem dois caminhos. Um se resolve com cálculo e ajuste de projeto no campo, sem tocar no inversor. O outro precisa de bancada, de medição de componentes e de alguém que saiba injetar tensão de referência e ler o que o ADC está enxergando.

O que une os dois é medir a tensão real nos bornes CC antes de qualquer outra decisão. Sem essa medição, qualquer ação é tentativa.

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

- Âncora: 'sobretensão CC na entrada' → URL: /fronius-state-102-tensao-cc-alta-causa-diagnostico → Contexto: seção "O que causa", ao descrever o mecanismo de disparo da proteção por tensão CC acima do limite — o Fronius State 102 aborda o mesmo fenômeno em outra marca
- Âncora: 'string calculada para 25°C' → URL: /weg-e001-sobretensao-cc-diagnostico → Contexto: seção "O que causa", ao explicar o erro de dimensionamento sem coeficiente de temperatura — o WEG E001 trata do mesmo problema de projeto em outra plataforma
- Âncora: 'tensão CC real nos bornes' → URL: /sma-erro-3501-falha-isolamento-diagnostico-fotovoltaico → Contexto: seção "Como identificar", ao descrever a medição direta com multímetro nos terminais CC do inversor
- Âncora: 'desgaste eletrônico real' → URL: /growatt-erro-102-falha-de-isolamento → Contexto: seção "O erro mais comum", ao mencionar dano cumulativo por ciclos de proteção — o post do Growatt Erro 102 aborda degradação acumulada no estágio de potência

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62109-2" → URL: https://www.iec.ch/homepage → Fonte: IEC — Safety of power converters for use in photovoltaic power systems, Part 2: Particular requirements for inverters
- Texto âncora: "αVoc entre −0,26%/°C e −0,35%/°C no datasheet" → URL: https://www.inmetro.gov.br/qualidade/rtepac/modulos_fotovoltaicos.asp → Fonte: INMETRO — Programa Brasileiro de Etiquetagem para módulos fotovoltaicos

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=1200
→ Por que foi escolhida: Inversor solar instalado com conexões CC visíveis — representa o ponto de medição de tensão nos bornes de entrada descrito no diagnóstico da Falha 101
→ Nome do arquivo: canadian-solar-falha-101-tensao-cc-elevada.webp
→ Alt Text (máx. 125 caracteres): Inversor on-grid Canadian Solar CSI — diagnóstico da Falha 101 tensão CC elevada por string mal calculada ou falha no circuito de medição
→ Legenda: Fig. 1 — Bornes de entrada CC do inversor Canadian Solar CSI: primeiro ponto de medição no diagnóstico da Falha 101
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=1200
→ Por que foi escolhida: Técnico com multímetro em bancada eletrônica — representa a medição do circuito de medição CC e comparação de tensão real vs. reportada descrita no diagnóstico
→ Nome do arquivo: diagnostico-circuito-medicao-cc-canadian-solar-falha101-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensão CC com multímetro em inversor Canadian Solar — diagnóstico de deriva no divisor resistivo, Falha 101
→ Legenda: Fig. 2 — Medição nos bornes CC com multímetro calibrado: divergência entre tensão real e valor reportado pelo inversor confirma deriva no circuito de medição interno
→ Onde inserir: Após H2 "Como identificar na prática"
