# Post 81 — Fronius State 701: Falha de Isolamento CA — cabeamento de saída ou problema interno?

---

## [PALAVRA-CHAVE FOCO]

Fronius State 701 falha isolamento CA

---

## [TÍTULO SEO — Title Tag]

Fronius State 701: Falha de Isolamento CA — Diagnóstico

---

## [SLUG — URL do Post]

fronius-state-701-falha-isolamento-ca-diagnostico

---

## [META DESCRIPTION]

Fronius State 701 indica isolamento CA comprometido. Saiba como separar cabeamento defeituoso de falha interna antes de trocar o inversor.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Fronius State 701, falha isolamento CA inversor solar, diagnóstico Fronius Symo, capacitor Y filtro EMI, isolamento cabeamento CA fotovoltaico

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Fronius State 701** trava o sistema sem entregar mais nada além do código no display. A geração cai para zero, o inversor entra em proteção permanente e o integrador fica na dúvida: problema no cabeamento CA de saída ou falha interna no equipamento?

A diferença importa porque muda tudo na abordagem. O State 701 indica falha de isolamento no lado CA — não no lado CC dos painéis e strings, que é onde a maioria dos técnicos procura primeiro quando vê qualquer erro de isolamento. No Fronius Symo e nos modelos da linha Primo, o circuito de monitoramento do inversor avalia o lado CC e o lado CA de forma independente. Quando o código é 701, o sinal veio do lado de saída.

Na nossa bancada, esse erro chega com dois padrões bem definidos. O primeiro: instalações com cabeamento CA antigo, pressionado contra calha metálica ou embutido em conduite sob telha, onde o isolamento do condutor cedeu por temperatura ou abrasão acumulada. O segundo: inversores com capacitores do filtro EMI no estágio de saída CA desenvolvendo fuga para o terra sem nenhum defeito externo. Os dois chegam com State 701 no display. O trabalho de diagnóstico é completamente diferente em cada caso.

## O que causa o State 701

O circuito de monitoramento de isolamento do Fronius Symo injeta um sinal de referência de baixa corrente entre os condutores CA de saída (R, S, T e N) e o terra de proteção (PE). A resistência medida precisa ficar acima de 1 MΩ em inversores trifásicos — valor de referência da IEC 62109-2 para inversores fotovoltaicos sem transformador. Quando cai abaixo desse limiar, o inversor registra State 701 e desconecta da rede.

Quatro causas concentram a maioria dos casos que chegam para diagnóstico:

Degradação do isolamento no cabeamento CA de saída: condutores entre o inversor e o quadro de distribuição com isolamento comprometido por temperatura de operação, abrasão em prensa-cabos mal dimensionados ou envelhecimento acelerado em instalações externas sem conduite adequado. Em regiões do Nordeste e do Centro-Oeste, o cabeamento embutido em calha sob telha metálica sofre variações térmicas diárias que chegam a 50°C — esse ciclo, repetido por anos, deteriora o isolamento de condutores que não são especificados para aquela condição.

Capacitores Y do filtro EMI de saída CA: o estágio de saída dos inversores Fronius Symo inclui um filtro de interferência eletromagnética com capacitores tipo Y conectando cada fase ao PE. Quando esses capacitores desenvolvem corrente de fuga elevada ou entram em curto parcial, criam um caminho de baixa resistência para o terra que o circuito de monitoramento lê como falha de isolamento CA. A causa é totalmente interna — o cabeamento externo pode estar perfeito.

Umidade nos terminais CA de saída: inversores instalados em área externa sem proteção adequada acumulam condensação nos bornes de saída. A condutividade superficial resultante reduz a resistência de isolamento de forma gradual até cruzar o limiar de proteção.

Relé de conexão de rede com isolamento deteriorado: o Fronius Symo usa relés eletromecânicos para conectar a saída CA à rede. Contatos com depósito carbonizado ou isolamento entre bobina e contatos degradado por temperatura contribuem para redução da resistência medida. Menos frequente que as causas anteriores, mas identificável na bancada.

## Como identificar na prática

O diagnóstico começa com uma bifurcação: a falha está fora do inversor ou dentro dele. Esse teste não exige instrumento além do próprio inversor e deve ser o primeiro passo — antes de medir qualquer coisa na instalação.

1. Desligue o inversor pelo procedimento correto: disjuntor CA primeiro, depois o DC isolator
2. Desconecte fisicamente todos os condutores CA de saída dos bornes do inversor — fases, neutro e PE de saída
3. Aguarde 5 minutos para descarga completa dos capacitores internos
4. Ligue o inversor somente com a entrada CC dos painéis, sem nenhuma conexão CA
5. Se o State 701 aparecer com os bornes CA completamente desconectados, a falha é interna: os capacitores Y do filtro EMI de saída ou o relé de rede são os alvos
6. Se o inversor inicializar sem erro, a origem está no cabeamento ou nos terminais — reconecte os condutores CA fase a fase, testando cada um separadamente até reproduzir o erro
7. Com o condutor identificado, meça a resistência de isolamento com megôhmímetro a 500 V CA entre esse condutor e o PE da instalação — valor abaixo de 1 MΩ confirma isolamento comprometido
8. Se a suspeita for interna, com o inversor desligado e descarregado, acesse os capacitores Y do filtro EMI de saída e meça a resistência entre cada terminal do capacitor e o chassi — o valor correto é da ordem de dezenas de megaohms; qualquer leitura abaixo de 1 MΩ aponta capacitor em fuga ou em curto parcial

