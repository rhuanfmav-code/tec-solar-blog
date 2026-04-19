# Post 18 — Canadian Solar Falha 117: Falha de Isolamento — cabo ou painel com isolamento ruim

---

## [PALAVRA-CHAVE FOCO]

Canadian Solar Falha 117 falha de isolamento diagnóstico

---

## [TÍTULO SEO — Title Tag]

Canadian Solar Falha 117: Diagnóstico de Isolamento CC

---

## [SLUG — URL do Post]

canadian-solar-falha-117-diagnostico-isolamento-cc

---

## [META DESCRIPTION]

Falha 117 Canadian Solar indica queda de isolamento CC. Veja como usar o megohmmeter, isolar string por string e encontrar o ponto de falha antes de trocar o inversor.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Canadian Solar Falha 117, falha de isolamento inversor solar, diagnóstico isolamento CC, megohmmeter inversor, resistência de isolamento fotovoltaico

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

A **Canadian Solar Falha 117** é um dos erros de isolamento mais frequentes que chegam até nós — e também um dos mais mal diagnosticados no campo. Quando o display exibe esse código, o inversor sinalizou que a resistência de isolamento da malha CC caiu abaixo do limite mínimo aceitável. O equipamento não pifou. Ele detectou um risco real e se protegeu.

Na nossa bancada, esse erro chega com uma história quase sempre igual: o técnico trocou o inversor, o novo foi instalado, e dois dias depois o mesmo código voltou. O problema nunca estava no inversor. Estava no cabo roteado sob a laje ou no painel com backsheet deteriorada que ninguém tinha verificado.

---

## O que causa a Falha 117

Os inversores Canadian Solar das séries CSI-GR e CSI-T monitoram continuamente a resistência de isolamento da malha CC por meio de um circuito interno chamado IMD (Isolation Monitoring Device). Esse circuito injeta uma tensão de referência no barramento e mede qualquer corrente que retorne pelo condutor de aterramento. Quando a impedância cai abaixo de aproximadamente 100 kΩ — o limiar varia por modelo e configuração — o inversor desliga o estágio de potência e registra a Falha 117.

As origens mais comuns no campo são estas:

1. Cabo CC com isolamento perfurado ou desgastado — abrasão em passagens por borda de calha, telha cerâmica ou parafuso exposto é o caso mais frequente
2. Backsheet rachada ou delaminada no painel solar — a umidade infiltra pela microfissura e cria caminho resistivo entre a célula e o frame metálico aterrado
3. Junction box com vedação rompida — infiltração de água no bloco de diodos ou nos bornes cria uma conexão resistiva com o terra que o inversor detecta facilmente
4. Conector MC4 mal crimpado — pino fora de posição ou vedação de borracha danificada abre caminho para umidade nos bornes energizados
5. PID em estágio avançado — em sistemas com barramento acima de 600 V e sem compensador, o processo de degradação por tensão induzida pode comprometer o isolamento de painéis específicos
6. Falso positivo do circuito IMD na placa de controle — capacitor de desacoplamento com derivação ou resistor de medição fora de especificação faz o inversor acusar falha mesmo com o sistema externo saudável

Esse sexto caso é o menos óbvio e costuma aparecer quando todos os testes externos já foram feitos e o erro persiste. Ainda não existe resposta rápida para ele. Depende do que você vai encontrar na placa.

---

## Como identificar na prática

O diagnóstico começa com o megohmmeter. Não com o multímetro.

O multímetro aplica no máximo 9 V na medição de resistência. A tensão de operação de um string de 10 painéis em série está entre 300 V e 600 V. Uma falha de isolamento que só se manifesta sob tensão real é completamente invisível para o multímetro.

O procedimento correto:

1. Desligar o inversor e aguardar a descarga do barramento CC
2. Desconectar todos os strings do inversor ao mesmo tempo — não um por vez
3. Aplicar 500 VDC com megohmmeter entre positivo e terra de cada string individualmente, depois entre negativo e terra
4. Valor mínimo aceitável: 1 MΩ conforme IEC 62109-1. Qualquer leitura abaixo disso exige investigação
5. Identificar qual string está com leitura baixa e, dentro dele, isolar painel por painel para localizar o ponto exato
6. Percorrer fisicamente todo o trajeto dos cabos CC daquele string — prestar atenção a pontos onde o cabo dobra, passa por metal exposto ou fica sem proteção mecânica
7. Abrir cada junction box do string suspeito e verificar umidade, oxidação nos bornes e integridade visual dos diodos de bypass

Em instalações no Norte e no Nordeste do Brasil — onde a umidade relativa é alta mesmo nas épocas secas e a amplitude térmica diária é menor — o padrão de infiltração é diferente. A água não seca durante o dia. O erro de isolamento tende a ser constante em vez de intermitente. Isso muda a prioridade do diagnóstico: em vez de suspeitar primeiro de condensação, suspeite de penetração por fissura permanente.

