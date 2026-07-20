# Post 13 — Fronius State 108: Oscilação de Rede — como identificar se o problema é externo ou interno

---

## [PALAVRA-CHAVE FOCO]

fronius state 108 oscilação de rede

---

## [TÍTULO SEO — Title Tag]

Fronius State 108: oscilação de rede — como diagnosticar

---

## [SLUG — URL do Post]

fronius-state-108-oscilacao-de-rede-diagnostico

---

## [META DESCRIPTION]

Fronius State 108 pode ser rede instável ou defeito interno. Saiba identificar a causa e quando o inversor precisa ir para bancada.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Fronius State 108, oscilação de rede inversor solar, qualidade de energia fotovoltaico, diagnóstico Fronius, ABNT NBR 16690

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Fronius State 108** no portal Solar.web, inversor em espera, geração zerada. O código indica oscilação de rede — mas isso pode ser a concessionária com problema, o cabeamento CA da instalação com falha de contato, ou o próprio circuito de medição do inversor gerando alarme falso.

Na nossa bancada, esse estado chega com um padrão bastante claro: inversor que funcionou por meses sem problema começa a registrar State 108 em horários específicos. O que a gente vê na prática é que o evento quase sempre tem correlação temporal — fim de tarde, início da noite, dias com alta temperatura ambiente. Metade dos casos tem origem completamente externa. A outra metade envolve algum problema de cabeamento CA que amplifica variações normais da rede até o nível de alarme.

Este post cobre o que o State 108 realmente indica, o processo de diagnóstico e como separar causa externa de defeito eletrônico interno.

---

## O que causa o State 108 no Fronius

O State 108 indica que o circuito de monitoramento de rede detectou oscilações nas grandezas elétricas da rede CA que extrapolaram os limiares operacionais configurados. O inversor monitora tensão RMS, frequência e taxa de variação de tensão (dV/dt) de forma contínua. Quando qualquer um desses parâmetros sofre variação rápida e repetida fora da faixa permitida, o alarme dispara e o relé de acoplamento abre.

No Brasil, frequência nominal é 60 Hz com tolerância de ±0,5 Hz, e tensão de 127 V ou 220 V com faixa aceitável de ±8%, conforme o PRODIST Módulo 8 da ANEEL. Os inversores Fronius seguem os critérios da ABNT NBR 16690 para conexão de sistemas fotovoltaicos à rede de distribuição.

Causas que chegam até nós com esse estado:

1. **Oscilação de tensão da concessionária** — queda momentânea causada por partida de motor de alta corrente, equipamento de soldagem industrial ou forno a arco no mesmo alimentador. A tensão sobe e desce mais rápido do que o threshold do inversor tolera.
2. **Rede fraca com alta impedância de linha** — circuitos de baixa tensão com longa extensão ou transformador de distribuição sobrecarregado. Em zonas rurais do Nordeste e Norte, onde a distância até a subestação é grande e o transformador atende muitos pontos, qualquer carga pesada cria queda de tensão abrupta visível pelo inversor.
3. **Frequência instável** — menos comum no sistema interligado nacional, mas frequente em instalações que coexistem com grupos geradores ou sistemas isolados. Variação de frequência acima de 0,2 Hz por segundo já aciona o monitoramento.
4. **Conexão CA com resistência variável** — parafuso de terminal solto no barramento de saída, cabo subdimensionado ou conector oxidado. A queda de tensão no próprio cabeamento varia com a corrente e o inversor interpreta isso como oscilação da rede. A origem parece externa, mas está na instalação.
5. **Relé de acoplamento com desgaste mecânico** — o relé de rede que conecta e desconecta o estágio CA pode apresentar resistência variável de contato. Isso cria variação de tensão no ponto de medição do microcontrolador, que o inversor registra como oscilação.
6. **Circuito de medição CA com defeito** — transformador de corrente (CT) com saturação, divisor resistivo de monitoramento com deriva de valor ou capacitor de filtro com ESR elevado. O inversor registra State 108 mesmo com a rede completamente estável. Está lendo errado, não a rede oscilando.

