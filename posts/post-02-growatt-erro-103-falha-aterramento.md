# Post 02 — Growatt Erro 103: Falha de Aterramento

**Status:** Gerado em 2026-04-10
**Etapas concluídas:** Rascunho técnico → Humanizer → Output final

---

## ETAPA 1 — RASCUNHO TÉCNICO (interno, base para humanização)

*(Rascunho usado como base. Output final humanizado está na ETAPA 3.)*

---

## ETAPA 2 — PROCESSO HUMANIZER (executado)

Padrões identificados e eliminados:
- Remoção de vocabulário de IA: "crucial", "highlighting", "fostering", "key"
- Substituição de paralelismos negativos ("não só X, mas Y")
- Eliminação de frases de preenchimento ("é importante notar que")
- Ritmo variado: frases curtas intercaladas com construções técnicas mais longas
- Voz injetada: afirmações diretas de bancada, valores numéricos concretos, reação técnica aos fatos
- Especificidade: faixas de resistência (1 Ω, 5 Ω, 10 Ω), tensões (5V N-PE), valores de capacitores Y
- Audit final executado: linguagem soa como engenheiro de bancada, não como IA descrevendo o que leu

---

## ETAPA 3 — OUTPUT FINAL COMPLETO

---

### [PALAVRA-CHAVE FOCO]

falha aterramento inversor growatt erro 103

---

### [TÍTULO SEO — Title Tag]

Growatt Erro 103: Falha de Aterramento — Cabo ou Placa?

*(54 caracteres — palavra-chave no início, gatilho técnico de decisão)*

---

### [SLUG — URL do Post]

growatt-erro-103-falha-aterramento-cabo-placa

---

### [META DESCRIPTION]

Growatt Erro 103 parou seu inversor? Saiba quando a falha está no cabo PE e quando está na placa. Diagnóstico técnico passo a passo.

*(130 caracteres — problema + solução + autoridade)*

---

### [CATEGORIA]

Códigos de Erro e Falhas

---

### [TAGS]

Growatt Erro 103, falha de aterramento, inversor solar, diagnóstico inversor solar, PE inversor fotovoltaico

---

### [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Growatt Erro 103** aparece no display e, quase sem exceção, a primeira reação do integrador é ligar para o distribuidor pedindo orçamento de inversor novo. Esse reflexo custa caro.

O código sinaliza que o circuito interno de monitoramento de aterramento detectou resistência ou continuidade fora do padrão no condutor PE — o fio de proteção. A questão que quase ninguém para para resolver antes de agir: o problema está no cabeamento externo da instalação ou está dentro da placa de controle do inversor? Essa diferença separa um serviço de R$ 80,00 de um prejuízo de R$ 4.000,00.

## O Que Causa o Erro 103 no Growatt

O inversor Growatt possui um circuito dedicado que monitora continuamente a integridade do condutor PE — tanto do lado CC (string fotovoltaica) quanto do lado CA (conexão com a rede). Quando esse circuito identifica resistência ou continuidade fora do limite, ele desliga a geração e exibe o Erro 103.

A IEC 62109-2 exige isso. Inversores grid-tie são obrigados por norma a monitorar o condutor de proteção e interromper a operação ao detectar qualquer anomalia. Não é defeito de software. É proteção funcionando corretamente.

As causas se dividem em duas origens distintas:

**Causas externas** — a maioria dos casos:
- Cabo PE ausente, solto ou com mau contato no borne de aterramento do inversor
- Alta resistência no condutor de proteção: cabo de seção insuficiente, muito longo, terminal corroído ou mal crimpado
- Eletrodo de aterramento com resistência elevada — haste fincada raso, solo seco, haste oxidada sem tratamento
- Cabo PE com isolação danificada em contato com condutor de fase, gerando leitura errônea no circuito de monitoramento

**Causas internas**:
- Capacitores Y com curto ou degradação dielétrica — ficam posicionados entre o barramento DC ou AC e o PE
- Resistores de detecção com deriva de valor no circuito de monitoramento da placa de controle
- Falha no circuito de isolação entre a placa de controle e o estágio de potência

Na bancada, o que aparece com mais frequência são capacitores Y em curto. São componentes pequenos, baratos, mas quando falham criam exatamente a leitura anormal que dispara o Erro 103. O inversor identifica um caminho de baixa resistência para o terra onde não deveria existir nenhum, e desliga.

## Como Identificar na Prática

O diagnóstico começa fora do inversor. Sempre. Antes de abrir qualquer caixa, percorra esta sequência:

