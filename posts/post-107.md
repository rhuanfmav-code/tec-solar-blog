# Post 107 — Bateria de lítio não carrega no inversor híbrido: BMS, SOC ou estágio de carga?

---

[PALAVRA-CHAVE FOCO]
bateria de lítio não carrega inversor híbrido

[TÍTULO SEO — Title Tag]
Bateria não carrega no inversor híbrido: BMS ou eletrônica?

[SLUG — URL do Post]
bateria-litio-nao-carrega-inversor-hibrido

[META DESCRIPTION]
Bateria parou de carregar no inversor híbrido? Veja como diferenciar falha de BMS, SOC descalibrado e defeito no estágio de carga.

[CATEGORIA]
Inversores Off-Grid e Híbridos

[TAGS]
bateria de lítio não carrega, inversor híbrido, BMS fault, SOC descalibrado, estágio de carga

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Bateria de lítio que não carrega em inversor híbrido** chega na bancada com um histórico quase sempre igual. O integrador foi ao campo, mediu a tensão nos terminais, viu um valor baixo e concluiu que o pack estava morto. Às vezes o inversor foi condenado junto. O cliente comprou peça nova. O sistema continuou sem funcionar.

Na nossa bancada, o que a gente vê na prática é diferente: em boa parte dos casos a bateria está boa. O que falhou foi a comunicação entre o BMS e o inversor, ou a leitura de SOC travada após um ciclo de descarga profunda, ou o estágio eletrônico de carga com um componente silenciosamente falhado. Três causas distintas. Três abordagens de diagnóstico completamente diferentes. Confundir as três é o erro que multiplica o prejuízo.

## O que causa esse problema

O inversor híbrido não é um carregador comum. Entre a rede elétrica e os terminais da bateria existe um conversor CC-CC bidirecional — uma montagem com IGBTs ou MOSFETs, driver de gate, shunt de medição e circuito de pré-carga — supervisionado por firmware e por dois sistemas que precisam estar em sincronia: o BMS da bateria e o controlador do inversor.

Para que a carga inicie, essas condições precisam ser verdadeiras ao mesmo tempo:

1. O inversor detecta a bateria via protocolo de comunicação (CAN bus ou RS485/Modbus)
2. O BMS reporta estado sem flags de proteção ativos — tensão, temperatura, desequilíbrio de células
3. O SOC lido está abaixo do ponto de corte configurado
4. O estágio de carga recebe sinal de ativação do driver de gate
5. A tensão no barramento CC está dentro da janela operacional do conversor
6. O circuito de pré-carga equalizou a tensão antes de fechar o relé principal do barramento

Se qualquer um desses pontos falhar, o inversor não inicia a carga. E o comportamento externo pode ser idêntico para causas completamente diferentes.

Baterias LiFePO4 — que dominam o mercado de híbridos hoje — raramente morrem de falha eletroquímica em instalações com menos de cinco anos. O que falha com mais frequência é a camada de comunicação e supervisão. No interior do Nordeste e do Centro-Oeste, onde armários técnicos mal ventilados chegam a 55°C no verão, o BMS entra em proteção térmica e bloqueia a carga mesmo com as células em ótimo estado.

É temperatura, não bateria.

## Como identificar

A separação entre as três causas começa antes de abrir qualquer equipamento.

1. Ler os logs de evento do inversor — Deye, Growatt e Sungrow registram em firmware o motivo pelo qual a carga não iniciou em praticamente todas as versões recentes
2. Verificar se o app de monitoramento (ShinePhone, iSolarCloud, SolarmanPV) exibe comunicação ativa com o BMS — "battery offline" ou "BMS timeout" aponta direto para o protocolo, não para o pack
3. Medir tensão nos terminais da bateria com multímetro antes de qualquer outra conclusão — LiFePO4 com tensão acima de 42 V em sistema 48 V ainda tem carga útil
4. Checar temperatura do pack com pirômetro ou sensor externo — BMS em proteção térmica bloqueia carga mesmo com bateria saudável e comunicação normal
5. Observar se o SOC exibido está parado no mesmo valor há dias, sem variação mesmo com consumo ativo — sinal de descalibração ou de leitura corrompida
6. Tentar reset do BMS pela sequência do fabricante: desligar o inversor, desligar o disjuntor CC da bateria, aguardar 2 minutos, religar na ordem inversa
7. Verificar no menu do inversor o protocolo de comunicação selecionado — protocolo errado configura tensão de carga incorreta e a bateria nunca é reconhecida

Se o inversor não detecta a bateria e não há comunicação: problema no protocolo. Cabo CAN ou RS485 com defeito, configuração incorreta no menu, ou falha no módulo de comunicação do BMS.

Se o inversor detecta a bateria mas o SOC trava em um valor fixo: problema de calibração. Exige ciclo completo de carga/descarga ou procedimento de recalibração via software.

Se o inversor detecta, SOC varia normalmente, mas a corrente de carga é zero mesmo com comando ativo: problema eletrônico no estágio de carga.

## Quando é falha eletrônica interna

A falha no estágio eletrônico tem sinais que a diferenciam das outras duas causas.