As causas 1, 2 e 3 são do sistema elétrico externo. As causas 4 e 5 são da instalação. A causa 6 é do equipamento.

---

## Como identificar na prática

A primeira pergunta é direta: o State 108 ocorre em horário previsível ou de forma aleatória?

Eventos que seguem padrão temporal, associados a horário de pico ou condições específicas de carga, quase sempre têm origem externa. Eventos completamente aleatórios, sem correlação com hora do dia ou clima, apontam para problema interno ou de cabeamento.

**1. Analise o histórico de eventos no Fronius Solar.web ou Datamanager.** O portal registra cada ocorrência de State 108 com timestamp. Exporte os dados de 15 a 30 dias e verifique se os eventos se concentram em períodos específicos. Esse levantamento não custa nada e já define a direção do diagnóstico.

**2. Instale um analisador de qualidade de energia no ponto de conexão.** Um power quality analyzer conectado ao barramento CA da instalação registra tensão, frequência e THD em tempo real. Se os eventos de oscilação no analisador coincidem com os registros de State 108, o problema está na rede da concessionária. Equipamentos como Fluke 435 e Hioki PW3360 estão disponíveis para aluguel na maioria das capitais brasileiras por menos de R$ 200/dia.

O tipo de distúrbio que dispara o anti-ilhamento do Fronius tem duração de 80 a 300 ms — o multímetro em valor RMS médio não captura isso.

**3. Meça a tensão no terminal CA do inversor com carga e sem carga.** Queda acima de 3 V entre as duas condições aponta para cabeamento subdimensionado. Tensão fora da faixa ANEEL confirma causa externa.

**4. Verifique os terminais CA com o inversor desligado.** Parafusos frouxos, terminais oxidados ou marcas de arco no ponto de conexão. Em instalações a menos de 50 km do litoral no Sul e Sudeste, terminais de alumínio sem proteção específica oxidam em um ou dois anos. A resistência de contato sobe de forma gradual até o ponto de gerar variação de tensão que o inversor detecta como oscilação.

**5. Confira os parâmetros de monitoramento no software de configuração Fronius.** Os thresholds de AC voltage high/low limit e AC frequency range podem ter sido alterados por atualização de firmware ou configuração manual sem registro. Um limite configurado mais restrito do que o padrão pode fazer o inversor disparar State 108 com oscilações dentro dos parâmetros ANEEL.

**6. Desconecte da rede e conecte a uma fonte estável.** Se o State 108 desaparecer com fonte regulada ou rede diferente, o defeito está na rede ou no cabeamento. Se persistir, o problema está dentro do equipamento e o próximo passo é bancada.

---

## O erro mais comum do mercado

O técnico vê o State 108, confere a tensão com o multímetro, vê "230 V", conclui que a rede está boa e encerra o atendimento. Quando o cliente reclama que o problema continuou, o inversor vai para troca.

Nenhum passo dessa sequência incluiu um analisador de qualidade de energia. Um dia de medição teria definido se a causa era externa ou interna e provavelmente evitado a substituição.

O State 108 tem outra armadilha menos óbvia: a configuração de parâmetros. O integrador que fez o comissionamento pode ter ajustado os limiares de tensão para um valor fora do padrão, e essa configuração persiste no equipamento. Se o inversor for trocado sem verificar os parâmetros, o substituto exibe o mesmo State 108 em dias.

---

## Quando o reparo é viável

Quando a causa é interna, o componente com defeito determina a viabilidade:

- CT com saturação ou deriva de ganho: substituição de componente, custo de peça, bancada padrão.
- Divisor resistivo de medição com deriva: identificação ponto por ponto com multímetro de precisão, troca do resistor responsável.
- Relé de acoplamento com desgaste: substituição com relé de mesma especificação. Em modelos Fronius IG Plus, o relé fica no PCB de potência com pinagem DIP. Em modelos Primo, a integração é mais profunda.
- Capacitor de filtro com ESR elevado: ESR meter, identificação direta, substituição.

