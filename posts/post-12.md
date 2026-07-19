# Post 12 — Growatt Erro 103: Falha de Aterramento — quando o problema está no cabo e quando está na placa

---

## [PALAVRA-CHAVE FOCO]

growatt erro 103 falha de aterramento

---

## [TÍTULO SEO — Title Tag]

Growatt Erro 103: falha de aterramento — diagnóstico

---

## [SLUG — URL do Post]

growatt-erro-103-falha-aterramento

---

## [META DESCRIPTION]

Growatt Erro 103 pode ser cabo, conector, painel ou placa de medição. Saiba como diagnosticar e separar causa externa de falha eletrônica interna.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Growatt Erro 103, falha de aterramento inversor, diagnóstico inversor Growatt, resistência de isolamento fotovoltaico, GFDI inversor solar

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Growatt Erro 103** no display, inversor travado, geração zerada. O código aponta falha de aterramento — mas isso pode ser qualquer ponto do sistema: cabo CC danificado, conector MC4 com umidade, módulo com isolamento comprometido, ou o próprio circuito de medição do inversor falhando e gerando alarme falso.

Na nossa bancada, esse erro chega com uma história quase sempre igual: integrador fez a instalação, sistema funcionou por algumas semanas, chuva chegou, e o 103 apareceu. No Norte e Nordeste do Brasil, a combinação de calor e umidade acelera a deterioração de isolamento de forma considerável — e boa parte desses inversores chega até nós com o rótulo de "placa queimada" sem que alguém tenha medido a resistência de isolamento do string antes.

Este post cobre a causa raiz do Erro 103, o processo de diagnóstico e o que diferencia causa externa de falha eletrônica interna.

---

## O que causa o Erro 103 no Growatt

O Growatt Erro 103 indica que a resistência de isolamento entre o barramento CC do string e o condutor de proteção (PE) caiu abaixo do limiar operacional. O valor padrão é 1 MΩ, conforme a IEC 62109-2, norma que define os requisitos de proteção GFDI (Ground Fault Detection and Interruption) para inversores fotovoltaicos. Quando esse parâmetro cai, o circuito de detecção bloqueia a operação automaticamente.

O inversor mede essa impedância continuamente por um divisor resistivo interno conectado ao DSP. Qualquer caminho de fuga que reduza essa impedância dispara o erro.

As causas mais frequentes na bancada:

1. **Cabo CC com isolamento degradado** — UV prolongado, atrito com borda de calha metálica ou dano por roedor. Cabos solares XLPE instalados sem calha em regiões do Nordeste, onde a irradiância pode passar de 6,5 kWh/m²/dia e a temperatura de superfície da calha ultrapassa 60°C no verão, envelhecem antes do prazo esperado.
2. **Conector MC4 com entrada de umidade** — crimpagem fora do padrão ou conector de fabricante não certificado. O contato entre a carcaça metálica e o condutor cria caminho de fuga para o PE do módulo. Em campo, a maioria desses casos não aparece com o cabo visivelmente danificado — o conector parece íntegro por fora.
3. **Módulo com EVA deteriorado** — o encapsulante absorve umidade quando o vidro trinca ou o laminado envelhece. A resistência entre as células e o frame de alumínio aterrado cai, fechando o circuito de fuga para o PE. Um único módulo nessa condição pode derrubar toda a string abaixo do limiar do inversor.
4. **Aterramento de estrutura com problema** — cabo PE da estrutura com resistência elevada, terminais oxidados ou bitola insuficiente. Sem aterramento adequado dos frames, a tensão de modo comum do string cria corrente de fuga que o inversor detecta.
5. **Circuito de medição interno com defeito** — o divisor resistivo na placa de controle pode ter resistor com deriva de valor ou capacitor de desacoplamento com fuga. Nesses casos o Erro 103 aparece mesmo com o string completamente desconectado. É o inversor lendo errado, não o sistema externo com problema.
6. **Umidade interna no inversor** — condensação por vedação comprometida altera a impedância dos planos de terra na placa, gerando leitura falsa de fuga.

