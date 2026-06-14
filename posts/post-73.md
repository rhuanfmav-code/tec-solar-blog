# Post 73 — Growatt Erro 302: Falta de Rede CA — diagnóstico completo do estágio de saída

---

[PALAVRA-CHAVE FOCO]
Growatt Erro 302 falta de rede CA

---

[TÍTULO SEO — Title Tag]
Growatt Erro 302: Falta de Rede CA — Como Diagnosticar

---

[SLUG — URL do Post]
growatt-erro-302-falta-rede-ca-diagnostico-estagio-saida

---

[META DESCRIPTION]
Growatt Erro 302 indica ausência de rede CA detectada. Relé de saída ou circuito de sensoriamento? Saiba como diagnosticar antes de trocar a placa.

---

[CATEGORIA]
Códigos de Erro e Falhas

---

[TAGS]
Growatt Erro 302, falta de rede CA inversor solar, relé de saída inversor Growatt, diagnóstico estágio saída CA, circuito sensoriamento tensão inversor

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Growatt Erro 302** — "No AC Connection" — aparece quando o inversor realiza a checagem pré-operacional de presença de tensão CA na saída e não encontra o sinal dentro do limiar de detecção. O sistema trava antes de iniciar a operação. Sem geração, sem log de produção, sem mensagem adicional. Só o código no display.

O que confunde quem está no campo é que, em boa parte dos casos, a rede elétrica está presente e funcionando. O problema não é ausência de energia — é que o circuito de sensoriamento do inversor não consegue ler essa energia. Na nossa bancada, esse erro chega com frequência vindo de instalações no interior de Minas Gerais, Bahia e Piauí, onde a tensão da concessionária oscila bastante ao longo do dia. O equipamento já passou por múltiplos ciclos de desconexão e religação forçada. A rede está lá. O inversor reporta que não tem nada.

## O que causa esse erro

Para entrar em operação conectado ao grid, o inversor precisa completar quatro verificações em sequência:

1. Detectar tensão CA dentro da faixa permitida — nominal ±10%, conforme ABNT NBR 16149
2. Confirmar frequência dentro do range operacional (entre 59,5 Hz e 60,5 Hz na configuração padrão brasileira)
3. Fechar o relé de saída, o componente que conecta fisicamente o inversor ao ponto de acoplamento com a rede
4. Confirmar que a tensão lida após o fechamento do relé corresponde ao valor medido antes

O Erro 302 é disparado quando o circuito de sensoriamento retorna leitura nula ou abaixo do limiar mínimo — mesmo com o grid presente. Tem origem externa ou interna.

Do lado externo: disjuntor CA com contato oxidado, cabo de saída com terminal frouxo, interruptor de desconexão aberto por descuido ou queda de tensão da concessionária abaixo de 85% da nominal por tempo suficiente para o firmware registrar ausência de rede.

Do lado interno, os pontos mais recorrentes são:

- Relé de saída com contatos desgastados (stuck open) — a bobina energiza, o contato não fecha
- Divisor resistivo do circuito de sensoriamento CA com deriva por temperatura ou envelhecimento
- Optoacoplador de isolamento do caminho de leitura aberto ou com ganho de corrente (CTR) muito reduzido
- Referência de tensão incorreta no comparador da placa de controle, gerando limiar de detecção deslocado

O divisor resistivo é o ponto que mais passa despercebido. Resistores com deriva elevada não queimam — simplesmente alteram o valor medido ao longo dos anos. Nenhum sinal visual na placa. A leitura de tensão CA que chega ao microcontrolador está 25 a 35% abaixo da real, e o firmware interpreta como ausência de rede.

É esse tipo de defeito que não aparece em inspeção visual nem em teste rápido com multímetro nos terminais de potência.

## Como identificar na prática

A separação entre causa externa e interna define o caminho. Começa com multímetro nos terminais certos:

1. Meça a tensão CA nos terminais de saída do inversor — os terminais pós-relé, no bloco de conexão CA — com o equipamento em standby. Se a tensão estiver presente e correta (220 V ±10%), a rede chegou até ali. O inversor é que não está lendo o sinal
2. Compare com a tensão no quadro CA, nos terminais de saída do disjuntor dedicado ao inversor. Diferença acima de 5 V indica resistência de contato elevada no disjuntor ou no cabeamento
3. Verifique o disjuntor fisicamente: terminal de parafuso com oxidação, cabo com isolamento amolecido pelo calor, bitola subdimensionada para a corrente nominal do inversor
4. Com o inversor aberto na bancada, localize o relé de saída CA. Aplique tensão de bobina diretamente (geralmente 5 VCC ou 12 VCC conforme especificação do componente) e meça a continuidade entre os contatos. Resistência de contato acima de 0,5 Ω indica desgaste
5. Identifique a rede de resistores do divisor resistivo de sensoriamento CA — normalmente uma série de resistores de alta impedância no caminho de entrada CA da placa de controle. Meça o valor individual com o circuito desligado e compare com o valor marcado no corpo do componente. Deriva acima de 5% já é suficiente para deslocar a leitura do firmware para fora do limiar
6. Teste o optoacoplador do circuito de medição: com sinal CA de referência aplicado na entrada, meça a tensão na saída do componente. Ausência de sinal na saída com sinal presente na entrada confirma componente aberto ou com CTR degradado abaixo do mínimo funcional
7. Verifique a tensão de referência no pino VREF do comparador da placa de controle — desvio da referência desloca o limiar de detecção e pode fazer o firmware "ver" ausência de tensão mesmo com 200 V presentes nos terminais

Se a tensão CA está nos terminais de saída do inversor e o Erro 302 persiste, a busca começa no circuito de leitura. Não no cabeamento.

