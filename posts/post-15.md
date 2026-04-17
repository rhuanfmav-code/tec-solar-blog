# Post 15 — SMA 3701: Tensão CC Muito Alta — string mal dimensionada ou falha de medição?

---

## [PALAVRA-CHAVE FOCO]

SMA 3701 tensão CC muito alta diagnóstico

---

## [TÍTULO SEO — Title Tag]

SMA 3701: Tensão CC Muito Alta — Causa e Diagnóstico

---

## [SLUG — URL do Post]

sma-3701-tensao-cc-muito-alta-diagnostico

---

## [META DESCRIPTION]

SMA 3701: tensão CC muito alta no Sunny Boy. Saiba como separar string mal dimensionado de defeito no circuito de medição antes de trocar o inversor.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

SMA 3701, tensão CC inversor solar, Sunny Boy diagnóstico, string fotovoltaico sobretenso, divisor de tensão inversor

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **SMA 3701 — tensão CC muito alta** trava o inversor antes mesmo de ele injetar potência na rede. O sistema para, a geração vai a zero, e quem chega ao quadro encontra o Sunny Boy em modo de erro com uma informação que parece clara mas não é: a tensão está alta — mas o código não diz se está alta de verdade ou se o inversor está medindo errado.

Na nossa bancada, esse código chega com frequência acompanhado de uma decisão já tomada: "string mal dimensionado." Às vezes está. Mas recebemos equipamentos vindos da região Sul do Brasil onde o instalador já havia recalculado o string, retirado um painel e o 3701 voltou dois dias depois. Quando o inversor chegou até nós, o problema era um divisor de tensão CC com resistor SMD fora de especificação — lendo 18% acima do valor real. O string estava dentro do limite desde o início.

Antes de mexer no projeto elétrico ou condenar o inversor, medir. Sempre medir primeiro.

---

## O que causa o SMA 3701

O SMA Sunny Boy monitora a tensão CC nos terminais de entrada por um circuito de condicionamento de sinal dedicado: um divisor resistivo de alta impedância reduz a tensão de entrada ao nível de operação do conversor ADC no DSP. Quando o valor lido ultrapassa o limiar de Vmax configurado — 600 V nos modelos residenciais da série anterior, até 1000 V nos modelos mais recentes — o evento 3701 é disparado e a conversão é interrompida imediatamente.

Isso significa que a leitura pode refletir a realidade ou pode estar errada. As causas se dividem em dois grupos com soluções completamente diferentes.

**Tensão real elevada — o string está fora do limite:**

- String dimensionado sem contemplar a temperatura mínima registrada no local de instalação. Painéis com coeficiente de temperatura de Voc de -0,34%/°C têm tensão de circuito aberto cerca de 10% maior a -5°C do que a 25°C. Em regiões serranas de Minas Gerais, do Paraná e de Santa Catarina, isso não é hipótese — é cenário real de inverno. A NBR 16149 exige que o cálculo de Vmax da string contemple a temperatura mínima histórica do local, não a média
- Painel substituto instalado durante manutenção com Voc maior do que o original — troca feita sem comparar os datasheets dos dois modelos
- Conexão errada de dois strings em série em vez de paralelo, dobrando a tensão de entrada do MPP tracker
- Diodo de bypass com curto em um ou mais painéis do string, alterando o comportamento de tensão em condições de sombra parcial e empurrando a tensão total para fora do ponto de operação esperado

**Tensão aparente elevada — o circuito de medição está errando:**

- Resistores SMD do divisor de tensão CC com tolerância desviada por ciclos térmicos acumulados. Esses componentes operam sob estresse contínuo e, com o tempo, saem da especificação de 0,1% para 3–5% — desvio suficiente para que a leitura ultrapasse o limiar de 3701 quando a tensão real ainda está dentro do limite
- Capacitores de desacoplamento no circuito de condicionamento do ADC com ESR elevado, introduzindo ruído na amostragem e causando leituras instáveis acima do threshold
- Canal ADC do DSP com degradação parcial por descarga eletrostática — não queima completamente, mas passa a reportar valores sistematicamente acima do real
- Varistor MOV na entrada CC operando próximo ao nível de clamping durante condições normais de tensão, sintoma de proteção de entrada degradada e não de tensão fora do limite

Dois cenários com diagnósticos opostos. Soluções opostas. Contas opostas.

---

## Como identificar na prática

O primeiro passo não é abrir o inversor. É medir a tensão real nos terminais de entrada antes de qualquer outra coisa.

