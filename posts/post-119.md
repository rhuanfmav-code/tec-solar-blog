# Post 119 — Growatt Híbrido: falha no modo backup (EPS) — carga não migra na queda de rede

---

[PALAVRA-CHAVE FOCO]

Growatt híbrido falha modo EPS

---

[TÍTULO SEO — Title Tag]

Growatt Híbrido: Falha no Modo EPS — Carga Não Migra

---

[SLUG — URL do Post]

growatt-hibrido-falha-modo-eps

---

[META DESCRIPTION]

Growatt Híbrido não comuta para backup (EPS) na queda de rede? Saiba as causas reais: relé, driver, BMS ou configuração incorreta.

---

[CATEGORIA]

Inversores Off-Grid e Híbridos

---

[TAGS]

Growatt híbrido EPS, falha modo backup solar, relé transferência EPS, Growatt SPH falha, inversor híbrido sem backup

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **Growatt Híbrido com falha no modo EPS** é um dos casos mais frustrantes: o sistema está completo, a bateria está carregada, mas na hora que a rede cai, as cargas ficam sem energia. O objetivo de ter backup simplesmente não funciona.

Na nossa bancada, esse equipamento chega com uma história quase sempre igual: o instalador conectou tudo certo, testou em modo normal e só descobriu o problema na primeira queda real de energia. A bateria estava em 80% de SOC, a rede caiu, e o inversor não comutou. Cliente furioso, instalador sem resposta.

O modo EPS transfere automaticamente as cargas da rede para a bateria quando a tensão CA cai abaixo do limite configurado. Quando essa comutação falha, o problema pode estar em quatro pontos distintos: configuração incorreta, falha no relé de transferência, problema de comunicação com o BMS ou defeito no circuito driver. Neste post vamos percorrer cada um desses pontos com o nível de detalhe que o diagnóstico exige.

## O que causa esse problema

O Growatt SPH e os modelos híbridos da linha MIN-TL utilizam um relé de transferência dedicado para o EPS — diferente do relé de rede principal. Esse relé é acionado por um circuito driver composto por transistor de potência e optocoupler, que recebe o comando da placa de controle (DSP).

Quando a rede cai, o DSP detecta a ausência de tensão CA e envia o sinal para acionar o relé EPS. Se qualquer elo dessa cadeia falhar — o sinal do DSP, o driver, o relé em si ou o cabeamento do circuito de backup — a carga não migra.

O que a gente encontra com mais frequência na bancada:

1. Relé de transferência EPS com contatos oxidados ou soldados em posição aberta — não fecha mesmo com o sinal de drive aplicado
2. Transistor driver danificado — o relé recebe tensão de alimentação mas o sinal de acionamento está ausente na medição
3. EPS não habilitado nos parâmetros — instalador configurou o sistema mas não ativou a função no menu do Shine App
4. SOC da bateria abaixo do limiar mínimo configurado — o inversor bloqueia o EPS mesmo com bateria disponível porque o threshold está alto
5. Falha de comunicação CAN/RS485 com o BMS — o inversor não confirma estado da bateria e bloqueia o backup por segurança
6. Carga conectada no terminal errado — o circuito de backup está ligado no terminal Grid em vez do terminal EPS

Cada um desses pontos exige uma abordagem diferente. Não existe atalho.

## Como identificar na prática

O diagnóstico começa pela leitura de parâmetros antes de abrir o equipamento.

1. Acessar o ShinePhone ou o ShineServer e verificar se a função EPS está habilitada
2. Checar o SOC atual da bateria e o limite mínimo de EPS configurado — se o threshold estiver em 50% e a bateria em 45%, o inversor não comuta por design
3. Ler o histórico de alarmes — o inversor registra "EPS Fault" ou "BMS Fault" quando bloqueia a comutação por segurança
4. Com a rede presente, medir tensão no terminal EPS output — não deve haver tensão em modo normal; tensão presente indica curtocircuito no relé
5. Simular queda de rede desligando o disjuntor CA e medir o terminal EPS output — deve aparecer a tensão de saída da bateria convertida para CA em menos de 20 ms
6. Se não comutar, medir resistência da bobina do relé EPS — valores entre 50 Ω e 200 Ω são típicos para esses modelos; resistência infinita confirma bobina aberta
7. Com a simulação de queda ativa, medir tensão de acionamento no relé — ausência de tensão aponta o driver como culpado
8. Verificar com osciloscópio o sinal de saída do DSP para o driver — se o sinal PWM está presente mas o driver não responde, o transistor de acionamento está com defeito ou em curto

Essa última medição leva dois minutos numa bancada equipada. Ela separa dois diagnósticos completamente diferentes: problema no driver versus problema no DSP.

## O erro mais comum do mercado

O diagnóstico errado mais frequente é culpar a bateria ou o BMS sem medir o relé. A lógica é: sistema não entra em backup, bateria deve ter problema. O técnico substitui o BMS ou conclui que a bateria está deteriorada — e o problema persiste.

O relé de transferência EPS raramente é medido porque parece simples demais para ser culpado. Mas é exatamente ele que falha depois de centenas de comutações. Em regiões do Nordeste e do interior de Minas Gerais, onde quedas de rede são frequentes, esse relé opera mais ciclos em seis meses do que a média dos inversores on-grid em dois anos.

Cargas reativas mal dimensionadas — ar-condicionado, motores pequenos — criam pico de corrente no momento da comutação que acelera o desgaste dos contatos. Com o tempo, oxidação e marcas de arco reduzem a capacidade de condução até o ponto em que o relé não fecha mais.

Substituir o relé sem medir o driver é outro erro. Se o transistor driver está com fuga de corrente, o novo relé vai falhar no mesmo ciclo.

## Quando o reparo é viável

Na maior parte dos casos com esse sintoma, o reparo compensa. O relé de transferência EPS tem referência disponível para reposição direta nos modelos SPH da Growatt. O transistor driver e o optocoupler são componentes discretos de custo baixo, presentes em distribuidores nacionais.

O critério técnico é direto: se a placa de potência principal está íntegra — IGBT, capacitor de barramento e indutor sem danos — o reparo do circuito de backup é economicamente viável. Um Growatt SPH novo custa entre R$ 4.000 e R$ 8.000 dependendo da potência. Um reparo de driver e relé fica em fração disso, mesmo com bancada especializada.

A inviabilidade aparece em dois cenários específicos: o relé fundiu sob carga acoplada e gerou sobretensão que danificou o IGBT; ou o DSP da placa de controle perdeu o firmware por corrupção durante uma atualização mal executada. O segundo caso é raro, mas acontece, e a placa de controle dificilmente tem recuperação simples.

Fora esses dois cenários, o inversor tem conserto.

## Conclusão

Growatt Híbrido que não comuta para EPS na queda de rede não é necessariamente um inversor morto. Na maior parte das vezes é um relé, um transistor driver ou um parâmetro não configurado.

O problema é que essa falha só aparece quando a energia cai de verdade. E quando aparece, não tem tempo para diagnóstico calmo.

Antes de condenar o equipamento — ou pior, de comprar um inversor novo — mande para a bancada. Um diagnóstico em nível de placa mostra exatamente o que falhou.

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

- Âncora: 'falha de comunicação CAN/RS485 com o BMS' → URL: /inversor-sumiu-do-app-monitoramento → Contexto: H2 "O que causa esse problema", item 5 da lista
- Âncora: 'transistor driver está com defeito' → URL: /driver-gate-igbt-funcao-modos-falha → Contexto: H2 "Como identificar na prática", penúltimo parágrafo
- Âncora: 'relé de rede e relé de bypass' → URL: /rele-rede-rele-bypass-falha-silenciosa → Contexto: H2 "O erro mais comum do mercado", contexto geral de relés
- Âncora: 'Erro de Bateria' → URL: /growatt-sph-hibrido-erro-bateria-batvolthigh-low → Contexto: H2 "O que causa esse problema", mencionar BMS e SOC

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "tensão CA cai abaixo do limite configurado" → URL: https://www.aneel.gov.br/modulo-8 → Fonte: ANEEL — Módulo 8, Qualidade da Energia Elétrica (padrões de tensão e frequência da rede)
- Texto âncora: "menos de 20 ms" → URL: https://www.iec.ch/homepage → Fonte: IEC 62109-2 — norma de segurança para inversores solares, tempo de resposta EPS

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Painel de controle eletrônico com circuito integrado, representa diagnóstico de placa de inversor
→ Nome do arquivo: growatt-hibrido-falha-eps-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Diagnóstico de placa de inversor híbrido Growatt com falha no modo EPS — bancada técnica eletrônica
→ Legenda: Fig. 1 — Diagnóstico em nível de placa: o relé de transferência EPS é o componente mais comum de falha nesse sintoma
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Instalação de painel solar fotovoltaico em residência, contexto de sistema híbrido com backup
→ Nome do arquivo: growatt-hibrido-falha-eps-sistema-backup-2.webp
→ Alt Text (máx. 125 caracteres): Sistema fotovoltaico híbrido residencial com inversor Growatt e bateria — falha no modo EPS de backup
→ Legenda: Fig. 2 — Sistema híbrido com backup: a falha no relé EPS impede a comutação automática na queda de rede
→ Onde inserir: Após H2 "Como identificar na prática"