As causas 1 a 4 ficam na instalação. As causas 5 e 6 ficam no equipamento.

---

## Como identificar na prática

O ponto de partida é uma pergunta objetiva: o erro existe com ou sem o string conectado?

**1. Retire todos os conectores MC4 da entrada do inversor.** Ligue o equipamento sem o string. Se o Erro 103 persistir com o CC desconectado, o problema está dentro — circuito de medição com defeito ou umidade na placa. Não há mais nada a testar no campo.

**2. Se o erro some sem o string: use um megôhmmetro.** Meça a resistência de isolamento entre cada polo do string (positivo e negativo) e o PE. Tensão de teste de 500 V CC. Acima de 10 MΩ: sistema saudável. Entre 1 MΩ e 10 MΩ: degradação presente. Abaixo de 1 MΩ: confirma a origem do Erro 103.

Multímetro comum não resolve esse diagnóstico. A tensão de teste de 500 V CC é o que força o defeito a aparecer — em modo ohmímetro convencional, cabos com isolamento deteriorado podem parecer perfeitos.

**3. Isole as strings individualmente.** Se o array tem mais de uma string, teste uma por vez. A que apresentar resistência mais baixa é a origem. Dentro da string, desconecte os módulos um por um até a leitura subir. O módulo que derruba a impedância quando conectado é o responsável.

**4. Inspecione cabos e conectores.** Fissura longitudinal no isolamento, marca de atrito com calha metálica, oxidação nos pinos de MC4 ou encaixe frouxo. São identificáveis visualmente, sem instrumento. Esse passo pode encerrar o diagnóstico antes de qualquer medição com equipamento.

**5. Meça o aterramento da estrutura.** Resistência entre o frame de cada módulo e o barramento de PE deve estar abaixo de 0,5 Ω. Resistência alta ou circuito aberto indica conexão de aterramento com problema. Fixadores de aço carbono sem proteção em regiões litorâneas oxidam em menos de dois anos e aparecem com frequência como causa do erro.

**6. Se o sistema externo estiver aprovado e o erro persistir: bancada.** Com o string desconectado e o Erro 103 ativo, o próximo passo é medir o divisor resistivo da placa de controle com multímetro. Resistores com deriva acima de 5% do valor nominal já explicam leitura errada. Essa medição não tem como ser feita no campo.

**7. Verifique umidade interna.** Condensação na placa, oxidação na borda do PCB ou vedação da tampa com folga. Aparece com mais frequência em inversores instalados no Centro-Oeste, onde a variação térmica entre noite e dia passa de 20°C em boa parte do ano.

---

## O erro mais comum do mercado

O técnico chega, vê o Erro 103, descarta o cabeamento "visualmente" e conclui que é defeito interno no inversor. Equipamento vai para reparo ou substituição. Sistema continua com o mesmo problema depois da troca.

O Erro 103 é um dos erros com maior proporção de causa externa. Condenar o inversor sem medir a resistência de isolamento string por string é pular a parte mais barata do diagnóstico. Inversores Growatt residenciais de 3 a 5 kW custam entre R$ 2.500 e R$ 4.500 novos. A substituição de um conector MC4 ou de um trecho de cabo custa menos de R$ 80.

Tem um detalhe que poucos consideram: se o técnico troca o inversor sem corrigir o defeito no cabeamento, o inversor novo exibe o mesmo Erro 103 em minutos após a partida. O cliente fica com dois inversores e o problema segue sem solução.

---

## Quando o reparo é viável

Quando a causa está no circuito de medição interno, a viabilidade depende do componente com defeito.

Resistor com deriva ou capacitor de desacoplamento com ESR elevado: troca simples, custo de componente, inversor volta à especificação de fábrica. Essa é a situação mais frequente quando o defeito é interno.

