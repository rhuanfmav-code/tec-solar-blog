# Post 79 — O que é diagnóstico em nível de placa e por que ele muda tudo no reparo

---

## [PALAVRA-CHAVE FOCO]

diagnóstico em nível de placa inversor solar

---

## [TÍTULO SEO — Title Tag]

Diagnóstico em Nível de Placa: O Que É e Por Que Importa

---

## [SLUG — URL do Post]

diagnostico-nivel-de-placa-inversor-solar

---

## [META DESCRIPTION]

Entenda o que é diagnóstico em nível de placa em inversores solares e como essa abordagem reduz custos e salva equipamentos condenados sem motivo.

---

## [CATEGORIA]

Manutenção e Diagnóstico

---

## [TAGS]

diagnóstico em nível de placa, reparo de inversor solar, análise eletrônica inversor, bancada de diagnóstico, laudo técnico inversor

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

Quando um inversor chega exibindo erro de hardware, a primeira decisão define o resultado: o técnico vai testar componente por componente, ou vai substituir a placa inteira tentando a sorte? Essa diferença tem nome. Chama-se **diagnóstico em nível de placa** — e separa quem conserta de quem troca às cegas.

Na nossa bancada, vemos com frequência inversores que já passaram por uma ou duas tentativas de reparo antes de chegar aqui. O cliente trocou a placa de potência. Não resolveu. Trocou a placa de controle. Também não funcionou. Em muitos desses casos, o problema original era um capacitor com falha no ESR, um driver de IGBT dessoldado ou um resistor de gate aberto. Custo das peças: menos de R$50. Custo das trocas desnecessárias: às vezes mais do que o inversor valia.

O diagnóstico em nível de placa muda essa equação. Mas para entender por quê, é preciso entender o que ele é — e o que ele definitivamente não é.

## O que é diagnóstico em nível de placa

Em reparo de eletrônica de potência, existem dois caminhos possíveis:

**Nível de módulo:** a placa que falhou é identificada e substituída por inteiro, sem abertura para análise interna.

**Nível de componente (ou nível de placa):** cada elemento da PCB é medido e testado individualmente até localizar o ponto exato de falha.

O diagnóstico em nível de placa trabalha no segundo caminho. Na prática, envolve:

- Medição de resistência e continuidade em todos os nós críticos da PCB
- Leitura do sinal de gate dos IGBTs com osciloscópio — forma de onda, amplitude e timing de disparo
- Teste de capacitores com medidor de ESR, em circuito e fora de circuito
- Verificação de drivers de IGBT com fonte auxiliar isolada
- Análise visual com lupa binocular em trilhas, vias e componentes SMD
- Medição da tensão de alimentação dos drivers (tipicamente +15 V / −8 V em relação ao emissor)
- Verificação do circuito de bootstrap e dos resistores de gate

Em inversores trifásicos de média potência, uma única placa de potência pode conter 6 a 12 IGBTs, seus respectivos drivers, circuitos de proteção e sensores de temperatura integrados. Diagnosticar em nível de placa significa mapear cada um desses pontos antes de tirar qualquer conclusão.

O código de erro no display indica o sintoma. A causa raiz está na placa.

## Como o processo funciona na bancada

O inversor chega, é isolado de qualquer fonte de alimentação e a inspeção começa pelo mais óbvio: visual.

Componente explodido, trilha queimada, condensação, corrosão por exposição à umidade — quando existe, aparece aqui. Mas na maioria dos casos não há nada visível. E é aí que começa o trabalho técnico de verdade.

A sequência padrão na nossa bancada:

1. Inspeção visual com lupa binocular em toda a PCB
2. Medição de resistência nos barramentos CC e CA com inversor desligado — IGBTs em curto aparecem como baixa resistência entre coletor e emissor
3. Alimentação isolada da placa de controle para verificar inicialização e presença de sinal nos gates
4. Captura de forma de onda com osciloscópio nos pinos de gate durante ciclo de potência reduzido
5. Teste ESR dos capacitores do barramento e do filtro de saída
6. Verificação da tensão de alimentação dos drivers — um driver sem tensão negativa não corta o IGBT corretamente no período de desligamento
7. Análise do circuito de pré-carga e dos resistores de snubber

Em inversores com arquitetura modular — driver board, power board e control board separadas — o diagnóstico isola qual placa gerou o defeito antes de qualquer substituição.

O que a gente encontra com mais frequência não é o componente principal com defeito. É o componente que devia proteger o componente principal.

