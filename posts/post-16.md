# Post 16 — Sungrow Arc Fault (AFCI): Arco Elétrico Detectado — conector MC4 mal crimpado

---

## [PALAVRA-CHAVE FOCO]

Sungrow Arc Fault AFCI conector MC4 mal crimpado

---

## [TÍTULO SEO — Title Tag]

Sungrow Arc Fault AFCI: arco elétrico e MC4 mal crimpado

---

## [SLUG — URL do Post]

sungrow-arc-fault-afci-conector-mc4-mal-crimpado

---

## [META DESCRIPTION]

Sungrow com erro Arc Fault AFCI? Veja como diagnosticar MC4 mal crimpado, rastrear o arco CC e decidir quando o inversor precisa de bancada.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Sungrow Arc Fault, AFCI solar, conector MC4 solar, arco elétrico CC, diagnóstico inversor solar

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **arco elétrico detectado pelo AFCI Sungrow** não é um erro de configuração. Não some com reinicialização. Quando o inversor dispara esse alerta, ele detectou — com medição real de espectro de frequência — uma descarga elétrica acontecendo dentro do circuito CC da string.

Na nossa bancada, esse erro chega com uma história quase sempre igual: inversor com shutdown recorrente, técnico que reiniciou e "voltou", semanas de operação intermitente — até o dia em que uma caixa de passagem chegou com marcas de calor. O padrão se repete, e quase sempre começa num conector MC4 crimpado com alicate comum, sem ferramenta calibrada para aquele conector específico.

---

## O que causa o arco elétrico no sistema CC

O arco elétrico em corrente contínua é diferente do arco CA. Na corrente alternada, a descarga se extingue no cruzamento por zero. No CC não existe esse mecanismo. Uma vez estabelecido, o arco persiste e se alimenta da própria resistência de contato — que aumenta com o calor gerado, que aumenta o arco, que aumenta o calor.

O sistema AFCI do Sungrow monitora continuamente o espectro de frequência da corrente de cada string. Arcos elétricos produzem ruído de alta frequência — tipicamente entre 10 kHz e 1 MHz — sobreposto ao sinal CC normal. O algoritmo de detecção identifica essa assinatura espectral e interrompe o rastreamento da MPPT afetada antes que o arco evolua para dano permanente.

Isso é proteção ativa. O inversor não está com defeito — ele funcionou corretamente.

As causas mais frequentes em campo:

1. Conector MC4 crimpado com alicate comum — compressão irregular no ferrule, contato parcial com resistência elevada
2. Conectores de marcas diferentes ligados entre si — housing com geometria incompatível, vedação mecânica precária e ponto de concentração de umidade
3. Isolação do cabo CC danificada por UV prolongado, roedor ou pressão de fixação com abraçadeira apertada demais
4. Terminação solta no barramento de entrada do inversor ou na caixa de string
5. Corrosão nos pinos MC4 por infiltração de água — condição comum em instalações no litoral nordestino, onde a névoa salina penetra em conectores com vedação comprometida
6. Pino mal assentado no housing antes da crimpagem — passa na inspeção visual inicial, mas opera com contato parcial sob carga

A IEC 62548 e a ABNT NBR 16274 exigem que conectores fotovoltaicos sejam crimpados com ferramenta homologada pelo fabricante do conector. Alicate comum não garante compressão uniforme. A junta pode parecer firme, ter continuidade no multímetro em teste estático e mesmo assim apresentar resistência de contato elevada o suficiente para gerar arco sob a corrente real da string em operação.

---

## Como identificar na prática

O que você vai encontrar:

1. Registro de "Arc Fault" ou "AFCI Alarm" no histórico do iSolarCloud — com timestamp da primeira ocorrência e identificação da entrada MPPT
2. Corrente da string afetada caindo abruptamente antes do shutdown completo visível no gráfico de monitoramento
3. Após reinicialização manual, o sistema pode operar por horas ou dias antes de repetir — o arco é intermitente no início e se torna permanente com o avanço da degradação do contato
4. MC4 com oxidação nos pinos, deformação no housing ou temperatura anormal ao toque logo após período de geração
5. Caixa de string ou bandeja de cabos com marcas de calor localizadas próximas a uma emenda

Procedimento de verificação em campo:

1. Acessar o iSolarCloud ou o display do inversor — identificar qual MPPT disparou e registrar o horário exato do evento
2. Desligar o sistema completamente e percorrer o trajeto da string afetada do painel até o inversor
3. Verificar cada MC4: o encaixe correto é firme, com clique audível; qualquer folga ou resistência irregular ao desconectar indica problema
4. Medir resistência de contato com miliohmímetro em cada emenda — valor aceitável abaixo de 0,1 Ω; acima disso, trocar o conector
5. Testar a isolação do cabo com megohmetro a 1000 V CC — resultado abaixo de 1 MΩ indica isolação comprometida e o trecho precisa de substituição
6. Aplicar câmera termográfica sob carga parcial para localizar pontos quentes não visíveis a olho nu

