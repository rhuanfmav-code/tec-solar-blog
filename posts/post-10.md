# Post 10 — Por que os IGBTs queimam em inversores solares: as 6 causas reais

---

## [PALAVRA-CHAVE FOCO]

queima de IGBT inversor solar causas

---

## [TÍTULO SEO — Title Tag]

Por que o IGBT do Inversor Solar Queima: 6 Causas

---

## [SLUG — URL do Post]

igbt-inversor-solar-causas-queima

---

## [META DESCRIPTION]

Descubra as 6 causas técnicas reais que queimam o IGBT de inversores solares: sobretensão, driver com defeito, ciclos térmicos e mais.

---

## [CATEGORIA]

Análise Técnica de Componentes

---

## [TAGS]

queima de IGBT, IGBT inversor solar, driver de IGBT, falha estágio de potência, diagnóstico inversor solar

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **IGBT (Insulated Gate Bipolar Transistor)** é o ponto de maior tensão elétrica e térmica em um inversor solar. Quando ele vai a curto, o inversor para — às vezes com um estouro, às vezes silenciosamente, sempre com o sistema parado. O técnico chega ao campo, o integrador liga reclamando, o cliente quer resposta.

Na nossa bancada, o IGBT danificado é a falha de estágio de potência que mais entra pela porta. E o que vemos com frequência não é só o módulo queimado — é o mesmo módulo sendo substituído pela segunda vez no mesmo equipamento, porque o primeiro reparo não investigou a causa raiz. O módulo novo chega, liga, e em semanas está no mesmo estado.

Antes de mandar buscar peça, você precisa entender por qual das 6 causas aquele módulo foi destruído.

---

## O que torna o IGBT vulnerável

O IGBT comuta centenas de vezes por segundo. Em cada ciclo ele vai de bloqueio total para condução plena e volta — alternando entre tensão máxima com corrente zero e corrente máxima com tensão mínima. Esse processo gera calor, estresse eletromagnético e tensão mecânica nas junções internas.

Os limites críticos definidos pelo fabricante — Vces (tensão coletor-emissor), Ic (corrente de coletor) e Tj máx. (temperatura de junção, tipicamente 150–175°C) — formam o envelope operacional. Qualquer cruzamento de limite, mesmo momentâneo, pode ser fatal.

Em nanossegundos.

---

## As 6 causas reais de queima do IGBT

### 1. Sobretensão por pico de comutação

No momento em que o IGBT bloqueia, a corrente de coletor cai abruptamente. A indutância parasita do barramento DC — pequena, mas presente em qualquer trilha de PCB — gera um pico de tensão proporcional à taxa de variação da corrente: V = L × (dI/dt).

Se esse pico ultrapassar o Vces do módulo, o IGBT entra em avalanche. A corrente se concentra em um ponto microscópico do die de silício, a temperatura naquele ponto excede 250°C em microssegundos — o limiar de condução intrínseca do silício — e o bloqueio se perde de forma permanente. O módulo fica em curto.

Os capacitores snubber e varistores do barramento DC existem para absorver esses picos. Quando degradam, o IGBT fica desprotegido.

### 2. Falha no driver de gate

O driver aplica tensão de gate ao IGBT para comandar condução (+15 V) e bloqueio (−8 V a −15 V). Se a tensão em nível alto cair abaixo do ponto correto — por optoacoplador degradado, resistor de gate com valor errado ou falha na fonte auxiliar do driver — o IGBT opera em região de saturação parcial.

Nessa condição, a queda de tensão Vce(sat) aumenta. Com mais tensão sobre o módulo durante a condução, a dissipação de potência cresce sem que os sensores de temperatura do inversor detectem rápido o suficiente. O módulo aquece de forma acelerada até a falha.

Já recebemos inversores com driver fornecendo 11–12 V no gate em vez de 15 V. A diferença é pequena na medição, mas o impacto térmico sobre o IGBT é considerável durante horas de operação contínua.

### 3. Fadiga de bond wire por ciclos térmicos

Essa é a causa mais lenta — e a que mais surpreende quando aparece num equipamento aparentemente bem mantido.

O coeficiente de expansão térmica do silício (~2,6 ppm/°C) é muito diferente do alumínio dos fios de bonding (~23 ppm/°C) e do substrato de cerâmica (~7 ppm/°C). A cada ciclo de geração — aquecimento ao amanhecer, pico solar ao meio-dia, resfriamento ao entardecer — esses materiais se expandem e contraem em proporções diferentes. O estresse mecânico se acumula nas interfaces.

