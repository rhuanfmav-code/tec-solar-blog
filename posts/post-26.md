# Post 26 — SMA 6001: Falha de Aterramento

---

## [PALAVRA-CHAVE FOCO]

SMA 6001 falha de aterramento resistência elevada inversor solar

---

## [TÍTULO SEO — Title Tag]

SMA 6001: Falha de Aterramento — Como Diagnosticar

---

## [SLUG — URL do Post]

sma-6001-falha-aterramento-diagnostico

---

## [META DESCRIPTION]

SMA 6001 indica resistência elevada no aterramento. Diagnóstico com telurômetro, inspeção do terminal PE e circuito interno de monitoramento. Reparo viável.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

SMA 6001 aterramento, falha de aterramento inversor solar, resistência de terra inversor SMA, diagnóstico PE inversor solar, NBR 16149 aterramento fotovoltaico

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **SMA 6001** indica que o inversor detectou resistência elevada no condutor de proteção de terra. Quando isso acontece, o Sunny Boy ou Sunny Tripower interrompe a geração e registra o evento. Não é capricho — é um circuito de monitoramento ativo de PE (Protective Earth) que opera conforme IEC 62109-1 e não libera geração enquanto o valor não estiver dentro do limite configurado.

Na nossa bancada, esse erro chega com um padrão que se repete: inversor SMA com 4 a 8 anos de operação, instalado em regiões do Centro-Oeste ou Nordeste, onde o solo argiloso seca completamente no inverno e a resistividade dispara. O técnico em campo reseta o inversor. Volta a gerar. Dois dias depois, 6001 de novo. O ciclo continua até alguém decidir que o inversor "está ruim".

O problema raramente é o inversor.

---

## O que causa o SMA 6001

O circuito interno de monitoramento de PE no SMA aplica uma corrente de teste entre o terminal de terra do inversor e o barramento de proteção do sistema durante a inicialização — e repetidamente durante operação. Se a resistência medida ultrapassar o limiar configurado (em geral 10 Ω a 100 Ω, dependendo do modelo), o evento 6001 é disparado e a geração para.

A IEC 62109-1 exige que o condutor de proteção tenha resistência inferior a 0,1 Ω entre a carcaça do inversor e o eletrodo de terra. A ABNT NBR 16149, que regula instalações fotovoltaicas no Brasil, incorpora esse requisito. O SMA monitora isso ativamente.

É monitoramento de segurança, não de performance.

As causas, em ordem de frequência de chegada na bancada:

- Conexão oxidada no terminal PE do inversor — parafuso frouxo ou torque insuficiente na instalação original
- Emenda no cabo de terra com resistência de contato elevada — junta mal executada, especialmente em instalações com distância maior que 15 metros até a haste
- Cabo de aterramento com seção insuficiente para o comprimento percorrido
- Solo com alta resistividade — argila seca, granito, laterita — onde o eletrodo não tem área de contato suficiente com o solo
- Corrosão galvânica entre haste de cobre e fio de aço galvanizado em solos ácidos do litoral nordestino
- Circuito interno de monitoramento PE com componente de medição com deriva — resistor de precisão deslocado ou amplificador operacional com offset fora de faixa

A maioria das causas está fora do inversor. Mas o subconjunto com falha interna existe — e diferenciar um do outro é o primeiro passo do diagnóstico.

---

## Como identificar na prática

A sequência vai do mais externo ao mais interno:

1. Medição de resistência do condutor PE com multímetro: terminal PE do inversor ao eletrodo de terra — valor esperado abaixo de 1 Ω; acima disso, o problema está no condutor ou nas conexões
2. Inspeção visual do terminal PE no inversor: oxidação no parafuso, fio fora de bitola, pressão de contato insuficiente — são detalhes que passam batido em comissionamentos rápidos
3. Medição de resistência de solo com telurômetro: NBR 5419 recomenda valor abaixo de 10 Ω para sistemas fotovoltaicos; em solo granítico seco do cerrado ou sertão nordestino, valores de 30 Ω a 80 Ω são comuns — suficientes para manter o 6001 ativo com o inversor completamente saudável
4. Teste com aterramento auxiliar de referência: cabo de cobre 6 mm² direto do terminal PE do inversor a uma haste auxiliar com solo umedecido e conexão limpa; se o 6001 some, o sistema de aterramento permanente é o problema — não o inversor
5. Se o erro persistir com aterramento auxiliar válido: abra o inversor; localize o circuito de monitoramento PE, geralmente próximo ao barramento CC; meça a tensão de referência do nó de medição e verifique presença de ripple com osciloscópio
6. Sonda de osciloscópio na saída do amplificador de medição: sinal DC estável esperado; ruído excessivo ou valor fora da faixa de calibração com aterramento correto confirma defeito interno no circuito de medição
   — O resistor de precisão do circuito de monitoramento é componente de 0,1% de tolerância. Substituição por peça de 1% mantém o erro ativo mesmo após o reparo. Esse detalhe mata o conserto.

Sinal físico que aparece às vezes: área escurecida na placa próxima ao terminal PE, com verniz craquelado. Indica arco por resistência de contato alta e repetida — o problema estava lá antes do 6001 aparecer no display.

---

## O erro mais comum do mercado

O técnico mede resistência do cabo de terra com multímetro. Lê 0,8 Ω — "aterramento ok". Emite laudo: inversor com defeito interno. Cotação de placa nova ou troca de equipamento.

