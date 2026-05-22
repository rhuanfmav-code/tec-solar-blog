[PALAVRA-CHAVE FOCO]
Growatt Erro 124 temperatura interna elevada

─────────────────────────────────────
[TÍTULO SEO — Title Tag]
─────────────────────────────────────
Growatt Erro 124: Temperatura Interna Elevada

─────────────────────────────────────
[SLUG — URL do Post]
─────────────────────────────────────
growatt-erro-124-temperatura-interna-elevada

─────────────────────────────────────
[META DESCRIPTION]
─────────────────────────────────────
Growatt Erro 124 parou seu inversor? Veja como identificar se a causa é ventilador travado, dissipador obstruído ou sensor NTC com defeito. Diagnóstico real.

─────────────────────────────────────
[CATEGORIA]
─────────────────────────────────────
Códigos de Erro e Falhas

─────────────────────────────────────
[TAGS]
─────────────────────────────────────
Growatt Erro 124, temperatura inversor solar, ventilador inversor Growatt, sensor NTC inversor, superaquecimento inversor solar

─────────────────────────────────────
[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]
─────────────────────────────────────

# Post 52 — Growatt Erro 124: Temperatura Interna Elevada — ventilador, dissipador ou sensor com defeito?

O **Growatt Erro 124** indica que a temperatura interna ultrapassou o limite de segurança do inversor — geralmente entre 75°C e 90°C dependendo do modelo. O firmware aciona proteção imediata: a geração cai, o equipamento tenta se proteger e, se a temperatura não ceder, o inversor desliga completamente.

Na nossa bancada, esse erro chega com uma história quase sempre igual: o inversor ficou semanas gerando abaixo da potência esperada antes de parar de vez. O ventilador havia travado parcialmente meses antes. O sistema continuou operando, a temperatura foi subindo, e o inversor aguentou o quanto pôde antes de entrar em proteção definitiva.

O erro 124 não é diagnóstico. É sintoma. A causa pode ser mecânica, eletrônica ou ambiental — e essa diferença define se o reparo é direto e barato ou se o IGBT já levou dano secundário antes da parada.

## O que causa o Growatt Erro 124

Os inversores Growatt monitoram temperatura por sensores NTC posicionados no dissipador de calor e, em alguns modelos, no barramento DC. Quando a leitura ultrapassa o limiar configurado no firmware, o erro 124 é registrado e o sistema entra em proteção.

As causas se agrupam em três frentes:

Falha mecânica no sistema de ventilação:
- Ventilador com rolamento desgastado — o ruído anormal aparece meses antes do travamento total; quando o rolamento trava por completo, o calor começa a acumular sem aviso visível no display
- Acúmulo de poeira compacta nas aletas do dissipador, bloqueando o fluxo de ar mesmo com o ventilador em operação
- Instalação em compartimento fechado sem circulação adequada, violando os requisitos mínimos da IEC 62109-1 para ventilação de inversores
- Filtro de entrada entupido em ambientes com partículas finas — mais frequente em galpões industriais, silos e instalações rurais com terra solta

Degradação do contato térmico:
- Pasta térmica ressecada na interface IGBT/dissipador, reduzindo drasticamente a condutância térmica
- Fixação mecânica do módulo IGBT afrouxada por ciclos térmicos repetidos ao longo dos anos

Falha no circuito eletrônico:
- Sensor NTC com deriva de leitura — reporta temperatura acima do real e aciona proteção em condições normais de operação
- Falha no circuito de acionamento do ventilador — o fan não recebe sinal do controlador mesmo quando o firmware determina que ele deve ligar
- Transistor driver do ventilador queimado na placa de controle

Em inversores com mais de 4 anos operando em regiões com temperatura ambiente acima de 35°C — Nordeste, Centro-Oeste, Norte do Brasil — a degradação da pasta térmica e o desgaste do ventilador costumam ocorrer simultaneamente. Um problema esconde o outro até os dois falharem juntos.