Depois de centenas de milhares de ciclos, os fios de bonding se desprendem da superfície do die (processo chamado de lift-off). Os fios restantes passam a carregar mais corrente, aquecendo mais rápido, acelerando o processo.

Estudos publicados no IEEE Transactions on Power Electronics mostram que a amplitude ΔTj — variação de temperatura de junção por ciclo — é o principal preditor de vida útil dos bond wires. Para ΔTj de 80°C, a expectativa de vida pode ficar abaixo de 10.000 ciclos. Em módulos com 8–12 anos de operação em regiões de alta irradiância como o Nordeste e o Centro-Oeste brasileiro, essa causa aparece com frequência crescente.

### 4. Superaquecimento por falha no sistema de refrigeração

Ventilador parado. Dissipador entupido de poeira. Pasta térmica ressecada entre o módulo e o dissipador. Qualquer um desses fatores eleva a temperatura de junção acima do limite máximo — e o módulo falha por degradação acelerada das soldas internas.

Em galpões sem climatização, em telhados fechados sem circulação de ar, em inversores instalados diretamente ao sol — condições comuns no Brasil, especialmente em instalações de baixo custo — a temperatura ambiente já reduz a margem de segurança térmica disponível. Um ventilador que gira na metade da velocidade nominal por desgaste nos rolamentos não aparece em nenhum código de erro. Mas está destruindo o módulo devagar.

Pasta térmica seca é especialmente traiçoeira. Não tem alarme, não tem código. A resistência térmica entre o módulo e o dissipador simplesmente aumenta.

### 5. Sobrecorrente por shoot-through ou falha de sincronismo PWM

Num braço do inversor, há dois IGBTs: um superior e um inferior. Se ambos conduzirem ao mesmo tempo — mesmo por microsegundos — a tensão do barramento DC cai diretamente sobre os módulos. A corrente sobe para centenas de ampères em questão de microssegundos.

Esse evento, chamado de shoot-through, destrói o módulo. A proteção de desaturação (dessat) detecta sobrecorrente pela elevação de Vce e tenta desligar o gate em 2–10 µs, mas se a corrente subir rápido demais, o dano já está feito antes de a proteção agir.

Shoot-through acontece quando o sincronismo PWM falha — geralmente por problema na placa de controle, sinal corrompido no barramento de dados, ou perda temporária de tensão na fonte auxiliar. É o modo de falha mais destrutivo: frequentemente queima o módulo, o driver e o fusível DC ao mesmo tempo.

### 6. Contaminação e umidade no módulo

Módulos IGBT têm encapsulamento de resina epóxi e gel de silicone interno. Com o tempo, especialmente em ambientes úmidos — áreas costeiras, regiões de chuva intensa, galpões com vapor — a umidade penetra pelos terminais ou pela interface entre o módulo e o dissipador.

Na superfície do substrato de cerâmica, a umidade cria caminhos de condução não intencional entre trilhas de potencial diferente. Com alta tensão CC aplicada, ocorre corrosão eletroquímica e tracking — trilhamento dielétrico que progride lentamente até o arco ou o curto-circuito.

O módulo pode aparecer visualmente intacto por fora. O diagnóstico correto exige megohmmêtro ou câmera térmica em operação.

---

## Como identificar na prática

O diagnóstico começa com o inversor desligado e os capacitores de barramento descarregados — aguardar no mínimo 5 minutos após desligar a tensão CC antes de tocar na placa:

1. Medir em modo diodo entre coletor e emissor de cada IGBT. IGBT em curto indica resistência próxima de zero ou condução direta nas duas direções, sem polaridade preferencial.
2. Verificar a tensão de saída do driver com o inversor energizado apenas pela CC, sem CA habilitado. Gate em nível alto deve estar entre +14 V e +16 V. Qualquer leitura abaixo de 13 V já é suspeita.
3. Inspecionar capacitores snubber e varistores do barramento DC: capacitores com tampa abaulada ou varistores com marcas de arco confirmam sobretensão como causa provável.
4. Verificar o ventilador: girar manualmente para detectar travamento, medir continuidade das bobinas. Um ventilador que gira lento não aciona proteção alguma, mas é suficiente para elevar Tj acima do limite.
   — Se o dissipador estiver com acúmulo de poeira, limpar antes de qualquer outra conclusão. Poeira em dissipador de alumínio com aletas reduz drasticamente a troca de calor por convecção.
