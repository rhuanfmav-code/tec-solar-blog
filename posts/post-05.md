# Post 05 — Sungrow Grid Lost: Perda de Rede — Disjuntor, Cabeamento ou Defeito Interno?

---

## [PALAVRA-CHAVE FOCO]

sungrow grid lost perda de rede diagnóstico inversor solar

---

## [TÍTULO SEO — Title Tag]

Sungrow Grid Lost: Perda de Rede — Causa e Diagnóstico

---

## [SLUG — URL do Post]

sungrow-grid-lost-perda-de-rede-diagnostico

---

## [META DESCRIPTION]

Inversor Sungrow com Grid Lost? Veja como identificar se o problema é disjuntor, cabeamento AC ou circuito interno — diagnóstico em nível de placa.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Sungrow, Grid Lost, perda de rede, erro inversor solar, diagnóstico AC

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **erro Grid Lost no inversor Sungrow** trava o sistema, e o integrador recebe a ligação do cliente às 10h da manhã com inversor parado e zero geração no dia. Parece problema de rede. Às vezes é. Mas na maioria dos casos que chegam até nós, a rede elétrica estava funcionando normalmente — e o inversor estava errado sobre o que aconteceu.

Na nossa bancada, o padrão é consistente: o inversor reporta Grid Lost, o técnico verifica a tomada mais próxima, vê tensão, decide que é bug e faz reset. O inversor volta por alguns dias. O ciclo se repete até que não volta mais. Nesse ponto, o cliente quer trocar o equipamento. Antes de assinar o pedido de compra, vale a pena medir o que está chegando de fato nos bornes de entrada AC do inversor.

O "Grid Lost" — ou "AC Grid Lost", dependendo da versão de firmware — indica que o circuito de supervisão de rede do Sungrow não está detectando tensão AC dentro dos parâmetros operacionais. Isso não significa, obrigatoriamente, que a rede elétrica sumiu. Significa que o inversor não está vendo a rede.

São dois problemas completamente diferentes.

---

## O que causa esse erro no Sungrow

O circuito de supervisão de rede nos inversores Sungrow (famílias SG, SH e SG-RT) monitora continuamente a tensão, a frequência e, nos modelos trifásicos, a simetria de fases. Quando qualquer desses parâmetros sai do envelope operacional — ou desaparece completamente — o inversor dispara a proteção anti-ilhamento, abre o relé de rede e registra o erro.

A proteção anti-ilhamento nos modelos Sungrow homologados para o Brasil segue a ABNT NBR 16149, que exige desconexão em menos de 2 segundos quando a frequência sai de 55–65 Hz ou a tensão ultrapassa 10% da nominal. Isso é correto e obrigatório. O problema começa quando o inversor dispara fora dessas condições — e continua reportando Grid Lost com rede presente.

Causas reais, em ordem de frequência:

1. **Disjuntor AC com mau contato ou subdimensionado** — micro-abertura cíclica que o técnico não detecta sem medição direta no barramento de saída
2. **Cabos AC subdimensionados ou com queda de tensão excessiva** — o inversor não enxerga a tensão mínima no borne AC mesmo com rede presente no quadro
3. **Terminal de conexão AC com aperto insuficiente** — vibração e ciclos térmicos afrouxam terminais de cobre progressivamente; o contato piora durante geração de pico
4. **Relé de rede interno com falha de fechamento** — contato oxidado ou com carbonização que não fecha com confiabilidade, gerando leitura de tensão intermitente no circuito de supervisão
5. **Circuito de amostragem de tensão AC com deriva** — divisor resistivo ou amplificador operacional na placa de controle com leitura distorcida por corrosão ou variação de temperatura
6. **Transiente de rede da concessionária** — queda de tensão momentânea de 200 ms já basta para disparar a proteção em alguns firmwares Sungrow, dependendo da parametrização

Nenhum desses pontos aparece com visual de "inversor queimado". O equipamento parece intacto. Por isso o Grid Lost leva tanto tempo para ser diagnosticado corretamente.

---

## Como identificar na prática

O diagnóstico começa do ponto mais externo e vai entrando. Não o contrário.

**Procedimento de verificação:**

1. Meça a tensão CA no barramento do QDC (quadro de distribuição) com carga real ligada — não em tomada
2. Meça na saída do disjuntor dedicado do inversor
3. Meça diretamente nos bornes de conexão AC do inversor, com o equipamento em standby
4. Calcule a queda de tensão entre o ponto 2 e o ponto 3: qualquer valor acima de 3V com o inversor desligado indica resistência elevada no cabeamento ou nos terminais
5. Com o inversor desenergizado, retire os cabos AC dos bornes e meça a resistência de cada condutor entre o QDC e o inversor — limite prático: máximo 0,3 Ω por condutor em cabos até 15 m
6. Verifique o torque de aperto dos terminais conforme a especificação Sungrow: 1,5 a 2,5 Nm para bornes AC residenciais

Se a tensão chega corretamente nos bornes e o inversor continua reportando Grid Lost após religar, o problema é interno.