O problema é o instrumento.

Multímetro em modo resistência não substitui telurômetro para diagnóstico de aterramento. O telurômetro usa corrente alternada em frequências específicas para eliminar o erro de polarização galvânica no solo e nas emendas. O multímetro lê a resistência ôhmica do condutor isoladamente — mas não captura a resistência de interface eletrodo-solo, que é onde o circuito de monitoramento do SMA está medindo.

Já pegamos casos aqui onde o 6001 sumiu depois de limpar o terminal PE, reapertar o parafuso de fixação e refazer a conexão na haste. Dez minutos de bancada. O laudo anterior indicava troca do inversor.

O diagnóstico encerrado antes do tempo sempre custa caro para alguém.

---

## Quando o reparo é viável

Quando o problema está no sistema de aterramento externo:

- Limpeza e reaperto do terminal PE: custo zero, 10 minutos — viável em todos os casos
- Substituição do cabo com seção adequada: R$ 80 a R$ 300 dependendo da extensão
- Melhoria do eletrodo de terra — nova haste em profundidade maior, solo tratado com bentonita ou composto condutor GEM: R$ 200 a R$ 600
- Aterramento em múltiplos eletrodos interligados em anel, necessário em solos resistivos do Nordeste e Cerrado

Quando o problema está no circuito interno de monitoramento:

- Resistor de precisão do nó de medição — componente de 0,1%: R$ 5 a R$ 20, viável
- Capacitor de filtro com ESR elevado: R$ 15 a R$ 40, viável
- Amplificador operacional de medição com offset: R$ 10 a R$ 50, viável
- Relé de desconexão PE com contato oxidado: R$ 80 a R$ 200, viável

O único caso sem saída prática é corrosão severa na placa próxima ao terminal PE — trilhas destruídas por arco repetido exigem reconstrução extensiva. A decisão de reparar ou substituir depende do modelo e da potência. Não tem resposta padrão para isso.

Um SMA Sunny Boy 5 kW novo sai por R$ 4.000 a R$ 6.000. O reparo para o SMA 6001, na maioria dos casos que chegam até nós, fica abaixo de R$ 600.

---

## Conclusão

O SMA 6001 engana por parecer simples. "Problema de aterramento" soa como algo de campo, de cabo e alicate. E na maioria das vezes é exatamente isso. Mas quando o aterramento externo está correto e o erro persiste, o diagnóstico precisa entrar no circuito interno de monitoramento de PE.

Antes de condenar, diagnostique. Com o instrumento certo.

---

Condenaram seu inversor por causa desse erro?

Antes de comprar equipamento novo, envie para a nossa bancada. A TEC Solar realiza diagnóstico eletrônico completo em nível de componente — abrimos o inversor, medimos a placa, identificamos a causa raiz e entregamos um laudo técnico detalhado.

Se o reparo for viável, você recebe o equipamento funcionando por uma fração do custo de substituição. Se não for, o laudo serve de base para qualquer decisão.

Atendemos todo o Brasil via logística reversa.

👉 [Envie seu inversor agora](https://wa.me/5538998891587) | [Falar no WhatsApp](https://wa.me/5538998891587)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "falha de isolamento" → Link para: SMA 3501: Falha de Isolamento — diagnóstico completo do sistema fotovoltaico (Post 04)
- Âncora: "falha de aterramento" → Link para: Growatt Erro 103: Falha de Aterramento — quando o problema está no cabo e quando está na placa (Post 12)
- Âncora: "IGBTs" → Link para: Por que os IGBTs queimam em inversores solares: as 6 causas reais (Post 10)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62109-1" → Fonte: IEC — Safety of power converters for use in photovoltaic power systems (iec.ch)
- Texto âncora: "ABNT NBR 16149" → Fonte: ABNT — Sistemas de geração de energia fotovoltaica — Características da interface de conexão com a rede elétrica de distribuição (abnt.org.br)
- Texto âncora: "NBR 5419" → Fonte: ABNT — Proteção de estruturas contra descargas atmosféricas (abnt.org.br)
- Texto âncora: "telurômetro" → Fonte: Megger — Earth/Ground Resistance Testing — Application Guide (megger.com)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Técnico trabalhando em painel elétrico com conexões de terra visíveis — representa o contexto de verificação de aterramento e diagnóstico descrito no post
→ Nome do arquivo: sma-6001-falha-aterramento-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Inversor SMA com falha 6001 de aterramento — diagnóstico de resistência de terra com telurômetro e terminal PE
→ Legenda: Fig. 1 — O SMA 6001 é disparado quando o circuito de monitoramento PE detecta resistência acima do limiar; o diagnóstico começa pelo terminal de terra e avança ao circuito interno
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092335397-9583eb92d232?w=1200
→ Por que foi escolhida: Técnico com multímetro medindo em placa eletrônica — representa o passo de verificação de resistência e diagnóstico do circuito interno de monitoramento PE
→ Nome do arquivo: sma-6001-diagnostico-circuito-monitoramento-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo resistência com multímetro em inversor solar SMA — diagnóstico de falha 6001 de aterramento em nível de placa
→ Legenda: Fig. 2 — A medição com multímetro identifica falhas no condutor de terra; o telurômetro é necessário para medir a resistência eletrodo-solo que o circuito do SMA monitora ativamente
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB

<!-- trigger-video-workflow -->