## Como identificar na prática

O diagnóstico começa antes de abrir o equipamento.

1. Verificar o histórico de erros no display ou no aplicativo de monitoramento — frequência crescente do erro 124 ao longo de semanas indica causa gradual (pasta ou ventilador em deterioração progressiva)
2. Com o inversor em operação, aproximar a mão da saída de ar — ausência de fluxo com aparente giro do ventilador indica obstrução nas aletas ou ventilador girando sem pressão
3. Medir a temperatura da carcaça com termopar ou câmera termográfica — diferença acima de 25°C em relação à temperatura ambiente, com carga moderada, aponta falha no sistema de dissipação
4. Após desligar e aguardar 10 minutos, abrir o equipamento e verificar o ventilador manualmente — rolamento com desgaste apresenta resistência perceptível ao giro com o dedo; ventilador íntegro gira quase sem atrito
5. Inspecionar o dissipador de calor — acúmulo de poeira compacta entre as aletas é diagnóstico visual imediato de obstrução ao fluxo
6. Com multímetro em modo resistência, medir o NTC em temperatura ambiente e aquecer levemente com soprador — a resistência deve cair de forma contínua com o aumento de temperatura; leitura fixa ou sem variação confirma sensor com defeito

Um detalhe de campo: inversores Growatt instalados em telhados de fibrocimento no semiárido nordestino acumulam poeira vermelha do solo na grade de entrada. Já recebemos equipamentos com essa obstrução quase total — o ventilador girava normalmente, mas o ar simplesmente não entrava. O IGBT estava íntegro. A solução foi limpeza técnica completa.

## O erro mais comum do mercado

O técnico chega, vê o erro 124, limpa o dissipador com ar comprimido, liga o inversor. O equipamento volta a funcionar. Dois dias depois, o erro retorna.

O que esse fluxo pula é a verificação do ventilador e da pasta térmica. Limpar as aletas remove o sintoma visível mas deixa o rolamento desgastado no lugar e a pasta ressecada na interface IGBT/dissipador. A temperatura volta a subir. A proteção volta a atuar.

O que complica mais: se o inversor operou por semanas acima do limite antes de parar, o IGBT pode ter sofrido degradação parcial da junção sem rompimento imediato. O equipamento religar e funcionar não prova que o módulo de potência está íntegro. Prova apenas que ainda não falhou completamente.

Essa diferença não aparece no multímetro com o inversor frio. Aparece em teste de carga com monitoramento de temperatura de junção — ou quando o IGBT cede semanas depois, com a planta em operação plena.

## Quando o reparo é viável

A maior parte dos casos de Growatt Erro 124 tem reparo direto e custo controlado. O fator que complica é a extensão do dano secundário ao IGBT.

Situações com boa viabilidade:

- Ventilador travado sem dano ao IGBT: substituição por modelo compatível com a especificação de tensão e vazão de ar do modelo Growatt (não qualquer fan de computador serve — verificar no datasheet do equipamento), com reaplicação de pasta térmica no contato IGBT/dissipador
- Pasta térmica ressecada como causa isolada: limpeza da superfície metálica com isopropílico e reaplicação com composto de condutância acima de 4 W/m·K — resultado imediato e duradouro
- Sensor NTC com deriva: substituição do termistor por componente equivalente em valor nominal, custo baixo; exige acesso à placa de controle e identificação pelo datasheet do modelo
- Obstrução de poeira sem dano eletrônico: limpeza técnica completa com inspeção visual das trilhas e verificação elétrica do ventilador e do circuito driver

O que complica o reparo:

- IGBT com degradação da junção por operação prolongada acima de Tjmax — o reparo inclui substituição do módulo de potência, custo mais alto mas ainda abaixo de um inversor novo na maioria dos modelos Growatt de médio porte
- Falha no transistor driver do ventilador na placa de controle — exige diagnóstico fino e acesso aos pontos de teste da placa
- Corrosão nas aletas do dissipador por condensação acumulada — situação mais comum em instalações costeiras do Sul e Sudeste, onde a amplitude térmica diária cria ciclos de condensação no alumínio

