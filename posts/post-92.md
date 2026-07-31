# Post 92 — Deye Híbrido SUN-5K: Falha de Comunicação com a Bateria (BMS Fault) — CAN, RS485 ou bateria?

---

[PALAVRA-CHAVE FOCO]
falha de comunicação BMS inversor Deye híbrido

---

[TÍTULO SEO — Title Tag]
Deye Híbrido BMS Fault: Falha de Comunicação da Bateria

---

[SLUG — URL do Post]
deye-hibrido-bms-fault-falha-comunicacao-bateria

---

[META DESCRIPTION]
BMS Fault no Deye híbrido trava a bateria e derruba o backup. Veja se é protocolo, cabo CAN ou defeito na placa antes de trocar o inversor.

---

[CATEGORIA]
Códigos de Erro e Falhas

---

[TAGS]
deye híbrido, BMS Fault Deye, comunicação CAN bateria, inversor híbrido Deye, diagnóstico BMS inversor

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

A **falha de comunicação BMS inversor Deye híbrido** é hoje um dos chamados que mais crescem na bancada — e quase nunca o problema está onde o instalador olha primeiro. O ícone da bateria fica vermelho no display, o inversor exibe "BMS Fault", "Batt Comm Fault" ou simplesmente para de reconhecer o banco de lítio, e o sistema de backup deixa de funcionar na hora em que mais se precisa dele.

Na nossa bancada, esse caso chega com uma história quase sempre igual: o sistema funcionou por semanas, veio uma queda de energia, o backup não entrou, e a bateria "sumiu" do inversor. O instalador troca o cabo, reinicia tudo, liga para o suporte da marca da bateria, e no fim empurra o inversor para reparo achando que a placa de controle morreu. Na maioria dos Deye híbridos que recebemos do interior de Minas e da Bahia — onde a bateria fica num anexo quente, sem ventilação, e o cabeamento é crimpado em campo — o defeito nem sempre está no inversor.

Este post separa o que é configuração, o que é cabo, e o que é defeito real na placa.

## O Que Causa Este Erro

O Deye híbrido não conversa com a bateria de lítio por fios de potência. Ele troca dados com o BMS do banco por um barramento de comunicação — na maioria das instalações, CAN bus; em alguns bancos, RS485. É por esse canal que a bateria informa tensão, corrente, SOC, temperatura de cada célula e os limites de carga e descarga.

Quando esse diálogo para, o inversor não tem como saber se pode puxar corrente da bateria. Por segurança, ele bloqueia o banco e dispara o BMS Fault. O erro não diz que a bateria está ruim. Ele diz que o inversor parou de ouvir a bateria.

A raiz da perda de comunicação cai em um destes pontos:

- Protocolo de bateria errado no menu do Deye — o inversor precisa estar setado para a marca exata do BMS (Pylontech, BYD, WeCo, Growatt, genérico), e cada uma usa um código diferente
- Pinagem do cabo CAN incorreta — o RJ45 do Deye usa pinos específicos para CAN-H e CAN-L, e a bateria usa outros; cabo de rede comum crimpado direto quase nunca casa
- Resistor de terminação de 120 Ω ausente ou dip switch de terminação na posição errada no último módulo do banco
- Endereço (address) da bateria configurado errado nos dip switches quando há mais de um módulo em paralelo
- Transceptor CAN da placa de comunicação do inversor danificado — o CI que converte o sinal (tipo TJA1050 / SIT1050) queima por surto ou sobretensão no barramento
- BMS da bateria em modo de proteção ou "dormindo" após descarga profunda, sem responder ao inversor

Repare que só um desses seis pontos é defeito interno do inversor.

## Como Identificar na Prática

O que a gente vê na prática é diferente do que o suporte descreve por telefone. O display do Deye mostra o alarme, mas não aponta a causa. É preciso medir.

Com o sistema energizado e o multímetro em tensão CC, o barramento CAN em repouso fica em torno de 2,5 V em cada linha para o terra, com uma pequena diferença entre CAN-H e CAN-L quando há tráfego. Linha morta, 0 V ou 5 V travado, indica transceptor ou cabo.

Passo a passo de verificação:

1. Confirmar no menu do Deye se o tipo de bateria está em "Lithium" e se o protocolo/código do BMS corresponde exatamente à marca do banco instalado. Código errado é a causa número um.
2. Conferir a pinagem real do cabo de comunicação contra o manual do Deye E do manual da bateria — os dois lados. Pino de CAN-H de um não é o mesmo pino do outro.
3. Medir continuidade de cada via do cabo RJ45, ponta a ponta. Cabo crimpado em campo com alicate ruim abre uma via e derruba o CAN inteiro.
4. Verificar o resistor de terminação de 120 Ω no último módulo — medir resistência entre CAN-H e CAN-L com o banco desligado. Sem terminação, o sinal reflete e corrompe.
5. Checar os dip switches de endereço e terminação em cada módulo do banco, especialmente em instalações com dois ou mais módulos em paralelo.
6. Testar com um cabo de comunicação sabidamente bom, feito na bancada. Se o BMS Fault some, o problema era o cabo — não abra o inversor.
7. Se, com protocolo correto, cabo bom e terminação presente, o inversor ainda não enxerga a bateria: aí sim a suspeita recai sobre o transceptor CAN da placa de comunicação.

