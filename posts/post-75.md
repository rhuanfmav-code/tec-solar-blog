# Post 75 — Deye F29: Falha de IGBT — curto ou sobrecarga no estágio de potência

---

[PALAVRA-CHAVE FOCO]

Deye F29 falha IGBT inversor solar

---

[TÍTULO SEO — Title Tag]

Deye F29: Falha de IGBT — Curto ou Sobrecarga no Inversor

---

[SLUG — URL do Post]

deye-f29-falha-igbt-curto-sobrecarga

---

[META DESCRIPTION]

Deye F29 indica falha no IGBT do estágio de potência. Veja como diagnosticar se é curto, desaturação ou colapso térmico — e quando o reparo compensa.

---

[CATEGORIA]

Códigos de Erro e Falhas

---

[TAGS]

Deye F29, falha IGBT inversor solar, diagnóstico inversor Deye, reparo estágio de potência, curto IGBT solar

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **Deye F29** é um dos erros que chegam com mais frequência acompanhados da sentença "equipamento condenado". O inversor parou, o técnico tentou resetar duas vezes, o F29 voltou, e o diagnóstico foi feito na hora: placa destruída, troca imediata. Isso é a descrição do erro mais comum que a gente vê no mercado, e não é o F29 em si — é o diagnóstico precipitado.

Na nossa bancada, esse erro chega com uma história quase sempre igual: inversor parou de repente durante o dia, às vezes com cheiro de queimado, às vezes sem. Técnico reseta, F29 aparece de novo. Inversor embalado e enviado. Quando abrimos, em boa parte dos casos há um IGBT destruído em curto — e o restante da placa está íntegro. O reparo é viável, e o equipamento poderia ter voltado à operação em dias.

O F29 é a indicação do circuito de proteção de que o módulo IGBT do estágio de potência falhou. Não é genérico. É o sistema dizendo: detectei anomalia no chaveamento principal. Entender por qual caminho essa anomalia chegou é o que define a complexidade do reparo.

## O que causa o erro F29 no Deye

O IGBT — Transistor Bipolar de Porta Isolada — é o componente que executa a conversão DC-AC: chaveia a corrente do barramento CC em alta frequência para gerar a senoide na saída. Quando ele falha, o inversor para. Há três caminhos principais para isso acontecer.

**Curto entre coletor e emissor:** O IGBT conduz permanentemente sem controle de gate. A corrente irrestrita percorre trilhas da placa antes que a proteção atue, e pode arrastar o driver de gate junto. Acontece geralmente após pico de tensão no barramento DC causado por string superdimensionada, surto atmosférico ou falha no circuito de pré-carga.

**Desaturação:** O IGBT não entra em curto abrupto, mas perde a capacidade de controlar a corrente quando em condução. O driver de gate detecta isso via pino DESAT e dispara o desligamento de emergência. As causas mais comuns são curto-circuito na saída CA, sobrecarga severa ou falha de isolamento na instalação que gera corrente anômala no circuito de saída.

**Colapso térmico:** A temperatura de junção supera o limite do módulo — geralmente entre 150 °C e 175 °C. Isso acontece quando a pasta térmica degradou, o dissipador está obstruído por poeira, ou o ventilador parou. Em instalações no norte e nordeste do Brasil, com temperatura ambiente acima de 40 °C e inversor em ambiente fechado sem ventilação, esse caminho é mais rápido do que parece.

Nos inversores Deye de geração atual, o circuito de gate opera com +15 V na condução e -8 V no bloqueio. Qualquer desvio nesses valores já degrada o IGBT de forma silenciosa antes da falha total.

## Como identificar na prática

O diagnóstico começa com o inversor completamente desenergizado. Espere ao menos cinco minutos após o desligamento e confirme com multímetro que a tensão residual no barramento DC está abaixo de 10 V antes de tocar na placa.

1. Medir resistência entre Coletor e Emissor de cada IGBT: valor próximo de zero ou continuidade direta indica curto-circuito. O IGBT está destruído.
2. Testar na função diodo: de Emissor para Coletor deve aparecer queda de diodo (~0,4 a 0,6 V); de Coletor para Emissor deve aparecer circuito aberto. Condução nos dois sentidos confirma curto interno.
3. Inspecionar visualmente: rachaduras no revestimento epóxi do módulo, manchas escuras nos terminais ou trilhas queimadas no caminho C-E indicam que o curto teve corrente alta antes de ser interrompido.
4. Verificar o driver de gate com osciloscópio na tentativa de partida: a saída deve apresentar pulsos em +15 V / -8 V. Ausência de sinal ou amplitude incorreta indica falha no driver — independente do estado do IGBT.
5. Medir o resistor de gate (Rg): valor fora da especificação do datasheet aponta degradação no amortecedor de oscilação, o que causa anomalias no chaveamento antes da falha total.
6. Verificar o capacitor de bootstrap do driver: capacitor aberto interrompe a alimentação do driver do IGBT superior, resultando em disparo assimétrico e eventual F29.
   — Esse ponto é frequentemente ignorado. Em inversores com mais de três anos de uso, o capacitor de bootstrap é um dos primeiros a degradar silenciosamente.

## O erro mais comum do mercado

O técnico encontra o IGBT em curto, troca o módulo, testa o inversor, aparentemente funciona, devolve. Duas semanas depois, o F29 volta.

O driver de gate falhou antes do IGBT, ou junto com ele. Se o driver estava com saída incorreta antes da troca, o módulo novo vai ser destruído pelo mesmo mecanismo. Não importa quantas vezes trocar o IGBT enquanto o driver não for verificado com osciloscópio.

## Quando o reparo é viável

Se apenas o módulo IGBT está em curto e o driver de gate está entregando tensão correta na saída — confirmado com osciloscópio — o reparo é direto. O custo do módulo IGBT para inversores Deye de 3 a 10 kW representa, em geral, entre 10% e 20% do preço de um equipamento novo. Não tem argumento financeiro para substituição nesse cenário.

Quando o driver também falhou mas a placa não apresenta trilhas queimadas, o reparo ainda é viável. Exige troca do CI driver — modelos comuns no circuito Deye incluem IR2110, HCPL-314J e variantes com proteção DESAT integrada — limpeza da placa e recomissionamento com carga controlada.

O cenário mais complexo é quando a corrente de curto percorreu trilhas da placa de potência antes que a proteção interrompesse. Nesses casos pode haver dano no shunt de corrente, no CI de medição ou no próprio conector de gate. Ainda reparável em bancada com equipamento adequado, mas exige mapeamento completo do caminho do defeito antes de qualquer substituição de componente.

Ainda não existe resposta automática para isso. Depende do que você vai encontrar na placa quando abrir.

## Conclusão

O Deye F29 tem diagnóstico definido e, na maioria dos casos que chegam até nós, tem reparo viável. A questão não é o erro em si, mas o que foi feito antes de enviar o equipamento.

Medir o driver antes de trocar o IGBT. Identificar o que causou o stress original na instalação. Verificar se o dano ficou contido no módulo ou se se propagou. Sem esse levantamento, o reparo é um chute com data de validade curta.

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

- Âncora: 'Por que os IGBTs queimam em inversores solares' → URL: /por-que-igbts-queimam-inversores-solares → Contexto: seção "O que causa o erro F29", após mencionar pico de tensão no barramento DC
- Âncora: 'driver de gate' → URL: /o-que-e-driver-igbt-falha-estagio-potencia → Contexto: seção "O erro mais comum do mercado", ao explicar que o driver falhou antes do IGBT
- Âncora: 'falha no circuito de pré-carga' → URL: /deye-f17-sobretensao-barramento-dc-falha-pre-carga → Contexto: seção "O que causa o erro F29", ao citar pré-carga como origem de pico de tensão
- Âncora: 'colapso térmico' → URL: /superaquecimento-inversor-solar-causas-consequencias → Contexto: seção "O que causa o erro F29", terceiro mecanismo descrito
- Âncora: 'placa de potência' → URL: /placa-controle-vs-placa-potencia-como-diferenciar-defeito → Contexto: seção "Quando o reparo é viável", ao mencionar dano na placa de potência

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "Transistor Bipolar de Porta Isolada" → URL: https://www.iec.ch/homepage → Fonte: IEC — normas internacionais de componentes eletrônicos para conversores de potência (IEC 62109)
- Texto âncora: "temperatura ambiente acima de 40 °C" → URL: https://www.aneel.gov.br → Fonte: ANEEL — referência às condições climáticas e requisitos de operação de inversores no Brasil

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1581092921461-eab62e97a780
→ Por que foi escolhida: placa eletrônica de potência com módulos e trilhas visíveis, adequada para representar o estágio de potência do inversor
→ Nome do arquivo: deye-f29-igbt-placa-potencia.webp
→ Alt Text (máx. 125 caracteres): Placa de potência de inversor solar com módulo IGBT — diagnóstico do erro Deye F29
→ Legenda: Fig. 1 — Estágio de potência de inversor solar: módulo IGBT é o componente central do chaveamento DC-AC
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475
→ Por que foi escolhida: técnico com multímetro realizando medição em placa eletrônica, representando o diagnóstico prático descrito na seção
→ Nome do arquivo: deye-f29-diagnostico-multimetro-igbt.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo IGBT com multímetro em placa de inversor solar — diagnóstico Deye F29
→ Legenda: Fig. 2 — Diagnóstico em bancada: medição de continuidade entre Coletor e Emissor do IGBT para confirmar curto-circuito interno
→ Onde inserir: Após H2 "Como identificar na prática"
