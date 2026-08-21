# Post 113 — Deye Híbrido: modo On-Grid/Off-Grid não comuta — relé, contator ou firmware?

---

[PALAVRA-CHAVE FOCO]
Deye híbrido não comuta On-Grid Off-Grid

---

[TÍTULO SEO — Title Tag]
Deye Híbrido Não Comuta: Relé, Contator ou Firmware?

---

[SLUG — URL do Post]
deye-hibrido-nao-comuta-on-grid-off-grid

---

[META DESCRIPTION]
Deye híbrido não troca entre On-Grid e Off-Grid? Causa real quase sempre é relé travado ou driver com defeito — não firmware.

---

[CATEGORIA]
Inversores Off-Grid e Híbridos

---

[TAGS]
Deye híbrido, falha de comutação, relé de rede, modo EPS, inversor híbrido

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **Deye híbrido não comuta entre On-Grid e Off-Grid** é um dos problemas mais difíceis de diagnosticar em campo porque o inversor continua operando — sem alarme no display, sem código de erro, sem nada que indique, de forma óbvia, que a comutação falhou.

Na nossa bancada, esse problema chega de duas formas. A mais frequente: o inversor fica preso no modo On-Grid mesmo depois que a rede caiu. O LED de EPS não acende, a carga de backup fica sem energia e o cliente liga achando que o sistema inteiro travou. A segunda forma: o equipamento não sai do modo Off-Grid mesmo com a rede recuperada, e a geração solar para de exportar. Em ambos os casos, o reflexo imediato é apontar para o firmware. Essa conclusão está errada na maioria das vezes.

O problema quase sempre está em três componentes físicos: o relé de rede, o driver de relé na placa de controle, ou o contator externo nos sistemas trifásicos.

## O que causa a falha de comutação no Deye híbrido

O inversor híbrido Deye opera com um sistema de comutação baseado em relés de alta corrente. Quando a rede está presente, um relé conecta a saída CA do inversor ao grid. Quando a rede cai, esse relé precisa abrir em milissegundos para isolar o inversor e acionar o modo EPS — alimentando a carga de backup por bateria e solar.

O ponto de falha mais comum é o relé em si. Esses relés, geralmente do tipo Omron G7L ou equivalente, suportam correntes de 30 a 40 A. Com o tempo, os contatos oxidam, podem soldar por sobrecorrente transitória, ou a bobina aumenta sua resistência e passa a não receber corrente suficiente para acionar. Quando o contato solda, o inversor não consegue abrir o circuito — fica preso em On-Grid independentemente do que o firmware manda fazer.

Isso tem peso.

O segundo ponto de falha é o driver de relé na placa de controle. A bobina do relé é acionada por um transistor ou MOSFET que recebe o sinal do MCU. Se esse componente abre ou curta, o comando de comutação chega na placa mas nunca chega na bobina. O relé não clica. O modo não muda.

Firmware, na maioria dos casos reais, é causa secundária. Entra em cena quando o relé está íntegro, o driver funciona, mas a lógica de controle tem um bug que trava a transição — cenário mais comum em versões antigas de firmware ou em condições específicas de carga que a lógica não consegue resolver sozinha.

## Como identificar na prática

O primeiro diagnóstico é auditivo. Durante um teste de comutação forçada — via display ou via app SolarmanPV — ouça se há o clique característico do relé. Sem clique, o relé não está acionando: o problema está no driver ou no próprio relé. Com clique mas sem mudança de modo, o relé aciona mas os contatos não comutam — indicativo de contatos soldados ou severamente oxidados.

Verificações na sequência:

1. Acesse o menu de diagnóstico do Deye e tente forçar a comutação via *Configurações > Controle de Modo*
2. Meça a tensão nos terminais da bobina do relé durante a tentativa — deve aparecer 12 V ou 24 V por alguns segundos, dependendo do modelo
3. Se a tensão está presente mas o relé não clica, o relé tem defeito mecânico ou de bobina
4. Se a tensão está ausente, o driver de relé tem defeito — meça o transistor de acionamento com o multímetro no modo diodo; um transistor aberto no par coletor-emissor confirma a falha
5. Verifique o log de eventos no SolarmanPV: erros de relé aparecem como *Relay Fault* ou associados a falha de EPS
6. Em sistemas trifásicos com contator externo, meça a tensão na bobina do contator durante a tentativa de comutação — contator com bobina aberta é uma causa frequente que o inversor reporta como falha genérica de EPS, sem indicar o ponto exato

Em inversores que chegam do Nordeste e do Centro-Oeste, onde as oscilações de tensão de rede são mais frequentes, vemos com mais frequência os contatos do relé principal com marcas de arco elétrico. A sobretensão transitória queima os contatos antes de qualquer proteção atuar.

## O erro mais comum do mercado

O técnico atualiza o firmware. O problema persiste. Faz o reset de fábrica. O problema persiste. Fica dois ou três dias tentando configuração diferente antes de abrir o equipamento.

Isso tem uma razão: o manual Deye é vago sobre a comutação de modo, e o suporte técnico da marca costuma indicar atualização de firmware como primeiro passo para qualquer falha. O resultado é que um defeito eletrônico físico fica mascarado por semanas de tentativas por software.

Outro erro frequente: substituir o inversor inteiro por suspeita de defeito irreparável. Em mais de um caso que chegou até nós, o problema estava em um relé de menos de R$ 100. O cliente já tinha adquirido um inversor novo.

## Quando o reparo é viável

Relé de comutação com defeito: reparo direto. O componente custa entre R$ 40 e R$ 120 dependendo do modelo, e a substituição é feita na bancada em poucas horas. A placa de controle não precisa ser trocada.

Driver de relé com transistor aberto: reparo viável. Localiza-se o componente pelo esquemático, confirma-se o defeito com multímetro e substitui-se. O custo do componente é irrisório — o custo real está na mão de obra técnica e no tempo de diagnóstico preciso.

Placa de controle com trilha danificada próxima ao circuito de drive: depende da extensão do dano. Penetração de umidade ou calor excessivo podem comprometer o substrato da placa. Retrabalho é possível em bancada equipada, mas o diagnóstico precisa ser cuidadoso para não tratar o sintoma sem chegar à causa.

Firmware como único problema: técnico com acesso ao ShineTools ou ao modo de atualização USB consegue resolver sem abrir o equipamento. Mas confirme antes que o relé clica durante a tentativa de comutação. Sem esse clique, atualizar firmware não vai mudar nada.

## Conclusão

Antes de atualizar firmware ou fazer reset de fábrica, ouça o relé.

Um clique ausente já resolve a dúvida.

Firmware é software. Relé é eletrônica. Confundir os dois custa tempo, custa dinheiro e, às vezes, custa um equipamento que ainda tinha conserto na bancada.

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

- Âncora: 'relés de alta corrente' → URL: /relés-de-bypass-em-inversores-solares → Contexto: no H2 "O que causa a falha de comutação", ao mencionar relés de alta corrente
- Âncora: 'driver de relé na placa de controle' → URL: /deye-f23-falha-rele-saida → Contexto: no H2 "O que causa", ao introduzir o driver de relé como segundo ponto de falha
- Âncora: 'diagnóstico em nível de placa' → URL: /o-que-e-diagnostico-em-nivel-de-placa → Contexto: no H2 "Quando o reparo é viável", ao mencionar bancada equipada
- Âncora: 'Deye Híbrido SUN-5K' → URL: /deye-hibrido-sun5k-falha-comunicacao-bateria-bms → Contexto: na introdução, como referência cruzada sobre comportamento de inversores híbridos Deye
- Âncora: 'substituir o inversor inteiro' → URL: /inversor-fora-de-garantia-trocar-ou-reparar → Contexto: no H2 "O erro mais comum do mercado", ao abordar substituição precipitada

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "NBR 16150" → URL: https://www.abnt.org.br → Fonte: ABNT — norma técnica de sistemas fotovoltaicos conectados à rede
- Texto âncora: "ANEEL" → URL: https://www.aneel.gov.br/resolucoes-normativas → Fonte: ANEEL — resoluções normativas sobre requisitos de proteção e comutação de sistemas fotovoltaicos

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Mostra inversor solar em instalação, contexto direto do tema
→ Nome do arquivo: deye-hibrido-comutacao-on-grid-off-grid.webp
→ Alt Text (máx. 125 caracteres): Inversor híbrido Deye com falha de comutação entre modo On-Grid e Off-Grid — diagnóstico de relé e driver
→ Legenda: Fig. 1 — Inversor híbrido Deye: falha de comutação entre modos pode ter origem no relé, no driver ou no firmware
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200
→ Por que foi escolhida: Técnico realizando medição eletrônica em bancada — representa o diagnóstico prático descrito no H2
→ Nome do arquivo: diagnostico-rele-inversor-hibrido-bancada.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensão em relé de inversor híbrido — diagnóstico de falha de comutação On-Grid Off-Grid
→ Legenda: Fig. 2 — Medição de tensão na bobina do relé: ausência de sinal confirma defeito no driver de acionamento
→ Onde inserir: Após H2 "Como identificar na prática"
