# Post 80 — Growatt Erro 403: Falha de Corrente de Fuga — capacitor de filtro ou isolamento comprometido?

---

## [PALAVRA-CHAVE FOCO]

Growatt Erro 403 corrente de fuga

---

## [TÍTULO SEO — Title Tag]

Growatt Erro 403: Corrente de Fuga — Diagnóstico Completo

---

## [SLUG — URL do Post]

growatt-erro-403-corrente-de-fuga-capacitor-filtro-isolamento

---

## [META DESCRIPTION]

Growatt Erro 403 indica fuga de corrente. Saiba como separar causa externa (cabos, painéis) de falha interna (capacitor Y ou sensor) antes de trocar o inversor.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Growatt Erro 403, corrente de fuga inversor solar, capacitor Y inversor, falha isolamento fotovoltaico, diagnóstico Growatt

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Growatt Erro 403** paralisa o sistema sem dar mais informação do que o código no display. A geração cai para zero, o equipamento entra em proteção e o integrador fica diante de uma dúvida real: o problema está na instalação — cabo, painel, aterramento — ou dentro do inversor?

O Erro 403 nos modelos Growatt string sinaliza corrente de fuga acima do limiar de proteção. Nos inversores sem transformador, categoria que inclui a grande maioria dos equipamentos Growatt instalados no Brasil, a corrente de fuga é monitorada de forma contínua porque representa risco elétrico real para o sistema e para quem o opera. A proteção está correta. O que falta, na maioria dos casos que chegam até nós, é o diagnóstico preciso de onde a fuga está acontecendo.

Na nossa bancada, esse erro chega dividido em dois grupos. No primeiro: instalações com problema externo real — cabo com isolamento rompido, painel com infiltração de umidade, conexão de terra mal executada ou cabo pressionado contra perfil metálico por meses de dilatação térmica. No segundo, menor mas relevante: inversores com o circuito de detecção ou os capacitores do filtro EMI falhando internamente, gerando leitura de fuga sem que haja corrente escapando pela instalação. Os dois grupos têm causas diferentes e exigem abordagens completamente diferentes.

## O que causa o Erro 403

Inversores string sem transformador operam com os painéis fotovoltaicos flutuando em relação ao terra de proteção (PE). Essa condição cria uma capacitância parasítica distribuída entre as células do painel, o quadro metálico e a estrutura de suporte — que está aterrada. Quando o inversor opera, a variação de tensão no barramento CC induz corrente através dessa capacitância. Isso é normal até um limite definido em norma.

A IEC 62109-2, que regula inversores fotovoltaicos, estabelece o limiar máximo de corrente de fuga residual em 300 mA para proteção imediata. A ABNT NBR 16149, referência brasileira para sistemas fotovoltaicos conectados à rede, estabelece requisitos equivalentes de proteção e monitoramento de corrente de fuga.

O Erro 403 é disparado quando a corrente medida pelo sensor interno ultrapassa esse limiar. As fontes possíveis são quatro:

Capacitância parasítica dos painéis: aumenta com umidade. Em dias de chuva ou neblina, especialmente nas regiões Sul e Sudeste durante o inverno, a condutividade da superfície do vidro dos módulos eleva a corrente de fuga naturalmente. Se o erro aparece só nessas condições e some depois, a instalação pode estar operando próxima ao limite — mas a causa é ambiental, não um defeito.

Isolamento comprometido em cabos CC ou CA: ruptura mecânica no isolamento, abrasão por borda de perfil metálico ou degradação por exposição UV sem proteção adequada criam condutividade entre o condutor e a estrutura aterrada. A corrente de fuga muda de capacitiva para resistiva — e ultrapassa o limiar com muito mais facilidade.

Degradação do painel fotovoltaico: infiltração de umidade no laminado do módulo, falha no encapsulante ou dano físico criam um caminho de baixa resistência entre as células e o quadro metálico. O padrão típico é fuga que aumenta progressivamente ao longo dos meses, não de forma abrupta.

Capacitores Y do filtro EMI com defeito: inversores string incluem capacitores do tipo Y conectando o barramento CC ao PE para supressão de interferência eletromagnética. Quando esses componentes entram em curto ou degradam com ESR elevado, criam um caminho direto de corrente para o terra sem qualquer problema externo na instalação. É a causa interna mais frequente de Erro 403 em inversores com tempo de uso superior a cinco anos.

## Como identificar na prática

A investigação começa pela separação entre causa externa e interna. O processo tem ordem definida e não deve ser pulado:

1. Registre o padrão temporal do erro — horário do dia, condições climáticas, se persiste ou auto-reseta após algumas horas de operação
2. Desconecte todos os strings CC do inversor, mantendo apenas a conexão CA com a rede elétrica
3. Energize o inversor somente pela rede CA e aguarde alguns minutos
4. Se o Erro 403 aparecer com os strings CC desconectados, a falha é interna — o sensor de corrente de fuga ou os capacitores Y estão com defeito
5. Se o erro some sem os strings, a origem é no lado CC — reconecte os strings um a um, testando cada circuito isoladamente até identificar qual desencadeia o erro
6. Com o string identificado, meça a resistência de isolamento com megôhmímetro a 1000 V CC entre cada polo (positivo e negativo) e o terra — valor esperado acima de 1 MΩ por IEC 62109-1; abaixo disso indica isolamento comprometido
7. Inspecione fisicamente o cabo do string com o erro — procure trechos pressionados contra estrutura metálica, exposição solar sem proteção UV, crimpagem com condutor parcialmente fora do terminal ou conectores MC4 com encaixe incompleto
8. Se o megôhmímetro indicar isolamento adequado em todos os strings, verifique os módulos — inspeção visual em busca de trincas, deformações, manchas escuras no vidro ou bordas com sinais de infiltração
9. Com o inversor completamente desenergizado, meça a resistência entre os terminais dos capacitores Y do filtro EMI e o chassi — curto de capacitor Y aparece como resistência muito baixa (abaixo de 1 kΩ) onde o valor correto é de dezenas de megaohms

