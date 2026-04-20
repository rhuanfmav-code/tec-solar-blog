# Post 22 — Inversor on-grid vs. off-grid: os defeitos são diferentes — saiba por quê

---

## [PALAVRA-CHAVE FOCO]

diferença entre inversor on-grid e off-grid defeitos

---

## [TÍTULO SEO — Title Tag]

On-grid vs off-grid: por que os defeitos são diferentes

---

## [SLUG — URL do Post]

inversor-on-grid-vs-off-grid-defeitos-diferentes

---

## [META DESCRIPTION]

On-grid e off-grid têm arquiteturas distintas. Veja por que os defeitos são diferentes e como diagnosticar cada tipo sem cometer erros de bancada.

---

## [CATEGORIA]

Manutenção e Diagnóstico

---

## [TAGS]

inversor on-grid off-grid diferença, defeitos inversor solar, diagnóstico inversor off-grid, reparo inversor solar bancada, falha inversor fotovoltaico

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **inversor on-grid** e o **inversor off-grid** parecem cumprir a mesma função para quem olha de fora: converter energia solar em corrente alternada utilizável. Mas a arquitetura interna de cada um é diferente o suficiente para que os modos de falha sejam completamente distintos.

Na nossa bancada, recebemos com frequência inversores off-grid que passaram por técnico antes de chegar até nós. O padrão se repete: a rotina de diagnóstico foi a mesma usada em on-grid, nada foi encontrado, o equipamento foi devolvido ao cliente como "sem defeito aparente". O cliente retornou porque o inversor não carregava a bateria direito. O estágio de carregamento nunca tinha sido verificado.

---

## A arquitetura define onde o problema aparece

O inversor on-grid trabalha com referência externa: a rede elétrica. Ele sincroniza fase, frequência e tensão com o que a concessionária entrega. Quando a rede cai ou fica fora do padrão, o inversor para — por projeto. Isso é exigência de norma (ABNT NBR 16149 / IEC 62116). O circuito responsável por isso é chamado de proteção anti-ilha.

O inversor off-grid gera a própria referência de tensão e frequência. Não existe rede como ponto fixo. Ele precisa manter 220 V / 60 Hz estáveis com qualquer carga conectada, sem ajuda externa. Para isso, tem um estágio inversor de saída geralmente baseado em transformador e, na maioria dos modelos, um estágio de carregador de bateria separado — com seus próprios MOSFETs, indutores e circuito de controle.

São dois produtos diferentes, com componentes diferentes e pontos de falha diferentes.

---

## Os defeitos que aparecem no on-grid

O ponto mais sensível de um on-grid transformerless — topologia dominante nos inversores de string atuais — é o circuito de monitoramento de isolamento entre o barramento CC e a terra. Qualquer painel com isolamento degradado, conector MC4 amolecido ou cabo com falha de cobertura gera corrente de fuga que o inversor detecta e usa como motivo para desligar. A falha está no sistema fotovoltaico, mas o inversor que exibe o erro — e é quem vai para a bancada.

O segundo ponto crítico é o relé de anti-ilhamento. É um contato eletromecânico que abre quando o inversor detecta ausência de rede. Em regiões com muitas oscilações de rede — interior do Nordeste e do Norte, onde a qualidade da concessionária é historicamente instável — esse relé acumula arcos nos contatos ao longo dos anos. O contato fica resistivo, o inversor passa a falhar ao tentar se reconectar à rede.

O terceiro ponto é o circuito de PLL (Phase-Locked Loop) e detecção de cruzamento por zero. Se os capacitores eletrolíticos do filtro de PLL aumentam ESR, o inversor começa a enxergar variações de frequência que não existem — e desliga por falsa proteção de frequência.

IGBTs no on-grid falham principalmente por evento: surto de rede que escapa pelo varistor, curto momentâneo no barramento CC. Não por desgaste progressivo com a mesma frequência que acontece no off-grid.

---

## Os defeitos que aparecem no off-grid

No off-grid, o estágio de carregador de bateria é o que falha com mais frequência. Esse circuito opera continuamente enquanto há fonte de energia disponível — painel, rede auxiliar ou gerador. Os MOSFETs do estágio de carregamento sofrem ciclagem térmica intensa, especialmente em instalações rurais sem ventilação adequada do quadro, comuns em fazendas e sítios no cerrado e no sertão. A falha típica é o MOSFET em curto, que pode destruir o indutor do estágio e queimar trilhas da placa junto.

O segundo problema característico do off-grid é a degradação dos capacitores do barramento CC e do filtro de saída. Como o inversor opera 24 horas — carregando a bateria quando há sol e convertendo energia da bateria quando não há — a temperatura interna nunca cai tanto quanto num on-grid que para à noite. A vida útil dos eletrolíticos cai de forma mensurável com temperatura de operação elevada e contínua. ESR sobe. Ripple de tensão aumenta. O circuito de controle começa a tomar decisões erradas com base em leituras de tensão distorcidas.

