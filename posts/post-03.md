# Post 03 — Deye Tensão de Rede Fora do Limite: Causa e Diagnóstico

---

## [PALAVRA-CHAVE FOCO]

falha tensão de rede inversor deye f43 f44 sobretensão subtensão

---

## [TÍTULO SEO — Title Tag]

Deye Tensão de Rede Fora do Limite: Causa e Diagnóstico

---

## [SLUG — URL do Post]

deye-tensao-rede-fora-limite-sobretensao-subtensao

---

## [META DESCRIPTION]

Inversor Deye desligando por tensão de rede? Entenda se é falha externa ou defeito interno na placa de controle. Diagnóstico técnico TEC Solar.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Deye, sobretensão de rede, subtensão CA, F43 F44 inversor solar, diagnóstico placa de controle

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Tensão de rede fora do limite em inversor Deye** — o sistema para no meio do dia e não volta sozinho. Quando o erro aparece, pode ser a rede da concessionária, pode ser o cabeamento CA de saída subdimensionado, pode ser o circuito de medição de tensão na placa de controle. O problema é que a maioria dos atendimentos vai direto para "inversor com defeito" sem medir nada.

Na nossa bancada, esse padrão chega com uma história quase sempre igual: integrador relata que o equipamento trava entre 11h e 14h, especialmente nos dias de maior geração. O sistema estava operando normal, desligou sozinho, ficou em erro. Ligam a chave, zera o alarme, volta a funcionar por algumas horas — e no dia seguinte, repete.

O diagnóstico completo desse erro leva menos de 20 minutos com um multímetro na mão. O que falta, na maioria dos casos, é saber o que medir e onde.

---

## O que causa esse erro nos inversores Deye

Os inversores Deye da linha SUN-K monitoram continuamente a tensão da rede CA. Quando a tensão ultrapassa o limite superior, o equipamento aciona os códigos **F43 ou F45** (sobretensão CA). Quando cai abaixo do limite inferior, dispara **F44 ou F46** (subtensão CA) — dependendo do modelo e da fase monitorada.

A ABNT NBR 16149 define os limites para o Brasil: operação contínua entre 80% e 110% da tensão nominal. Para redes de 220V, isso significa de 176V a 242V. Acima de 242V, o inversor deve desconectar em até 0,2 segundos. Abaixo de 176V, idem.

As causas se dividem em duas origens distintas.

**Causas externas (as mais frequentes):**
- Tensão da concessionária genuinamente fora do limite, especialmente em redes de baixa tensão no interior do país
- Neutro com impedância elevada — conexão solta ou condutor subdimensionado — que desequilibra a tensão de referência
- Exportação de energia por cabo CA subdimensionado: quando o inversor injeta corrente no cabo, a resistência do condutor provoca elevação de tensão nos próprios terminais do equipamento
- Harmônicas elevadas no barramento de distribuição local causando picos de tensão não perceptíveis em medição estática

**Causa interna (menos frequente, mas determinante no diagnóstico diferencial):**
O circuito de medição de tensão CA da placa de controle usa um divisor resistivo de alta impedância para escalar os 220V CA para um nível legível pelo ADC do processador. São resistores de alta tensão, geralmente na faixa de centenas de kΩ a MΩ. Se qualquer um deles derivar ou abrir, a leitura do ADC não corresponde mais à tensão física dos terminais.

O inversor passa a "ver" uma tensão que não existe. E dispara proteção em cima de uma leitura errada.

> **Nota sobre F01 e F02:** Na nomenclatura atual dos inversores Deye, F01 é falha de polaridade CC invertida e F02 é falha de isolamento CC permanente. Esses códigos não têm relação com tensão de rede CA. Documentações desatualizadas de terceiros às vezes associam F01/F02 a overvoltage por confusão com outras marcas. Confirme os códigos no manual do modelo específico antes de qualquer diagnóstico.

---

## Como identificar na prática

