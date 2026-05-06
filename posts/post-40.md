# Post 40 — SMA 6120: Falha de Hardware Interno — placa principal danificada, o que é recuperável

---

[PALAVRA-CHAVE FOCO]
SMA 6120 falha de hardware interno

---

[TÍTULO SEO — Title Tag]
SMA 6120: Falha de Hardware — O Que É Recuperável

---

[SLUG — URL do Post]
sma-6120-falha-de-hardware-interno

---

[META DESCRIPTION]
O erro SMA 6120 indica falha de hardware interna. Diagnóstico em nível de placa revela o que quebrou e se o inversor tem conserto.

---

[CATEGORIA]
Códigos de Erro e Falhas

---

[TAGS]
SMA 6120, falha de hardware inversor solar, diagnóstico SMA Sunny Boy, reparo inversor SMA, IGBT inversor solar

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**SMA 6120 falha de hardware interno** aparece no display ou no portal de monitoramento sem aviso. Um momento o inversor está gerando; no outro, o sistema trava com essa mensagem e não sai mais. Nenhum reset funciona. O cliente para de produzir e começa a ligar.

Na nossa bancada, esse erro chega com frequência vindo do interior de Minas Gerais e do sertão nordestino — regiões com rede elétrica instável, surtos frequentes e variações de tensão que ninguém mede até o equipamento parar. O padrão é quase sempre o mesmo: inversor que funcionou bem por dois, três anos, passou por algum evento de tensão ou calor, e nunca mais voltou.

O problema específico com o 6120 é que ele é um código genérico. O SMA não aponta o componente — só avisa que algo falhou internamente. E isso complica tudo se o diagnóstico for superficial.

## O Que Causa Este Erro

O código 6120 nos inversores SMA (Sunny Boy e Sunny Tripower) indica uma falha detectada pelo sistema de proteção interno. Não é erro de configuração, não é alarme de rede — é o próprio inversor dizendo que algo quebrou dentro dele e ele não consegue mais operar com segurança.

A arquitetura SMA monitora continuamente a tensão do barramento CC interno, a corrente em cada fase do estágio de saída, a temperatura dos IGBTs e a integridade da comunicação entre a placa de controle e a placa de potência. Quando qualquer dessas leituras sai do envelope seguro de operação e o inversor não consegue se recuperar por si mesmo, ele trava com o 6120.

As causas que chegam com mais frequência até nós:

1. **Falha no circuito de driver de IGBT** — o CI driver (IR2110 ou similar) que controla o gate dos transistores queima antes do IGBT em si. O inversor detecta que os sinais de disparo não chegam corretamente e para.
2. **Módulo IGBT destruído** — sobretensão transitória ou sobrecorrente rompe a junção. É a causa mais frequente depois de eventos de raio ou surto de rede sem proteção adequada.
3. **Capacitores eletrolíticos do barramento CC com ESR elevado** — degradação que causa ripple excessivo, aciona a proteção interna e resulta em travamento permanente.
4. **Falha na fonte de alimentação interna (SMPS)** — a fonte chaveada que alimenta a placa de controle perde regulação. O DSP não opera de forma estável e o sistema trava em modo de proteção.
5. **Solda fria no barramento de comunicação interno** — o SPI ou CAN interno entre as placas apresenta falha intermitente que vira permanente com o tempo e ciclos térmicos repetidos.
6. **Problema no transformador de corrente de saída (CT)** — leitura incorreta de corrente de fase que dispara a proteção de hardware de forma falsa, sem dano real no estágio de potência.

Não existe uma causa única para o 6120. Cada caso abre um diagnóstico diferente.

## Como Identificar na Prática

Antes de ligar qualquer coisa, a inspeção visual já filtra bastante.

**Inspeção visual com o inversor aberto e desligado:**
1. Verificar o barramento CC e a placa de potência — procurar marcas de queimado, componente explodido ou trilha rompida
2. Verificar os capacitores do barramento: topos abaulados, eletrolítico vazado, plástico escurecido ao redor
3. Inspecionar os IGBTs — marcas de calor no encapsulamento ou na trilha de cobre adjacente
4. Verificar os CIs drivers — deformação, escurecimento, solda estourada no encapsulamento
5. Examinar a placa de controle: capacitores SMD, reguladores de tensão, trilhas próximas ao microcontrolador
6. Verificar conexões internas entre placas — conector oxidado ou mal encaixado já resolveu casos que pareciam dano grave
7. Inspecionar os transformadores de corrente na saída CA — núcleo rachado ou enrolamento com queimado indicam leitura falsa

Com multímetro, o técnico mede a resistência entre gate e source/drain de cada IGBT — curto indica transistor destruído. ESR elevado nos capacitores eletrolíticos, com capacímetro que tenha essa função, aponta degradação severa.

O osciloscópio entra quando a inspeção visual não resolve. Formas de onda PWM ausentes ou distorcidas na saída do driver, tensão da alimentação interna instável, comunicação entre placas sem sinal — cada uma dessas leituras direciona o diagnóstico para um ponto específico.

O que aparece no campo: o display trava em 6120 de forma permanente. Nenhum reset pela interface limpa o erro. O Sunny Portal registra o timestamp exato do evento — dado útil para correlacionar com queda de tensão da concessionária ou com surto de raio registrado na região.

## O Erro Mais Comum do Mercado

O integrador recebe o inversor com 6120, vê "falha de hardware interno" e assume que é perda total. O inversor vai para o depósito ou é mandado de volta ao fabricante sem análise prévia.