## O Erro Mais Comum do Mercado

O erro clássico é condenar a placa de comunicação do Deye antes de olhar o cabo.

O técnico vê "BMS Fault", assume defeito eletrônico, e orça um inversor novo ou uma troca de placa. Enquanto isso, o defeito real era um RJ45 com uma via aberta ou o protocolo da bateria setado na marca errada depois de uma atualização de firmware que resetou o menu.

Trocar equipamento sem medir o barramento CAN é jogar dinheiro fora. Um cabo refeito resolve o que parecia uma pane de milhares de reais.

## Quando o Reparo é Viável

Quando a comunicação falha por defeito real na placa, o reparo quase sempre vale — e fica muito abaixo do custo de um inversor híbrido novo.

O transceptor CAN é um circuito integrado de baixo custo. Substituído em bancada, com o padrão de sinal restaurado e testado contra uma bateria real, o inversor volta a reconhecer o banco normalmente. O que exige cuidado é descobrir por que o transceptor queimou: se houve surto que entrou pelo barramento, pode ter atingido também o isolador ou a fonte de alimentação da lógica de comunicação, e trocar só o CI resolve por pouco tempo.

Por isso o diagnóstico não para no primeiro componente danificado. A gente rastreia até onde a energia do surto chegou.

Ainda não existe resposta fechada para todo caso. Depende do que a placa mostrar quando abre.

## Conclusão

BMS Fault no Deye híbrido é, na maioria das vezes, um problema de comunicação — não de bateria morta nem de placa queimada. Protocolo, pinagem e terminação respondem pela maior parte dos chamados. O defeito eletrônico interno existe, é real, mas é o último da fila, não o primeiro.

Antes de condenar, diagnostique. Meça o barramento antes de assinar um orçamento de troca.

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

- Âncora: 'Deye Híbrido: os erros mais comuns' → URL: /deye-hibrido-erros-mais-comuns-inversores-hibridos → Contexto: introdução, ao situar o BMS Fault dentro do conjunto de falhas típicas de inversores híbridos Deye
- Âncora: 'RS485' → URL: /growatt-erro-603-falha-comunicacao-rs485 → Contexto: seção "O Que Causa Este Erro", ao mencionar o barramento RS485 como alternativa ao CAN em alguns bancos
- Âncora: 'diagnóstico em nível de placa' → URL: /diagnostico-nivel-placa-inversor-solar → Contexto: seção "Quando o Reparo é Viável", ao explicar o rastreamento do surto além do primeiro componente danificado
- Âncora: 'logística reversa' → URL: /logistica-reversa-reparo-inversores-como-funciona → Contexto: bloco CTA, reforçando o atendimento nacional

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "barramento CAN" → URL: https://www.iso.org/standard/63648.html → Fonte: ISO 11898 — norma que define a camada física e de enlace do barramento CAN, base da comunicação entre inversor e BMS
- Texto âncora: "limites de carga e descarga" → URL: https://www.iec.ch/homepage → Fonte: IEC 62619 — requisitos de segurança para baterias de lítio em aplicações estacionárias, incluindo a função do BMS

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1620714223084-8fcacc6dfd8d?w=1200
→ Por que foi escolhida: banco de bateria de lítio com inversor híbrido em instalação residencial, contexto direto do sistema onde ocorre a falha de comunicação BMS
→ Nome do arquivo: deye-hibrido-bms-fault-comunicacao-bateria.webp
→ Alt Text (máx. 125 caracteres): Inversor Deye híbrido e bateria de lítio — falha de comunicação BMS no barramento CAN e diagnóstico do backup
→ Legenda: Fig. 1 — No sistema híbrido, inversor e BMS da bateria trocam dados por um barramento de comunicação; quando ele falha, o Deye bloqueia a bateria e dispara o BMS Fault
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=1200
→ Por que foi escolhida: técnico medindo sinal em placa eletrônica com multímetro, representando a verificação do barramento CAN e do transceptor durante o diagnóstico
→ Nome do arquivo: diagnostico-barramento-can-transceptor-deye.webp
→ Alt Text (máx. 125 caracteres): Medição do barramento CAN em placa de comunicação de inversor Deye híbrido durante diagnóstico de BMS Fault
→ Legenda: Fig. 2 — A medição de tensão e continuidade no barramento CAN separa o defeito de cabo do defeito no transceptor da placa de comunicação
→ Onde inserir: Após H2 "Como Identificar na Prática"