Em instalações no interior de Minas Gerais e de Goiás — onde a variação térmica entre manhã e tarde pode passar de 20 °C — o ciclo de expansão e contração mecânica dos cabos é mais agressivo. Conectores com crimpagem fraca cedem mais rápido nessas condições e o arco se instala antes do que em climas mais estáveis.

---

## O erro mais comum do mercado

Reiniciar e aguardar.

AFCI não é evento aleatório. Quando dispara pela primeira vez, existe uma causa física real e verificável. Aguardar o segundo ou terceiro evento para investigar é deixar o sistema operando com foco de incêndio potencial — especialmente em telhados com estrutura de madeira ou telha com revestimento combustível.

O segundo erro é trocar o inversor sem inspecionar o cabeamento. Se o arco está no MC4, no trecho de cabo ou na caixa de string, o inversor novo vai apresentar Arc Fault nas primeiras horas de operação. Resultado: equipamento novo, custo de instalação repetido, problema original intacto.

---

## Quando o reparo é viável

Na maioria dos casos de AFCI Sungrow, o inversor não precisa de bancada. O problema está no campo.

O conector MC4 defeituoso, o cabo com isolação comprometida ou a terminação solta são reparos mecânicos de custo baixo. Ferramenta de crimpagem calibrada, conector certificado, trecho de cabo substituído. O inversor reinicia e não apresenta mais Arc Fault.

O cenário que exige bancada é quando o arco ocorreu internamente — nos terminais de entrada CC, no barramento ou no circuito de detecção AFCI do próprio inversor. Isso acontece quando o sistema operou com arco ativo por tempo longo sem intervenção. Nesses casos, há risco de dano nos componentes do estágio de entrada, nos capacitores de filtro do barramento CC ou na placa de controle.

Critério objetivo: se o Arc Fault dispara em menos de 5 minutos após reinicialização, independente de qual string está ativa, o problema pode ser interno ao inversor. Se dispara apenas com a string específica identificada no histórico e sob carga solar, o problema está no campo.

Mesmo quando o diagnóstico aponta para o campo, vale inspecionar os terminais de entrada do inversor antes de religar. Um arco que queimou o pino de um MC4 pode ter deixado resíduo metálico no terminal de entrada do equipamento.

---

## Conclusão

Arco elétrico CC não é glitch. Não passa sozinho com o tempo.

O que o Sungrow sinaliza com o Arc Fault é que detectou uma condição capaz de destruir cabos, queimar caixas e — em telhados residenciais com estrutura de madeira — evoluir para incêndio. O inversor fez o que deveria: desligou e avisou.

Rastreie o ponto de falha antes de reiniciar. Inspecione cada MC4 da string afetada antes de concluir qualquer coisa sobre o inversor.

Se após a inspeção completa do cabeamento o problema persistir, o inversor precisa de diagnóstico eletrônico. Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "falha de isolamento" → Link para: post sobre Sungrow GFCI Fault: Corrente de Fuga à Terra (Post 27) — ainda não publicado, não inserir link no texto
- Âncora: "conector MC4" → Link para: post sobre Canadian Solar Falha 117: Falha de Isolamento (Post 18) — ainda não publicado, não inserir link no texto

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16274" → Fonte: ABNT — Sistemas fotovoltaicos conectados à rede — Requisitos mínimos para documentação, ensaios de comissionamento, inspeção e avaliação de desempenho (abnt.org.br)
- Texto âncora: "IEC 62548" → Fonte: IEC — Photovoltaic arrays: design requirements (iec.ch)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Conectores MC4 em cabos de painel solar — representa diretamente o ponto onde o arco elétrico se forma e onde o diagnóstico do AFCI Sungrow começa
→ Nome do arquivo: sungrow-arc-fault-afci-conector-mc4-arco-eletrico.webp
→ Alt Text (máx. 125 caracteres): Conectores MC4 em sistema solar fotovoltaico — diagnóstico do erro Arc Fault AFCI Sungrow por crimpagem incorreta
→ Legenda: Fig. 1 — Conector MC4 mal crimpado é a causa mais comum do Arc Fault AFCI em inversores Sungrow; o arco começa no contato parcial e evolui silenciosamente
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092335397-9583eb92d232?w=1200
→ Por que foi escolhida: Técnico realizando medição com multímetro em painel de controle elétrico — representa o procedimento de rastreamento do ponto de arco descrito na seção "Como Identificar na Prática"
→ Nome do arquivo: sungrow-arc-fault-afci-diagnostico-campo-mc4-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo continuidade em conector MC4 solar — procedimento de diagnóstico do Arc Fault AFCI Sungrow em campo
→ Legenda: Fig. 2 — Medir resistência de contato em cada MC4 com miliohmímetro é etapa obrigatória antes de qualquer conclusão sobre o inversor
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB
