# Post 110 — Sensor de Corrente (Shunt e Efeito Hall): Leitura Falsa e Diagnóstico

---

[PALAVRA-CHAVE FOCO]
sensor de corrente inversor solar diagnóstico

---

[TÍTULO SEO — Title Tag]
Sensor de Corrente no Inversor Solar: Leitura Falsa

---

[SLUG — URL do Post]
sensor-corrente-inversor-solar-leitura-falsa-diagnostico

---

[META DESCRIPTION]
Shunt e sensor Hall com leitura falsa em inversores: causas reais, diagnóstico na bancada e quando o reparo é viável.

---

[CATEGORIA]
Análise Técnica de Componentes

---

[TAGS]
sensor de corrente inversor solar, sensor Hall fotovoltaico, shunt inversor diagnóstico, leitura falsa de corrente, falha de medição inversor

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **sensor de corrente em inversores solares** é um dos componentes menos discutidos no mercado — e um dos mais críticos. É ele que informa ao processador quanto está fluindo por cada estágio do circuito. Quando essa leitura falha, o inversor passa a tomar decisões com base em dados errados: pode deixar de acionar a proteção em uma sobrecorrente real, ou pode desligar o sistema inteiro por uma corrente que não existe.

Na nossa bancada, esse tipo de problema chega com um padrão quase sempre igual: técnico ou integrador com um inversor que "travou na proteção" ou "subestima a geração", sem código de erro claro, sem componente visualmente queimado. A gente abre o equipamento e encontra um shunt resistivo com resistência fora do nominal ou um sensor Hall com desvio de ponto zero. O inversor não estava quebrado do jeito que parecia. A causa era na camada de medição.

## O que causa esse problema

Dois tipos de sensor de corrente dominam os inversores solares modernos: **resistores shunt** e **sensores de efeito Hall**.

O shunt é um resistor de resistência muito baixa — tipicamente entre 100 µΩ e 10 mΩ — inserido em série no caminho da corrente. A queda de tensão sobre ele é amplificada e convertida na leitura de corrente pelo circuito de condicionamento. O método é simples, direto, confiável para muitas aplicações. O limite aparece com o tempo e com o calor: a resistência do shunt deriva, o valor muda, e a leitura de corrente se afasta da realidade sem que nada na aparência do componente indique o problema.

O sensor Hall não mede a corrente por contato elétrico. Ele detecta o campo magnético gerado pelo fluxo de corrente ao redor de um núcleo toroidal e converte esse campo em tensão proporcional. A vantagem é isolação galvânica — necessária em inversores on-grid por norma e por segurança. Os modelos mais comuns em inversores são fabricados pela LEM (séries LA, HC e HTFS), Allegro e Honeywell. O modo de falha do Hall é diferente do shunt: desvio de ponto zero por temperatura, perda de sensibilidade e, nos casos mais graves, desmagnetização do núcleo toroidal após passagem de corrente muito acima do nominal.

O calor é o gatilho mais frequente para os dois tipos. Em regiões como Mato Grosso, Tocantins e Bahia, inversores instalados em caixas metálicas fechadas sob incidência solar direta chegam a 70°C internamente durante horas por dia. Nessa condição, a deriva dos shunts e a instabilidade dos sensores Hall se aceleram consideravelmente.

## Como identificar

Os sinais de leitura falsa de corrente nem sempre disparam um código de erro explícito. Muitas vezes o inversor opera sem nenhum alerta — só com dados errados.

O que chega até nós com mais frequência:

1. Potência gerada consistentemente abaixo do esperado — descartadas sombra e sujeira no painel, a leitura de corrente CC está errada na entrada MPPT
2. Inversor exibe corrente CC negativa ou valor impossível no display ou no app de monitoramento
3. Proteção de sobrecorrente dispara repetidamente com carga normal instalada
4. Inversor não dispara proteção mesmo com corrente visivelmente acima do nominal — o pior cenário, porque a proteção deixou de funcionar
5. Em inversores com múltiplas strings: uma entrada aparece com corrente muito diferente das outras sem justificativa no layout do painel
6. Leitura de corrente completamente estática, sem variação mesmo com o sol oscilando ao longo do dia
7. Em inversores híbridos: divergência entre o que o BMS reporta de corrente de carga/descarga e o que o inversor exibe

Na bancada, o ponto de partida é o osciloscópio na saída analógica do sensor. Sensores Hall de laço aberto entregam tensão proporcional à corrente com referência em Vcc/2. Com corrente zero fluindo pelo barramento, a saída deve estar estabilizada exatamente na metade da tensão de alimentação. Qualquer desvio nessa condição aponta problema de offset. Com corrente aplicada de valor conhecido, verifica-se se o ganho está dentro do que o datasheet do fabricante especifica.

Para o shunt, o método correto é medição de resistência em 4 fios (Kelvin). Com resistências tão baixas, qualquer resistência de contato dos próprios cabos de medição distorce o resultado com um instrumento comum de 2 fios. Compara-se o valor medido com o nominal e calcula-se o desvio percentual — acima de 2% já compromete a precisão da leitura em inversores com proteção afinada.

A alimentação do sensor também entra obrigatoriamente no checklist. Sensores Hall operam com ±15 V ou +5 V regulados dependendo do modelo. Tensão de alimentação fora do especificado contamina a leitura mesmo que o sensor em si esteja íntegro. Vale cruzar esse diagnóstico com o que foi encontrado em sensores de temperatura com comportamento similar de leitura falsa — o circuito de condicionamento compartilhado entre os dois pode ser a causa comum.

## Quando é falha eletrônica interna

Nem todo erro de leitura vem do sensor. O sinal gerado passa por um circuito de condicionamento — amplificadores operacionais, filtros RC, conversor analógico-digital — antes de chegar ao microcontrolador. Qualquer ponto desse caminho pode introduzir erro ou instabilidade.