Esse raciocínio tem um custo alto.

O 6120 é um código genérico — ele não diz o que quebrou. Um driver de IGBT queimado pode ser trocado por menos de R$ 50 em componente. Um capacitor com ESR fora de especificação custa centavos. O que encarece a conta não é o componente em si — é a ausência de diagnóstico que leva o integrador a desistir antes de olhar o que está dentro do equipamento.

Pior: quando o inversor é substituído sem identificar a causa raiz, o mesmo evento pode se repetir no equipamento novo. Surto de rede sem proteção adequada, ponto de aquecimento por ventilação insuficiente, dimensionamento incorreto de string — nada disso some com a troca do inversor.

Ainda não existe uma regra geral que determine, pelo código de erro, se o reparo vai valer a pena. Depende do que você vai encontrar na placa.

## Quando o Reparo é Viável

**Alta viabilidade de reparo:**
- CI driver de IGBT queimado sem dano no transistor em si — troca direta, custo baixo
- Capacitores eletrolíticos do barramento com ESR elevado — troca em lote, procedimento padrão
- Falha na SMPS interna com componente identificado — custo de componente muito abaixo do equipamento
- Solda fria em conector ou barramento interno — retrabalho com estação de solda, sem substituição de componente
- Transformador de corrente com leitura falsa — substituição pontual sem impacto no restante da placa

**Viabilidade moderada:**
- IGBT único danificado — viável se o componente estiver disponível e o dano não se propagou para o driver e para o dissipador
- Placa de controle com regulador de tensão ou CI de interface danificado — depende da disponibilidade do componente no mercado nacional

**Raramente compensa:**
- Múltiplos IGBTs destruídos com dano em cascata para drivers, dissipador e barramento
- Dano por inundação com corrosão generalizada em ambas as placas simultaneamente

Em números: um SMA Sunny Boy de 5 kWp novo sai em torno de R$ 3.500 a R$ 4.500 no mercado atual. Um reparo de driver mais capacitores, com laudo técnico, fica em torno de R$ 600 a R$ 900. Quando o dano é pontual, a conta fecha com folga a favor do reparo.

## Conclusão

O 6120 não é sentença de morte. É um código genérico que aponta para dentro do equipamento — e o que está dentro determina tudo.

Na maioria dos casos que chegam até nós, o inversor tem conserto. Não porque queremos vender reparo, mas porque o diagnóstico eletrônico em nível de placa revela que o dano é isolado. Um componente, às vezes dois. O sistema de proteção funcionou, salvou o restante, e o que ficou danificado é identificável e trocável.

A decisão de reparar ou substituir tem que ser baseada em diagnóstico. Não em suposição.

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

- Âncora: 'Falha no circuito de driver de IGBT' → URL: /o-que-e-o-driver-de-igbt-e-por-que-sua-falha-destroi-o-estagio-de-potencia → Contexto: Seção "O Que Causa Este Erro", item 1 — vincula ao Post 21 sobre driver de IGBT
- Âncora: 'Capacitores eletrolíticos do barramento CC' → URL: /capacitores-eletrolíticos-em-inversores-vida-util-degradacao-e-quando-trocar → Contexto: Seção "O Que Causa Este Erro", item 3 — vincula ao Post 33 sobre capacitores
- Âncora: 'Módulo IGBT destruído' → URL: /por-que-os-igbts-queimam-em-inversores-solares-as-6-causas-reais → Contexto: Seção "O Que Causa Este Erro", item 2 — vincula ao Post 10 sobre IGBTs
- Âncora: 'queda de tensão da concessionária' → URL: /sma-3501-falha-de-isolamento-diagnostico-completo → Contexto: Seção "Como Identificar na Prática", último parágrafo — vincula ao Post 4 sobre SMA com falha relacionada à rede

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "surto de rede sem proteção adequada" → URL: https://www.aneel.gov.br/procedimentos-de-distribuicao → Fonte: ANEEL — PRODIST Módulo 8, qualidade de energia e proteção contra surtos em sistemas de distribuição

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://unsplash.com/s/photos/circuit-board-electronics (buscar por "inverter circuit board repair" em unsplash.com)
→ Por que foi escolhida: Mostra placa de circuito de inversor eletrônico em nível de componente, diretamente relevante ao diagnóstico do SMA 6120
→ Nome do arquivo: sma-6120-placa-de-potencia-inversor.webp
→ Alt Text (máx. 125 caracteres): Placa de potência de inversor solar SMA com IGBTs e capacitores do barramento CC visíveis para diagnóstico do erro 6120
→ Legenda: Fig. 1 — Placa de potência de inversor solar — ponto crítico no diagnóstico do SMA 6120
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://unsplash.com/s/photos/multimeter-electronics (buscar por "multimeter electronics measurement repair" em unsplash.com)
→ Por que foi escolhida: Técnico medindo componentes eletrônicos com multímetro, representando o diagnóstico prático sequencial descrito no post
→ Nome do arquivo: diagnostico-sma-6120-medicao-componentes-2.webp
→ Alt Text (máx. 125 caracteres): Técnico usando multímetro para medir IGBT e capacitores em placa de inversor solar durante diagnóstico do SMA 6120
→ Legenda: Fig. 2 — Medição sequencial de IGBTs e capacitores no diagnóstico do erro SMA 6120
→ Onde inserir: Após H2 "Como Identificar na Prática"