O inversor exibe "charging" no display mas a corrente medida nos terminais da bateria com alicate amperímetro é zero ou quase zero. A bateria drena normalmente em modo descarga mas recusa carga — assimetria que indica problema no sentido de carga do conversor bidirecional, não no pack. O inversor reseta ou entra em proteção logo após tentar iniciar o ciclo de carga.

Na placa, o que aparece com mais frequência nesses casos: IGBT ou MOSFET do conversor com curto entre gate e source, driver de gate com sinal de saída incorreto ou ausente, shunt de medição de corrente com deriva que faz o firmware acreditar que já está carregando quando não está.

Há também a falha no circuito de pré-carga — o resistor e o relé que equalizam a tensão antes de fechar o barramento principal. Se esse circuito não atua corretamente, o inversor bloqueia a carga por proteção em todas as tentativas.

Diagnóstico sem osciloscópio aqui é incompleto. O sinal de gate precisa ser verificado na forma de onda, não apenas no nível CC.

## Vale a pena consertar?

Depende de onde está o defeito. E a resposta muda bastante dependendo disso.

Problema de comunicação BMS: resolvível na maior parte dos casos sem custo de componente. Reconfiguração de protocolo, troca de cabo, reset do BMS ou atualização de firmware. O custo é do tempo de diagnóstico, não de peça.

Descalibração de SOC: resolução por software na maioria das situações. Às vezes exige um ciclo completo de carga/descarga para recalibrar o algoritmo interno. Sem custo de componente.

Defeito eletrônico no estágio de carga: a conta muda de figura. Um inversor híbrido de 5 kW tem valor de mercado entre R$ 6.000 e R$ 12.000 dependendo da marca. Os componentes do estágio de carga — IGBTs, drivers de gate, shunts de precisão — individualmente custam entre R$ 50 e R$ 350. O reparo é tecnicamente viável na maioria dos casos, desde que o dano não tenha se propagado para a placa de controle ou para o barramento CC.

O erro financeiro mais caro nesse defeito específico: comprar uma bateria nova achando que a bateria era o problema. A segunda bateria danifica pelo mesmo defeito eletrônico que ainda está ativo no estágio de carga. Diagnóstico antes de qualquer compra.

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

[LINKS INTERNOS SUGERIDOS]

- Âncora: 'driver de gate com sinal de saída incorreto ou ausente' → URL: /driver-gate-igbt-funcao-modos-de-falha-diagnostico-bancada → Contexto: seção "Quando é falha eletrônica interna", ao descrever o componente com defeito
- Âncora: 'Falha de Comunicação com a Bateria' → URL: /deye-hibrido-sun-5k-falha-comunicacao-bateria-bms-fault → Contexto: seção "Como identificar", ao mencionar falha de protocolo BMS
- Âncora: 'Falha de Comunicação BMS' → URL: /sungrow-sh-hibrido-falha-comunicacao-bms-cabo-can-bateria-ou-inversor → Contexto: seção "Como identificar", ao mencionar "BMS timeout"
- Âncora: 'placa de controle ou para o barramento CC' → URL: /placa-de-controle-vs-placa-de-potencia-como-diferenciar-onde-esta-o-defeito → Contexto: seção "Vale a pena consertar?", ao avaliar propagação do dano
- Âncora: 'Erro de Bateria' → URL: /growatt-sph-hibrido-erro-bateria-batvolt-high-low-bms-ou-estagio-de-carga → Contexto: seção "Como identificar", ao mencionar verificação de logs do inversor Growatt

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "protocolo de comunicação (CAN bus ou RS485/Modbus)" → URL: https://www.abntcatalogo.com.br/norma.aspx?ID=313029 → Fonte: ABNT NBR — norma técnica de comunicação serial em sistemas industriais
- Texto âncora: "tensão no barramento CC está dentro da janela operacional" → URL: https://www.aneel.gov.br/cedoc/ren20211000.pdf → Fonte: ANEEL Resolução 1000/2021 — padrões de qualidade de energia na rede de distribuição

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1620714223084-8fcacc2dbe4d?w=1200
→ Por que foi escolhida: banco de baterias de lítio instalado em sistema de energia solar, contexto técnico direto
→ Nome do arquivo: bateria-litio-nao-carrega-inversor-hibrido.webp
→ Alt Text (máx. 125 caracteres): Banco de baterias de lítio em sistema solar híbrido — diagnóstico de falha de carga TEC Solar
→ Legenda: Fig. 1 — Banco de baterias LiFePO4 em inversor híbrido: quando a carga para, o diagnóstico precisa separar BMS, SOC e eletrônica
→ Onde inserir: Topo do post, antes da introdução

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: placa eletrônica com componentes de potência, contexto de diagnóstico em bancada
→ Nome do arquivo: estagio-de-carga-inversor-hibrido-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Estágio de carga de inversor híbrido na bancada — diagnóstico de IGBT e driver de gate TEC Solar
→ Legenda: Fig. 2 — Conversor CC-CC bidirecional do inversor híbrido: o estágio de carga que não ativa pode ter IGBT, driver ou shunt com defeito
→ Onde inserir: Após H2 "Como identificar"