1. Com o disjuntor CA do inversor aberto e os strings CC expostos à irradiação solar, medir a tensão CC nos terminais de entrada com multímetro calibrado — positivo e negativo de cada entrada MPPT separadamente
2. Comparar o valor medido com o Voc calculado para as condições do momento: aplicar o coeficiente de temperatura de Voc do painel à temperatura ambiente registrada no instante da medição
3. Se a tensão medida estiver dentro do limite operacional do modelo: o problema está no circuito interno de medição — o string não precisa ser alterado
4. Se a tensão real estiver acima do Vmáx do inversor: o string precisa de adequação antes de qualquer trabalho em bancada
5. Com o inversor em bancada, medir a tensão real nos pontos de entrada internos com osciloscópio e comparar com o valor que o DSP está reportando na interface. Discrepância de 10% ou mais entre o valor medido fisicamente e o valor reportado aponta diretamente para o divisor resistivo ou para o ADC
6. Identificar os resistores do divisor de tensão CC no esquema do modelo e medir o valor real com multímetro de alta precisão (4,5 dígitos). Resistores de 100 kΩ lendo 106 kΩ ou mais, combinados em série no divisor, somam desvio suficiente para disparar o 3701 com tensão real dentro do limite

Um padrão que aparece com alguma regularidade: o 3701 ocorrendo em horários específicos — manhã fria ou final de tarde. String com subdimensionamento térmico se manifesta nas temperaturas mais baixas do dia. Circuito interno com problema térmico pode fazer o mesmo. Registrar o horário das falhas antes de qualquer conclusão.

---

## O erro mais comum do mercado

Reconfigurar o string sem medir a tensão real nos terminais primeiro.

O instalador vê o 3701, revisa o projeto, percebe que o string está próximo ao limite e remove um painel "como precaução". O inversor volta a funcionar. Na próxima manhã fria de julho, o 3701 retorna — porque o problema nunca foi o string.

O oposto também acontece: substituir o inversor sem verificar se a tensão real realmente estava acima do limite. Um SMA Sunny Boy residencial custa entre R$ 3.000 e R$ 5.000 novo. Um divisor de tensão CC reconstruído com resistores SMD de precisão sai por menos de R$ 100 em componentes. Não são situações equivalentes — mas sem medir antes, é impossível saber em qual delas você está.

Condenar sem medir não é diagnóstico. É aposta.

---

## Quando o reparo é viável

Se o diagnóstico confirmou origem interna, o componente define o prognóstico.

**Resistores SMD do divisor de tensão CC** — componentes passivos, substituição com equivalentes de tolerância ≤ 0,1%. Reparo viável, custo de componentes baixo. Exige identificação correta no esquema do modelo e multímetro de precisão para verificação pós-reparo.

**Capacitores de desacoplamento no condicionamento ADC** — substituição direta com equivalentes de mesma especificação. Viável em bancada equipada.

**Varistor MOV da entrada CC** — componente de proteção, substituição com equivalente dentro da especificação do datasheet. Necessário independente da decisão sobre o restante.

**Canal ADC do DSP com degradação** — o cenário mais trabalhoso. Dependendo do modelo, pode exigir substituição do DSP ou da placa de controle completa. A viabilidade depende do que está disponível no mercado para aquele modelo específico e do custo comparado ao inversor novo. Não há como concluir isso antes de abrir o equipamento e medir.

O que define se o reparo é possível não é o código de erro — é o componente que falhou.

---

## Conclusão

SMA 3701 não diz se o string está errado ou se a placa está lendo errado. Diz só que a tensão registrada pelo DSP passou do limite. São dois diagnósticos, duas soluções e duas contas completamente diferentes.

Antes de reprojetar o string ou comprar um inversor novo, leve até a bancada. Meça a tensão real. Compare com o que o circuito está reportando. É aí que o 3701 mostra o que realmente é.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "tensão CC nos terminais de entrada" → Link para: post sobre SMA 3501: Falha de Isolamento (Post 04)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "NBR 16149" → Fonte: ABNT — Sistemas fotovoltaicos — Características da interface de conexão com a rede elétrica de distribuição (abnt.org.br)
- Texto âncora: "coeficiente de temperatura de Voc" → Fonte: IEC 60891 — Photovoltaic devices: procedures for temperature and irradiance corrections (iec.ch)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Inversor solar instalado com conexão CC visível — representa diretamente o ponto onde a tensão de string entra no SMA Sunny Boy e onde o 3701 é disparado
→ Nome do arquivo: sma-3701-tensao-cc-muito-alta-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Inversor solar SMA Sunny Boy instalado — diagnóstico do erro 3701 por tensão CC muito alta no string fotovoltaico
→ Legenda: Fig. 1 — SMA 3701 pode indicar string sobretenso ou falha no circuito de medição interno; apenas a medição real diferencia os dois
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=1200
→ Por que foi escolhida: Técnico medindo com multímetro em instalação elétrica — representa o procedimento de medição da tensão CC real nos terminais descrito na seção "Como Identificar na Prática"
→ Nome do arquivo: sma-3701-medicao-tensao-cc-string-multimetro-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensão CC com multímetro em string fotovoltaico — diagnóstico SMA 3701 tensão muito alta
→ Legenda: Fig. 2 — Medir a tensão real nos terminais de entrada antes de abrir o inversor é o primeiro passo do diagnóstico do SMA 3701
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB
