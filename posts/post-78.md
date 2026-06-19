# Post 78 — Transformadores de Corrente (CT) em Inversores Solares: Defeitos e Diagnóstico

---

[PALAVRA-CHAVE FOCO]

transformador de corrente CT inversor solar defeito diagnóstico

---

[TÍTULO SEO — Title Tag]

Transformadores de Corrente (CT) em Inversores Solares: Diagnóstico

---

[SLUG — URL do Post]

transformadores-de-corrente-ct-inversores-solares-defeito-diagnostico

---

[META DESCRIPTION]

Defeito em transformador de corrente (CT) em inversor solar: saturação do núcleo, secundário aberto e impacto na placa de controle. Como diagnosticar.

---

[CATEGORIA]

Análise Técnica de Componentes

---

[TAGS]

transformador de corrente CT inversor solar, saturação de núcleo CT, diagnóstico de placa inversor, defeito de medição inversor solar, reparo eletrônico inversor

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

# Post 78 — Transformadores de Corrente (CT) em Inversores Solares: Defeitos e Diagnóstico

**Transformadores de corrente em inversores solares** são componentes que custam entre R$ 8 e R$ 80 e raramente entram no diagnóstico de campo. Quando o técnico vê erro de overcurrent sem carga excessiva, ou leitura de potência abaixo do esperado sem causa aparente, o caminho natural é ir para o IGBT, para o capacitor do barramento, para a placa de potência. O CT fica para o final — ou nem entra na lista.

Na nossa bancada, o padrão se repete com frequência suficiente para virar regra: o inversor chega com diagnóstico de "placa de potência com defeito" feito no campo. IGBT: intacto. Tensão no barramento DC: normal. Fusíveis: bons. Medimos o CT e encontramos núcleo saturado ou secundário em circuito aberto. O problema estava ali desde o começo.

## O que causa esse problema

O transformador de corrente (CT) tem função crítica nos inversores solares: mede a corrente CA de saída com precisão para alimentar os circuitos de proteção e o controle do MPPT. Nos inversores on-grid sem transformador de isolamento — que são a maioria dos modelos residenciais e comerciais hoje em dia — o CT também detecta componente CC na corrente de saída, que é vedada pelas normas ABNT NBR 16149 e IEC 61000-3-2 e pode danificar transformadores da rede pública.

A saturação magnética é a causa mais frequente. Quando a corrente de entrada supera a capacidade linear do núcleo ferromagnético, a relação de transformação perde a proporcionalidade e o sinal de saída distorce. Harmônicos gerados por cargas não-lineares na rede e componente CC elevada no output do inversor são os principais aceleradores do processo — e a saturação permanente do núcleo toroidal não reverte sozinha.

Outras causas que chegam na bancada:

- Circuito aberto no secundário — gera tensão induzida que pode superar 150 V em CTs de relação 1000:1 com carga de 20 A; essa tensão destrói o circuito de medição na placa de controle antes de qualquer fusível atuar
- Curto no secundário — zera a leitura de corrente; o inversor opera sem proteção de overcurrent efetiva sem apresentar erro claro
- Deterioração do isolamento por umidade — mais comum em inversores instalados sem proteção adequada no litoral e em regiões do Norte e Nordeste com umidade relativa acima de 80%
- Vibração mecânica persistente — inversores em telhados metálicos de galpões industriais são mais vulneráveis; a vibração solta a fixação física do CT e gera leitura instável antes da falha total
- Microfissuras no núcleo ferrita — resultado de ciclos térmicos intensos em equipamentos com mais de 7 anos em operação
- Transitório de corrente na energização — sistemas com gerador a diesel como backup são particularmente vulneráveis; o transitório de partida pode saturar permanentemente o núcleo em um único evento

## Como identificar

O diagnóstico começa com uma comparação direta: corrente medida no cabo de saída com alicate amperímetro calibrado versus o valor que o inversor está reportando no display ou no software de monitoramento.

Sequência de verificação:

1. Consultar o histórico de erros do inversor — erros de overcurrent sem carga excessiva confirmada no lado CA são o indicador mais frequente
2. Medir a corrente CA de saída com alicate amperímetro calibrado
3. Comparar com o valor reportado pelo inversor — divergência acima de 5% já aponta para problema no CT ou no circuito de condicionamento de sinal
4. Com o inversor desligado e o secundário do CT desconectado da placa: medir resistência do secundário com multímetro — circuito aberto ou valor fora do especificado no datasheet confirmam falha
5. Verificar continuidade da fiação entre o CT e o conector na placa de controle — solda fria em conector subminiatura é causa real, especialmente após manuseio em campo
6. Verificar presença de umidade, oxidação ou resíduo branco no corpo do CT e nas proximidades do conector
7. Em bancada com osciloscópio: injetar sinal AC de teste na janela do CT e verificar se o sinal de saída é proporcional e sem distorção harmônica
8. Observar comportamento por faixa de carga: se o inversor opera normalmente até 60-70% da potência nominal mas falha acima disso, saturação parcial do núcleo é o primeiro suspeito

Esse último padrão — falha intermitente acima de uma determinada carga — é o que mais confunde o diagnóstico no campo, porque em medição rápida sem carga o inversor parece completamente normal.