Condensação com corrosão nos pads do circuito de detecção: depende da extensão. Oxidação localizada é tratável. Oxidação que alcançou o plano de terra ou comprometeu trilhas da camada base do PCB: a viabilidade precisa ser avaliada ponto por ponto.

Para equipamentos com até 7 anos de uso, o reparo é justificável — especialmente quando o modelo não está descontinuado. Reparo em bancada sai entre R$ 350 e R$ 700. Inversor novo equivalente sai entre R$ 2.500 e R$ 4.500.

Não existe número antes de abrir e medir.

---

## Conclusão

O Growatt Erro 103 não vai para bancada até que o sistema externo tenha sido descartado.

Megôhmmetro, trinta minutos, isolamento por string. Esse procedimento resolve a maioria dos casos sem nenhum reparo eletrônico. O que sobra depois disso vai para a bancada — e geralmente é menos do que parece.

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

- Âncora: 'resistência de isolamento entre os condutores CC (positivo e/ou negativo) e o terra (PE)' → URL: /growatt-erro-102-falha-de-isolamento → Contexto: seção "O que causa o Erro 103", parágrafo de definição técnica — o Post 01 cobre falha de isolamento com análise de string leakage no Growatt Erro 102, tema diretamente relacionado
- Âncora: 'Um único módulo nessa condição pode derrubar toda a string abaixo do limiar do inversor' → URL: /sma-erro-3501-falha-isolamento-diagnostico-fotovoltaico → Contexto: seção "O que causa o Erro 103", item 3 — o Post 04 aborda falha de isolamento no SMA com análise de módulo como fonte da fuga
- Âncora: 'Não há mais nada a testar no campo' → URL: /inversor-solar-parou-de-funcionar-checklist → Contexto: seção "Como identificar na prática", passo 1 — o Post 11 apresenta o checklist completo para diagnóstico externo antes de envio para bancada
- Âncora: 'resistores com deriva acima de 5% do valor nominal já explicam leitura errada' → URL: /igbt-queimado-inversor-solar-6-causas → Contexto: seção "Como identificar na prática", passo 6 — o Post 10 detalha as causas de falha eletrônica interna em inversores, incluindo deriva de componentes da placa de controle

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62109-2, norma que define os requisitos de proteção GFDI" → URL: https://www.iec.ch/homepage → Fonte: IEC — IEC 62109-2: Safety of power converters for use in photovoltaic power systems, norma internacional que define os requisitos de detecção e interrupção de falta à terra em inversores fotovoltaicos
- Texto âncora: "tensão de modo comum do string cria corrente de fuga" → URL: https://www.aneel.gov.br/qualidade-da-energia-eletrica → Fonte: ANEEL — Resolução Normativa 1000/2021, que estabelece os limites de qualidade de energia e parâmetros operacionais para conexão de sistemas fotovoltaicos à rede de distribuição

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Cabos e conectores de sistema fotovoltaico em instalação — representa o contexto de falha de aterramento por cabeamento CC comprometido, ponto de partida do diagnóstico do Erro 103
→ Nome do arquivo: growatt-erro-103-falha-aterramento-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Conectores MC4 e cabeamento CC de sistema fotovoltaico — diagnóstico do Growatt Erro 103 falha de aterramento no campo
→ Legenda: Fig. 1 — Cabeamento CC e conectores MC4 são os primeiros pontos a verificar no diagnóstico do Growatt Erro 103
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=1200
→ Por que foi escolhida: Equipamento de medição elétrica — representa o uso do megôhmmetro para teste de resistência de isolamento descrito na seção de identificação
→ Nome do arquivo: medicao-isolamento-inversor-growatt-erro103-2.webp
→ Alt Text (máx. 125 caracteres): Medição de resistência de isolamento em string fotovoltaico com megôhmmetro — diagnóstico de Growatt Erro 103 no campo
→ Legenda: Fig. 2 — Teste de isolamento com megôhmmetro a 500 V CC: procedimento que define se o Erro 103 está no sistema externo ou dentro do inversor
→ Onde inserir: Após H2 "Como identificar na prática"