O passo 4 e 5 é o divisor diagnóstico. Ele define se o trabalho continua dentro do inversor ou na instalação — e evita horas de inspeção no lugar errado.

## O erro mais comum do mercado

O técnico vê State 701, lê "falha de isolamento CA" e vai direto para o cabeamento externo. Usa multímetro em faixa de resistência, não encontra curto aparente, conclui que "o inversor queimou internamente" e emite parecer de substituição.

O capacitor Y com curto parcial mede 15 kΩ onde deveria ser 50 MΩ. O multímetro comum não revela isso. O megôhmímetro a 500 V revela.

Sem o instrumento correto e sem o procedimento na sequência certa, o diagnóstico não fecha. E sem o passo de isolar os bornes CA antes de qualquer outra medição, o técnico vai investir tempo inspecionando a instalação enquanto o problema está dentro do equipamento — ou vai trocar o inversor enquanto o problema está no condutor do cabeamento.

## Quando o reparo é viável

Se o passo 5 confirmar falha interna pelos capacitores Y do filtro EMI de saída: componentes de baixo custo com alta disponibilidade no mercado de componentes eletrônicos. O valor de capacitância e a classe de segurança (Y1 ou Y2, com tensão de pico nominal de acordo com a especificação do modelo Symo) precisam ser respeitados — a substituição por componente de especificação diferente compromete a função de supressão de EMI e cria risco elétrico. Custo de componente entre R$25 e R$130. Tempo de bancada de 2 a 4 horas incluindo testes funcionais.

Se o relé de rede for identificado: disponível para os modelos Symo 3.7, 5.0, 8.2 e variantes mais comuns no Brasil. Custo entre R$80 e R$250. Requer soldagem profissional na placa de potência de saída — não é trabalho de campo.

Se a causa for isolamento comprometido no cabeamento externo: o inversor não vai para bancada. O trabalho é na instalação — identificação e substituição do trecho de condutor degradado, com reavaliação do trajeto para eliminação das condições que causaram o problema. Em instalações com mais de 8 anos, vale revisar todo o cabeamento CA ao mesmo tempo.

Em qualquer dos três cenários, o custo de resolução fica muito abaixo do valor de reposição do inversor. Para os modelos Symo de 5 a 15 kW, essa diferença representa entre R$3.500 e R$9.000 dependendo da potência e do canal de compra.

## Conclusão

O State 701 tem causa rastreável. Pode ser um metro de condutor com isolamento cedido, pode ser um capacitor Y de R$40 dentro do filtro de saída. Nenhum dos dois justifica condenar o equipamento.

O que define o diagnóstico é a sequência: isolar os bornes CA, testar o inversor sem conexão externa, e usar megôhmímetro no lugar de multímetro. Feito isso, a origem fica clara antes de qualquer desmontagem aprofundada.

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

## [LINKS INTERNOS SUGERIDOS]

- Âncora: 'capacitores Y do filtro EMI' → URL: /capacitor-eletrolitico-inversor-solar-vida-util-degradacao → Contexto: seção "O que causa o State 701", ao explicar a falha dos capacitores Y como causa interna do erro; e seção "Quando o reparo é viável", ao detalhar o componente e o custo de reparo
- Âncora: 'falha de isolamento em sistemas fotovoltaicos' → URL: /falha-isolamento-sistemas-fotovoltaicos-como-rastrear → Contexto: seção "O que causa o State 701", ao introduzir o conceito de resistência de isolamento e as causas de degradação no cabeamento externo
- Âncora: 'relés eletromecânicos' → URL: /reles-bypass-inversores-solares-falha-silenciosa → Contexto: seção "O que causa o State 701", ao mencionar o relé de conexão de rede como causa menos frequente de State 701
- Âncora: 'diagnóstico eletrônico completo em nível de componente' → URL: /diagnostico-nivel-de-placa-inversor-solar → Contexto: bloco CTA, reforçando o diferencial da TEC Solar no diagnóstico antes da troca do equipamento

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62109-2" → URL: https://www.iec.ch/homepage → Fonte: IEC — norma internacional que define os limiares de resistência de isolamento para inversores fotovoltaicos sem transformador, incluindo o valor de 1 MΩ citado no post
- Texto âncora: "resistência de isolamento" → URL: https://www.abnt.org.br → Fonte: ABNT — repositório das normas ABNT NBR 16149 e complementares que regulam os requisitos de isolamento em sistemas fotovoltaicos conectados à rede no Brasil

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1621905252507-b35492cc74b4?w=1200
→ Por que foi escolhida: Inversor solar instalado com cabeamento CA visível — representa o contexto técnico de diagnóstico de isolamento no lado de saída do equipamento
→ Nome do arquivo: fronius-state-701-falha-isolamento-ca-inversor.webp
→ Alt Text (máx. 125 caracteres): Inversor solar Fronius com cabeamento CA de saída — diagnóstico de falha de isolamento State 701 em bancada técnica
→ Legenda: Fig. 1 — O State 701 monitora o lado CA de saída: condutores, terminais e filtro EMI são os alvos do diagnóstico
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Técnico realizando medição elétrica com instrumento de teste — representa o uso do megôhmímetro no procedimento de diagnóstico descrito no passo a passo
→ Nome do arquivo: diagnostico-isolamento-ca-megaohmetro-fronius-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo resistência de isolamento com megôhmímetro em inversor solar Fronius — diagnóstico State 701
→ Legenda: Fig. 2 — Megôhmímetro a 500 V: ferramenta que diferencia curto parcial de capacitor Y do que o multímetro comum não revela
→ Onde inserir: Após H2 "Como identificar na prática"
