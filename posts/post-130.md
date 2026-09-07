# Post 130 — Ventilador do inversor não gira: controle PWM, rolamento ou driver do ventilador?

---

[PALAVRA-CHAVE FOCO]
ventilador de inversor solar não gira

---

[TÍTULO SEO — Title Tag]
Ventilador do Inversor Solar Não Gira: PWM, Driver ou Rolamento?

---

[SLUG — URL do Post]
ventilador-inversor-solar-nao-gira-pwm-driver-rolamento

---

[META DESCRIPTION]
Ventilador do inversor solar parado? Entenda as causas reais: rolamento, driver PWM ou sensor de temperatura — e quando o reparo ainda vale a pena.

---

[CATEGORIA]
Manutenção e Diagnóstico

---

[TAGS]
ventilador inversor solar, driver PWM ventilador, rolamento inversor solar, superaquecimento inversor, diagnóstico placa inversor

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Ventilador do inversor solar que não gira** é um dos defeitos mais silenciosos e destrutivos nesse tipo de equipamento. O inversor continua operando normalmente — às vezes por semanas — até que a temperatura interna ultrapassa o limite de proteção e o IGBT queima. Aí o prejuízo real começa.

Na nossa bancada, esse defeito chega com um padrão quase sempre igual: o instalador trocou o ventilador inteiro, o equipamento voltou a funcionar por algumas semanas, e o ventilador parou de novo. Nesse ponto, o problema não está no ventilador — está no circuito que controla ele.

## O que causa esse problema

O ventilador de um inversor solar não é simplesmente um componente mecânico ligado a uma tensão fixa. Na maioria dos modelos modernos, ele é controlado por um sinal PWM gerado pelo microcontrolador da placa de controle, com base na leitura de um sensor NTC de temperatura.

A lógica é direta: com o inversor frio, o duty cycle do PWM é baixo ou nulo e o ventilador nem gira. Conforme a temperatura sobe, o duty cycle aumenta e o ventilador acelera. Quem executa essa lógica é o MCU da placa de controle, com base na tensão que o NTC entrega ao circuito analógico de aquisição.

As causas de falha se dividem em quatro caminhos distintos:

1. **Falha mecânica no rolamento** — o mais comum em campo. O rolamento de esfera ou a bucha seca gripam pelo acúmulo de poeira, calor e ausência de lubrificação. O motor tenta girar, consome corrente acima do nominal e o driver desabilita por proteção de sobrecorrente.

2. **Falha no driver do ventilador** — um MOSFET ou transistor na placa principal que recebe o sinal PWM e entrega corrente ao motor. Se esse componente queima em modo aberto, o sinal existe mas o motor não recebe potência.

3. **Falha no sinal PWM** — o MCU para de gerar o sinal, ou o sinal chega corrompido até o driver. Pode ocorrer por defeito no firmware, no próprio MCU, ou em componentes passivos do circuito de saída digital.

4. **Falha no sensor de temperatura NTC** — com resistência desviada, o MCU interpreta que o inversor está frio e nunca aciona o ventilador. O equipamento superaquece sem que nenhuma proteção ativa de resfriamento entre.

## Como identificar

A verificação começa com três medições básicas no conector do ventilador — antes de desmontar qualquer coisa:

1. Confirme a tensão de alimentação do ventilador. A maioria dos modelos opera com 12V DC ou 24V DC. Sem tensão no conector, o problema está no driver ou na alimentação auxiliar da placa.

2. Meça o sinal PWM com osciloscópio ou multímetro com função de frequência. Se o sinal existe e tem amplitude correta, mas o motor não gira, o problema é mecânico ou está no driver de potência.

3. Gire o cubo do ventilador com a mão. Resistência excessiva ou ruído de ranger indica rolamento gripado — nesse caso, troca mecânica primeiro.

4. Com o conector desconectado, meça a resistência do motor entre os terminais de alimentação. Um curto-circuito interno lê próximo de zero ohm. Isso pode ter queimado o driver de potência junto.

5. Meça a resistência do NTC com o inversor frio e compare com a tabela do datasheet do modelo. Desvio acima de 10% já gera leitura suficientemente errada para não ativar o ventilador nas condições normais de trabalho.

6. Verifique visualmente a superfície do dissipador de alumínio próximo ao IGBT. Oxidação escurecida ou resíduo de fluxo fundido na PCB ao redor indica que o superaquecimento já aconteceu.

