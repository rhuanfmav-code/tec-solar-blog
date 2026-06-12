# Post 71 — Sensores de temperatura em inversores: como identificar leitura falsa

---

[PALAVRA-CHAVE FOCO]
sensor de temperatura inversor solar leitura falsa

---

[TÍTULO SEO — Title Tag]
Sensor de Temperatura Inversor Solar: Leitura Falsa

---

[SLUG — URL do Post]
sensor-de-temperatura-inversor-solar-leitura-falsa

---

[META DESCRIPTION]
Sensor com leitura falsa desliga o inversor sem motivo real. Como diagnosticar o termistor NTC e identificar quando o reparo é viável.

---

[CATEGORIA]
Manutenção e Diagnóstico

---

[TAGS]
sensor de temperatura inversor solar, termistor NTC inversor, leitura falsa temperatura inversor, diagnóstico superaquecimento inversor, reparo inversor solar

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

Um **sensor de temperatura com leitura falsa** é uma das falhas mais silenciosas em inversores solares. O equipamento desliga por superaquecimento, o técnico verifica ventilador e dissipador, encontra tudo funcionando, e fica sem resposta. O próximo passo costuma ser orçamento de inversor novo.

Na nossa bancada, esse padrão chega toda semana. Já recebemos inversores de São Paulo, Bahia e do interior de Mato Grosso com o mesmo histórico: desligamentos térmicos repetidos, sistema de refrigeração ok, nenhuma causa aparente. Em todos os casos, o termistor estava com problema. Não o IGBT, não o ventilador. O sensor.

## O que causa esse problema

A maioria dos inversores usa termistores NTC (Coeficiente de Temperatura Negativo) para monitorar a temperatura do dissipador e dos IGBTs. O princípio é direto: quanto mais quente, menor a resistência elétrica do componente. A placa de controle lê essa resistência via divisor de tensão e converte em graus Celsius.

As falhas ocorrem em quatro modos:

1. **Circuito aberto** — a resistência vai a infinito. A placa interpreta como temperatura extrema e dispara o erro de superaquecimento, mesmo com o inversor completamente frio.
2. **Curto-circuito** — a resistência vai a zero. A placa lê temperatura impossível (negativa ou absurda) e pode travar o sistema por detecção de erro de sinal.
3. **Deriva de característica** — o termistor ainda funciona, mas a curva de resistência mudou. Lê 88°C quando a temperatura real é 58°C. O inversor desliga dentro de limites operacionais seguros, sem nenhum risco real.
4. **Conector oxidado** — não é falha do componente em si, mas o efeito é o mesmo. Em inversores instalados no litoral ou no semiárido nordestino, a oxidação dos pinos adiciona resistência parasita na leitura. A placa enxerga 15 a 20°C a mais sem que nenhum componente eletrônico tenha falhado.

Esse quarto modo é o que mais gera confusão. O técnico mede o termistor, encontra resistência dentro do esperado, e descarta o sensor como causa. Mas o problema estava no conector.

## Como identificar

O diagnóstico começa com uma comparação direta entre o que o inversor reporta e o que você mede externamente.

1. Com o inversor operando, registre a temperatura exibida no display ou no software de monitoramento
2. Posicione um termopar tipo K (ou câmera termográfica) no mesmo ponto físico onde o sensor está montado no dissipador
3. Diferença acima de 8°C indica problema — não é variação normal de medição
4. Desligue o inversor e remova a tensão completamente. Desconecte o termistor do conector da placa
5. Meça a resistência com multímetro digital. NTC padrão de 10kΩ deve ler próximo a esse valor a 25°C — consulte a tabela do fabricante para o modelo exato
6. Resistência em aberto (OL no display do multímetro) ou em zero? Sensor danificado, troca direta
7. Limpe os pinos do conector com álcool isopropílico e verifique oxidação visual e folga mecânica nos terminais

Termistor com deriva de característica pode parecer normal na medição estática a temperatura ambiente. O problema só aparece quando aquece. Use um secador de ar quente para aquecê-lo progressivamente e refaça a leitura em diferentes pontos, comparando com a curva teórica do fabricante.

## Quando é falha eletrônica interna

Quando o termistor mede correto e o conector está limpo, mas a leitura no display ainda está errada, o problema está na placa de controle.

O circuito de condicionamento de sinal — divisor de tensão, resistor de pull-up ou canal ADC do microcontrolador — pode ter um componente derivado. Para isolar isso: desconecte o termistor da placa e substitua temporariamente por um resistor fixo de 10kΩ. Em temperatura ambiente, a placa deveria mostrar próximo a 25°C. Se mostrar outro valor, o circuito de leitura está com problema, não o sensor externo.

Isso é diagnóstico em nível de componente. E muda completamente o que precisa ser substituído.

## Vale a pena consertar?

Quase sempre.

Um termistor NTC de 10kΩ custa entre R$ 5 e R$ 15. O tipo exato — coeficiente B, dimensão física, encapsulamento — está no datasheet do inversor. Na falta do datasheet, a curva pode ser determinada medindo o componente em pelo menos dois pontos de temperatura e comparando com tabelas padrão de NTC.

Inversor de 5 kW parado por um sensor de R$ 8 resolve em bancada em menos de uma hora.

A conta muda quando o sensor é interno ao IGBT — um diodo de temperatura embutido no die semicondutor. Nesse caso não é possível substituir o sensor isolado. Mas nem isso significa condenar o inversor: o que precisa ser avaliado é o IGBT como conjunto. E há situações em que o componente físico ainda funciona e o problema está na interpretação do sinal na placa de controle.

Não existe resposta definitiva sem medir. Depende do que você vai encontrar na placa.

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
- Âncora: 'superaquecimento de inversor solar' → URL: /superaquecimento-inversor-solar-causas-prevencao → Contexto: seção "O que causa esse problema", ao mencionar desligamentos térmicos
- Âncora: 'IGBTs' → URL: /por-que-os-igbts-queimam-inversores-solares → Contexto: introdução, ao citar IGBT como causa descartada
- Âncora: 'placa de controle' → URL: /placa-de-controle-vs-placa-de-potencia-onde-esta-o-defeito → Contexto: seção "Quando é falha eletrônica interna"
- Âncora: 'driver de IGBT' → URL: /o-que-e-driver-igbt-falha-estagio-de-potencia → Contexto: seção "Quando é falha eletrônica interna", ao mencionar componentes da placa

---

[LINKS EXTERNOS SUGERIDOS]
- Texto âncora: "NTC (Coeficiente de Temperatura Negativo)" → URL: https://www.abnt.org.br → Fonte: ABNT — normas técnicas de componentes eletrônicos
- Texto âncora: "dissipador" → URL: https://www.inmetro.gov.br → Fonte: INMETRO — certificações de inversores solares fotovoltaicos

---

[IMAGEM PRINCIPAL — USE ESTA]
IMAGEM PRINCIPAL:
→ URL para download: buscar "NTC thermistor circuit board electronics" em unsplash.com ou pexels.com
→ Por que foi escolhida: placa eletrônica com componentes visíveis — contextualiza diagnóstico de termistor em nível de componente
→ Nome do arquivo: sensor-temperatura-inversor-solar-termistor.webp
→ Alt Text (máx. 125 caracteres): Termistor NTC em placa de inversor solar — diagnóstico de sensor de temperatura com leitura falsa
→ Legenda: Fig. 1 — Termistor NTC no dissipador: ponto de falha mais comum em erros de superaquecimento
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]
IMAGEM SECUNDÁRIA:
→ URL para download: buscar "multimeter electronics technician repair" em pexels.com ou unsplash.com
→ Por que foi escolhida: técnico com multímetro — ilustra o processo de medição de resistência do termistor
→ Nome do arquivo: diagnostico-termistor-multimetro-inversor-solar.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo resistência de termistor NTC com multímetro — diagnóstico de leitura falsa em inversor solar
→ Legenda: Fig. 2 — Resistência OL no multímetro indica termistor em circuito aberto
→ Onde inserir: Após H2 "Como identificar"