O relé de saída do off-grid enfrenta demanda diferente. Em sistemas residenciais, o inversor absorve partidas de motor de geladeira, ar-condicionado, bomba d'água — sobrecargas transitórias repetidas que o on-grid nunca sofre diretamente, porque a rede amortece. No off-grid, toda a corrente de partida passa pelo inversor.

O transformador de saída, quando presente, é ponto de avaliação obrigatória em casos de sobrecarga grave: enrolamentos com sinais de superaquecimento, verniz com cheiro diferente, resistência de enrolamento fora do esperado são indicadores que não aparecem em on-grid transformerless.

---

## O erro que se repete no mercado

O técnico aplica no off-grid o mesmo roteiro do on-grid: mede os IGBTs, testa o estágio de saída, verifica a placa de controle. Não acha nada. Devolve o equipamento.

O estágio de carregador nunca foi verificado.

É um circuito separado dentro do mesmo equipamento, com seus próprios semicondutores e controle. Em muitos modelos, está numa seção física diferente da placa ou numa placa filha. Técnico que trata off-grid como on-grid vai deixar essa seção intacta enquanto o problema está exatamente ali.

Não é falta de capacidade técnica. É ausência de método específico para o tipo de equipamento.

---

## Quando o reparo é viável

No on-grid, o reparo é viável quando o dano é localizado: relé de anti-ilhamento com contatos gastos, capacitores de filtro com ESR elevado, resistores de divisor de tensão fora de valor. São componentes acessíveis, com custo baixo e substituição direta. Quando o IGBT falhou por evento, a viabilidade depende de quanto o evento se espalhou — se ficou no módulo de potência e no driver, o reparo custa bem menos do que um inversor novo.

No off-grid, o reparo do estágio de carregador exige identificação precisa dos MOSFETs, que muitas vezes são de modelos menos comuns. Equivalentes técnicos existem para a maioria. A decisão passa por: extensão do dano, se o transformador foi afetado e o preço de um inversor off-grid equivalente no mercado.

Um inversor off-grid de qualidade custa mais do que um on-grid equivalente. O argumento financeiro para o reparo é proporcionalmente mais forte.

---

## Conclusão

On-grid e off-grid não são versões do mesmo equipamento. São projetos com objetivos diferentes, topologias diferentes e modos de falha diferentes.

Aplicar o mesmo diagnóstico nos dois é como usar o mesmo protocolo de medição num motor CA e num motor CC: você mede, anota, e chega à conclusão errada.

---

Condenaram seu inversor por causa desse erro?

Antes de comprar equipamento novo, envie para a nossa bancada. A TEC Solar realiza diagnóstico eletrônico completo em nível de componente — abrimos o inversor, medimos a placa, identificamos a causa raiz e entregamos um laudo técnico detalhado.

Se o reparo for viável, você recebe o equipamento funcionando por uma fração do custo de substituição. Se não for, o laudo serve de base para qualquer decisão.

Atendemos todo o Brasil via logística reversa.

👉 [Envie seu inversor agora](https://wa.me/5538998891587) | [Falar no WhatsApp](https://wa.me/5538998891587)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "Por que os IGBTs queimam em inversores solares" → Link para: post sobre as 6 causas reais de queima de IGBT (Post 10)
- Âncora: "driver de IGBT" → Link para: O que é o driver de IGBT e por que sua falha destrói o estágio de potência (Post 21)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16149" → Fonte: ABNT — Sistemas fotovoltaicos — Características da interface de conexão com a rede elétrica de distribuição (abnt.org.br)
- Texto âncora: "IEC 62116" → Fonte: IEC — Test procedure of islanding prevention measures for utility-interconnected photovoltaic inverters (iec.ch)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Painéis solares com instalação visível de inversor em ambiente externo — representa sistema fotovoltaico completo, contexto direto do post sobre tipos de inversores
→ Nome do arquivo: inversor-on-grid-off-grid-diferenca-defeitos.webp
→ Alt Text (máx. 125 caracteres): Instalação de inversores solares on-grid e off-grid — diferenças de arquitetura e modos de falha em diagnóstico técnico
→ Legenda: Fig. 1 — On-grid e off-grid compartilham o mesmo nome mas operam com lógicas distintas; os pontos de falha são diferentes e o diagnóstico precisa acompanhar essa diferença
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1200
→ Por que foi escolhida: Técnico inspecionando placa eletrônica de equipamento de potência — representa a avaliação específica do estágio de carregador de bateria no off-grid descrita na seção de defeitos
→ Nome do arquivo: diagnostico-inversor-off-grid-estágio-carregador-2.webp
→ Alt Text (máx. 125 caracteres): Técnico diagnosticando placa de inversor off-grid com estágio de carregador de bateria — análise em bancada de reparo
→ Legenda: Fig. 2 — O estágio de carregador de bateria é um circuito separado dentro do off-grid e é o ponto de falha mais ignorado em diagnósticos feitos com roteiro de on-grid
→ Onde inserir: Após H2 "Os defeitos que aparecem no off-grid"
→ Converter para WebP — máximo 150 KB

<!-- trigger-video-workflow -->

<!-- debug-elevenlabs-v2 -->
<!-- trigger-adam-voice -->
