# Post 128 — Ponte retificadora e estágio de entrada CC: diagnóstico do front-end do inversor

---

[PALAVRA-CHAVE FOCO]
diagnóstico estágio entrada CC inversor solar

---

[TÍTULO SEO — Title Tag]
Estágio de Entrada CC: Diagnóstico do Front-End do Inversor

---

[SLUG — URL do Post]
estagio-entrada-cc-diagnostico-front-end-inversor

---

[META DESCRIPTION]
Ponte retificadora, MOSFETs, varistores e capacitores de filtro: como diagnosticar o front-end do inversor solar na bancada.

---

[CATEGORIA]
Análise Técnica de Componentes

---

[TAGS]
estágio de entrada CC inversor solar, ponte retificadora inversor, diagnóstico front-end inversor, varistor MOV inversor solar, MOSFET entrada inversor

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **estágio de entrada CC** é o primeiro ponto de contato entre os painéis fotovoltaicos e o circuito interno do inversor. É aqui que a energia da string encontra a eletrônica de potência — e onde uma parcela relevante das falhas se origina, antes mesmo de chegar ao estágio de saída.

Na nossa bancada, o padrão é conhecido: chega um inversor condenado por "placa de potência queimada". A gente abre, vai para o front-end, e encontra um varistor estourado, um MOSFET de entrada em curto, ou um capacitor de filtro com ESR alto. Nenhum deles é a placa de potência. E nenhum deles obriga a substituição do inversor.

O estágio de entrada não recebe quase nenhuma atenção nos diagnósticos de campo. Isso tem custo.

## O que causa falha no estágio de entrada CC

O front-end de um inversor solar opera em condições severas. A tensão CC vinda dos painéis pode variar de 150V a mais de 1.000V, dependendo do modelo e da configuração da string. Essa variação, somada aos picos de tensão gerados por indutância parasita durante o chaveamento dos IGBTs internos, cria stress contínuo nos semicondutores do estágio de entrada.

As causas mais frequentes que chegam até nós:

1. Surto de tensão por descarga atmosférica — o pico entra pela string CC, ultrapassa a capacidade dos varistores (MOVs) de proteção e destrói diodos ou MOSFETs de entrada antes que qualquer proteção reaja
2. Polaridade invertida durante a instalação — CC+ e CC- trocados destroem os diodos anti-retorno em milissegundos, sem cheiro, sem fumaça visível, sem marca óbvia em alguns modelos
3. Sobretensão de string por subdimensionamento — string configurada acima do Voc máximo declarado pelo fabricante, especialmente em dias frios quando a tensão dos painéis sobe além do ponto de projeto
4. Corrente reversa por falha em cascata — quando o IGBT do estágio de saída falha primeiro, a corrente reversa destrói o front-end como segundo evento; o técnico de campo encontra dois defeitos e não entende a sequência
5. Degradação térmica por ventilador com folga — o dissipador compartilhado perde eficiência gradualmente, e o capacitor de barramento CC degrada antes de qualquer componente mais visível
6. Conector MC4 com resistência elevada — arcos elétricos intermitentes injetam picos de tensão que danificam o circuito de medição de corrente, em especial shunts e sensores Hall
7. Ausência de SPD na string CC — sem dispositivo de proteção contra surto no quadro CC, qualquer descarga atmosférica chega direto ao front-end sem amortecimento

Esse último ponto é crítico em regiões como o Triângulo Mineiro, o interior da Bahia e o Mato Grosso do Sul, onde a incidência de raios está entre as mais altas do Brasil. A gente recebe inversores com menos de dois anos de uso, front-end destruído, e a instalação sem nenhuma proteção CC. A falha era previsível.

## Como identificar na prática

O diagnóstico do estágio de entrada começa antes de conectar qualquer equipamento de medição. Inspeção visual primeiro, sempre.

Sinais físicos mais comuns:
- Varistor (MOV) com corpo estourado, escurecido ou com respingo de material ao redor no PCB
- Fusível CC aberto — teste de continuidade confirma em segundos
- Capacitor de filtro CC com topo abaulado ou eletrólito extravasado pela base
- Trilha queimada na região entre os terminais CC e o circuito MPPT
- MOSFET de entrada com marca de calor localizado ou corpo craterizado

Sequência de verificação na bancada:

1. Descarregar os capacitores internos antes de tocar em qualquer ponto — o barramento CC de 600V ou 1.000V armazena energia letal mesmo com o equipamento desligado e desconectado
2. Medir resistência entre CC+ e CC- com o inversor desconectado; leitura abaixo de 100Ω indica curto nos capacitores ou nos MOSFETs de entrada
3. Testar cada diodo do estágio em modo diodo do multímetro — queda esperada entre 0,4V e 0,7V; leitura zero confirma curto; OL indica diodo aberto
4. Medir varistores: resistência alta em condição normal (megaohms); leitura baixa confirma saturação
5. Verificar fusíveis CC com continuidade
6. Medir capacitância e ESR com medidor dedicado — ESR elevado é o sinal mais importante de degradação, mesmo em capacitor com aparência física normal
7. Checar o divisor resistivo do circuito de medição de tensão CC — resistores abertos causam leitura zero de tensão no display sem falha nos semicondutores de potência