A distinção prática: mede-se a saída do sensor diretamente nos seus pinos de saída. Se o sinal já está errado antes de entrar no restante do circuito, o sensor é o problema. Se a saída do sensor está dentro da especificação mas a leitura no lado do processador diverge, o problema está no condicionamento. O diagnóstico em nível de placa é o que separa esses dois cenários com precisão — não tem como fazer isso sem ler o circuito e medir ponto a ponto.

Ponto de solda frio no shunt é mais frequente do que parece. O sinal vai e vem: o inversor apresenta erro intermitente, às vezes "resolvido" com repercussão da placa até o próximo ciclo térmico desfazer o contato.

A desmagnetização do núcleo do sensor Hall acontece após uma falha severa anterior no estágio de potência. Um IGBT queimado em curto pode fazer passar pelo barramento uma corrente muito acima do nominal do sensor. O núcleo perde parte da magnetização e a leitura fica permanentemente comprometida. O técnico substitui o IGBT queimado, o inversor volta a funcionar — mas com leitura de corrente errada, porque o sensor foi afetado junto na mesma falha.

Essa combinação passa despercebida se o diagnóstico não contemplar a verificação dos sensores depois do reparo do estágio de potência.

## Vale a pena consertar?

Na maioria dos casos, sim.

Um sensor Hall LEM novo custa entre R$ 80 e R$ 250 dependendo do modelo e da corrente nominal. O shunt resistivo é mais barato ainda — em geral abaixo de R$ 30 para os modelos mais comuns. O trabalho está em identificar com precisão qual sensor falhou, obter o componente correto e verificar a calibração depois da troca.

O que torna o reparo mais trabalhoso: alguns fabricantes integram o sensor em um módulo sem referência de componente direta. Nesses casos, o caminho é identificar o equivalente por especificação — corrente nominal, tensão de alimentação, sensibilidade em mV/A — e adaptar o circuito de condicionamento se o ganho for diferente. Exige leitura de esquemático e, às vezes, acesso ao parâmetro de calibração no firmware.

A pergunta que define a decisão: o inversor ainda gera energia mas mede errado, ou parou completamente? Se a geração está normal e só a leitura está comprometida, o problema é de medição — não de potência. O custo do sensor cabe facilmente na conta. Se o inversor parou, a análise muda, mas raramente o sensor de corrente sozinho é responsável pela parada total.

O risco real de não reparar é outro: um sensor de corrente com offset alto pode deixar a proteção de sobrecorrente inoperante. A proteção existe, mas age em um valor de corrente que o sensor nunca vai reportar. Isso não é um problema estético no display — é uma condição insegura de operação.

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

[LINKS INTERNOS SUGERIDOS]

- Âncora: 'IGBT queimado' → URL: /igbt-queimado-inversor-solar-6-causas → Contexto: seção "Quando é falha eletrônica interna", ao descrever como um curto no IGBT pode desmagnetizar o sensor Hall na mesma falha
- Âncora: 'sensores de temperatura com comportamento similar de leitura falsa' → URL: /sensor-de-temperatura-inversor-solar-leitura-falsa → Contexto: seção "Como identificar", ao mencionar que o circuito de condicionamento compartilhado pode ser causa comum de leituras incorretas
- Âncora: 'diagnóstico em nível de placa' → URL: /diagnostico-nivel-de-placa-inversor-solar → Contexto: seção "Quando é falha eletrônica interna", ao explicar que o diagnóstico ponto a ponto é o que diferencia falha no sensor da falha no condicionamento
- Âncora: 'IGBT queimado em curto' → URL: /igbt-queimado-inversor-solar-6-causas → Contexto: segundo uso na seção "Quando é falha eletrônica interna", reforçando a relação entre falha de IGBT e comprometimento do sensor Hall
- Âncora: 'placa de controle' → URL: /placa-controle-vs-potencia-como-diferenciar-defeito-inversor-solar → Contexto: seção "Vale a pena consertar?", ao mencionar parâmetros de calibração no firmware e a necessidade de acesso à placa principal

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "isolação galvânica" → URL: https://www.iec.ch/homepage → Fonte: IEC 62109-1 — norma internacional de segurança para conversores de potência em sistemas fotovoltaicos, que define requisitos de isolação entre circuitos CC e CA
- Texto âncora: "normas de instalação de sistemas fotovoltaicos" → URL: https://www.abnt.org.br → Fonte: ABNT NBR 16274 — norma brasileira para comissionamento de sistemas fotovoltaicos, inclui requisitos de instrumentação e medição de corrente no sistema

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: placa eletrônica com ICs, resistores e componentes SMD visíveis, representando a camada de medição e condicionamento de sinal de um inversor
→ Nome do arquivo: sensor-corrente-inversor-solar-shunt-hall.webp
→ Alt Text (máx. 125 caracteres): Placa eletrônica com sensor de corrente e circuito de condicionamento — diagnóstico de leitura falsa em inversor solar
→ Legenda: Fig. 1 — O sensor de corrente e seu circuito de condicionamento são responsáveis por toda a leitura de corrente que o processador usa para proteger e controlar o inversor
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=1200
→ Por que foi escolhida: técnico realizando medição com multímetro em bancada eletrônica, contexto direto de diagnóstico de componente
→ Nome do arquivo: sensor-corrente-inversor-solar-diagnostico-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensão de saída de sensor Hall em bancada de diagnóstico de inversor solar fotovoltaico
→ Legenda: Fig. 2 — Com corrente zero no barramento, a saída do sensor Hall deve estar estabilizada em exatamente metade da tensão de alimentação — qualquer desvio aponta falha de offset
→ Onde inserir: Após H2 "Como identificar"