Fronius tem disponibilidade de peças razoável para os modelos mais vendidos no Brasil: IG, IG Plus, Galvo e Primo. Para modelos com mais de 10 anos, vale consultar antes de qualquer orçamento.

Inversores Fronius de 1,5 a 5 kW: reparo de bancada sai entre R$ 400 e R$ 900. No mercado secundário, um equivalente parte de R$ 1.200. A conta quase sempre favorece o reparo quando o laudo confirma defeito isolado.

Ainda não existe resposta definitiva sobre viabilidade sem abrir e medir. Depende do que você vai encontrar na placa.

---

## Conclusão

O State 108 não diz nada sobre onde está o problema. Diz que o monitoramento de rede disparou.

Histórico de eventos, analisador de qualidade de energia, inspeção de terminais CA, verificação de parâmetros — esse é o caminho. Só depois disso o inversor vai para bancada, se ainda precisar.

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

- Âncora: 'Os inversores Fronius seguem os critérios da ABNT NBR 16690 para conexão de sistemas fotovoltaicos à rede de distribuição' → URL: /fronius-state-102-tensao-cc-alta-causa-diagnostico → Contexto: seção "O que causa o State 108", parágrafo de normas técnicas — o Post 02 cobre o State 102 no Fronius com análise de tensão CC e monitoramento da mesma plataforma de equipamentos
- Âncora: 'O portal registra cada ocorrência de State 108 com timestamp' → URL: /inversor-solar-parou-de-funcionar-checklist → Contexto: seção "Como identificar na prática", passo 1 — o Post 11 apresenta o checklist completo de diagnóstico antes de envio para bancada, com protocolo de análise de histórico de eventos
- Âncora: 'o relé de rede que conecta e desconecta o estágio CA pode apresentar resistência variável de contato' → URL: /sungrow-grid-lost-perda-de-rede-diagnostico → Contexto: seção "O que causa o State 108", causa 5 — o Post 05 aborda perda de rede no Sungrow com análise de relé de acoplamento e diagnóstico do estágio CA

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "PRODIST Módulo 8 da ANEEL" → URL: https://www.aneel.gov.br/prodist → Fonte: ANEEL — Procedimentos de Distribuição de Energia Elétrica no Sistema Elétrico Nacional, Módulo 8, que define os indicadores e limites de qualidade de energia para os parâmetros de monitoramento dos inversores fotovoltaicos
- Texto âncora: "ABNT NBR 16690 para conexão de sistemas fotovoltaicos à rede de distribuição" → URL: https://www.abnt.org.br → Fonte: ABNT — NBR 16690: Instalações elétricas de arranjos fotovoltaicos, norma brasileira que define os requisitos de conexão à rede e parâmetros de monitoramento de rede e proteções

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Inversor solar instalado em parede — representa o contexto do Fronius State 108 com o equipamento em operação e o ponto de conexão à rede CA como objeto central do diagnóstico
→ Nome do arquivo: fronius-state-108-oscilacao-de-rede-inversor.webp
→ Alt Text (máx. 125 caracteres): Inversor solar Fronius instalado em parede — diagnóstico do State 108 por oscilação de rede CA em sistema fotovoltaico
→ Legenda: Fig. 1 — O State 108 no Fronius indica oscilação de rede detectada pelo circuito de monitoramento CA do inversor
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=1200
→ Por que foi escolhida: Técnico com equipamento de medição analisando forma de onda elétrica — representa o procedimento de diagnóstico com analisador de qualidade de energia descrito na seção prática
→ Nome do arquivo: analisador-qualidade-energia-fronius-state108-2.webp
→ Alt Text (máx. 125 caracteres): Técnico usando analisador de qualidade de energia — diagnóstico Fronius State 108 oscilação de rede CA
→ Legenda: Fig. 2 — Analisador de qualidade de energia: a medição que diferencia causa externa de defeito interno no State 108
→ Onde inserir: Após H2 "Como identificar na prática"