Nesse ponto, o diagnóstico vai para a placa. O circuito de supervisão AC do Sungrow usa um divisor resistivo para escalonamento de tensão, seguido de um condicionador de sinal. Na bancada, o procedimento é medir a tensão antes e depois do divisor. Se a tensão real está presente na entrada mas o sinal processado está ausente ou distorcido, o problema está nos resistores de precisão ou no amplificador de condicionamento.

Inversores Sungrow que operam no litoral brasileiro — especialmente no trecho entre Pernambuco, Alagoas e Sergipe — chegam com esse circuito corroído por névoa salina. A corrosão aumenta a resistência dos resistores de divisão e distorce completamente a leitura. O inversor reporta Grid Lost porque genuinamente não está lendo tensão nenhuma, mesmo com a rede normal.

---

## O erro mais comum do mercado

O técnico mede a tensão na tomada mais próxima do quadro, vê 220 V, e conclui que a rede está normal. Fecha o chamado como "falha transitória da concessionária" e reseta o inversor.

Ninguém mediu os bornes AC do inversor. Ninguém verificou o disjuntor dedicado sob carga. Ninguém apertou os terminais.

O inversor volta, funciona por uma semana, e o Grid Lost aparece de novo — normalmente no horário de pico de geração, quando a corrente AC está no máximo e a queda de tensão nos cabos atinge o valor mais alto. Não é coincidência. É física: corrente alta em cabo subdimensionado gera queda de tensão que empurra a leitura do inversor para fora do envelope da ABNT NBR 16149.

O segundo erro frequente é trocar o inversor inteiro por "falha recorrente de rede" sem checar o relé interno. O relé de rede num Sungrow residencial custa entre R$ 30 e R$ 80. O inversor novo vai ao telhado, o relé defeituoso desce no lixo junto com o chassi de R$ 3.500. Três semanas depois, o cliente liga de novo — porque o cabeamento subdimensionado continua lá.

---

## Quando o reparo é viável

A decisão depende do que o diagnóstico encontrou:

**Em campo, sem envio para bancada:**
- Disjuntor com mau contato: substituição direta, sem mexer no inversor
- Cabo AC com queda de tensão: redimensionamento ou substituição do trecho
- Terminais com aperto insuficiente: retorque dentro da especificação Sungrow

**Em bancada, reparo interno:**
- Relé de rede com falha de contato: substituição do componente, custo de R$ 30–80 mais mão de obra
- Divisor resistivo com deriva por corrosão: troca dos resistores de precisão, custo de componente abaixo de R$ 20
- Amplificador de condicionamento com drift: identificação e substituição em nível SMD

Um inversor Sungrow SG5K-D ou SG8K-D novo sai entre R$ 2.500 e R$ 4.500 dependendo da potência e do canal de compra. Um reparo no relé de rede ou no circuito de supervisão AC, quando bem diagnosticado, fica entre R$ 300 e R$ 600.

O que não está claro é quem vai abrir o equipamento e medir o que precisa ser medido antes de emitir o laudo.

---

## Conclusão

O erro Grid Lost no Sungrow não significa que a rede elétrica falhou. Significa que o inversor não está vendo a rede. São diagnósticos diferentes, soluções diferentes, custos diferentes.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

Antes de pedir inversor novo, mede os bornes AC com o equipamento em standby. Um aperto de terminal de 2 minutos já resolveu mais Grid Lost do que qualquer reset de fábrica.

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "falha de isolamento em inversor solar" → Link para: post sobre Growatt Erro 102 – Falha de Isolamento (Post 01)
- Âncora: "placa de controle com deriva de leitura" → Link para: post sobre placa de controle vs. placa de potência (Post 43)
- Âncora: "inversor parado com sistema funcionando" → Link para: post sobre inversor solar parado – checklist completo (Post 11)
- Âncora: "relé de bypass com defeito" → Link para: post sobre relés de bypass em inversores (Post 54)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16149" → Fonte: ABNT – Sistemas fotovoltaicos — Requisitos de conexão à rede elétrica de distribuição (abnt.org.br)
- Texto âncora: "proteção anti-ilhamento" → Fonte: ANEEL – Resolução Normativa 482/2012 e 687/2015 (aneel.gov.br)
- Texto âncora: "relé de rede em inversores solares" → Fonte: Sungrow – SG Series Installation and Operation Manual (sungrowpower.com)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Painel de distribuição elétrica residencial com disjuntores — contexto direto do diagnóstico de perda de rede descrito no post
→ Nome do arquivo: sungrow-grid-lost-perda-de-rede-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Quadro de distribuição elétrica com disjuntor AC de inversor Sungrow — diagnóstico de erro Grid Lost perda de rede
→ Legenda: Fig. 1 — Ponto de medição no disjuntor dedicado do inversor: primeiro passo no diagnóstico do erro Grid Lost
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=1200
→ Por que foi escolhida: Técnico usando multímetro em equipamento eletrônico — representa a medição de tensão nos bornes AC e o diagnóstico do circuito de supervisão
→ Nome do arquivo: medicao-bornes-ac-inversor-sungrow-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensão nos bornes AC de inversor Sungrow com multímetro para diagnóstico de erro Grid Lost
→ Legenda: Fig. 2 — Medição direta nos bornes AC do inversor em standby. A queda de tensão entre o QDC e o borne é o primeiro indicador de problema no cabeamento
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB
