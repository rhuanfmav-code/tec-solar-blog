# Post 45 — Bomba Solar Não Liga: Guia de Diagnóstico para Drive Solar

---

## [PALAVRA-CHAVE FOCO]

bomba solar não liga diagnóstico drive solar

---

## [TÍTULO SEO — Title Tag]

Bomba Solar Não Liga: Como Diagnosticar o Drive Solar

---

## [SLUG — URL do Post]

bomba-solar-nao-liga-como-diagnosticar-drive-solar

---

## [META DESCRIPTION]

Bomba solar não liga? Veja como diagnosticar o drive solar passo a passo: tensão CC, proteção a seco, parâmetros e falha eletrônica interna.

---

## [CATEGORIA]

Drive Solar e Bombeamento

---

## [TAGS]

bomba solar não liga, drive solar diagnóstico, drive solar defeito, IGBT bombeamento solar, proteção seco drive solar

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Bomba solar não liga** — e o gado ficou sem água. O poço está lá, os painéis estão no sol, o drive está energizado. Mas a saída não aparece e a bomba não gira.

Na nossa bancada, esse é um dos chamados mais recorrentes que a gente recebe de instaladores no interior. O equipamento chega como "defeito no drive", e em boa parte dos casos o drive está funcionando. O problema estava no campo. Parâmetro mal configurado, painel sujo, nível do poço baixo, motor com isolamento ruim. A triagem em campo não foi feita, o equipamento viajou sem necessidade, e a perda de tempo podia ter sido evitada.

Este guia cobre as causas reais de uma bomba solar que não liga, em que ordem investigar cada uma, e como identificar quando o problema é de fato eletrônico.

## O que causa esse problema

O drive solar de bombeamento converte tensão CC dos painéis em CA regulado para acionar o motor. Para partir, ele precisa de três condições ao mesmo tempo: tensão CC dentro da faixa de operação, ausência de condição de proteção ativa, e parâmetros de configuração compatíveis com o sistema instalado.

Se qualquer uma dessas condições falhar, o drive não parte — mesmo estando eletrônica e mecanicamente íntegro.

**Tensão CC insuficiente na entrada.** Cada drive tem uma tensão mínima de ativação do MPPT, que varia entre 80 V e 200 V dependendo do modelo e da potência. Painel sujo com camada de poeira fina, sombreamento parcial por galho ou estrutura, temperatura excessiva nos módulos — tudo isso derruba a tensão do string abaixo do mínimo operacional. O drive fica em standby. No display, geralmente aparece "undervolte" ou nenhuma sinalização. Não é defeito.

**Proteção de operação a seco (dry-run).** A maioria dos drives monitora a corrente de saída para detectar se a bomba está operando com água. Com o lençol freático baixo — situação comum no semiárido nordestino e no cerrado durante o período seco — a bomba tenta partir, a corrente fica abaixo do threshold de carga, e o drive bloqueia o acionamento. O ciclo se repete a cada intervalo programado. O comportamento é confundido com falha porque o equipamento tenta ligar e não consegue manter a operação.

**Parâmetro de tensão mínima configurado incorretamente.** O parâmetro de tensão mínima de partida pode ser ajustado via interface. Se alguém configurou 200 V de mínimo para um string que entrega 150 V no horário de pico, o drive nunca vai partir. Não importa a irradiância — o critério configurado não é atingido. Esse tipo de configuração errada acontece com frequência em instalações feitas sem verificação posterior dos parâmetros.

**Resistência elevada no cabo ou conector MC4.** Conector MC4 oxidado, emenda improvisada no ramal CC ou cabo subdimensionado criam queda de tensão que, somada à variação natural da irradiância, mantém a tensão de entrada abaixo do limiar. O detalhe: medir a tensão diretamente nos painéis não revela o problema — a queda aparece com corrente fluindo. Você precisa medir no terminal de entrada do drive, com o sistema operando.

**Motor submerso com isolamento comprometido.** Motor com enrolamento em contato com a carcaça ou com água no cabo de alimentação aciona a proteção de corrente de fuga do drive na tentativa de partida. O drive tenta ligar, detecta corrente de fuga e bloqueia. Em campo: o equipamento para menos de um segundo após o comando de partida, sem chegar a girar a bomba.

**Falha eletrônica interna.** IGBT em curto, driver de gate danificado, falha no circuito de pré-carga do barramento ou no circuito auxiliar de controle. Esses problemas impedem a partida de forma definitiva. O reset não recupera. Esse é o último item da lista — não o primeiro a ser investigado.

## Como identificar na prática

A triagem segue uma ordem. Não adianta pular etapas.

1. Registrar o código de erro no display antes de qualquer reset — fotografe. O código indica o subsistema que acionou a proteção e direciona o diagnóstico.
2. Medir tensão CC na entrada do drive com irradiância acima de 500 W/m², entre 10h e 14h. Comparar com a tensão mínima de operação descrita no manual do modelo. Tensão abaixo do mínimo: o problema está no string ou na fiação CC, não no drive.
3. Medir tensão de cada string separadamente. String com tensão muito abaixo dos demais indica módulo em falha, diodo bypass queimado ou problema de sombreamento localizado.
4. Inspecionar conectores MC4 no ramal de alimentação do drive: verificar travamento mecânico, puxar levemente, observar oxidação na área de crimpagem. Em instalações rurais com mais de três anos de operação sem manutenção, esse ponto de falha aparece com frequência.
5. Verificar os parâmetros de configuração: tensão mínima de partida, frequência mínima de saída, modo de operação, configuração do sensor de nível ou pressão.
6. Testar o motor com megôhmetro 500 V CC — medir entre cada fase do cabo de saída e o terra. Valor abaixo de 1 MΩ confirma isolamento comprometido no cabo ou no motor, e o problema é externo ao drive.
7. Com o motor desconectado, tentar a partida. Se o drive funciona sem carga, a falha está no motor ou no cabo. Se não funciona sem carga, a falha está no drive.

Em instalações de propriedades rurais no interior de Minas e Bahia, a gente vê muito o item 4 como causa — conector MC4 crimpado sem ferramenta calibrada, com contato parcial que se deteriora depois de alguns ciclos de aquecimento e resfriamento.

## Quando é falha eletrônica interna

Alguns padrões indicam falha interna com consistência suficiente para justificar o envio para bancada:

- Drive exibe erro de overcurrent ou IGBT fault durante a tentativa de partida mesmo com motor desconectado da saída
- Após reset, o erro retorna imediatamente — sem variação conforme condições externas ou horário
- Display não energiza mesmo com tensão CC correta na entrada — falha no circuito de controle ou fonte auxiliar interna
- Cheiro de componente queimado ao abrir a carcaça do equipamento
- O drive tentava partir normalmente, sofreu um evento externo conhecido — raio próximo, pico de tensão da rede, entrada de água durante chuva — e nunca mais funcionou

Um padrão específico que aparece na bancada: quando o driver de gate de um dos IGBTs queima, o drive pode tentar partir, gerar uma vibração curta no motor e bloquear com erro genérico. O instalador troca o motor. Não resolve. Volta o erro. O problema não estava no motor — estava no drive, no circuito de disparo dos IGBTs. Substituir um IGBT sem verificar o driver de gate antes é garantia de queimar o IGBT novo.

## Vale a pena consertar?

Drives de bombeamento solar entre 750 W e 7,5 kW custam entre R$ 900 e R$ 7.000 novos. O custo de reparo em falha restrita ao estágio de potência fica entre R$ 350 e R$ 1.400 com laudo técnico. Para falha isolada no driver de gate, ainda menos — é componente discreto de baixo custo.

A inviabilidade aparece quando a placa de controle tem dano por arco em múltiplos pontos, quando o transformador flyback auxiliar está fisicamente destruído, ou quando o modelo foi descontinuado e não há componentes disponíveis.

Para o contexto rural, tem outro fator que costuma ser ignorado: prazo. O equipamento novo pode demorar 20 a 40 dias para chegar no interior. Um drive reparado sai em dias. A conta não é só financeira — é também o tempo de parada do sistema.

Sem abrir e medir, a análise de viabilidade é especulação.

## Conclusão

A maioria das bombas solares que não ligam tem causa externa ao drive. String fotovoltaico com problema, parâmetro errado, motor com isolamento deteriorado, conector MC4 com resistência elevada. A triagem correta resolve em campo, sem movimentar equipamento.

Quando a causa é eletrônica, o diagnóstico em bancada separa o que é reparável do que não é. Condenar um drive sem abrir é um erro técnico — e financeiro.

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

- Âncora: 'drive solar para bombeamento' → URL: /drive-solar-para-bombeamento-defeitos-diagnostico → Contexto: primeira menção ao termo no segundo parágrafo do H2 "O que causa esse problema"
- Âncora: 'driver de gate de um dos IGBTs queima' → URL: /o-que-e-driver-de-igbt-falha-estagio-potencia → Contexto: seção "Quando é falha eletrônica interna", parágrafo sobre padrão específico
- Âncora: 'Por que os IGBTs queimam' → URL: /por-que-igbts-queimam-inversores-solares → Contexto: seção "O que causa esse problema", item sobre IGBT em curto
- Âncora: 'Inversor solar parou de funcionar' → URL: /inversor-solar-parou-de-funcionar-checklist → Contexto: conclusão, como link complementar ao checklist geral

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: 'megôhmetro 500 V CC' → URL: https://www.abnt.org.br → Fonte: ABNT NBR IEC 60364-6 — Instalações elétricas de baixa tensão — Verificação
- Texto âncora: 'proteção de corrente de fuga' → URL: https://www.aneel.gov.br → Fonte: ANEEL — Resolução Normativa 482 — Sistemas de Micro e Minigeração Distribuída

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Painéis solares em área rural com bomba de água ao fundo — contexto direto do tema bombeamento solar
→ Nome do arquivo: bomba-solar-nao-liga-drive-solar-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Sistema de bombeamento solar com drive solar — diagnóstico quando a bomba solar não liga
→ Legenda: Fig. 1 — A maioria das bombas solares que não ligam tem causa externa ao drive; triagem correta evita envio desnecessário do equipamento
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092335397-9583eb92d232?w=1200
→ Por que foi escolhida: Técnico com multímetro realizando medição elétrica — representa a sequência de diagnóstico do drive solar em campo
→ Nome do arquivo: diagnostico-drive-solar-bombeamento-campo-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensão CC em sistema de bombeamento solar com multímetro — diagnóstico drive solar
→ Legenda: Fig. 2 — Medir a tensão CC na entrada do drive com irradiância acima de 500 W/m² é o primeiro passo do diagnóstico correto
→ Onde inserir: Após H2 "Como identificar na prática"