## Por que a maioria dos reparos sem diagnóstico falha

Trocar placa sem diagnóstico não é conserto. É aposta.

O erro mais recorrente é substituir a placa de potência sem entender o que a matou. O novo componente fica exposto ao mesmo problema que destruiu o anterior: sobretensão de barramento não detectada, resistor de gate aberto que causou saturação no IGBT, capacitor de filtro degradado que não amortecer o ripple de corrente no barramento.

Tem um padrão específico que se repete aqui: o IGBT queimou porque o driver perdeu a tensão negativa de polarização (−8 V). Sem ela, o transistor não fecha completamente no período de desligamento, entra em condução linear e dissipa energia como calor até entrar em curto. Trocar o IGBT sem restaurar o circuito de polarização do driver é condenar o inversor a repetir a falha em dias, não meses.

No Nordeste e no Centro-Oeste brasileiro, onde a temperatura ambiente pode ultrapassar 45°C no verão, esse tipo de falha em cascata é mais frequente. Os componentes já operam próximos dos limites térmicos estabelecidos pelo fabricante. Qualquer ponto fraco na placa cede mais rápido.

Isso não aparece em nenhum relatório de erro do inversor.

## Vale a pena pagar por diagnóstico antes de comprar um inversor novo?

A conta é direta.

Um inversor de 5 kW novo custa entre R$3.500 e R$6.000 dependendo da marca e do canal de compra. O diagnóstico em nível de placa custa uma fração disso — e entrega um laudo que diz exatamente o que está com defeito, se o reparo é viável e qual o custo estimado de restauração.

Se o reparo for inviável — placa de potência destruída além de recuperação, múltiplos IGBTs em curto com dano térmico extenso na PCB — o laudo serve como documento técnico para acionar garantia, seguro ou tomar a decisão de substituição com base em dados, não em suposição.

Se o reparo for viável, e na nossa experiência a maioria é, o custo de restauração fica entre 20% e 40% do valor de um equipamento novo.

A pergunta não é se o diagnóstico vale o custo. A pergunta é: faz sentido gastar R$5.000 num inversor novo sem antes saber se o que está parado pode voltar a funcionar por R$800?

---

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

- Âncora: 'por que os IGBTs queimam' → URL: /igbt-inversor-solar-causas-queima → Contexto: Na seção "Por que a maioria dos reparos sem diagnóstico falha", ao explicar o IGBT saturado por perda de tensão negativa no driver
- Âncora: 'placa de controle vs. placa de potência' → URL: /placa-controle-vs-potencia-como-diferenciar-defeito-inversor-solar → Contexto: Na seção "O que é diagnóstico em nível de placa", ao mencionar a diferença entre módulos
- Âncora: 'inversor fora de garantia' → URL: /inversor-solar-fora-de-garantia-trocar-ou-reparar → Contexto: Na seção "Vale a pena pagar por diagnóstico", ao mencionar decisão de substituição
- Âncora: 'capacitores do barramento' → URL: /capacitor-eletrolitico-inversor-solar-vida-util-degradacao → Contexto: Na seção "Como o processo funciona na bancada", ao citar teste ESR dos capacitores

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "diagnóstico em nível de placa" → URL: https://www.inmetro.gov.br → Fonte: INMETRO — certificações e requisitos técnicos para equipamentos de energia solar no Brasil
- Texto âncora: "logística reversa" → URL: https://www.aneel.gov.br → Fonte: ANEEL — regulação de atendimento a sistemas fotovoltaicos conectados à rede

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Placa eletrônica em close representando análise técnica em nível de componente
→ Nome do arquivo: diagnostico-nivel-placa-inversor-solar.webp
→ Alt Text (máx. 125 caracteres): Técnico realizando diagnóstico em nível de placa em inversor solar com osciloscópio e multímetro
→ Legenda: Fig. 1 — Diagnóstico em nível de componente: a análise começa pelos nós críticos da PCB
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=1200
→ Por que foi escolhida: Técnico com osciloscópio analisando placa eletrônica — representa o processo de bancada descrito no post
→ Nome do arquivo: bancada-diagnostico-inversor-solar-2.webp
→ Alt Text (máx. 125 caracteres): Bancada técnica com osciloscópio medindo sinal de gate em IGBT de inversor solar
→ Legenda: Fig. 2 — Captura de forma de onda no gate do IGBT: uma das etapas do diagnóstico em nível de placa
→ Onde inserir: Após H2 "Como o processo funciona na bancada"
