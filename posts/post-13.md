# Post 13 — Fronius State 108: Oscilação de Rede — como identificar se o problema é externo ou interno

---

## [PALAVRA-CHAVE FOCO]

Fronius State 108 oscilação de rede

---

## [TÍTULO SEO — Title Tag]

Fronius State 108: Oscilação de Rede — Externo ou Interno?

---

## [SLUG — URL do Post]

fronius-state-108-oscilacao-de-rede-diagnostico

---

## [META DESCRIPTION]

Fronius State 108: oscilação de rede? Veja como diferenciar falha da concessionária de defeito interno no sensor de tensão CA — diagnóstico técnico.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Fronius State 108, oscilação de rede inversor solar, diagnóstico Fronius Symo, qualidade de energia fotovoltaica, sensor tensão CA inversor

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **Fronius State 108** aparece no display sem aviso prévio, o inversor desconecta da rede e a geração vai a zero. O integrador é chamado, faz inspeção visual, checa a tensão nos terminais CA com o multímetro, não encontra nada obviamente errado — e o inversor continua caindo no mesmo código.

Na nossa bancada, esse caso chega com frequência de regiões com redes de distribuição sobrecarregadas: interior de Minas, interior de São Paulo, áreas rurais do Centro-Oeste. O padrão se repete sempre. O State 108 aparece especialmente no período da tarde, quando a rede local está com maior demanda. Isso não é coincidência — é o primeiro dado clínico para o diagnóstico.

O problema central é saber se a instabilidade está vindo de fora ou se o inversor está medindo errado por dentro. São dois caminhos completamente diferentes, com custo e solução completamente diferentes.

---

## O que causa o Fronius State 108

O State 108 nos inversores Fronius (Symo, Primo, Eco, GEN24 e variantes) é gerado quando o sistema de monitoramento de rede detecta oscilação ou desvio fora dos parâmetros de operação. Na prática, o inversor interpreta que está operando em ilha — sem a rede da concessionária — e desconecta por proteção anti-ilhamento. Esse comportamento é obrigatório por norma: IEC 62116 e NBR 16149 exigem que inversores grid-tie interrompam a injeção de energia em até 2 segundos ao detectar perda ou instabilidade da rede.

No Brasil, o PRODIST Módulo 8 (ANEEL Resolução 956/2021) define os limites de qualidade de energia da rede pública. A tensão deve se manter dentro de ±10% da tensão nominal e a frequência entre 59,8 Hz e 60,2 Hz para operação contínua. O Fronius monitora esses parâmetros continuamente via circuito PLL (Phase-Locked Loop) e divisor de tensão CA. Qualquer desvio detectado dentro da janela de proteção dispara o State 108.

As causas se dividem em dois grupos completamente distintos.

**Causas externas — a rede está fora do padrão:**

- Transformador de distribuição sobrecarregado ou com regulação deficiente, gerando quedas transitórias de tensão no horário de pico de demanda
- Chaveamento de cargas pesadas na mesma subestação: compressores de câmaras frigoríficas, motores de irrigação, secadores de grão — distúrbios de tensão de curta duração que o multímetro não registra mas o inversor captura
- Cabos de distribuição subdimensionados ao longo do alimentador, causando queda de tensão proporcional à carga
- Desequilíbrio de fases em instalações trifásicas, com uma fase fora da janela enquanto as outras estão dentro — Fronius Symo trifásico desconecta por proteção mesmo que só uma fase esteja fora

**Causas internas — o inversor está medindo errado:**

- Resistores do divisor de tensão CA com tolerância deslocada por temperatura ou envelhecimento, causando leitura sistematicamente fora do valor real
- Capacitor de filtro no circuito de monitoramento AC com ESR aumentado, introduzindo defasagem na leitura de frequência e disparando o PLL por diferença de fase
- Falha no circuito de detecção de cruzamento por zero (zero-crossing detection) — responsável por alimentar o PLL e determinar a frequência medida pelo DSP. Quando esse circuito falha, o inversor "enxerga" uma frequência que não existe
- Borne CA frouxo ou oxidado internamente, gerando resistência de contato variável sob carga e leitura de tensão instável

Esse segundo grupo é o mais difícil de identificar sem bancada — porque em campo, a rede parece normal e o inversor parece normal. Mas os dois não concordam.

---

## Como identificar na prática

A chave é comparar o que o inversor está medindo com o que a rede está realmente fazendo naquele momento exato.

1. **Instale um analisador de qualidade de energia no ponto de conexão CA do inversor** e registre por pelo menos 24 horas, priorizando o período histórico de falhas. O analisador captura tensão, frequência e THD com registro temporal — o multímetro em valor médio não serve aqui. Distúrbios de 50 a 200 ms não aparecem em medição de valor eficaz sem resolução temporal.

2. **Acesse o portal Fronius Solar.web ou o histórico local de eventos.** O inversor registra o State 108 com timestamp e com os valores de tensão e frequência no momento da desconexão. Exporte esse log. Com ele em mãos, é possível cruzar o horário exato do State 108 com os dados do analisador externo.

3. **Compare os valores medidos pelo inversor com os do analisador durante operação normal e estável.** Se o Fronius lê 223 V enquanto o analisador marca 231 V de forma consistente, o divisor de tensão interno tem desvio. Se os valores coincidirem em condições estáveis e o State 108 ainda ocorrer, a causa é circuito PLL ou zero-crossing.

4. **Verifique os bornes de conexão CA** com o inversor desligado e capacitores descarregados. Aperte todos os terminais com o torque especificado no manual (Fronius Symo: 2,5 a 3,0 Nm). Borne frouxo em barra CA gera queda de tensão localizada que só aparece sob carga.

5. **Com osciloscópio nos terminais CA internos**, verifique a forma de onda antes do circuito de medição. Distorção, ruído ou assimetria indicam problema no filtro LC de entrada CA. Isso não aparece no multímetro. Não aparece no analisador ligado no lado externo.

6. **Se o State 108 aparecer consistentemente com rede estável e valores do inversor coincidindo com a medição externa**, o circuito PLL ou o zero-crossing detection está falhando. Esse diagnóstico não tem como ser finalizado sem bancada.

---

## O erro mais comum do mercado

O técnico registra o State 108, confere a tensão na tomada com o multímetro, vê "230 V" e conclui que a rede está boa. Nenhum problema externo visível. Inversor condenado. Equipamento encaminhado para reparo ou troca.

Esse fluxo falha em um ponto: multímetro em valor RMS médio não captura transitórios de tensão. O tipo de distúrbio que dispara o anti-ilhamento do Fronius tem duração de 80 a 300 ms e amplitude suficiente para cruzar o limite da janela de proteção. Esses eventos não aparecem no display de um multímetro comum.

Sem registro temporal, o técnico nunca vai ver o que o inversor viu.

Um Fronius Symo 8.2-3-M custa acima de R$ 7.000 novo. Se o problema for um transformador sobrecarregado da distribuidora, a solicitação de melhoria ao órgão regulador não custa nada. O analisador de qualidade de energia — alugado por dia — custa menos de R$ 200.

---

## Quando o reparo é viável

Se o diagnóstico confirmou origem interna, o cenário depende do componente identificado.

**Divisor de tensão com resistor fora de tolerância** — componente de alta precisão com valor desviado por temperatura ou ciclos térmicos — é reparável em nível de componente com custo entre R$ 300 e R$ 600. O Fronius novo, dependendo do modelo, custa de R$ 5.000 a R$ 9.000.

**Capacitor de filtro AC com ESR elevado** — mesmo cenário: componente individual, substituição direta, viável em qualquer oficina com equipamento de análise de componentes.

**Falha no módulo de controle ou no processador DSP que executa o algoritmo PLL** é o caso mais complexo. Se o componente do circuito integrado está danificado, o custo da placa de reposição pode tornar o reparo inviável, especialmente em modelos com mais de 8 anos ou fora de linha. Só o diagnóstico define isso antes de qualquer orçamento.

Ainda não existe resposta definitiva sobre viabilidade de reparo sem abrir o equipamento e medir os pontos certos. Depende do que você vai encontrar na placa.

---

## Conclusão

Fronius State 108 não é diagnóstico. É o início do diagnóstico.

A rede elétrica brasileira oscila. Transformadores sobrecarregados, alimentadores subdimensionados, cargas pesadas em subestações rurais — esses fatores existem e disparam o anti-ilhamento por norma. O inversor não está com defeito quando faz isso. Mas o inversor também pode estar medindo errado. E sem dado temporal, não dá para separar os dois casos.

Meça antes de concluir. Analisador de qualidade no ponto de conexão, log de eventos do inversor, comparação temporal. Esse processo leva um a dois dias e diferencia um problema de R$ 0 — distribuidora sobrecarregada — de um reparo de R$ 500 ou de um inversor novo de R$ 8.000.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "falha de isolamento" → Link para: post sobre SMA 3501 – Falha de Isolamento (Post 04) — se publicado
- Âncora: "sensor de tensão" → Link para: post sobre Fronius State 102: Tensão CC Muito Alta (Post 02)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "PRODIST Módulo 8" → Fonte: ANEEL — Procedimentos de Distribuição de Energia Elétrica (gov.br/aneel)
- Texto âncora: "NBR 16149" → Fonte: ABNT — Sistemas fotovoltaicos: características da interface de conexão (abntcatalogo.com.br)
- Texto âncora: "IEC 62116" → Fonte: IEC — Utility-interconnected photovoltaic inverters: test procedure of islanding prevention measures (iec.ch)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Inversor solar instalado em ambiente industrial com painel elétrico ao fundo — representa diretamente o contexto de falha de rede CA em sistema grid-tie
→ Nome do arquivo: fronius-state-108-oscilacao-rede-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Inversor solar Fronius instalado com conexão CA — diagnóstico do State 108 por oscilação de rede elétrica
→ Legenda: Fig. 1 — Fronius State 108 pode ter origem externa (rede instável) ou interna (circuito de medição CA com defeito)
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=1200
→ Por que foi escolhida: Técnico com osciloscópio medindo forma de onda elétrica em equipamento eletrônico — representa o procedimento de diagnóstico com medição temporal descrito na seção "Como Identificar na Prática"
→ Nome do arquivo: diagnostico-oscilacao-rede-fronius-osciloscópio-2.webp
→ Alt Text (máx. 125 caracteres): Técnico analisando forma de onda CA com osciloscópio — diagnóstico Fronius State 108 oscilação de rede
→ Legenda: Fig. 2 — Osciloscópio e analisador de qualidade de energia são as ferramentas corretas para diagnosticar o Fronius State 108 — o multímetro não captura transitórios de 80 a 300 ms
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB
