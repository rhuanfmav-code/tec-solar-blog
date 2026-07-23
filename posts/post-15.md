# Post 15 — SMA 3701: Tensão CC Muito Alta — string mal dimensionada ou falha de medição?

---

[PALAVRA-CHAVE FOCO]

SMA 3701 tensão CC muito alta

---

[TÍTULO SEO — Title Tag]

SMA 3701: Tensão CC Muito Alta — Diagnóstico Completo

---

[SLUG — URL do Post]

sma-3701-tensao-cc-muito-alta-string-ou-falha-de-medicao

---

[META DESCRIPTION]

SMA 3701: tensão CC alta demais. Saiba separar string fora do limite de falha no circuito de medição interno — diagnóstico técnico em nível de bancada.

---

[CATEGORIA]

Códigos de Erro e Falhas

---

[TAGS]

SMA 3701, tensão CC inversor solar, sobretensão CC SMA, diagnóstico string fotovoltaica, circuito de medição inversor

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **SMA 3701 tensão CC muito alta** aparece no monitoramento, o inversor para, e o técnico recebe o chamado sem muito contexto. O log registra o evento, a planta está parada, e a pergunta imediata é: o que mudou?

Na nossa bancada, esse código chega com dois históricos distintos. O mais comum é o inversor instalado no segundo semestre, com string no limite máximo do modelo. Nos primeiros meses funcionou sem problema. Junho chegou, o 3701 passou a aparecer antes das 8h, e o instalador entrou em contato sem saber explicar o que havia mudado. Nada mudou — a temperatura caiu. O segundo histórico é diferente: sistema com 3 a 5 anos, mesma string desde o início, e o 3701 começou a aparecer de forma intermitente sem relação com temperatura ou horário. Esse segundo perfil é problema de medição interna.

São dois caminhos de diagnóstico completamente distintos. Identificar qual é o caso antes de mexer em qualquer coisa economiza tempo e evita que o problema volte na semana seguinte.

## O que causa o SMA 3701

O SMA monitora a tensão CC de entrada por um divisor resistivo de alta impedância que alimenta o conversor A/D do DSP. Quando o valor medido ultrapassa o limite configurado — Udc máx, que varia por modelo entre 600 V, 800 V e 1000 V — o evento 3701 é disparado e o estágio CC é desativado. A ABNT NBR 16274 define os parâmetros operacionais de inversores fotovoltaicos conectados à rede. A IEC 62109-1 estabelece os requisitos de segurança no estágio de entrada CC. O 3701 é o cumprimento dessas exigências.

As causas se dividem em dois grupos.

Causas ligadas à string — a tensão realmente está alta:

- String com mais painéis em série do que o modelo suporta na temperatura mínima local. Painéis de silício cristalino têm coeficiente de temperatura da Voc entre -0,30%/°C e -0,36%/°C. Em manhãs de 5°C — frequentes no sul de Minas, na Serra Gaúcha e nas regiões serranas do Paraná e Santa Catarina — a Voc real é cerca de 7% maior que o STC. Em uma string de 16 painéis com Voc de 40 V cada, isso representa 44,8 V adicionais que não aparecem no cálculo feito com a planilha de projeto.
- Painéis com Voc significativamente acima do datasheet — variação de lote, painel substituído por modelo diferente, ou módulo com falha interna que eleva a tensão de circuito aberto
- String dimensionado com temperatura de projeto de 25°C sem aplicação do fator de correção para a mínima histórica do local
- Módulos com Voc desbalanceada por degradação assimétrica — painel com isolamento interno comprometido pode apresentar comportamento de tensão aberrante em certas condições de irradiância, puxando a leitura do MPPT para fora do esperado

Causas internas — o inversor está medindo errado:

- Resistores SMD do divisor de tensão CC com valor derivado por envelhecimento ou stress térmico. Um resistor de 1 MΩ com desvio de 5% do nominal altera proporcionalmente a leitura — o DSP pode registrar 680 V onde a tensão real é 580 V.
- Capacitor de filtro do circuito de medição CC com ESR elevado, gerando ruído na amostra e leituras instáveis acima do threshold de proteção
- Offset do conversor A/D desviado — ocorre principalmente em inversores com mais de 5 anos de operação em ambiente quente e empoeirado, situação comum em instalações de telhado no Brasil central
- Parâmetros de calibração corrompidos na memória do DSP por surto de tensão ou descarga eletrostática — menos frequente, mas quando acontece o comportamento é errático e não responde a reinicializações

## Como identificar na prática

A ferramenta que diferencia os dois grupos não é o multímetro usado no horário da visita técnica.

1. Exporte o log de eventos do SMA via Sunny Portal ou interface local RS485/Bluetooth. O evento 3701 registra o timestamp e o valor exato de Udc medido internamente no momento da desconexão.

2. Calcule a Voc corrigida para a temperatura mínima histórica do local: **Voc_corrigida = Voc_STC × n_painéis × [1 + αVoc × (T_mínima − 25)]**. Se o resultado supera o Udc máx do modelo, o problema é dimensional. Nenhum componente com defeito.

3. Meça a tensão CC real nos terminais do inversor nos mesmos horários históricos das falhas — preferencialmente entre 6h30 e 8h em dias frios. Compare com o valor registrado no log.

4. Se o log registrou 690 V enquanto o multímetro indicava 570 V no mesmo momento, o circuito interno de medição está divergindo da realidade. Esse é o sinal mais claro de falha eletrônica no divisor resistivo.

5. Com o inversor desligado e o circuito CC totalmente descarregado, meça a resistência dos resistores do divisor de tensão na placa de controle. Compare com os valores nominais do esquema do modelo — desvio acima de 2% em resistores de precisão é causa suficiente para o disparo incorreto.