O passo 4 é o ponto de decisão do diagnóstico. Ele elimina ou confirma a origem interna sem nenhum instrumento além do próprio inversor.

## O erro mais comum do mercado

O integrador vai ao campo, vê o Erro 403 no display, inspeciona visualmente a instalação, não encontra nada óbvio e conclui que o inversor "falhou internamente". O equipamento é removido.

O string com cabo de isolamento rompido — pressionado contra a calha de alumínio por dois anos de expansão térmica — continua no telhado. O inversor substituto encontra exatamente o mesmo problema em dias.

Esse ciclo se repete porque o diagnóstico saltou a etapa mais básica: isolar os strings CC antes de qualquer conclusão sobre o equipamento. Sem esse passo, a investigação começa no lugar errado. E termina no lugar errado também.

## Quando o reparo é viável

Se o passo 4 confirmar falha interna — Erro 403 com strings CC desconectados — existem dois cenários com viabilidades distintas:

Capacitores Y com defeito são componentes de baixo custo e alta disponibilidade. A falha é identificável na bancada com medição de resistência e capacitância fora de circuito. Custo de componente entre R$15 e R$80 dependendo da especificação de tensão e capacitância exigida pelo modelo. Reparo direto, sem substituição de placa.

Circuito de sensoriamento de corrente de fuga com deriva de leitura: o sensor — geralmente um transformador de corrente toroidal no circuito de medição — pode desenvolver offset por envelhecimento ou por surto associado. Identificável com osciloscópio medindo o sinal de saída do sensor sem carga aplicada. Componentes substitutos disponíveis para os modelos Growatt mais comuns no mercado brasileiro.

Em ambos os casos, o custo de reparo fica abaixo de 25% do valor de um inversor equivalente novo. Para equipamentos entre 5 e 15 kW, essa diferença representa de R$2.500 a R$5.000 dependendo da potência e do canal de compra.

O único cenário onde o reparo não fecha a conta é dano térmico extenso na placa de controle por surto associado ao evento de fuga — quando o mesmo surto que causou a falha no capacitor queimou outros componentes ao redor. Isso é identificável visualmente antes de qualquer trabalho aprofundado de componente.

## Conclusão

O Erro 403 tem origem rastreável. Está na instalação — cabo, painel, aterramento — ou está dentro do inversor nos capacitores do filtro ou no circuito de sensoriamento. Nenhum dos dois cenários justifica condenar o equipamento sem diagnóstico.

Dez minutos de teste sistemático separam a troca desnecessária do reparo correto.

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

- Âncora: 'capacitores do filtro EMI' → URL: /capacitor-eletrolitico-inversor-solar-vida-util-degradacao → Contexto: seção "O que causa o Erro 403", ao explicar a falha dos capacitores Y como causa interna mais frequente
- Âncora: 'resistência de isolamento' → URL: /fronius-state-240-corrente-de-fuga-diagnostico → Contexto: seção "Como identificar na prática", passo 6, ao citar a medição com megôhmímetro como procedimento padrão de diagnóstico de corrente de fuga
- Âncora: 'corrente de fuga' → URL: /sungrow-gfci-fault-corrente-de-fuga-terra → Contexto: seção "O que causa o Erro 403", ao introduzir o conceito de corrente de fuga em inversores sem transformador
- Âncora: 'diagnóstico em nível de componente' → URL: /diagnostico-nivel-de-placa-inversor-solar → Contexto: seção "Quando o reparo é viável", ao mencionar que a falha é identificável na bancada antes de qualquer substituição de placa

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16149" → URL: https://www.abnt.org.br → Fonte: ABNT — norma técnica brasileira para sistemas fotovoltaicos conectados à rede, incluindo requisitos de proteção contra corrente de fuga
- Texto âncora: "IEC 62109-2" → URL: https://www.iec.ch/homepage → Fonte: IEC — norma internacional que define os limiares de corrente de fuga residual para inversores fotovoltaicos

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Painéis solares em estrutura metálica aterrada — representa visualmente o contexto de capacitância parasítica e corrente de fuga em sistemas fotovoltaicos
→ Nome do arquivo: growatt-erro-403-corrente-de-fuga-inversor-solar.webp
→ Alt Text (máx. 125 caracteres): Painéis fotovoltaicos em estrutura aterrada — diagnóstico de corrente de fuga Growatt Erro 403 em sistemas solares
→ Legenda: Fig. 1 — A capacitância parasítica entre células e estrutura metálica é a origem física da corrente de fuga em inversores sem transformador
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=1200
→ Por que foi escolhida: Técnico com multímetro em painel elétrico — representa o processo de medição de isolamento e diagnóstico de corrente de fuga descrito no passo a passo
→ Nome do arquivo: diagnostico-corrente-de-fuga-megaohmetro-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo resistência de isolamento em sistema fotovoltaico para diagnóstico de corrente de fuga Growatt
→ Legenda: Fig. 2 — Medição com megôhmímetro a 1000 V CC: valor abaixo de 1 MΩ entre polo e terra indica isolamento comprometido no string
→ Onde inserir: Após H2 "Como identificar na prática"