## Quando é falha eletrônica interna

Nem toda falha no front-end indica defeito de fabricação. Quando o varistor abre por surto, ele funcionou exatamente como foi projetado — sacrificou-se para proteger o estágio de potência. A causa é externa.

A falha é interna quando:

- O MOSFET falhou sem histórico de surto e com a string dentro do Voc máximo declarado no datasheet
- O capacitor de barramento CC degradou antes da vida útil estimada, com o inversor operando dentro das condições de temperatura especificadas pelo fabricante
- O circuito de controle MPPT não responde mesmo com os semicondutores de potência íntegros e com tensão CC presente
- A placa perdeu leitura de tensão ou corrente CC por falha no divisor resistivo ou no sensor Hall, sem causa externa identificável

Essa distinção muda completamente o encaminhamento. Trocar o varistor sem instalar SPD na string é garantia de reincidência. O tempo até a próxima descarga atingir o ponto — meses ou anos — depende da localização e da frequência de tempestades. Não existe resposta padrão para isso.

## Vale a pena consertar?

Varistor ou fusível: componente abaixo de R$30, trabalho de bancada de menos de uma hora. Sempre viável.

Capacitor de barramento CC: entre R$80 e R$380 dependendo da capacitância e da tensão de trabalho. O procedimento inclui descarga segura do barramento, substituição e teste funcional completo. Viável na grande maioria dos casos.

MOSFET ou diodo de entrada: componente de R$20 a R$150. A dificuldade está em verificar se o gate driver do MOSFET também não foi danificado no mesmo evento — falhar nessa verificação garante reincidência em semanas. Reparável com bancada e instrumentação adequadas.

Dano em trilha de PCB por corrente de curto elevada: aqui o cenário muda. Trilhas de entrada de inversores de alta potência carregam dezenas de amperes em operação normal. Reconstrução sem os materiais corretos — fio de cobre com seção adequada, solda e processo de alta corrente — não sustenta a operação contínua.

O que a gente vê com frequência: técnico troca o componente queimado mais óbvio sem diagnosticar o causador. Seis semanas depois, o mesmo ponto falha de novo. O componente causador permaneceu no circuito.

O estágio de entrada não é onde a maioria dos técnicos começa o diagnóstico. É onde deveriam começar.

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

- Âncora: 'por que os IGBTs queimam' → URL: /por-que-os-igbts-queimam-em-inversores-solares → Contexto: Seção "O que causa falha no estágio de entrada CC", ao mencionar corrente reversa por falha de IGBT
- Âncora: 'fusível CC e varistor (MOV)' → URL: /fusivel-cc-varistor-mov-protecao-inversor → Contexto: Seção "O que causa falha no estágio de entrada CC", ao citar varistor e fusível como proteção do front-end
- Âncora: 'capacitor de barramento CC' → URL: /capacitor-barramento-cc-degradacao-esr-alto-quando-trocar → Contexto: Seção "Vale a pena consertar?", ao mencionar substituição do capacitor de barramento
- Âncora: 'sensor de corrente' → URL: /sensor-de-corrente-shunt-efeito-hall-leitura-falsa-diagnostico → Contexto: Seção "Como identificar na prática", ao citar shunts e sensores Hall no circuito de medição
- Âncora: 'driver de gate' → URL: /driver-de-gate-do-igbt-funcao-modos-de-falha-diagnostico → Contexto: Seção "Vale a pena consertar?", ao mencionar o gate driver do MOSFET como segundo componente afetado

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "Voc máximo declarado no datasheet" → URL: https://www.iec.ch/homepage → Fonte: IEC — International Electrotechnical Commission (norma IEC 62109 sobre segurança de conversores de potência para sistemas fotovoltaicos)
- Texto âncora: "dispositivo de proteção contra surto" → URL: https://www.aneel.gov.br → Fonte: ANEEL — Agência Nacional de Energia Elétrica (regulamentação de conexão de sistemas fotovoltaicos e proteção de instalações)

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=1200
→ Por que foi escolhida: Placa de circuito eletrônico com componentes de potência visíveis — representa diretamente o front-end do inversor solar em nível de componente
→ Nome do arquivo: estagio-entrada-cc-inversor-solar.webp
→ Alt Text (máx. 125 caracteres): Placa de front-end de inversor solar com MOSFET, capacitor e varistor de entrada para diagnóstico técnico
→ Legenda: Fig. 1 — Estágio de entrada CC: componentes de proteção e medição do front-end do inversor
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1498084393753-b411b2d26b34?w=1200
→ Por que foi escolhida: Técnico com multímetro realizando medição em equipamento eletrônico — representa o processo de diagnóstico de diodos e varistores na bancada
→ Nome do arquivo: diagnostico-front-end-inversor-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo componentes do estágio de entrada CC do inversor solar com multímetro na bancada
→ Legenda: Fig. 2 — Diagnóstico do estágio de entrada: teste de diodos, varistores e capacitores com multímetro e medidor de ESR
→ Onde inserir: Após H2 "Como identificar na prática"
