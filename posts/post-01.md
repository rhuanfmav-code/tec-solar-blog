# Post 01 — Growatt Erro 102: Falha de Isolamento (String Leakage)

---

## [PALAVRA-CHAVE FOCO]

Growatt erro 102 falha de isolamento string leakage

---

## [TÍTULO SEO — Title Tag]

Growatt Erro 102: Falha de Isolamento — Diagnóstico Completo

---

## [SLUG — URL do Post]

growatt-erro-102-falha-de-isolamento

---

## [META DESCRIPTION]

Growatt Erro 102 indica falha de isolamento na string CC. Veja como diagnosticar com megômetro e quando o defeito é interno no inversor.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Growatt erro 102, falha de isolamento, string leakage, diagnóstico inversor solar, capacitor Y

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **Growatt Erro 102** é um dos códigos de falha mais recorrentes nos inversores da marca que chegam até nós. O inversor para, o display trava nesse código, e o integrador fica sem saber se o problema está no campo, nos painéis ou dentro do equipamento.

Na nossa bancada, esse erro chega com uma história quase sempre igual: o instalador tentou religar o inversor três vezes, o erro voltou em todas, e o equipamento foi enviado como "defeito interno". Em boa parte dos casos, o problema estava no string — não no inversor.

O Erro 102 sinaliza que a resistência de isolamento entre a string fotovoltaica e o aterramento (PE) caiu abaixo do limiar mínimo de segurança. É uma proteção real, não um alarme falso. Este artigo explica a causa raiz, como diagnosticar corretamente na prática e quando a bancada eletrônica precisa entrar no processo.

## O que causa o Growatt Erro 102

O inversor mede continuamente a resistência de isolamento entre os condutores CC da string — positivo e negativo — e o terra. Quando essa resistência cai abaixo de aproximadamente 100 kΩ (o limite exato varia por modelo; consulte o datasheet do seu equipamento), o firmware trava a operação e exibe o Erro 102.

As causas externas são as mais frequentes:

1. Conector MC4 com infiltração de umidade — o mais comum no Brasil, especialmente em instalações no litoral ou no interior onde o ciclo dia/noite gera condensação intensa dentro dos conectores
2. Cabo CC com isolação danificada por roedor, esmagamento mecânico ou degradação por exposição direta ao sol sem proteção de conduite
3. Módulo fotovoltaico com microtrinca no vidro ou delaminação severa na laminação traseira, abrindo caminho para a umidade entrar na estrutura
4. Caixa de junção (junction box) no verso do painel com vedante ressecado ou rompido
5. Conduite com acúmulo de água em trechos horizontais — situação clássica em usinas instaladas sem inclinação adequada no duto
6. Contato elétrico entre cabo CC e a estrutura metálica da usina em algum ponto ao longo do string

Internamente, a falha mais comum são os **capacitores Y** — capacitores de segurança classe Y2, conectados entre o barramento CC e o PE para supressão de EMI. Quando um desses capacitores falha em curto, cria um caminho de baixa resistência ao terra. O firmware interpreta isso como falha de isolamento no string. O circuito físico está dentro do inversor, mas o comportamento imita exatamente um problema externo.

A ABNT NBR 16690 e a IEC 62109-1 estabelecem requisitos de isolamento para instalações fotovoltaicas. Sistemas com resistência abaixo do limiar mínimo não devem operar — o desligamento automático do inversor é exatamente a proteção prevista por essas normas.

## Como identificar na prática

O diagnóstico começa separando o campo do equipamento.

**No campo:**

1. Desligue o inversor e o disjuntor CC
2. Desconecte os cabos da string dos bornes CC do inversor
3. Conecte um megômetro (500 V CC ou 1000 V CC, conforme a tensão máxima da string)
4. Meça a resistência entre PV+ e PE — resultado esperado: acima de 1 MΩ
5. Meça entre PV- e PE — mesmo critério
6. Meça também entre PV+ e PV- para verificar curto entre condutores
7. Se qualquer leitura estiver abaixo de 100 kΩ, o problema está na string, não no inversor

**Sinais físicos que indicam onde está a falha:**

- Conector MC4 com cristalização branca nos pinos (sinal de oxidação por umidade) ou deformação na trava de encaixe
- Cabo CC com isolação rachada, amassada ou com marca visível de dente de roedor
- Módulo com vidro trincado, manchas escuras (hot spot) ou bolhas na laminação traseira
- Junction box com tampa aberta, vedante deteriorado ou resíduo de água na parte interna

**Na bancada, se o campo estiver limpo:**