5. Examinar a pasta térmica entre o módulo e o dissipador: pasta ressecada, fragmentada ou ausente é causa suficiente para queima progressiva.
6. Com osciloscópio nos pinos de gate do driver, verificar se os pulsos PWM chegam com temporização correta e sem assimetria de duty cycle. Borda de subida lenta indica resistor de gate com valor alto ou optoacoplador lento.

---

## O erro mais comum do mercado

Substituir o módulo IGBT sem eliminar a causa da queima.

O módulo novo é instalado, o inversor volta a funcionar, o chamado é fechado. Duas semanas depois o mesmo inversor volta — com o módulo novo queimado no mesmo padrão do anterior.

O custo de um módulo IGBT para inversor residencial fica entre R$200 e R$600 dependendo do modelo. Substituir duas vezes, sem resolver a causa, já sai mais caro do que um diagnóstico completo teria custado. E o cliente perdeu mais duas semanas de geração.

O que a gente vê com frequência: driver não verificado, pasta térmica não trocada, snubbers não checados. O módulo foi substituído em cima de uma causa ativa.

---

## Quando o reparo é viável

A viabilidade depende de até onde o dano se propagou. Um IGBT em curto contido na placa de potência, com driver intacto e placa de controle sem dano, é reparo direto na maioria dos casos.

Quando o shoot-through ocorre, o dano costuma se estender: módulo, driver, fusível CC, às vezes o barramento CC. Ainda assim, o reparo pode ser viável dependendo do modelo e do custo das peças.

A comparação objetiva: reparo com diagnóstico completo em inversores residenciais fica entre R$400 e R$900 na maioria dos casos. Inversor novo equivalente, entre R$3.000 e R$6.000. A diferença justifica sempre tentar o diagnóstico antes de decidir pelo descarte.

Placa de controle danificada junto com o estágio de potência complica — mas não descarta o reparo automaticamente. Depende da disponibilidade de peças e do modelo específico.

---

## Conclusão

O IGBT queima por uma razão. Às vezes é um evento único — pico de tensão, curto externo. Às vezes é acúmulo de anos: ciclos térmicos, pasta degradada, ventilador envelhecendo. Em qualquer caso, a causa existe e pode ser identificada antes de qualquer substituição.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "sobretensão CC no barramento" → Link para: post sobre WEG E001 – Sobretensão CC (Post 06)
- Âncora: "tensão CC acima do limite de entrada" → Link para: post sobre Fronius State 102 – Tensão CC Muito Alta (Post 02)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEEE Transactions on Power Electronics" → Fonte: IEEE Xplore — Prediction of Bond Wire Fatigue of IGBTs in a PV Inverter (ieeexplore.ieee.org)
- Texto âncora: "módulos IGBT" → Fonte: Dynex Semiconductor – AN6442: IGBT Module Failure Mechanisms (dynexsemi.com)
- Texto âncora: "proteção de desaturação" → Fonte: Fuji Electric – Failure Modes of IGBTs and How to Prevent Them (americas.fujielectric.com)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Close de placa de circuito eletrônico com componentes de potência — representa o ambiente de bancada e o foco em nível de componente do diagnóstico de IGBT descrito no post
→ Nome do arquivo: igbt-inversor-solar-causas-queima-placa-potencia.webp
→ Alt Text (máx. 125 caracteres): Placa de potência de inversor solar com módulo IGBT — diagnóstico das 6 causas reais de queima em nível de componente eletrônico
→ Legenda: Fig. 1 — Estágio de potência de inversor solar: o módulo IGBT é o componente de maior tensão e temperatura do circuito
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200
→ Por que foi escolhida: Técnico com equipamento de medição em ambiente de bancada — representa a etapa de diagnóstico com multímetro e osciloscópio descrita na seção "Como identificar na prática"
→ Nome do arquivo: diagnostico-igbt-inversor-solar-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Técnico realizando diagnóstico de IGBT em bancada eletrônica — medição de tensão de gate e verificação do driver de inversor solar
→ Legenda: Fig. 2 — Diagnóstico de IGBT na bancada: a verificação da tensão de gate e do driver precede qualquer decisão de substituição de módulo
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB
