# Post 02 — Fronius State 102: Tensão CC Muito Alta

---

## [PALAVRA-CHAVE FOCO]

Fronius State 102 tensão CC muito alta diagnóstico

---

## [TÍTULO SEO — Title Tag]

Fronius State 102: Tensão CC Alta — Causa e Diagnóstico

---

## [SLUG — URL do Post]

fronius-state-102-tensao-cc-alta-causa-diagnostico

---

## [META DESCRIPTION]

Fronius State 102: tensão CC muito alta. Veja como diferenciar string mal dimensionado de falha eletrônica interna no inversor solar.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Fronius State 102, tensão CC alta inversor solar, falha sensor tensão Fronius, diagnóstico inversor Fronius, string fotovoltaico sobretensão

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Fronius State 102 tensão CC muito alta** para a geração antes de o sol esquentar. O inversor trava, exibe o código no display e desliga. O técnico chega sem saber se precisa reconfigurar o string ou se está diante de um defeito eletrônico interno.

Na nossa bancada, esse erro chega com uma história quase sempre igual: o sistema funcionou bem por um, dois, às vezes três anos — e o State 102 apareceu recentemente, sem nenhuma alteração no string. Quando o padrão é esse, a suspeita vai direto para o circuito de medição. Mas sem medir, não dá para confirmar nada.

## O que causa o Fronius State 102

O código indica que a tensão no barramento CC ultrapassou o limite máximo de entrada configurado no inversor. Os modelos Fronius Primo, Symo e Galvo aceitam tensões de entrada entre 200 V e 800 V DC — ou até 1000 V em versões específicas — conforme especificado no datasheet de cada modelo.

O problema tem duas origens possíveis.

A primeira é a tensão real ultrapassando o limite. O string foi montado com módulos em série que, na temperatura mínima do local de instalação, geram tensão de circuito aberto acima do que o inversor suporta. A Voc dos módulos de silício cristalino sobe conforme a temperatura cai, seguindo a equação:

Voc(T) = Voc(STC) × [1 + αvoc × (Tmin − 25°C)]

O coeficiente αvoc fica entre −0,30%/°C e −0,35%/°C para a maioria dos módulos. Em instalações no Sul do Brasil — especialmente no Rio Grande do Sul e em regiões de altitude em Santa Catarina — a temperatura mínima histórica se aproxima de 0°C, o que representa aumento de 8 a 10% sobre o Voc em condições STC.

Esse aumento parece pequeno, mas em um string com 20 módulos de 40 V de Voc cada, o ganho de 10% coloca a tensão de circuito aberto em 880 V — acima do limite de 800 V de vários modelos Fronius.

A segunda origem é mais traiçoeira: o circuito de medição de tensão CC na placa de controle está com leitura incorreta. O divisor resistivo que reduz a tensão do barramento CC para nível compatível com o ADC pode ter um resistor fora de tolerância por envelhecimento ou estresse térmico acumulado. O conversor analógico-digital interpreta o sinal como sobretensão mesmo com a tensão real dentro do limite operacional.

Capacitores eletrolíticos de entrada degradados também geram picos transitórios de tensão que disparam o State 102 de forma pontual, sem que a tensão média do barramento esteja fora dos parâmetros.

Esse último caso é o mais difícil de capturar com multímetro.

## Como identificar na prática

O diagnóstico começa pelo histórico de eventos, não pelo string.

1. Acesse o Fronius Solar.web e filtre os eventos de State 102 por data e horário.
2. Verifique se os erros se concentram em manhãs frias ou em determinados meses do ano — esse padrão sazonal aponta quase sempre para problema de dimensionamento com temperatura.
3. Se o padrão for sazonal, calcule a Voc corrigida do string para a temperatura mínima histórica do município usando os dados disponíveis no portal do INMET para qualquer localidade do Brasil.
4. Compare a Voc calculada com o limite máximo de entrada CC do modelo específico do inversor, disponível no datasheet oficial do Fronius.
5. Meça a tensão CC nas bornes de entrada do inversor com multímetro calibrado, preferencialmente em dia frio e no horário em que o erro costuma aparecer.
6. Se a tensão medida ou calculada for maior que o limite: o problema é de dimensionamento.
7. Se estiver dentro do limite mas o erro continua aparecendo: a causa é eletrônica interna.

Para confirmar a suspeita eletrônica, use osciloscópio no barramento CC. Picos transitórios rápidos que o multímetro não registra aparecem claramente no escopo e indicam capacitores de filtro com ESR elevado. Inspecione visualmente os eletrolíticos do estágio de entrada: barriga, base com mancha escura, eletrólito seco ou fio de segurança rompido são sinais físicos visíveis antes mesmo de qualquer medição.

Se os capacitores estiverem aparentemente íntegros, o próximo passo é medir a resistência dos componentes do divisor de tensão com o circuito desenergizado. Um resistor com valor significativamente fora da tolerância especificada no esquemático já explica o drift de leitura.

## O erro mais comum do mercado

Reconfiguram o string sem medir nada primeiro.

O técnico vê "tensão CC muito alta", conta os módulos em série e conclui que precisa retirar um ou dois painéis da string. Às vezes resolve. Quando o problema é realmente de dimensionamento e temperatura, a retirada corrige o Voc e o inversor para de reclamar.

Mas quando a causa é eletrônica interna, o State 102 volta depois de alguns dias. O sistema continua parando. E agora o técnico já tirou painel — o cliente perdeu geração sem necessidade real.

Já recebemos inversores Fronius onde dois profissionais diferentes tinham retirado painéis em momentos distintos. O string foi reduzido ao ponto de o inversor sair da faixa de MPPT adequada para a potência instalada. O sistema gerava menos, o cliente pagava mais na conta de energia, e o erro continuava aparecendo em dias frios.

O problema original era um capacitor de entrada com ESR elevado. Um componente de centavos.

## Quando o reparo é viável

Se a causa for eletrônica, depende do componente afetado.

Capacitores de entrada com ESR elevado são substituição direta e custo baixo. O reparo é simples quando o técnico tem medidor de ESR e sabe interpretar os valores antes e depois da substituição. Resistores do divisor de tensão fora de tolerância exigem rastreamento preciso no circuito de medição da placa de controle — é um ponto pequeno, mas encontrável com multímetro e esquemático em mãos. Dano no próprio ADC ou no microcontrolador por pico de tensão é mais complexo, mas ainda viável dependendo do componente e da disponibilidade de peças de reposição.

Em nenhum dos cenários acima o inversor precisa ser descartado.

Um Fronius Primo de 6 kW novo está entre R$ 5.000 e R$ 8.000 dependendo do distribuidor e do câmbio do momento. Um reparo eletrônico em nível de componente, mesmo nos casos mais trabalhosos, raramente ultrapassa 30% desse valor. Sem contar o tempo de espera por importação — que em regiões mais afastadas dos grandes centros pode se estender por semanas, com o sistema parado e o cliente sem geração.

## Conclusão

State 102 por tensão real alta e State 102 por falha de medição têm a mesma cara no display. A diferença está na medição — não na contagem de painéis.

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

Nota: Por ser o Post 02, apenas o Post 01 está disponível como referência interna. Não há âncora natural neste post que se conecte ao Post 01 (Growatt Erro 102 — Falha de Isolamento). Links internos serão mais aplicáveis a partir do Post 03 em diante, conforme o acervo de posts anteriores cresce.

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "temperatura mínima histórica do município" → URL: https://www.inmet.gov.br/portal/index.php?r=clima/normaisClimatologicas → Fonte: INMET — Instituto Nacional de Meteorologia
- Texto âncora: "datasheet oficial do Fronius" → URL: https://www.fronius.com/pt-br/brasil/energia-solar/instaladores-e-parceiros/dados-tecnicos → Fonte: Fronius — Dados Técnicos Oficiais

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://unsplash.com/s/photos/solar-inverter (buscar imagem de inversor solar com painel de controle ou display)
→ Por que foi escolhida: Inversor solar com display visível — representa o contexto de leitura de código de erro State 102
→ Nome do arquivo: fronius-state-102-tensao-cc-inversor-solar.webp
→ Alt Text (máx. 125 caracteres): Inversor solar Fronius com display mostrando State 102 — tensão CC muito alta no barramento de entrada
→ Legenda: Fig. 1 — Fronius State 102 indica tensão CC acima do limite máximo de entrada do inversor
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://unsplash.com/s/photos/solar-panel (buscar imagem de string de painéis solares em série, preferencialmente em dia ensolarado com céu claro)
→ Por que foi escolhida: String de painéis em série — ilustra o dimensionamento de tensão CC e o cálculo de Voc
→ Nome do arquivo: string-paineis-solares-tensao-voc-fronius-2.webp
→ Alt Text (máx. 125 caracteres): String de painéis solares fotovoltaicos em série — cálculo de tensão Voc para diagnóstico Fronius State 102
→ Legenda: Fig. 2 — A tensão de circuito aberto do string aumenta com a queda de temperatura e pode ultrapassar o limite do inversor
→ Onde inserir: Após H2 "Como identificar na prática"
