# Post 34 — Drive solar para bombeamento: os 5 defeitos mais comuns e como diagnosticar

---

## [PALAVRA-CHAVE FOCO]

drive solar para bombeamento defeitos

---

## [TÍTULO SEO — Title Tag]

Drive solar para bombeamento: 5 defeitos e diagnóstico

---

## [SLUG — URL do Post]

drive-solar-para-bombeamento-defeitos-diagnostico

---

## [META DESCRIPTION]

Os 5 defeitos mais comuns em drives solares de bombeamento, como diagnosticar cada um e quando o reparo eletrônico é viável.

---

## [CATEGORIA]

Drive Solar e Bombeamento

---

## [TAGS]

drive solar bombeamento, falha IGBT drive solar, diagnóstico drive bombeamento, capacitor barramento drive, bomba solar defeito

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Drive solar para bombeamento** falha de formas que o inversor on-grid não falha. O perfil de carga é diferente — motor com corrente de partida alta, operação variável conforme a irradiância, paradas bruscas por poço seco ou entupimento de bomba — e o ambiente de instalação é geralmente pior: propriedade rural, sem assistência técnica próxima, caixa de campo sem ventilação adequada.

Na nossa bancada, drives de bombeamento chegam com histórico parecido. O equipamento parou, o técnico reiniciou, funcionou por um ou dois dias, parou de vez. Depois ficou em prateleira esperando uma decisão que nunca veio. O padrão se repete com frequência alta o suficiente para que a gente reconheça a causa provável antes mesmo de abrir a carcaça.

## O que causa esse problema

O drive solar para bombeamento opera num regime de estresse específico. A tensão de entrada varia com a irradiância, a frequência de saída varia para controlar a rotação da bomba, e a carga mecânica muda conforme o nível do poço e a pressão do sistema. Essa combinação cria cinco pontos de falha recorrentes — mais um sexto que não é falha de componente, mas causa falha secundária com a mesma frequência.

O primeiro é o estágio de potência por sobrecorrente de partida. O motor de bomba submersa tem corrente de partida até seis vezes maior que a corrente nominal. Se o banco de capacitores do barramento DC está degradado, ele não sustenta esse pico de demanda. A tensão de barramento cai abruptamente, o controlador de gate drive interpreta a situação de forma inadequada e o IGBT recebe um pulso fora de especificação. Na bancada: um ou mais IGBTs em curto, com marca de aquecimento localizada na placa de potência. O capacitor que falhou primeiro quase sempre ainda está no circuito, aparentemente intacto.

O segundo é a degradação do banco de capacitores do barramento. Drives instalados em caixas metálicas a campo, sem ventilação, com paredes da caixa aquecendo ao sol do cerrado ou do semiárido nordestino, atingem temperaturas internas que destroem o eletrólito dos capacitores em dois a três anos — bem antes do ciclo de manutenção de qualquer propriedade. ESR sobe, capacitância cai, o barramento oscila. O equipamento passa a apresentar erros intermitentes que somem após reset e voltam sem explicação. É o sinal mais típico de capacitor degradado, e é o defeito mais frequentemente confundido com "problema de firmware" ou "falha aleatória".

O terceiro é a falha no módulo de controle por umidade e insetos. A vedação da caixa de campo se deteriora com os ciclos de calor e chuva. Umidade se condensa na placa de controle durante as variações de temperatura entre o dia e a madrugada. Micro-arco começa em trilha de sinal, queima componente SMD, o drive para de reconhecer os sensores internos. Em instalações no interior de Minas, Bahia e Goiás, a gente encontra insetos que constroem ninhos entre os dissipadores — o calor gerado por esse material orgânico causa curto progressivo que pode demorar meses para se manifestar como falha definitiva.

O quarto é a falha por energia regenerativa no barramento. Quando a bomba para de carga de forma brusca — entupimento, acionamento do sensor de poço seco, fechamento brusco de registro — a energia cinética do motor retorna ao barramento CC na forma de tensão regenerativa. O circuito de chopper existe para dissipar essa energia. Quando o transistor de chopper ou o resistor de braking falham, a tensão do barramento sobe além do limite de proteção e queima IGBTs ou capacitores. O sinal em campo é específico: a proteção de sobretensão DC ativa toda vez que a bomba para sob carga, mas o drive opera normalmente enquanto a bomba está girando.

O quinto é a falha no sensor de corrente de fase. O drive monitora a corrente de cada fase para proteger o motor e para implementar a lógica de detecção de poço seco. O sensor — geralmente resistor shunt ou transformador de corrente de alta frequência na placa de potência — pode sair de calibração ou queimar. Quando falha para o lado conservador, o drive desliga com falso alarme de sobrecorrente sem causa aparente. Quando falha para o lado permissivo, ele deixa de desligar quando há sobrecorrente real — e o motor queima junto, transformando um reparo simples num custo muito maior.

O sexto ponto, que não é defeito de componente mas gera os mesmos sintomas: dimensionamento incorreto. Drive subdimensionado para a bomba sofre sobreaquecimento crônico. IGBTs trabalham próximos do limite de corrente na partida, a proteção térmica ativa com frequência, e o equipamento falha precocemente. Não é defeito de fabricação. É projeto errado, e o reparo não vai resolver enquanto o dimensionamento não for corrigido.

## Como identificar

O diagnóstico começa ainda em campo, antes de qualquer desmontagem:

