[PALAVRA-CHAVE FOCO]
---
Deye F18 corrente de fuga CA alta

[TÍTULO SEO — Title Tag]
---
Deye F18: Corrente de Fuga CA Alta — Como Localizar

[SLUG — URL do Post]
---
deye-f18-corrente-de-fuga-ca-alta

[META DESCRIPTION]
---
Erro F18 no inversor Deye indica corrente de fuga CA alta. Saiba como identificar se o problema está no cabeamento, filtro EMI ou placa interna.

[CATEGORIA]
---
Códigos de Erro e Falhas

[TAGS]
---
Deye F18, corrente de fuga CA, falha de isolamento inversor, filtro EMI inversor solar, diagnóstico inversor Deye

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]
---

# Post 55 — Deye F18: Corrente de Fuga CA Alta — Como Localizar o Ponto de Falha

O **Deye F18** é um código de proteção ativo: o inversor detectou corrente de fuga CA acima do limiar permitido e desligou o sistema para evitar risco elétrico. Não é pane. É o circuito de segurança funcionando como foi projetado para funcionar.

O problema começa quando o instalador ou o técnico assume que o inversor está morto e parte direto para a substituição. Esse caminho é caro, frequentemente desnecessário, e não resolve nada se a causa estiver fora do equipamento.

Na nossa bancada, boa parte dos Deye que chegam com F18 tem o cabeamento CA como culpado. Inversores instalados em obras onde o eletricista apertou o grampo de fixação demais, deixou a fiação com dobra forçada dentro da calha metálica, ou usou conector de qualidade duvidosa nas emendas de saída. O inversor está saudável. O isolamento do cabo é que cedeu.

## O que causa o F18 no inversor Deye

O circuito interno do Deye monitora continuamente a soma vetorial das correntes nas fases de saída. Num sistema sem fuga, essa soma é praticamente zero. Quando parte da corrente escapa para o condutor de terra (PE) por caminhos não previstos, o desequilíbrio é detectado e o F18 é acionado.

A norma IEC 62109-1 — Safety for power converters for use in photovoltaic power systems — define que inversores devem interromper a operação quando a corrente residual excede 300 mA por mais de 300 ms. O Deye segue esse parâmetro, com faixa ajustável via parâmetro interno de fábrica dependendo da versão de firmware.

As origens mais frequentes do F18:

- **Capacitores Y degradados no filtro EMI interno** — conectam as linhas de fase ao terra para filtragem de ruído de modo comum. Com ciclos térmicos repetidos, a resistência de isolamento desses componentes cai e a corrente que escapa para o PE aumenta progressivamente. Em inversores com mais de 5 anos de operação em ambiente quente, é a causa mais comum.
- **Isolamento do cabo CA danificado** — pontos de dobra forçada, compressão por grampos metálicos ou marcas de roedores no cabeamento de saída. Especialmente problemático em calhas metálicas sem aterramento adequado.
- **Infiltração de umidade no quadro de distribuição ou caixa de saída CA** — água condensada nos terminais cria caminho resistivo entre fase e terra. Inversores no litoral nordestino — Fortaleza, Salvador, Maceió — chegam com esse padrão com frequência nos meses de alta umidade relativa.
- **Contaminação interna da placa de potência** — poeira condutiva, resíduos de fluxo de solda ou umidade acumulada na placa criam trilhas de fuga que o circuito detecta antes que o dano seja visível ao olho.
- **Capacitor X com curto parcial** — falha mais severa, pode gerar corrente de fuga acima de 1 A e causar sobreaquecimento em componentes adjacentes se não detectado a tempo.
- **Terminais CA soltos ou oxidados na placa de bornes interna** — conexão com resistência elevada gera calor localizado, que degrada o isolamento do invólucro plástico do próprio conector.

Isso significa que a fuga pode estar completamente fora do inversor.

## Como identificar na prática

Antes de qualquer medição, o inversor precisa estar completamente isolado — CC e CA desligados. O processo de rastreamento vai do externo para o interno:

1. Desligar o disjuntor CA de saída do inversor. Isolar fisicamente o lado AC.
2. Com megohmmeter em 500 V CC, medir a resistência de isolamento entre cada fase (L1, L2, L3) e o terra (PE), direto nos bornais CA do inversor. Valor aceitável: acima de 1 MΩ. Abaixo de 100 kΩ — fuga severa, continuar o rastreamento.
3. Se a medição nos bornais estiver ok, medir nos terminais do quadro de distribuição. Isolar progressivamente cada segmento do cabeamento até identificar qual trecho tem resistência baixa.
4. Inspecionar visualmente todos os terminais CA: marcas de carbonização, oxidação nos parafusos, sinal de umidade ou condensação.
5. Se a fuga estiver no inversor: abrir o gabinete e inspecionar o módulo de filtro EMI — capacitores Y com barriga, marcas escuras ou odor característico de componente sobreaquecido.
6. Medir cada capacitor Y fora do circuito com capacímetro. Verificar resistência de isolamento individual — qualquer capacitor Y com corrente de fuga acima de 100 µA sob 500 V é candidato à substituição.
7. Inspecionar visualmente a placa de potência por sinais de contaminação, trilhas com carbonização ou depósito de poeira condutiva.

O sinal que mais frequentemente antecede o F18 é o disjuntor diferencial residual (DR) disparando de forma intermitente, às vezes semanas antes do código aparecer no display. Se o instalador relatar que o DR "às vezes disparava", a fuga está no sistema há mais tempo do que parece — e pode ter gerado dano secundário.