Se todos os strings passarem na medição com o megohmmeter e o erro persistir com o inversor reconectado, o problema é interno.

---

## O erro mais comum do mercado

O erro é não usar o megohmmeter.

Diagnóstico de isolamento CC com multímetro não tem validade técnica em sistemas fotovoltaicos. Ponto.

O segundo equívoco mais frequente é testar um único string, não encontrar nada, e concluir que o problema é o inversor. A Falha 117 é disparada por qualquer ponto da malha CC conectada ao barramento — um único cabo com isolamento degradado em qualquer string é suficiente para travar o sistema inteiro. O procedimento correto exige desconectar todos os strings e testá-los individualmente, sem exceção.

O terceiro erro, menos óbvio, é ignorar os conectores MC4. Em instalações feitas com pressa ou por equipes sem treinamento específico, o MC4 mal crimpado ou sem o travamento mecânico completo é frequente. O pino fora de posição cria um caminho de alta impedância que piora progressivamente com o calor e a umidade. No campo, parece um defeito aleatório e intermitente.

---

## Quando o reparo é viável

Quando o problema está no sistema externo, o reparo é quase sempre viável e direto:

- Substituição de trecho de cabo CC danificado: custo de material mais mão de obra, frequentemente abaixo de R$ 500
- MC4 com vedação comprometida: custo de conector novo é irrisório; o tempo de diagnóstico e localização é o maior custo
- Painel com backsheet deteriorada: depende se há garantia ativa — alguns fabricantes cobrem, muitos não, especialmente em módulos com mais de cinco anos
- Painel com PID avançado: tratamento possível com equipamento específico, mas a relação custo-benefício precisa ser avaliada caso a caso

Quando o problema é interno ao inversor, o diagnóstico em bancada define o caminho. Se o defeito estiver nos componentes do circuito IMD — resistores de medição SMD derivados, capacitores de referência com ESR elevado, amplificador de instrumentação com offset fora do especificado —, o reparo eletrônico é executável. Custo típico na TEC Solar: entre R$ 400 e R$ 700.

Um inversor Canadian Solar de 3 a 5 kW novo sai por R$ 3.000 a R$ 5.000. Condenar sem diagnóstico é uma decisão financeira ruim antes de qualquer coisa.

---

## Conclusão

A Falha 117 não é defeito do inversor na maior parte dos casos. O inversor está funcionando como foi projetado para funcionar: monitorando o isolamento e parando quando encontra risco.

O problema está em algum ponto entre os painéis e o barramento CC. Pode ser óbvio na primeira inspeção, pode ser difícil de encontrar.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "Sungrow GFCI Fault: Corrente de Fuga à Terra" → Link para: Post 27 — ainda não publicado, não inserir link no texto
- Âncora: "conector MC4 mal crimpado" → Link para: Post 16 — Sungrow Arc Fault (AFCI): Arco Elétrico Detectado — publicado, inserir link

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62109-1" → Fonte: IEC — Safety of power converters for use in photovoltaic power systems (iec.ch)
- Texto âncora: "Isolation Monitoring Device" → Fonte: Bender GmbH — Application notes on IMD in PV systems (bender.de)
- Texto âncora: "PID (Potential Induced Degradation)" → Fonte: Fraunhofer ISE — Potential Induced Degradation in PV modules (ise.fraunhofer.de)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Instalação de painéis solares em telhado residencial com cabeamento CC visível — representa diretamente o contexto onde a Falha 117 ocorre e onde o diagnóstico de isolamento começa
→ Nome do arquivo: canadian-solar-falha-117-falha-isolamento-cc.webp
→ Alt Text (máx. 125 caracteres): Painéis solares em telhado com cabeamento CC — diagnóstico da Canadian Solar Falha 117 de isolamento CC na string fotovoltaica
→ Legenda: Fig. 1 — A Falha 117 do Canadian Solar indica queda de resistência de isolamento na malha CC; o diagnóstico começa pelos cabos e painéis antes de qualquer intervenção no inversor
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581093806997-124204d9fa9d?w=1200
→ Por que foi escolhida: Técnico realizando medição com instrumento de teste em equipamento eletrônico — representa o uso do megohmmeter para diagnóstico de isolamento descrito na seção de identificação prática
→ Nome do arquivo: canadian-solar-falha-117-megohmmeter-diagnostico-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo resistência de isolamento com megohmmeter em string fotovoltaica — diagnóstico Canadian Solar Falha 117
→ Legenda: Fig. 2 — O megohmmeter aplicando 500 VDC é o instrumento correto para diagnóstico de isolamento em strings fotovoltaicos; o multímetro convencional não detecta falhas sob tensão real de operação
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB

<!-- trigger-video-workflow -->

<!-- debug-elevenlabs-v2 -->
<!-- trigger-adam-voice -->