Uma verificação que costuma ser ignorada: o estado da pasta térmica entre o IGBT e o dissipador. Se o ventilador ficou parado por tempo considerável, a pasta ressecou e a transferência de calor já está comprometida — independentemente do ventilador estar funcionando agora.

## Quando é falha eletrônica interna

Se a tensão de alimentação está presente no conector, o sinal PWM está sendo gerado pelo MCU com duty cycle adequado, mas o motor continua parado — a falha está no driver do ventilador.

O driver mais comum nesses circuitos é um MOSFET canal N com encapsulamento SOT-23 ou TO-220, modelos como AO3400 (baixa corrente) ou IRFZ44N (corrente mais alta). Quando queima em modo aberto, o sinal PWM não passa e o motor fica parado. Quando queima em curto, o ventilador gira em velocidade máxima sem nenhum controle de temperatura.

Antes de trocar o MOSFET, verificar o resistor de gate — tipicamente entre 10Ω e 33Ω em série. Esse resistor pode abrir sem danificar o MOSFET, com o exato mesmo sintoma: sinal na entrada, sem saída de corrente para o motor.

Há ainda uma falha menos óbvia. O diodo de roda livre em paralelo com o motor pode entrar em curto — nesse caso, a corrente circula pelo diodo em vez de acionar o enrolamento do motor. O MOSFET pode estar íntegro e o ventilador continua parado.

Não existe resposta antes de medir. Depende do que você vai encontrar na placa.

## Vale a pena consertar?

Na maioria dos casos, sim — e a conta é direta.

Um MOSFET driver custa menos de R$5. Um rolamento de reposição compatível com o ventilador sai entre R$3 e R$8. O ventilador completo, para as marcas mais comuns no mercado brasileiro, fica entre R$30 e R$90. O custo total de reparo raramente ultrapassa R$150 em peças.

O risco real é deixar o problema sem correção. Em inversores de 5kW, um IGBT queimado por superaquecimento gera uma conta de R$800 a R$1.500 só no estágio de potência — fora diagnóstico e mão de obra. Tudo por um componente de R$5 que não foi trocado.

Em regiões de interior, como o norte de Minas Gerais e o sertão nordestino, esse defeito aparece com frequência acima da média nacional. Temperatura ambiente mais alta, poeira fina que penetra no gabinete e abrasiona os rolamentos, inversores instalados em locais com ventilação insuficiente. A vida útil do ventilador, que nos manuais é estimada em 3 a 5 anos, cai para menos de dois na prática de campo.

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

- Âncora: 'o IGBT queima' → URL: /por-que-os-igbts-queimam-em-inversores-solares → Contexto: introdução, segundo parágrafo ("o IGBT queima")
- Âncora: 'pasta térmica' → URL: /pasta-termica-inversores-impacto-vida-util-igbt → Contexto: seção "Como identificar", último parágrafo
- Âncora: 'superaquecimento' → URL: /superaquecimento-inversor-solar-causas-consequencias → Contexto: seção "Vale a pena consertar?", terceiro parágrafo
- Âncora: 'falha mecânica vira problema eletrônico' → URL: /ventiladores-inversores-solares-falha-mecanica-problema-eletronico → Contexto: seção "O que causa esse problema"

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "sinal PWM" → URL: https://www.abnt.org.br/normalizacao/lista-de-publicacoes/abnt → Fonte: ABNT — norma de eficiência e segurança de inversores fotovoltaicos (NBR 16274)

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://www.pexels.com/search/cooling%20fan%20electronics/ (buscar "cooling fan electronic inverter")
→ Por que foi escolhida: ventilador de eletrônica industrial em destaque, diretamente relacionado ao tema de diagnóstico de ventilador de inversor
→ Nome do arquivo: ventilador-inversor-solar-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Ventilador de inversor solar com rolamento e circuito de controle PWM — diagnóstico de falha
→ Legenda: Fig. 1 — Ventilador de inversor solar: componente mecânico controlado por circuito eletrônico de potência
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://www.pexels.com/search/circuit%20board%20component/ (buscar "MOSFET PCB electronic circuit")
→ Por que foi escolhida: placa de circuito com componentes SMD representando o driver MOSFET do ventilador
→ Nome do arquivo: driver-pwm-ventilador-inversor-placa.webp
→ Alt Text (máx. 125 caracteres): Placa eletrônica de inversor solar com MOSFET driver PWM do ventilador e resistor de gate
→ Legenda: Fig. 2 — Driver do ventilador: MOSFET canal N controla corrente para o motor via sinal PWM da placa de controle
→ Onde inserir: Após H2 "Como identificar"