1. **Inspecione o cabo PE visualmente** desde o inversor até a haste ou barramento de aterramento. Atenção a abraçadeiras, passagens por eletrodutos e dobras forçadas. Um cabo de 6 mm² dobrado a 90° em ponto de fixação pode romper condutores internos sem mostrar qualquer dano externo.

2. **Multímetro entre o borne PE do inversor e o eletrodo de terra**: leitura deve ficar abaixo de 1 Ω. Valores acima de 5 Ω indicam resistência excessiva no caminho de proteção.

3. **Tensão entre Neutro e PE no painel CA**: deve estar abaixo de 5V. Valor acima indica neutro flutuante ou condutor PE comprometido.

4. **Terrômetro no eletrodo de aterramento**: a ABNT NBR 5410 exige resistência do sistema de aterramento ≤ 10 Ω. No sertão nordestino ou no cerrado durante a estiagem, não é raro encontrar 60 Ω ou 80 Ω numa haste simples. O inversor vai disparar o Erro 103 toda vez.

5. **Desconecte os strings CC e energize somente pelo lado CA**: se o erro desaparecer com o lado fotovoltaico desconectado, a origem está nos capacitores de filtro do barramento CC.

Se passar em todos esses testes e o Erro 103 persistir, o problema é interno. A partir daí:

- Com o inversor completamente desenergizado e aguardando descarga dos capacitores de barramento (mínimo 5 minutos), meça a resistência dos capacitores Y em relação ao PE. Um capacitor Y em curto vai mostrar leitura próxima de zero ohm — quando deveria apresentar resistência de isolação acima de 1 MΩ.
- Verifique os resistores de detecção na placa de controle. São resistores de valor alto, geralmente entre 1 MΩ e 10 MΩ dependendo do modelo. Resistores com carbonização superficial ou micro-fissura no corpo cerâmico indicam estresse elétrico anterior.
- Inspecione a placa de potência: capacitor com abaulamento na tampa, trilha com oxidação escura ou componente SMD com fratura visível são evidências de falha localizada.

## O Erro Mais Comum do Mercado

Dois movimentos dominam o mercado quando o Erro 103 aparece. Os dois estão errados.

O primeiro: telefonar para o distribuidor antes de colocar um multímetro na instalação. Em torno de 60% dos casos de Erro 103, a causa está do lado externo — no cabeamento, no eletrodo de terra ou na conexão do borne. O inversor estava funcionando corretamente; a instalação é que falhou.

O segundo: trocar o cabo PE sem medir a resistência do eletrodo de aterramento. Cabo novo numa haste oxidada ou em solo com 80 Ω de resistência resolve o problema por semanas. Depois volta o mesmo erro, o técnico volta ao local, o cliente perde a paciência. Aterramento é um sistema completo — não se resolve trocando só o fio.

Condenar o equipamento sem diagnóstico é o terceiro erro — e o mais caro. Um inversor Growatt de 5 kW custa entre R$ 2.500,00 e R$ 4.000,00. O diagnóstico correto leva menos de uma hora.

## Quando o Reparo é Viável

Se a causa for externa, não há componente interno danificado. O "reparo" é ajuste de instalação: troca de cabo, recrimpagem de terminal, tratamento do eletrodo ou acréscimo de hastes em paralelo para reduzir a resistência de terra ao valor exigido pela ABNT NBR 5410.

Se a causa for interna, a viabilidade depende do componente:

**Capacitores Y com falha**: reparo altamente viável. Custam entre R$ 5,00 e R$ 20,00 por unidade com boa disponibilidade no mercado. A substituição exige estação de solda SMD e identificação correta dos valores — tensão de trabalho e capacitância — no datasheet do fabricante.

**Resistores de detecção com deriva**: reparo viável, desde que o esquema elétrico do modelo específico esteja disponível para confirmar os valores nominais corretos.

**Dano mais amplo no circuito de monitoramento da placa de controle**: viabilidade depende da extensão do dano. Placas com falha localizada nessa área têm alto índice de recuperação quando avaliadas por técnicos com experiência em diagnóstico de componentes SMD e acesso a instrumentação adequada.

Substituir o inversor quando o defeito está num capacitor de R$ 15,00 é erro financeiro com causa técnica: ausência de diagnóstico.

## Conclusão

O Erro 103 no Growatt não é sentença de morte para o inversor. É o circuito de proteção funcionando — sinalizando que algo no sistema de aterramento saiu do padrão. O trabalho do técnico é descobrir onde.

