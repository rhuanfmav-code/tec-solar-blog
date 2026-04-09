# POST 01 — Growatt Erro 102: Falha de Isolamento (String Leakage)
**Status:** Gerado em 2026-04-09 | Pronto para WordPress

---

## PROCESSO DE GERAÇÃO

### ETAPA 1 — RASCUNHO TÉCNICO

**Tema:** Growatt Erro 102: Falha de Isolamento (String Leakage) — causa raiz e como diagnosticar na bancada

**Pesquisa realizada:**
- IEC 62109-1 / NBR IEC 62109-1: limiar mínimo de Riso para inversores fotovoltaicos
- ABNT NBR 16274: procedimento de ensaio de resistência de isolamento em sistemas FV
- Fóruns técnicos de instaladores (DIY Solar Forum, SolarRepairService)
- Boletins técnicos Growatt: limiar de detecção 50 kΩ–500 kΩ dependendo do modelo
- Artigo técnico "PV ISO LOW nos inversores Growatt" (LinkedIn / Guilherme)
- Guia "PV Isolation Low Countermeasure" (Midsummer Wholesale)

*(Rascunho técnico e Humanizer aplicados internamente — output final a seguir)*

---

## ETAPA 3 — OUTPUT FINAL COMPLETO

---

### [PALAVRA-CHAVE FOCO]

growatt erro 102 falha de isolamento string leakage diagnóstico

---

### [TÍTULO SEO — Title Tag]

Growatt Erro 102: Falha de Isolamento — Diagnóstico Técnico

---

### [SLUG — URL do Post]

growatt-erro-102-falha-isolamento-diagnostico

---

### [META DESCRIPTION]

Growatt Erro 102 indica falha de isolamento no circuito CC. Veja a causa raiz, como medir o Riso na bancada e quando o reparo é viável.

---

### [CATEGORIA]

Códigos de Erro e Falhas

---

### [TAGS]

growatt erro 102, falha de isolamento solar, string leakage inversor, diagnóstico inversor solar, Riso fotovoltaico

---

### [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Growatt Erro 102 — falha de isolamento** aparece no display e o inversor para. O integrador chega ao local, tenta resetar, o erro volta. Na maioria dos casos que chegam à nossa bancada, o equipamento nem está com defeito.

O erro indica que o inversor mediu resistência de isolamento abaixo do limiar aceitável entre o circuito CC e o terra — e se recusou a conectar à rede. Isso não é mau funcionamento. É o circuito de proteção fazendo exatamente o que foi projetado para fazer: bloqueando uma condição que representa risco elétrico real para o instalador e para o sistema.

O problema vem depois: a decisão de condenar o equipamento sem medir nada. Isso transforma um diagnóstico de R$ 200 em uma troca de R$ 5.000. Neste artigo, você vai entender a causa raiz real do erro, como localizar o ponto de falha de forma sistemática e quando — de fato — o problema está dentro do inversor.

---

## O que causa o Growatt Erro 102

Antes de qualquer coisa: o Erro 102 não é um código de falha interna. É o resultado de uma medição de resistência de isolamento que ficou abaixo do limiar configurado no firmware.

O inversor Growatt, em modelos transformerless, mede o Riso — resistência de isolamento — entre o circuito de corrente contínua (positivo e negativo da string) e o barramento de terra (PE) antes de cada tentativa de conexão à rede. Se esse valor cair abaixo de 50 kΩ em determinados modelos, ou abaixo de 500 kΩ em outros com firmware mais restritivo, o inversor bloqueia a saída e registra o erro. A NBR IEC 62109-1 exige Riso mínimo de 1 MΩ para operação segura — o inversor está cumprindo a norma.

O ponto de origem do vazamento resistivo pode estar em vários lugares. Em ordem de frequência na bancada:

1. **Cabos CC com isolamento degradado** — Exposição UV, calor cíclico e cabos de qualidade inferior que trinam com o tempo criam caminhos de fuga para a carcaça aterrada do eletroduto ou para a estrutura metálica. Chicotes que passam por bordas sem bucha de borracha se degradam silenciosamente por meses antes de travar o sistema.

2. **Conectores MC4 com umidade interna** — MC4 sem vedação adequada ou com trava quebrada acumulam água. A água condutora fecha um circuito resistivo entre o condutor e o contato metálico externo, que por sua vez está em contato mecânico com a estrutura aterrada. Você vai encontrar Riso na faixa de 200 a 500 kΩ nesse cenário — abaixo do limiar, mas sem indicar curto direto.

3. **Módulos fotovoltaicos com backsheet comprometida** — Microtrincas, descolamento de moldura ou danos por granizo permitem que umidade alcance as células energizadas. Frequente em módulos com mais de 8 anos sem inspeção visual rotineira.

