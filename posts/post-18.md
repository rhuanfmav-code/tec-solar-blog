# Post 18 — Canadian Solar Falha 117: Falha de Isolamento — cabo ou painel com isolamento ruim

---

[PALAVRA-CHAVE FOCO]

Canadian Solar Falha 117 falha de isolamento

---

[TÍTULO SEO — Title Tag]

Canadian Solar Falha 117: Falha de Isolamento Solar

---

[SLUG — URL do Post]

canadian-solar-falha-117-falha-de-isolamento

---

[META DESCRIPTION]

Canadian Solar Falha 117 indica isolamento comprometido no campo. Veja como diagnosticar com megôhmetro antes de enviar o inversor para reparo.

---

[CATEGORIA]

Códigos de Erro e Falhas

---

[TAGS]

Canadian Solar Falha 117, falha de isolamento solar, teste megôhmetro string, diagnóstico CC fotovoltaico, isolamento cabo painel

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

A **Canadian Solar Falha 117** interrompe a geração quando o inversor detecta que a resistência de isolamento do sistema fotovoltaico caiu abaixo do limite mínimo de segurança. O display registra o alarme, o inversor desliga a saída CC e a geração para. Sem aquecimento aparente, sem odor, sem componente visualmente danificado — só o equipamento parado e o cliente sem geração.

Na nossa bancada, esse erro chega com o mesmo histórico toda vez: o técnico foi ao local, resetou o equipamento, o sistema voltou a gerar por horas ou dias, e a Falha 117 retornou. Depois de dois ou três ciclos assim, o inversor foi enviado como "defeito eletrônico". Em boa parte dos casos que chegam com esse histórico, o inversor funciona exatamente como foi projetado. O problema está no campo.

Medir antes de mandar.

## O que causa a Falha 117

Nos inversores CSI da Canadian Solar, a Falha 117 indica que a resistência de isolamento medida entre o barramento CC e o terra de proteção ficou abaixo do limiar operacional. Para modelos monofásicos, o limite fica em torno de 600 kΩ. Para modelos trifásicos, 1 MΩ. Abaixo desses valores, o inversor desliga e registra a falha — comportamento obrigatório conforme a IEC 62109-2, norma de segurança para inversores fotovoltaicos adotada no mercado brasileiro.

É uma proteção. Não é defeito do inversor.

As origens mais comuns na instalação:

- **Cabos CC com isolamento degradado**: exposição UV intensa, curvatura forçada em borda de calha ou esmagamento sob estrutura metálica rompe o dielétrico do cabo. Em telhados no Nordeste e no Centro-Oeste — onde a temperatura de superfície do telhado ultrapassa 70°C nos meses secos — a degradação do PVC externo avança bem mais rápido do que o fabricante projeta para clima temperado.
- **Conectores MC4 com umidade interna**: crimpagem fora do padrão ou conector parcialmente encaixado exposto à chuva acumula condensação. A umidade cria um caminho resistivo entre o condutor e a carcaça metálica aterrada.
- **Caixa de junção do painel infiltrada**: água acumulada dentro da junction box dissolve resíduos minerais e forma uma ponte condutiva entre o circuito elétrico e a moldura do painel.
- **Painel com delaminação no laminado**: umidade que entra entre a célula e o encapsulante EVA aumenta a corrente de fuga em direção à moldura metálica aterrada. Painéis com mais de 8 anos de campo ou instalados sem ventilação adequada são os mais suscetíveis.
- **DPS com varistor degradado**: o elemento varistor do dispositivo de proteção contra surto se deteriora com o uso e pode criar caminho de baixa resistência para o terra mesmo sem nenhum evento de surto recente.
- **Cabo em contato direto com perfil de alumínio**: sem grampos de fixação adequados, o cabo CC encosta na borda do perfil e o isolamento se desgasta progressivamente com vibração e dilatação térmica.

## Como identificar na prática

O diagnóstico da Falha 117 começa com o megôhmetro. O multímetro convencional não aplica tensão suficiente para revelar falhas de isolamento em circuitos CC de alta tensão.

Procedimento:

1. Desligue o inversor e abra o disjuntor CC
2. Desconecte os cabos CC do inversor — positivo e negativo de cada string, individualmente
3. Ajuste o megôhmetro para 500 Vcc (ou 1000 Vcc para strings com tensão de circuito aberto acima de 500 V)
4. Meça a resistência de isolamento de cada string separadamente:
   - Positivo da string → barra de terra de proteção (PE)
   - Negativo da string → barra PE
5. Registre e compare os valores:
   - Acima de 10 MΩ: isolamento saudável
   - Entre 1 MΩ e 10 MΩ: atenção, inspecionar os pontos de risco antes de religar
   - Abaixo de 1 MΩ: falha de isolamento confirmada nessa string
   - Abaixo de 100 kΩ: falha severa, não religar sem localizar a origem
6. Na string problemática, desconecte painel por painel e reaplique a medição após cada remoção — o valor que sobe aponta o painel ou trecho de cabo com defeito
7. Com a string problemática isolada, inspecione fisicamente cada conector MC4: oxidação, eflorescência branca (depósito por infiltração de água), carbonização ou conector parcialmente encaixado

Câmera térmica durante a geração complementa bem: ponto quente em MC4 ou em trecho de cabo indica resistência de contato elevada — sinal de que o isolamento já está cedendo antes de a falha aparecer no display.

## O erro mais comum do mercado

O inversor vai para assistência antes de qualquer medição de campo.

É o caminho mais demorado e mais caro. E, na maioria das ocorrências, completamente evitável.

O raciocínio é: "o inversor acusou a falha, logo o defeito é do inversor". Só que o equipamento registra o que o circuito externo impõe — se o isolamento do campo está comprometido, o alarme é correto. A assistência testa o inversor sem a string conectada, não encontra nada, devolve com "sem problema identificado". O sistema volta ao campo e a Falha 117 retorna no primeiro dia de chuva.

Outro erro recorrente: o técnico localiza o painel com baixa resistência de isolamento e cota a substituição no mesmo dia. Sem abrir a junction box. Sem inspecionar os conectores. Em boa parte dos casos, o problema é um MC4 com umidade que custa menos de R$ 10,00 e é resolvido em campo em 20 minutos.

O diagnóstico precede a compra. Sempre.

## Quando o reparo é viável

Se o campo estiver dentro dos parâmetros — todas as strings com resistência de isolamento acima de 1 MΩ — e a Falha 117 persistir com o inversor reconectado, o problema pode ser interno.

Dentro do inversor, o circuito de monitoramento de isolamento usa resistores de alta impedância, capacitores de filtro e um CI de medição. Esses componentes têm vida útil menor que o restante do circuito em ambientes com umidade alta e amplitude térmica acentuada. Resistores de 1 MΩ a 10 MΩ em encapsulamento SMD com desvio de valor geram leitura incorreta no ADC — o inversor "vê" isolamento baixo mesmo com o campo em ordem.

O reparo desse circuito é possível e o custo fica bem abaixo de um equipamento novo. Um CSI de 5 kW novo está entre R$ 3.500 e R$ 5.500 no mercado atual. O conserto do circuito de sensoriamento sai por uma fração disso, com componentes rastreáveis e laudo técnico.

Há casos em que a corrente de fuga não controlada danificou componentes do estágio de potência ao longo do tempo. Nesses casos, o laudo define o que é recuperável — não existe resposta sem abrir o equipamento e medir.

## Conclusão

A Falha 117 é o Canadian Solar fazendo o que foi programado para fazer. O inversor identificou um caminho de fuga entre o circuito CC e o terra e desligou a geração para proteger a instalação.

O megôhmetro resolve o diagnóstico antes de qualquer decisão de remessa.

Se o campo vier limpo e a falha continuar, a bancada abre o circuito de monitoramento e identifica o componente com desvio. Campo primeiro, bancada depois.

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

- Âncora: 'resistência de isolamento' → URL: /growatt-erro-102-falha-de-isolamento-string-leakage → Contexto: Introdução e seção "O que causa a Falha 117" — referência cruzada com Post 01, que aborda o mesmo tipo de proteção em inversores Growatt e detalha o diagnóstico de string leakage
- Âncora: 'MC4 com umidade' → URL: /sungrow-arc-fault-afci-conector-mc4-mal-crimpado → Contexto: Seção "O erro mais comum do mercado" — referência cruzada com Post 16, que detalha como conectores MC4 mal crimpados ou com falha de vedação geram proteções em inversores Sungrow
- Âncora: 'corrente de fuga' → URL: /sma-3501-falha-de-isolamento-diagnostico-completo → Contexto: Seção "Quando o reparo é viável" — referência cruzada com Post 04, que trata da mesma classe de falha em inversores SMA e discute os limites de corrente de fuga em sistemas fotovoltaicos

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62109-2" → URL: https://www.abnt.org.br → Fonte: ABNT — a norma brasileira ABNT NBR IEC 62109-2 adota os requisitos da IEC 62109-2 para segurança de inversores fotovoltaicos conectados à rede, incluindo a obrigatoriedade do monitoramento de isolamento em tempo real
- Texto âncora: "resistência de isolamento" → URL: https://www.aneel.gov.br → Fonte: ANEEL — Resolução Normativa n.º 1.059/2023 regulamenta a conexão de sistemas de micro e minigeração distribuída à rede, com requisitos de segurança que incluem monitoramento de isolamento CC

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Cabos CC de sistema fotovoltaico sobre telhado — representa o ponto de origem da Canadian Solar Falha 117, onde o diagnóstico de isolamento começa antes de qualquer remessa do inversor
→ Nome do arquivo: canadian-solar-falha-117-falha-isolamento-cabo-fotovoltaico.webp
→ Alt Text (máx. 125 caracteres): Cabos CC de sistema fotovoltaico em telhado — diagnóstico da Canadian Solar Falha 117 por cabo ou painel com isolamento comprometido
→ Legenda: Fig. 1 — A Canadian Solar Falha 117 exige diagnóstico de isolamento no campo antes da remessa do inversor para bancada
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=1200
→ Por que foi escolhida: Técnico realizando medição com equipamento de teste — representa o procedimento de diagnóstico com megôhmetro descrito na seção "Como identificar na prática"
→ Nome do arquivo: canadian-solar-falha-117-teste-megohmetro-string-2.webp
→ Alt Text (máx. 125 caracteres): Técnico realizando teste de isolamento com megôhmetro em string fotovoltaico — diagnóstico da Canadian Solar Falha 117
→ Legenda: Fig. 2 — O megôhmetro ajustado para 500 Vcc é o único instrumento capaz de revelar falhas de isolamento em circuitos CC de alta tensão fotovoltaica
→ Onde inserir: Após H2 "Como identificar na prática"