1. Anotar o código de erro exato no display — drives de bombeamento têm códigos específicos para regime de bomba (seco, sobrecarga, frequência mínima) que não existem em equipamentos on-grid; o código direciona o diagnóstico
2. Medir a tensão CC de entrada com irradiância acima de 600 W/m² — tensão abaixo do mínimo operacional do drive indica problema no string fotovoltaico, não no drive
3. Verificar temperatura da carcaça ao toque e inspecionar entradas de ventilação — poeira de campo bloqueia filtros em seis meses de operação sem manutenção
4. Desconectar o motor e medir resistência de isolamento entre cada fase de saída e terra — valor abaixo de 1 MΩ indica cabo ou motor comprometido, não o drive
5. Tentar partir com motor desconectado e monitorar a tensão do barramento DC durante a energização — barramento que oscila sem carga já aponta capacitor degradado
6. Inspecionar o interior da carcaça: capacitores abaulados, trilha escurecida na placa de controle, oxidação nos terminais, presença de material orgânico entre os componentes

Na bancada, o procedimento acrescenta:
- Medir cada IGBT com multímetro em modo diodo antes de aplicar qualquer tensão ao circuito
- Medir ESR e capacitância de cada capacitor do barramento com LCR meter — multímetro comum mede capacitância dentro da faixa nominal e não detecta ESR elevado; essa medição resolve ou descarta o segundo defeito mais comum
- Verificar placa de controle com lupa em busca de componentes SMD com marca de calor, trilhas com arco e conectores com oxidação
- Testar o circuito de gate drive de forma isolada antes de reinstalar os IGBTs

Energizar o drive sem verificar o estágio de potência primeiro é o caminho mais rápido para queimar uma placa de potência nova.

## Quando é falha eletrônica interna

Alguns padrões apontam para origem interna com consistência suficiente para justificar o envio para bancada sem tentar mais nada em campo:

- Drive desliga com erro de sobrecorrente mesmo com motor novo, cabo correto e irradiância adequada — troca de motor não mudou nada
- Erro ocorre no mesmo ponto da sequência de partida, independente do que está conectado na saída
- Display indica temperatura alta, mas dissipador e carcaça estão frios ao toque — sensor de temperatura com leitura falsa, não problema térmico real
- Comportamento errático sem padrão de carga ou horário: funciona uma hora, para, reinicia sozinho

Quando a causa é externa, o comportamento muda ao variar as condições: desconectar o motor, mudar o cabo, testar com irradiância diferente. Quando é interna, o padrão não muda.

Ainda não existe critério de triagem perfeito para essa distinção em campo. Às vezes você só descobre na bancada.

## Vale a pena consertar?

Drives solares de bombeamento de 1,5 kW a 7,5 kW custam entre R$ 1.200 e R$ 6.500 novos, dependendo da marca e do modelo. O reparo de falha em IGBT com capacitores íntegros fica em torno de 20% a 30% desse valor. Substituição de banco de capacitores fica abaixo disso.

O reparo é tecnicamente viável quando o dano está restrito ao estágio de potência ou ao banco de capacitores, sem comprometimento da placa de controle. A placa de controle é o critério determinante — é ela que concentra o valor intelectual do equipamento e a que é mais difícil de substituir por componente equivalente quando o dano é por arco elétrico.

Reparo inviável: placa de controle com dano por arco em múltiplos pontos, transformador de alta frequência fisicamente destruído, ou modelo fora de linha sem disponibilidade de componentes.

A conta é simples. Um drive de 3 kW que custa R$ 3.000 novo pode ser reparado por R$ 600 a R$ 900 numa falha de IGBT com capacitores íntegros. Condenar esse equipamento sem abrir e sem medir é jogar fora dinheiro do dono da propriedade — e geralmente é o que acontece quando não existe diagnóstico real.

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

- Âncora: "IGBTs em curto, com marca de aquecimento localizada na placa de potência" → Link para: Por que os IGBTs queimam em inversores solares: as 6 causas reais (Post 10)
- Âncora: "controlador de gate drive interpreta a situação de forma inadequada" → Link para: O que é o driver de IGBT e por que sua falha destrói o estágio de potência (Post 21)
- Âncora: "ESR sobe, capacitância cai, o barramento oscila" → Link para: Capacitores eletrolíticos em inversores solares: vida útil, degradação e quando trocar (Post 33)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "corrente de partida até seis vezes maior que a corrente nominal" → Fonte: WEG — Manual do Inversor CFW500 Solar (weg.net)
- Texto âncora: "resistência de isolamento entre cada fase de saída e terra" → Fonte: ABNT NBR 16149 — Sistemas fotovoltaicos — Características da interface de conexão com a rede elétrica de distribuição

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1504711434969-e33886168f5c?w=1200
→ Por que foi escolhida: Sistema de bombeamento solar em área rural, contexto direto do tema
→ Nome do arquivo: drive-solar-bombeamento-sistema-rural.webp
→ Alt Text (máx. 125 caracteres): Sistema de bombeamento solar fotovoltaico em área rural — drive solar e motor de bomba submersa
→ Legenda: Fig. 1 — Drive solar para bombeamento opera em condições de campo mais severas que inversores on-grid instalados em ambiente controlado
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200
→ Por que foi escolhida: Técnico com instrumento de medição, representando diagnóstico de IGBT e capacitor em bancada
→ Nome do arquivo: diagnostico-drive-solar-bombeamento-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Técnico realizando diagnóstico eletrônico de drive solar para bombeamento em bancada — medição de IGBT e ESR
→ Legenda: Fig. 2 — Diagnóstico correto começa pela medição do estágio de potência antes de qualquer energização
→ Onde inserir: Após H2 "Como identificar"