## O erro mais comum do mercado

O inversor chega na bancada com laudo de "defeito interno irreparável". Abrimos, medimos, e o hardware está intacto. A fuga estava no cabo de saída, num ponto de compressão dentro da calha metálica. Isso acontece mais do que o mercado admite.

Há também quem substitua os capacitores Y sem investigar por que eles degradaram antes do prazo. Se a instalação está em telhado de telha metálica sem isolamento térmico — situação comum no Norte e Nordeste, com temperatura interna facilmente acima de 70°C no pico do verão — os capacitores novos vão durar menos que os originais. Trocar sem resolver a causa é garantia de reincidência.

## Quando o reparo é viável

A viabilidade depende de onde a fuga está:

- **Fuga no cabeamento externo** — troca de cabo ou reposicionamento do segmento com isolamento danificado. Custo de material. Não precisa de bancada.
- **Capacitores Y no filtro EMI** — reparo de baixo custo. Componentes acessíveis, trabalho de dessoldagem e substituição na placa de filtro. Custo total tipicamente entre R$ 300 e R$ 600, incluindo laudo e teste de bancada.
- **Contaminação da placa por poeira ou umidade** — limpeza ultrassônica, secagem em estufa e aplicação de verniz conformal. Custo moderado.
- **Capacitor X com curto parcial e dano em componentes adjacentes** — depende da extensão. Se o curto gerou sobreaquecimento em MOSFETs ou no circuito de gate drive próximo, a análise se expande e o custo sobe proporcionalmente.
- **Dano extenso na placa de potência** — menos frequente no F18 isolado, mas acontece quando a falha ficou sem diagnóstico por período prolongado.

Um Deye 5 kW fora de garantia custa, no mercado secundário, entre R$ 2.000 e R$ 3.500. O reparo de F18 por capacitores Y fica tipicamente em R$ 400 a R$ 800 com laudo e teste de carga. A diferença compensa o envio via logística reversa.

## Conclusão

F18 é proteção ativa, não morte do equipamento. O que determina o custo não é o código de erro — é quanto tempo o sistema ficou com a fuga antes de alguém investigar com um megohmmeter.

Comece pelo cabeamento. Se a fuga não está no externo, aí você abre o inversor.

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

[LINKS INTERNOS SUGERIDOS]
---
- Âncora: 'capacitores Y degradados no filtro EMI' → URL: /capacitores-eletrolíticos-inversores-vida-util-degradacao-quando-trocar → Contexto: H2 "O que causa o F18", primeiro item da lista de causas
- Âncora: 'placa de controle vs. placa de potência' → URL: /placa-de-controle-vs-placa-de-potencia-onde-esta-o-defeito → Contexto: H2 "Quando o reparo é viável", ao mencionar dano na placa de potência
- Âncora: 'inversor fora de garantia' → URL: /inversor-fora-de-garantia-trocar-ou-reparar → Contexto: H2 "Quando o reparo é viável", ao mencionar custo de inversor fora de garantia
- Âncora: 'corrente de fuga' → URL: /sungrow-gfci-fault-corrente-de-fuga-terra-painel-isolamento → Contexto: Introdução, ao mencionar corrente de fuga como conceito técnico
- Âncora: 'logística reversa' → URL: /logistica-reversa-equipamento-eletronico-brasil → Contexto: H2 "Quando o reparo é viável", última linha sobre envio

[LINKS EXTERNOS SUGERIDOS]
---
- Texto âncora: "IEC 62109-1" → URL: https://www.iec.ch/homepage → Fonte: IEC — International Electrotechnical Commission
- Texto âncora: "corrente residual excede 300 mA" → URL: https://www.aneel.gov.br/resolucoes-normativas → Fonte: ANEEL — Agência Nacional de Energia Elétrica

[IMAGEM PRINCIPAL — USE ESTA]
---
IMAGEM PRINCIPAL:
→ URL para download: https://unsplash.com/s/photos/solar-inverter-electrical-test (buscar: técnico medindo inversor solar com multímetro)
→ Por que foi escolhida: representa diagnóstico elétrico em equipamento de energia solar, contexto direto do post
→ Nome do arquivo: deye-f18-corrente-de-fuga-ca-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Técnico realizando diagnóstico de corrente de fuga CA em inversor solar Deye com megohmmeter
→ Legenda: Fig. 1 — Medição de resistência de isolamento no lado CA do inversor: primeiro passo para rastrear o F18
→ Onde inserir: Topo do post, antes da introdução

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]
---
IMAGEM SECUNDÁRIA:
→ URL para download: https://unsplash.com/s/photos/electrical-cable-wiring-inspection (buscar: inspeção de cabeamento elétrico, fios CA)
→ Por que foi escolhida: representa o cabeamento CA de saída — primeiro ponto de verificação no rastreamento do F18
→ Nome do arquivo: deye-f18-cabeamento-ca-isolamento-2.webp
→ Alt Text (máx. 125 caracteres): Cabeamento elétrico CA com isolamento inspecionado em instalação solar — rastreamento de falha de fuga
→ Legenda: Fig. 2 — Inspeção do isolamento do cabeamento CA: ponto de partida antes de abrir o inversor
→ Onde inserir: Após H2 "Como identificar na prática"