Ainda não existe uma regra simples que diga "esse modelo Growatt sempre vale o reparo". Depende do que você vai encontrar na placa.

## Conclusão

Erro 124 no Growatt é, na maioria das vezes, um problema mecânico com solução direta. Ventilador, pasta, sensor — cada um com verificação específica, cada um com custo baixo quando isolado.

O que encurece a conta é o tempo que o inversor ficou operando acima do limite antes de alguém agir.

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

─────────────────────────────────────
[LINKS INTERNOS SUGERIDOS]
─────────────────────────────────────
- Âncora: 'IGBT com degradação da junção por operação prolongada acima de Tjmax' → URL: /por-que-os-igbts-queimam-em-inversores-solares → Contexto: seção "Quando o reparo é viável", lista "O que complica o reparo"
- Âncora: 'Falha no transistor driver do ventilador na placa de controle' → URL: /o-que-e-driver-igbt-por-que-sua-falha-destroi-estagio-potencia → Contexto: seção "Quando o reparo é viável", segundo item da lista de complicações
- Âncora: 'pasta térmica ressecada na interface IGBT/dissipador' → URL: /placa-controle-vs-potencia-como-diferenciar-defeito-inversor-solar → Contexto: seção "O que causa o Growatt Erro 124", item sobre degradação do contato térmico
- Âncora: 'superaquecimento de inversor solar' → URL: /por-que-inversores-solares-falham-mais-no-verao → Contexto: conclusão ou seção sobre causas, referência a temperaturas elevadas no Brasil

─────────────────────────────────────
[LINKS EXTERNOS SUGERIDOS]
─────────────────────────────────────
- Texto âncora: "requisitos mínimos da IEC 62109-1 para ventilação de inversores" → URL: https://www.iec.ch/homepage → Fonte: IEC — norma IEC 62109-1 de segurança para conversores de potência em sistemas fotovoltaicos
- Texto âncora: "limiar configurado no firmware" → URL: https://www.inmetro.gov.br → Fonte: INMETRO — Portaria 004/2011 e atualizações, requisitos técnicos de certificação para inversores fotovoltaicos no Brasil

─────────────────────────────────────
[IMAGEM PRINCIPAL — USE ESTA]
─────────────────────────────────────
IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=1200
→ Por que foi escolhida: Técnico inspecionando componentes eletrônicos de inversor — contexto direto de diagnóstico de temperatura e falha mecânica
→ Nome do arquivo: growatt-erro-124-temperatura-interna-elevada.webp
→ Alt Text (máx. 125 caracteres): Inversor solar aberto em bancada técnica mostrando dissipador e ventilador — diagnóstico de Growatt Erro 124 temperatura elevada
→ Legenda: Fig. 1 — Growatt Erro 124: dissipador obstruído, pasta ressecada ou ventilador travado são as causas mais comuns de temperatura interna elevada
→ Onde inserir: Topo do post, antes da introdução

─────────────────────────────────────
[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]
─────────────────────────────────────
IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Placa eletrônica com componentes de potência — representa visualmente a inspeção do NTC, ventilador e IGBT na bancada
→ Nome do arquivo: growatt-erro-124-diagnostico-placa-sensor-ntc-2.webp
→ Alt Text (máx. 125 caracteres): Placa eletrônica de inversor solar com sensor NTC e circuito de controle de ventilador — diagnóstico de Growatt Erro 124
→ Legenda: Fig. 2 — Sensor NTC, circuito driver do ventilador e módulo IGBT são os três pontos de verificação obrigatória no diagnóstico do Erro 124
→ Onde inserir: Após H2 "Como identificar na prática"