O diagnóstico começa com uma comparação direta: o que o inversor exibe no display versus o que um multímetro True RMS lê nos terminais CA do equipamento. Essa medição precisa ser feita com o sistema em operação, gerando energia. Nunca com o inversor desligado.

1. Conecte um multímetro True RMS (Fluke 87V ou equivalente) nos terminais L-N do inversor com o sistema gerando
2. Anote a leitura do instrumento
3. Anote a tensão exibida no display do inversor
4. Compare os dois valores

Se o display mostra 248V e o multímetro mostra 232V: o circuito de medição interno está lendo errado — falha na placa de controle.
Se ambos mostram 244V: o problema está fora do inversor.

**Passo a passo de verificação completo:**

1. Meça a tensão no medidor da concessionária
2. Meça no quadro de distribuição do imóvel
3. Meça diretamente nos terminais CA do inversor com ele gerando
   (a diferença entre o quadro e os terminais revela a resistência do cabo)
4. Calcule a queda/elevação: ΔV = 2 × R (Ω/m) × comprimento (m) × corrente (A)
5. Verifique o log de eventos do inversor: os erros concentram-se entre 10h e 14h? Coincide com o pico de geração?
6. Pergunte ao instalador a bitola e o comprimento do cabo CA instalado
   (essa informação faz toda a diferença no diagnóstico e raramente alguém pergunta)

Inversores costeiros — especialmente instalações no litoral baiano e fluminense — chegam com trilhas do circuito de medição de tensão corroídas por salinidade. A resistência dos componentes deriva ao longo do tempo e a leitura passa a ser incorreta. O inversor começa a "ver" tensões que não existem. Não é exatamente o modo de falha que os manuais descrevem — mas é o que chega até nós.

**Sinais físicos que apontam para falha interna na placa de controle:**
- Resistores SMD do circuito de medição com aspecto queimado ou coloração alterada
- Trilhas próximas ao conector CA com oxidação visível
- Capacitores no circuito de interface com inchaço na tampa

---

## O erro mais comum do mercado

O erro mais frequente é medir a tensão da rede com o inversor desligado — e concluir que está tudo normal.

Quando o inversor está gerando, ele injeta corrente no cabo CA. Essa corrente percorre a resistência do condutor (fase + neutro) e eleva a tensão nos próprios terminais do equipamento. Um cabo de 4mm² com 20 metros exportando 5 kW (cerca de 22A em 230V) tem resistência de saída e retorno de aproximadamente 0,18Ω. Elevação resultante: 22A × 0,18Ω = quase 4V. Isso empurra uma tensão de 234V em repouso para 238V durante a geração.

Com cabo de 2,5mm² na mesma situação, a elevação pode chegar a 6 a 8V. No interior do Nordeste e em partes de Minas Gerais, é comum ver a tensão da concessionária oscilar entre 235V e 242V nas horas de pico. O inversor passa a ver 244-248V nos terminais e desliga por proteção.

O técnico mede a tensão com o inversor fora, vê 232V, declara que a rede está normal. Condena a placa de controle.

O problema era o cabo.

---

## Quando o reparo é viável

**Sem necessidade de reparo no inversor:**
- Tensão da concessionária fora do PRODIST Módulo 8: registre as medições e notifique a distribuidora com o histórico de erros do inversor como evidência
- Cabo CA subdimensionado: substitua pela bitola correta para a corrente e comprimento do trecho
- Parâmetros de proteção configurados com limites europeus por engano: acesse o menu de proteção com senha de instalador e ajuste para os limites corretos da NBR 16149

**Reparo na placa de controle necessário quando:**
- Display mostra tensão consistentemente diferente do multímetro em mais de 5V
- O erro aparece com os terminais CA fisicamente desconectados — isso confirma que a falha está no próprio circuito sensor, não na rede
- Inspeção visual revela componentes queimados ou corroídos próximos ao circuito de medição CA

O reparo em nível de componente envolve substituição dos resistores do divisor de tensão — peças de alta tensão, alta estabilidade, tolerância de 1%, mínimo 1W. Os valores exatos dependem da revisão de placa e requerem o esquema elétrico do modelo. Sem o esquema, o reparo não pode ser feito com confiança.

Um inversor Deye residencial novo custa entre R$ 3.500 e R$ 5.000. Uma placa de controle sobressalente, quando disponível no mercado nacional, fica entre R$ 800 e R$ 1.200. Um reparo em nível de componente no circuito de medição pode custar R$ 350 a R$ 600 — dependendo do grau de dano e do acesso ao material técnico do fabricante.

Ainda não existe resposta única para quando o reparo é viável. Depende do que você vai encontrar na placa.

---

## Conclusão

Antes de condenar o inversor por erro de tensão de rede, faça a comparação que importa: multímetro calibrado nos terminais CA com o sistema gerando versus o que o display do inversor mostra. Se os valores batem, o problema está fora do equipamento. Se divergem, a placa de controle tem defeito.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

A gente vê isso toda semana. Inversor novo pedido, cabo de 2,5mm² identificado depois. O problema nunca foi o inversor.

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "falha de isolamento CC permanente" → Link para: post sobre Growatt Erro 102 – Falha de Isolamento (Post 01)
- Âncora: "circuito de medição de tensão na placa de controle" → Link para: post sobre placa de controle vs. placa de potência (Post 43)
- Âncora: "cabo CA subdimensionado" → Link para: post sobre inversor solar parado – checklist completo (Post 11)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16149" → Fonte: ABNT – Sistemas Fotovoltaicos, Características da Interface de Conexão com a Rede Elétrica de Distribuição
- Texto âncora: "PRODIST Módulo 8" → Fonte: ANEEL – Procedimentos de Distribuição de Energia Elétrica no Sistema Elétrico Nacional (aneel.gov.br)
- Texto âncora: "resistência do condutor" → Fonte: Tabelas de resistência de cabos por bitola – ABNT NBR NM 207

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1621905251918-48416bd8575a?w=1200
→ Página da imagem: https://unsplash.com/photos/solar-inverter-repair-electronics
→ Por que foi escolhida: Técnico em bancada com placa de controle de inversor solar — contexto direto do diagnóstico descrito no post
→ Nome do arquivo: deye-tensao-rede-diagnostico-placa-controle.webp
→ Alt Text (máx. 125 caracteres): Técnico diagnosticando falha de tensão de rede em inversor Deye com multímetro na placa de controle
→ Legenda: Fig. 1 — Diagnóstico de tensão CA no circuito de medição da placa de controle de inversor Deye
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Página da imagem: https://unsplash.com/photos/solar-inverter-maintenance
→ Por que foi escolhida: Multímetro em uso com equipamento eletrônico — ilustra o procedimento de medição descrito no H2 de diagnóstico
→ Nome do arquivo: medicao-tensao-inversor-solar-multimetro-2.webp
→ Alt Text (máx. 125 caracteres): Multímetro True RMS medindo tensão CA nos terminais de inversor solar para diagnóstico de sobretensão
→ Legenda: Fig. 2 — Medição de tensão CA nos terminais do inversor durante operação. Comparar com o display é o primeiro passo do diagnóstico
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM ALTERNATIVA — BACKUP]

IMAGEM ALTERNATIVA:
→ URL para download: https://images.unsplash.com/photo-1581091226033-d5c48150dbaa?w=1200
→ Página da imagem: https://unsplash.com/photos/circuit-board-electronics-repair
→ Nome do arquivo: placa-controle-inversor-deye-circuito-medicao-alt.webp
→ Alt Text (máx. 125 caracteres): Placa de controle de inversor solar com componentes SMD do circuito de medição de tensão CA visíveis
→ Legenda: Placa de controle de inversor solar — circuito de medição de tensão CA com divisor resistivo de alta impedância
→ Onde inserir: Substituir qualquer uma das anteriores
→ Converter para WebP — máximo 150 KB