4. **Condensação interna na string box** — Umidade acumulada na caixa combinadora cria caminhos resistivos entre o barramento CC e a carcaça aterrada. Comum em instalações sem dreno de condensação ou com vedação de calha deteriorada.

5. **Capacitores Y internos ao inversor** — Em inversores transformerless, capacitores Y (filtro EMI) conectam o barramento CC ao terra para filtragem de interferência eletromagnética. Quando envelhecem ou sofrem estresse térmico, a impedância cai. O circuito de medição de Riso lê isso como vazamento — porque tecnicamente é.

6. **Contaminação da PCB por umidade ou corrosão** — Umidade que entrou pelo prensa-cabo ou condensação interna forma trilhas condutoras entre pontos do barramento e o GND do chassi. Você vai encontrar trilhas escurecidas ou resíduo branco-acinzentado característico de corrosão por umidade.

---

## Como identificar na prática

O diagnóstico segue exclusão por segmento. Sem megôhmetro calibrado, você está adivinhando.

**Passo 1: Isole o inversor do circuito externo.**
Desconecte os cabos CC da entrada (positivo e negativo da string) e o cabo CA da saída. Com o inversor completamente isolado, meça a resistência de isolamento nos terminais CC do próprio equipamento em relação ao PE. Use megôhmetro em 500V DC. Se o Riso do inversor, desconectado, estiver abaixo de 1 MΩ, o problema é interno — PCB contaminada ou capacitores Y com impedância reduzida.

**Passo 2: Meça o Riso do circuito externo.**
Reconecte os cabos CC, mantenha o CA desconectado. Meça:
- Terminal positivo (+) da string vs. PE
- Terminal negativo (–) da string vs. PE

Leitura abaixo de 1 MΩ em qualquer um dos dois indica problema no circuito externo.

**Passo 3: Isole segmento a segmento.**
Desconecte módulo a módulo ou string a string (em sistemas com string box). A cada remoção, repita a medição. Quando o Riso voltar acima de 1 MΩ, você identificou o segmento com falha.

**Passo 4: Inspecione os MC4 visualmente.**
Procure oxidação no contato central, presença de água visível no interior e trava quebrada que comprometeu a vedação. MC4 com vedação ruim apresenta Riso típico de 200 a 400 kΩ em dias úmidos — suficiente para travar o inversor toda manhã com orvalho.

**O que você vai encontrar fisicamente:** cheiro de borracha carbonizada ou plástico degradado no cabo indica ponto de aquecimento por resistência de contato elevada. Na PCB do inversor, trilha escurecida ou queimada mostra que corrente de fuga já passou por ali antes de você chegar. Conector MC4 com oxidação verde-acinzentada no contato metálico é sinal claro de corrosão por umidade prolongada.

---

## O erro mais comum do mercado

Chega o técnico, vê o Erro 102, reseta, o erro volta. Conclui que o inversor está com defeito. Recomenda substituição. O cliente compra um inversor novo. Instala. O Erro 102 aparece na primeira semana.

Porque o problema estava na string. O inversor estava correto.

O Erro 102 não significa que o inversor quebrou. Significa que ele recusou operar em uma condição de risco elétrico real — exatamente o que deve fazer. Condenar o equipamento sem medir o Riso no circuito externo não é só um erro técnico. É um erro financeiro grave, e o cliente paga a conta.

O ponto mais crítico dessa falha de diagnóstico é a repetição. O integrador que não identificou a causa raiz vai receber a mesma chamada em seis meses — com o inversor novo exibindo o mesmo código.

---

## Quando o reparo é viável

Se o diagnóstico confirmar que o problema está dentro do inversor — capacitores Y degradados ou PCB contaminada — o reparo é viável na quase totalidade dos casos.

Capacitores Y (classe X2/Y2, tipicamente 100 nF a 470 nF, 275V AC a 500V AC) custam menos de R$ 10 a unidade em distribuidoras de eletrônica. O serviço em bancada, com substituição dos capacitores, limpeza da PCB com isopropanol grau eletrônico e reteste de Riso com megôhmetro, raramente passa de R$ 600 a R$ 800 para inversores de até 10 kW.

Um Growatt 5 kW novo custa entre R$ 3.500 e R$ 5.000 dependendo do modelo e do distribuidor. A relação é direta.

Se houver trilha carbonizada na placa de potência — situação em que o sistema operou com Riso baixo por tempo suficiente para queimar componentes — a viabilidade depende da extensão do dano. Nesse caso, laudo técnico com inspeção em alta ampliação e teste individual de componentes é indispensável antes de qualquer decisão.

O critério objetivo: se a placa de potência principal não foi comprometida pela corrente de fuga, o reparo quase sempre compensa. Se foi, você precisa saber o que está danificado antes de cotar qualquer coisa.

---

## Conclusão

O Growatt Erro 102 para o inversor. Não condena o inversor.

Na maioria dos casos que chegam à bancada, o equipamento está funcionando corretamente — é o circuito externo que criou a condição de falha. Cabos, conectores, painéis, string box. Uma medição de Riso com megôhmetro leva menos de 10 minutos e pode poupar ao cliente R$ 4.000 em equipamento que não precisava ser trocado.

Quando o problema está de fato dentro do inversor, o diagnóstico em nível de placa mostra exatamente o que está comprometido — e se o reparo faz sentido financeiro.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. Fale com nossa equipe pelo WhatsApp.

---

### [LINKS INTERNOS SUGERIDOS]

- Âncora: "capacitores Y (filtro EMI)" → Link para: post sobre capacitores eletrolíticos em inversores (Post 67)
- Âncora: "diagnóstico em nível de placa" → Link para: post sobre o que é diagnóstico em nível de placa (Post 81)
- Âncora: "falha de isolamento em sistemas fotovoltaicos" → Link para: post sobre falha de isolamento em sistemas FV (Post 80)
- Âncora: "superaquecimento de inversor solar" → Link para: post sobre superaquecimento de inversor solar (Post 79)

---

### [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "NBR IEC 62109-1" → Fonte: ABNT — Norma Brasileira de Segurança para Conversores de Potência em Sistemas Fotovoltaicos (abnt.org.br)
- Texto âncora: "ABNT NBR 16274" → Fonte: ABNT — Sistemas fotovoltaicos conectados à rede: requisitos mínimos para documentação, ensaios e inspeção (abnt.org.br)
- Texto âncora: "megôhmetro calibrado" → Fonte: Hioki IR4053 — Megômetro digital para sistemas fotovoltaicos (hioki-getrotech.com.br)

---

### BLOCO DE IMAGENS

---

#### [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://unsplash.com/photos/circuit-board-repair-with-screwdriver-tDIzK0B5Sp8 (clicar em "Download free")
→ Página da imagem: https://unsplash.com/photos/circuit-board-repair-with-screwdriver-tDIzK0B5Sp8
→ Por que foi escolhida: Mostra técnico realizando reparo em placa de circuito impresso, contexto direto de diagnóstico eletrônico em bancada
→ Nome do arquivo: growatt-erro-102-reparo-placa-inversor.webp
→ Alt Text (máx. 125 caracteres): Técnico diagnosticando placa de circuito inversor solar com chave de fenda — Growatt Erro 102 falha de isolamento
→ Legenda: Fig. 1 — Diagnóstico em nível de placa: ponto de partida para identificar falha de isolamento no Growatt Erro 102
→ Onde inserir: Topo do post, antes da introdução
→ ⚠️ Converter para WebP — máximo 150 KB (usar squoosh.app)

---

#### [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://unsplash.com/photos/blue-circuit-board-jXd2FSvcRr8 (clicar em "Download free")
→ Página da imagem: https://unsplash.com/photos/blue-circuit-board-jXd2FSvcRr8
→ Por que foi escolhida: Placa de circuito eletrônico em close — visual técnico que contextualiza a PCB do inversor e os capacitores Y
→ Nome do arquivo: growatt-erro-102-pcb-capacitores-isolamento-2.webp
→ Alt Text (máx. 125 caracteres): Close de placa PCB de inversor solar com capacitores — diagnóstico de falha de isolamento Growatt Erro 102
→ Legenda: Fig. 2 — Capacitores Y na PCB do inversor: componente frequente na origem interna do Growatt Erro 102
→ Onde inserir: Após H2 "Como identificar na prática"
→ ⚠️ Converter para WebP — máximo 150 KB (usar squoosh.app)

---

#### [IMAGEM ALTERNATIVA — BACKUP]

IMAGEM ALTERNATIVA:
→ URL para download: https://unsplash.com/photos/flat-lay-photography-of-circuit-board-zP7X_B86xOg (clicar em "Download free")
→ Página da imagem: https://unsplash.com/photos/flat-lay-photography-of-circuit-board-zP7X_B86xOg
→ Nome do arquivo: growatt-erro-102-placa-eletrica-inversor-alt.webp
→ Alt Text (máx. 125 caracteres): Placa eletrônica de inversor solar aberta em bancada — análise de falha de isolamento Growatt
→ Legenda: Análise de placa de inversores solar em nível de componente — TEC Solar
→ Onde inserir: Substituir qualquer uma das anteriores se necessário
→ ⚠️ Converter para WebP — máximo 150 KB (usar squoosh.app)

---

**Post gerado: Post 01 — Growatt Erro 102: Falha de Isolamento (String Leakage)**