6. Avalie o padrão temporal: 3701 restrito a manhãs de inverno, antes das 9h, aponta para causa dimensional. 3701 aleatório, qualquer horário, com Udc registrado inconsistente com a string real, direciona para o circuito interno.

7. Verifique o histórico de eventos anterior ao primeiro 3701. Se houver registros de outros eventos fora do padrão — subtensão súbita, falha de comunicação, eventos sem código identificado — pode indicar surto que corrompeu os parâmetros de medição.

## O erro mais comum do mercado

O técnico chega às 11h, temperatura a 31°C, painéis a 55°C. Mede 510 V nos terminais. Registra "tensão dentro do limite, evento transitório" e fecha o chamado.

O 3701 tinha ocorrido às 7h10, com 7°C. A tensão real naquele momento estava em 635 V. O SMA desligou corretamente — foi o diagnóstico que falhou.

A mesma lógica invertida vale para a falha de medição: o técnico mede a tensão externamente, encontra valor normal, e conclui que o inversor está disparando sem motivo. O circuito interno pode estar lendo 120 V acima do real. Isso não aparece em nenhuma medição feita do lado de fora do equipamento.

## Quando o reparo é viável

Se a causa for dimensional, não há componente defeituoso. A solução é reduzir a string ou trocar por modelo com Udc máx mais alto.

Se o diagnóstico confirmou falha no circuito de medição interna:

- Resistores SMD do divisor CC: componentes passivos de custo baixo, substituição com resistores de precisão 0,1% ou 0,5%. É o cenário mais frequente na bancada e o de resolução mais direta.
- Capacitor de filtro CC: substituição direta, custo mínimo, resultado imediato.
- Offset do conversor A/D: viabilidade depende do modelo do CI e da disponibilidade do procedimento de recalibração — alguns modelos SMA permitem recalibração via parâmetros de firmware, outros não. Precisa verificar no modelo específico antes de qualquer conclusão.
- Parâmetros corrompidos na memória: substituição ou regravação do IC de memória, viável quando o arquivo de calibração correto está disponível para o modelo.

Inversores SMA Sunny Boy e Sunny Tripower custam entre R$ 3.800 e R$ 22.000 dependendo da potência. O diagnóstico em bancada sai por uma fração disso. E define com clareza se o reparo faz sentido ou se o problema está no projeto desde o início.

## Conclusão

SMA 3701 é proteção de sobretensão CC. O inversor detectou tensão acima do Udc máx e desligou o estágio de entrada — como deve fazer. A questão é se a tensão estava realmente alta ou se o divisor resistivo interno estava reportando um número falso.

Essa diferença só aparece com o log do evento, a Voc calculada na temperatura certa, e a medição dos componentes na placa. Não dá para saber pela visita às 11h com o sol a pino.

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

- Âncora: 'tensão CC de entrada' → URL: /abb-f003-tensao-cc-alta-string-mal-dimensionada-ou-defeito-de-medicao → Contexto: Seção "O que causa o SMA 3701", na frase sobre o divisor resistivo que monitora a tensão CC de entrada — referência cruzada com o ABB F003 (Post 09), mesmo fenômeno em outra marca
- Âncora: 'coeficiente de temperatura da Voc' → URL: /fronius-state-102-tensao-cc-muito-alta-string-mal-dimensionada-ou-falha-no-sensor-de-tensao → Contexto: Seção "O que causa o SMA 3701", lista de causas dimensionais — referência cruzada com Fronius State 102 (Post 02), que aborda o efeito de temperatura na Voc da string
- Âncora: 'por que os IGBTs queimam' → URL: /por-que-os-igbts-queimam-em-inversores-solares-as-6-causas-reais → Contexto: Seção "Quando o reparo é viável", ao mencionar stress térmico nos componentes — link para Post 10 que detalha o impacto de ciclos térmicos
- Âncora: 'inversor solar parou de funcionar' → URL: /inversor-solar-parou-de-funcionar-checklist-completo → Contexto: Introdução, ao mencionar a planta parada — link para o checklist de diagnóstico inicial (Post 11)

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16274" → URL: https://www.abnt.org.br → Fonte: ABNT — norma técnica para avaliação de desempenho de sistemas fotovoltaicos conectados à rede, incluindo parâmetros operacionais de inversores
- Texto âncora: "IEC 62109-1" → URL: https://www.aneel.gov.br → Fonte: ANEEL — referência às normas internacionais de segurança para conversores de energia usados em sistemas fotovoltaicos, adotadas como base pela regulação brasileira

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Inversor solar instalado em parede com conexões CC visíveis — representa o ponto de entrada onde a tensão CC é monitorada e onde o SMA 3701 é disparado
→ Nome do arquivo: sma-3701-tensao-cc-muito-alta-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Inversor solar SMA instalado com entradas CC — diagnóstico do erro 3701 por tensão CC acima do limite máximo
→ Legenda: Fig. 1 — O SMA 3701 indica tensão CC acima do Udc máx: pode ser string mal dimensionado para a temperatura mínima local ou falha no circuito interno de medição
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=1200
→ Por que foi escolhida: Técnico medindo com multímetro em instalação elétrica — representa o procedimento de medição da tensão CC real nos terminais descrito na seção "Como identificar na prática"
→ Nome do arquivo: sma-3701-medicao-tensao-cc-string-multimetro-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensão CC com multímetro em string fotovoltaico — diagnóstico SMA 3701 tensão muito alta
→ Legenda: Fig. 2 — Medir a tensão real nos terminais de entrada e cruzar com o log do evento é o primeiro passo do diagnóstico do SMA 3701
→ Onde inserir: Após H2 "Como identificar na prática"