## Quando é falha eletrônica interna

A distinção entre problema externo — fiação, conector solto — e falha interna no CT nem sempre é evidente. O circuito aberto no secundário, porém, deixa uma assinatura clara na placa.

Sem carga conectada ao secundário, o CT se comporta como um indutor em série com a linha primária. A tensão induzida é proporcional ao número de espiras e à corrente primária. O circuito de condicionamento de sinal da placa de controle — projetado para trabalhar com sinais de 0 a 3,3 V — não sobrevive a essa tensão. O dano é localizado, rápido e sem sinal visual óbvio: nenhuma marca de queima evidente, nenhum odor característico.

Quando a placa de controle chega na bancada com queima localizada na seção de medição de corrente, a primeira pergunta é: qual era o estado do CT que alimentava esse canal?

A saturação permanente do núcleo não é detectável com multímetro convencional. Exige injeção de sinal AC controlado e análise da linearidade da resposta do CT isolado do circuito. Não existe teste de campo confiável para diferenciar saturação temporária de permanente — e esse ponto ainda não tem solução simples.

## Vale a pena consertar?

O CT em si é um componente de custo baixo. O problema é a especificação.

Inversores das principais marcas — Growatt, Sungrow, Deye, Fronius, WEG — utilizam CTs com parâmetros customizados que não aparecem em catálogos abertos: relação de transformação específica (1000:1, 2500:1), frequência de corte, carga resistiva do secundário (burden resistor calibrado para a entrada do ADC). Substituir por um CT genérico de mesma corrente nominal sem confirmar esses parâmetros resulta em leitura descalibrada. O inversor vai continuar apresentando erros mesmo com o CT novo instalado.

O reparo exige:

- Identificar o CT com referência cruzada no esquema da placa de controle
- Confirmar a relação de transformação e o valor exato do burden resistor no secundário
- Verificar se a placa de controle foi danificada pelo CT com defeito — se o circuito de medição foi destruído por tensão de secundário aberto, o CT novo não resolve sem reparar a placa também
- Em alguns modelos, o CT é integrado em posição que exige retrabalho de SMD — o que muda a estimativa de tempo de bancada

O custo de diagnóstico e substituição do CT, somado à verificação da placa de controle, raramente ultrapassa 15% do valor de um inversor novo. Quando o campo condena o equipamento sem investigar esse componente, o prejuízo é duplo: financeiro e técnico. Um diagnóstico errado que vira referência para os próximos casos.

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

- Âncora: 'placa de controle vs. placa de potência' → URL: /placa-controle-vs-placa-potencia-como-diferenciar-defeito → Contexto: seção "Quando é falha eletrônica interna", ao mencionar que queima localizada na seção de medição aponta para dano causado pelo CT com defeito
- Âncora: 'inversores on-grid sem transformador de isolamento' → URL: /inversor-on-grid-vs-off-grid-os-defeitos-sao-diferentes → Contexto: seção "O que causa esse problema", explicando por que esses inversores dependem do CT para detecção de CC
- Âncora: 'diagnóstico eletrônico completo em nível de componente' → URL: /o-que-e-diagnostico-nivel-placa-por-que-muda-tudo-reparo → Contexto: bloco CTA, reforçando a proposta de valor da bancada
- Âncora: 'Por que os IGBTs queimam em inversores solares' → URL: /por-que-igbts-queimam-inversores-solares → Contexto: introdução, ao citar que o técnico vai primeiro para o IGBT antes de investigar o CT

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16149" → URL: https://www.abnt.org.br → Fonte: ABNT — norma que regulamenta as características de interfaces de conexão de sistemas fotovoltaicos à rede de distribuição de energia elétrica, incluindo limitação de injeção de componente CC
- Texto âncora: "IEC 61000-3-2" → URL: https://www.iec.ch/homepage → Fonte: IEC — norma internacional que limita as emissões de harmônicos de corrente em equipamentos conectados à rede pública de baixa tensão

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1562408590-e32931084e23
→ Por que foi escolhida: placa de circuito eletrônico com componentes de medição visíveis, representando a placa de controle do inversor onde o CT injeta o sinal de corrente
→ Nome do arquivo: transformador-corrente-ct-inversor-solar-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Placa de controle de inversor solar com circuito de medição de corrente — diagnóstico de falha em transformador de corrente CT
→ Legenda: Fig. 1 — Circuito de medição de corrente na placa de controle: o CT injeta sinal proporcional à corrente CA; falha nesse componente distorce toda a leitura do inversor
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092162384-8987c1d64718
→ Por que foi escolhida: técnico realizando medições com multímetro em componentes eletrônicos, representando a verificação de resistência do secundário do CT descrita na sequência de diagnóstico
→ Nome do arquivo: transformador-corrente-ct-medicao-resistencia-secundario.webp
→ Alt Text (máx. 125 caracteres): Medição de resistência no secundário do transformador de corrente CT de inversor solar com multímetro em bancada de diagnóstico
→ Legenda: Fig. 2 — Diagnóstico do CT: medição de resistência do secundário com inversor desligado é o primeiro passo para confirmar circuito aberto ou curto no transformador de corrente
→ Onde inserir: Após H2 "Como identificar"
