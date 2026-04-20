# Post 21 — O que é o driver de IGBT e por que sua falha destrói o estágio de potência

---

## [PALAVRA-CHAVE FOCO]

driver de IGBT inversor solar

---

## [TÍTULO SEO — Title Tag]

Driver de IGBT: o que é e por que sua falha destrói o inversor

---

## [SLUG — URL do Post]

driver-de-igbt-inversor-solar

---

## [META DESCRIPTION]

Entenda o que é o driver de IGBT, como ele falha de forma silenciosa e por que destrói o estágio de potência antes de qualquer alarme aparecer.

---

## [CATEGORIA]

Análise Técnica de Componentes

---

## [TAGS]

driver de IGBT inversor solar, gate driver IGBT, IGBT queimado causa raiz, estágio de potência inversor, diagnóstico inversor solar bancada

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **driver de IGBT** é o componente que fica entre o processador de controle e o transistor de potência. Parece simples — recebe um pulso digital e aciona um gate. Mas quando falha, o inversor não para de forma limpa. Ele queima tudo que tem pela frente.

Na nossa bancada, a maior parte dos inversores que chegam com IGBT destruído não teve o transistor como primeiro a falhar. O driver cedeu antes. O IGBT foi a vítima. E o técnico anterior trocou o módulo de potência sem perceber isso — o equipamento voltou a queimar em semanas, às vezes menos.

---

## O que o driver realmente faz no circuito

O DSP de controle trabalha com sinais de 3,3 V ou 5 V — corrente insuficiente para comutar um gate de IGBT com velocidade adequada. O gate driver amplifica esse sinal e entrega tensões na faixa de **+15 V para condução** e de **−8 V a −15 V para bloqueio**.

A tensão negativa no bloqueio não é detalhe. Sem ela, o IGBT pode conduzir parcialmente durante a transição, especialmente com barramento DC elevado e frequência de chaveamento alta. Em inversores operando em regiões com irradiância intensa — como o sertão nordestino ou o planalto central — o barramento DC passa boa parte do dia próximo ao valor máximo de projeto. Qualquer instabilidade no driver nesse ponto vira problema térmico rapidamente.

Os ICs de driver mais comuns em inversores on-grid de potência média são o HCPL-314J (Broadcom), o 2ED020I12-F (Infineon) e o SKHI22A (Semikron). Todos oferecem isolação galvânica, proteção por detecção de dessaturação (DESAT) e capacidade de corrente de pico para carga rápida do gate.

O gate de um IGBT de potência média tem capacitância entre 10 nF e 100 nF. O driver precisa transferir essa carga em menos de 500 ns — e repetir isso dezenas de milhares de vezes por segundo. É um trabalho constante, invisível e crítico.

Quando o driver para de fazer isso corretamente, o efeito nem sempre é imediato.

---

## Como o driver falha na prática

Existem quatro modos que aparecem com frequência:

**Degradação do optoacoplador de isolação.** O LED interno perde eficiência ao longo do tempo. A corrente de transferência (CTR) cai. O sinal chega ao gate com atraso ou com amplitude reduzida — a tensão cai de +15 V para +12 V ou +11 V. O IGBT ainda comuta, mas opera em saturação parcial. O Vce(sat) sobe, a dissipação de potência cresce. Nenhum alarme é acionado. Nada aparece no display.

**Queda de tensão na fonte bootstrap.** Em circuitos que usam capacitor de bootstrap para gerar a alimentação do driver do IGBT superior do braço: se esse transistor ficar muito tempo desligado, o capacitor descarrega. A tensão do driver cai abaixo do limiar de UVLO (under-voltage lockout) do IC — geralmente 13 V. A saída é desabilitada. Por instantes, o gate fica flutuante, em potencial intermediário. Condução parcial não controlada.

**Falha na proteção DESAT.** A detecção de dessaturação monitora o Vce durante a condução: em operação normal, fica abaixo de 2 V. Com um curto-circuito, a corrente sobe, o IGBT sai da saturação e o Vce vai para 5 V, 10 V ou mais. O DESAT detecta isso e desliga o gate em 2 a 10 µs. Se o diodo de blanking abre, ou o resistor de detecção saiu de valor, a proteção não age. O curto passa inteiro.

**Resistor de gate fora de valor.** Se abre, o IGBT para de comutar. Se curta, o gate é carregado rápido demais — os picos de Vce durante o bloqueio ultrapassam o rating do módulo. O IGBT vai a avalanche. O primeiro evento pode não destruir. No segundo, destrói.

Quatro modos. Cada um com assinatura diferente no osciloscópio.

---

## O que verificar na bancada

Antes de qualquer conclusão sobre o IGBT, o circuito de driver precisa ser avaliado:

1. Desligar o inversor e aguardar mínimo de 5 minutos para descarga dos capacitores do barramento DC. Medir a tensão antes de tocar no circuito.
2. Medir o IGBT com multímetro em modo diodo entre coletor e emissor, com gate desconectado. IGBT saudável tem alta impedância em ambas as direções — exceto o diodo de roda livre, que conduz apenas em polaridade direta.
3. Com o inversor energizado em CC (CA desabilitada), medir a tensão de saída do driver no gate durante operação. Nível alto entre +14 V e +16 V. Nível baixo entre −8 V e −15 V. Tensão acima de −3 V no bloqueio indica falha.
4. Verificar a tensão de alimentação do IC de driver — a fonte auxiliar isolada deve estar dentro da faixa de operação. IC em UVLO não gera sinal mesmo com entrada correta.
5. Inspecionar o circuito DESAT: diodo de blanking, resistor de detecção e capacitor de filtro. São os componentes que garantem que o driver consiga derrubar o gate em uma falha de curto-circuito.
6. Osciloscópio no gate: borda de subida com overshoot acima de 20 V de pico indica Rg errado ou ausente. Tempo de rise acima de 1 µs indica driver degradado ou optoacoplador com CTR baixo.
7. Verificar se há assimetria entre os braços — um braço chaveando com timing diferente do outro quase sempre aponta para problema no driver daquele braço específico.