Com o inversor na bancada, meça a resistência entre o barramento CC positivo e o PE, sem nenhuma string conectada. Leitura abaixo de 50 kΩ aponta para problema interno. Localize os capacitores Y na placa de potência — geralmente identificados como CY1, CY2 ou similares, valores típicos entre 100 nF e 470 nF, tensão 250 V, classe Y2. Meça cada um individualmente. Um capacitor Y em curto vai aparecer como resistência próxima de zero no multímetro em modo continuidade ou resistência.

## O erro mais comum do mercado

Enviar o inversor para troca sem medir a isolação do string primeiro.

O Growatt Erro 102 se comporta de forma idêntica nos dois cenários: problema externo e problema interno. O display mostra o mesmo código, o inversor desliga da mesma forma. Sem megômetro no campo, é impossível distinguir os dois casos só pela leitura do display.

Substituir um inversor de 3 kW — que custa entre R$ 1.800 e R$ 3.200 — por causa de um conector MC4 com umidade, que custa menos de R$ 10, é o tipo de desperdício que a gente vê com frequência. Principalmente em instalações no interior de Minas Gerais e no Nordeste, onde o ciclo térmico intenso e a umidade sazonal degradam os conectores muito mais rápido do que em regiões de clima mais estável.

O segundo erro é religar o inversor repetidamente com baixo isolamento. Cada tentativa força corrente de fuga pelo aterramento. Isso pode danificar o próprio circuito de medição interno — transformando um problema externo simples em um defeito eletrônico real.

Não existe forma de "forçar o inversor a ignorar o erro". Quem tenta contornar essa proteção por configuração de parâmetro cria um risco elétrico concreto.

## Quando o reparo é viável

**Problema externo (string, cabos ou módulos):** sempre viável. Substituição do conector MC4, troca do trecho de cabo danificado ou do módulo com falha de vedação resolve completamente. Custo de material: baixo.

**Capacitor Y interno em curto:** viável na quase totalidade dos casos. O componente custa entre R$ 2 e R$ 10 na bancada. A substituição é direta. Antes de religar, vale verificar se o curto gerou tensão residual em outros pontos do circuito de filtragem adjacente.

**Circuito de medição de isolamento danificado:** mais trabalhoso, mas viável com esquemático ou placa de referência funcional. A seção de medição nos modelos Growatt (séries MIN, SPH, MIC) usa amplificadores operacionais e divisores resistivos de precisão. Com o componente identificado, a substituição é direta. Sem referência, exige comparação com uma unidade funcional da mesma série.

Na prática: custo médio de reparo em bancada fica entre R$ 200 e R$ 450. Um inversor novo, entre R$ 1.800 e R$ 4.000. A conta fala por si.

## Conclusão

Antes de condenar qualquer inversor com Growatt Erro 102, meça a isolação do string. Um megômetro de 500 V resolve essa dúvida em dez minutos — e pode evitar a compra de um equipamento novo que não resolverá o problema se a causa for externa.

Se o campo estiver limpo e o defeito for interno, o caminho é a bancada com diagnóstico em nível de componente. Trocar o inversor inteiro por causa de um capacitor Y de R$ 5 não faz sentido técnico. Nem financeiro.

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

Post 01 é o primeiro do calendário — não há posts anteriores para linkar internamente.

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16690" → URL: https://www.abnt.org.br/normalizacao/lista-de-publicacoes/abnt → Fonte: ABNT (Associação Brasileira de Normas Técnicas)
- Texto âncora: "IEC 62109-1" → URL: https://www.iec.ch/homepage → Fonte: IEC (International Electrotechnical Commission)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Painel solar fotovoltaico com foco no conjunto de módulos, contexto direto do tema de string CC
→ Nome do arquivo: growatt-erro-102-falha-isolamento-string.webp
→ Alt Text (máx. 125 caracteres): Painel solar fotovoltaico — diagnóstico de falha de isolamento Growatt Erro 102 em string CC
→ Legenda: Fig. 1 — String fotovoltaica: ponto de origem mais frequente do Growatt Erro 102
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200
→ Por que foi escolhida: Técnico realizando medição elétrica com equipamento de teste, contexto de diagnóstico com megômetro
→ Nome do arquivo: growatt-erro-102-diagnostico-megohmetro-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo resistência de isolamento com megômetro em string fotovoltaica — diagnóstico Growatt Erro 102
→ Legenda: Fig. 2 — Medição de isolamento com megômetro: primeiro passo do diagnóstico correto
→ Onde inserir: Após H2 "Como identificar na prática"