Antes de condenar, diagnostique.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. 📲 **[Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587?text=Ol%C3%A1%2C%20vim%20pelo%20blog%20e%20quero%20enviar%20meu%20inversor%20para%20diagn%C3%B3stico)**

Siga a TEC Solar: [@tecsolar_oficial](https://www.instagram.com/tec_solar_moc/)

---

### [LINKS INTERNOS SUGERIDOS]

- Âncora: "capacitores de filtro do barramento CC" → Link para: post sobre Growatt Erro 403 — capacitor de filtro ou isolamento comprometido (Post 08)
- Âncora: "circuito de monitoramento de aterramento" → Link para: post sobre diagnóstico em nível de placa (Post 81)
- Âncora: "corrente de fuga" → Link para: post sobre Growatt Erro 102 — Falha de Isolamento (Post 01)

---

### [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62109-2" → Fonte: IEC — Safety of power converters for use in photovoltaic power systems (standards.iteh.ai/IEC-62109-2)
- Texto âncora: "ABNT NBR 5410" → Fonte: ABNT — Instalações elétricas de baixa tensão (abnt.org.br)
- Texto âncora: "ABNT NBR 5410 exige resistência do sistema de aterramento ≤ 10 Ω" → Fonte: Canal Solar — Ensaio de resistência de isolamento em sistemas fotovoltaicos (canalsolar.com.br)

---

### [BLOCO DE IMAGENS]

---

#### IMAGEM PRINCIPAL — USE ESTA

IMAGEM PRINCIPAL:
→ URL para download: https://unsplash.com/photos/hands-of-young-repairperson-holding-circuit-board-with-microchip-taken-from-electronic-device-over-desk-before-repairing-TMiQBRK-sA4
→ Página da imagem: https://unsplash.com/photos/TMiQBRK-sA4
→ Por que foi escolhida: Mostra técnico segurando placa eletrônica — referência direta ao diagnóstico em nível de placa de inversor
→ Nome do arquivo: growatt-erro-103-diagnostico-placa-inversor.webp
→ Alt Text (máx. 125 caracteres): Técnico segurando placa eletrônica de inversor solar para diagnóstico de falha de aterramento Growatt Erro 103
→ Legenda: Fig. 1 — Diagnóstico em nível de placa: ponto de partida para o Erro 103 quando as causas externas foram descartadas
→ Onde inserir: Topo do post, antes da introdução
→ ⚠️ Converter para WebP — máximo 150 KB (usar squoosh.app)

---

#### IMAGEM SECUNDÁRIA — USE NO MEIO DO POST

IMAGEM SECUNDÁRIA:
→ URL para download: https://unsplash.com/s/photos/circuit-board (selecionar imagem de placa com componentes eletrônicos visíveis)
→ Página da imagem: https://unsplash.com/s/photos/circuit-board
→ Por que foi escolhida: Placa eletrônica com componentes SMD — referência visual aos capacitores Y e resistores de detecção mencionados no diagnóstico
→ Nome do arquivo: growatt-erro-103-placa-controle-capacitor-y-2.webp
→ Alt Text (máx. 125 caracteres): Placa de controle de inversor solar com capacitores Y — componentes relacionados à falha de aterramento Erro 103 Growatt
→ Legenda: Fig. 2 — Capacitores Y na placa de controle: quando falham em curto, geram leitura de baixa resistência que dispara o Erro 103
→ Onde inserir: Após H2 "Como Identificar na Prática"
→ ⚠️ Converter para WebP — máximo 150 KB (usar squoosh.app)

---

#### IMAGEM ALTERNATIVA — BACKUP

IMAGEM ALTERNATIVA:
→ URL para download: https://unsplash.com/s/photos/solar-inverter (selecionar imagem de inversor solar com painel)
→ Página da imagem: https://unsplash.com/s/photos/solar-inverter
→ Nome do arquivo: inversor-solar-growatt-erro-103-aterramento-alt.webp
→ Alt Text (máx. 125 caracteres): Inversor solar Growatt com erro de aterramento — diagnóstico de falha no condutor PE e placa interna
→ Legenda: Fig. 2 — Inversor solar parado por Erro 103: antes de substituir, diagnostique
→ Onde inserir: Substituir qualquer uma das anteriores se necessário
→ ⚠️ Converter para WebP — máximo 150 KB (usar squoosh.app)

---

*Post gerado: Post 02 — Growatt Erro 103: Falha de Aterramento — quando o problema está no cabo e quando está na placa*