Cada ponto desses responde a uma pergunta diferente. Pular etapas não adianta.

---

## O erro que repete o problema

Técnico abre o inversor, mede o IGBT em curto, troca o módulo, fecha e devolve. Semanas depois o mesmo módulo está destruído de novo.

Isso acontece toda semana em algum lugar.

O driver nunca foi verificado. O optoacoplador continua degradado. A fonte bootstrap continua trabalhando no limite. E o módulo novo entrou num ambiente que já demonstrou, com o módulo anterior, que vai destruir o que vier pela frente.

Não é negligência — é falta de método. O IGBT em curto é o sintoma mais óbvio, então vira o diagnóstico. Mas o diagnóstico verdadeiro está no que matou o IGBT, não no IGBT morto.

---

## Quando o reparo faz sentido

O estágio de potência com driver e IGBT destruídos é viável de reparar quando:

- O dano está localizado: módulo IGBT e IC de driver danificados, sem carbonização da placa de potência
- Os demais IGBTs do mesmo braço e das outras fases ainda estão íntegros ao teste de diodo
- A placa de controle não foi afetada — os sinais PWM chegam corretos ao circuito de driver
- As trilhas de cobre da placa de potência estão intactas, sem vaporização ou levantamento de cobre
- Os resistores de gate e capacitores snubber passam na verificação passiva
- Não há carbonização visível entre trilhas do barramento DC

Se o evento foi um shoot-through completo — curto simultâneo entre IGBT superior e inferior do mesmo braço — o barramento DC descarregou sobre os módulos com corrente de centenas de ampères. A destruição se espalha para componentes passivos do entorno. Nesse caso, a avaliação precisa ser mais detalhada antes de decidir pelo reparo.

Mas quando o dano está contido, a conta é direta: módulo IGBT de 600 V/50 A sai entre R$ 80 e R$ 200. IC de driver, entre R$ 30 e R$ 80. Total abaixo de R$ 300 em componentes, mais o serviço. Versus inversor novo de 5 kW: R$ 2.500 a R$ 4.000.

Não tem como ignorar essa diferença.

---

## Conclusão

O driver de IGBT não é acessório. É a estrutura que mantém o transistor de potência sob controle — e quando essa estrutura quebra de forma silenciosa, o IGBT não tem como sobreviver.

Trocar o módulo sem diagnosticar o driver é resolver o sintoma. O problema continua lá, esperando o próximo ciclo.

---

Condenaram seu inversor por causa desse erro?

Antes de comprar equipamento novo, envie para a nossa bancada. A TEC Solar realiza diagnóstico eletrônico completo em nível de componente — abrimos o inversor, medimos a placa, identificamos a causa raiz e entregamos um laudo técnico detalhado.

Se o reparo for viável, você recebe o equipamento funcionando por uma fração do custo de substituição. Se não for, o laudo serve de base para qualquer decisão.

Atendemos todo o Brasil via logística reversa.

👉 [Envie seu inversor agora](https://wa.me/5538998891587) | [Falar no WhatsApp](https://wa.me/5538998891587)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "Por que os IGBTs queimam em inversores solares" → Link para: post sobre as 6 causas reais de queima de IGBT (Post 10)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "HCPL-314J" → Fonte: Datasheet Broadcom HCPL-314J Gate Drive Optocoupler (broadcom.com)
- Texto âncora: "2ED020I12-F" → Fonte: Datasheet Infineon 2ED020I12-F EiceDRIVER Gate Driver IC (infineon.com)
- Texto âncora: "detecção de dessaturação (DESAT)" → Fonte: Infineon Application Note — IGBT Gate Driver with Desaturation Detection (infineon.com)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Placa de circuito impresso com componentes de potência em destaque — representa diretamente o circuito de driver de gate e o ambiente de diagnóstico em bancada
→ Nome do arquivo: driver-igbt-inversor-solar-placa-potencia.webp
→ Alt Text (máx. 125 caracteres): Placa de circuito com componentes de driver de IGBT em inversor solar — diagnóstico do estágio de potência em bancada
→ Legenda: Fig. 1 — O circuito de driver de IGBT fica entre o DSP de controle e o módulo de potência; sua falha silenciosa destrói o transistor antes de qualquer alarme ser gerado
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=1200
→ Por que foi escolhida: Técnico com osciloscópio medindo sinais em placa eletrônica — representa o procedimento de verificação da tensão de gate e forma de onda PWM descrito na seção de diagnóstico na bancada
→ Nome do arquivo: driver-igbt-osciloscópio-gate-diagnostico-2.webp
→ Alt Text (máx. 125 caracteres): Técnico usando osciloscópio para medir tensão de gate do driver de IGBT em placa de inversor solar — diagnóstico em bancada
→ Legenda: Fig. 2 — O osciloscópio no gate do IGBT revela a assinatura da falha do driver: borda de subida lenta, overshoot excessivo ou tensão de bloqueio insuficiente
→ Onde inserir: Após H2 "O que verificar na bancada"
→ Converter para WebP — máximo 150 KB

<!-- trigger-video-workflow -->

<!-- debug-elevenlabs-v2 -->
<!-- trigger-adam-voice -->