## O erro mais comum do mercado

O técnico mede a tensão no quadro, confirma que a rede está presente e conclui que o inversor tem "problema interno na placa principal". O laudo vai para o fabricante sem diagnóstico detalhado. Meses depois, o cliente recebe orçamento de troca de placa principal — às vezes ao custo de 60 a 80% do inversor novo.

Confirmar presença de rede não é diagnóstico. É a primeira linha de uma checklist que tem mais seis passos abaixo dela.

O relé de saída é o componente com maior taxa de falha nesse erro específico — principalmente em inversores com mais de três anos operando em regiões onde a rede oscila, como o interior do Nordeste e zonas rurais com subestação sobrecarregada. O relé tenta fechar dezenas de vezes por dia durante eventos de reconexão. O contato desgasta progressivamente. Custo do componente de reposição: entre R$ 15 e R$ 60 dependendo do modelo e da especificação de contato. Não é troca de placa.

Mandar o inversor para fábrica com laudo de "placa com defeito" sem identificar o componente específico é garantia de orçamento inflado. O que chega no serviço autorizado sem diagnóstico prévio recebe o reparo mais amplo possível. Às vezes necessário. Frequentemente não.

## Quando o reparo é viável

Se o circuito de potência está intacto — IGBTs, drivers, filtros de saída, capacitores de barramento — o Erro 302 é reparável com custo baixo e alta taxa de sucesso.

Os componentes do circuito de sensoriamento CA têm custo unitário abaixo de R$ 80 e ficam em regiões acessíveis da placa de controle. O diagnóstico exige instrumento adequado e referência do schematic do modelo — mas o reparo é cirúrgico quando a causa está corretamente isolada.

Inversores Growatt monofásicos de 3 kW a 5 kW estão entre R$ 2.500 e R$ 4.000 no mercado atual. Um reparo de circuito de sensoriamento CA fica entre R$ 180 e R$ 500 incluindo componentes e mão de obra de bancada. A relação é direta.

O que pode ampliar o escopo: relé que operou com arco elétrico sustentado por tempo prolongado — contato parcialmente oxidado que abriu e fechou repetidamente com carga — pode ter danificado a trilha de cobre adjacente ou o componente snubber de proteção da bobina. Isso requer reparo adicional de placa. Mas ainda estamos bem abaixo do valor de substituição do equipamento. Depende do que vai aparecer quando abrir a placa e medir componente por componente.

Antes de qualquer decisão, medir. O diagnóstico é o que define se é R$ 300 de reparo ou R$ 3.500 de inversor novo.

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
- Âncora: 'relés de bypass' → URL: /reles-de-bypass-inversores-solares-falha-silenciosa → Contexto: seção "O que causa esse erro", ao mencionar relé de saída com contatos desgastados
- Âncora: 'placa de controle' → URL: /placa-de-controle-vs-placa-de-potencia-onde-esta-o-defeito → Contexto: seção "Como identificar na prática", ao mencionar a placa de controle e o comparador
- Âncora: 'por que os IGBTs queimam' → URL: /por-que-igbts-queimam-inversores-solares-causas → Contexto: seção "Quando o reparo é viável", ao citar o circuito de potência com IGBTs
- Âncora: 'superaquecimento de inversor solar' → URL: /superaquecimento-inversor-solar-causas-prevencao → Contexto: seção "O que causa esse erro", ao mencionar deriva de componentes por temperatura
- Âncora: 'diagnóstico em nível de placa' → URL: /o-que-e-diagnostico-nivel-de-placa-reparo-inversor → Contexto: seção "Quando o reparo é viável", ao citar diagnóstico por componente

---

[LINKS EXTERNOS SUGERIDOS]
- Texto âncora: "ABNT NBR 16149" → URL: https://www.abnt.org.br → Fonte: ABNT — norma técnica de requisitos de conexão de inversores fotovoltaicos à rede de distribuição de energia elétrica
- Texto âncora: "tensão da concessionária" → URL: https://www.aneel.gov.br → Fonte: ANEEL — regulação dos padrões de qualidade de tensão na rede de distribuição (Módulo 8 do PRODIST)

---

[IMAGEM PRINCIPAL — USE ESTA]
IMAGEM PRINCIPAL:
→ URL para download: buscar "solar inverter open repair circuit board technician" em unsplash.com ou pexels.com
→ Por que foi escolhida: inversor aberto em bancada — ilustra o contexto de diagnóstico interno do estágio de saída CA
→ Nome do arquivo: growatt-erro-302-diagnostico-estagio-saida-ca.webp
→ Alt Text (máx. 125 caracteres): Inversor solar Growatt aberto em bancada de diagnóstico — circuito de saída CA com relé e sensoriamento de tensão
→ Legenda: Fig. 1 — Diagnóstico interno do estágio de saída CA: relé, divisor resistivo e optoacoplador são os pontos de falha do Erro 302
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]
IMAGEM SECUNDÁRIA:
→ URL para download: buscar "multimeter measuring AC voltage electrical panel solar" em pexels.com ou pixabay.com
→ Por que foi escolhida: multímetro medindo tensão CA — ilustra o primeiro passo de diagnóstico entre causa externa e interna
→ Nome do arquivo: medicao-tensao-ca-terminais-inversor-growatt.webp
→ Alt Text (máx. 125 caracteres): Multímetro medindo tensão CA nos terminais de saída de inversor solar — diagnóstico Growatt Erro 302 falta de rede
→ Legenda: Fig. 2 — Medição de tensão CA nos terminais de saída do inversor: primeiro passo para separar causa externa de falha interna no circuito de sensoriamento
→ Onde inserir: Após H2 "Como identificar na prática"
