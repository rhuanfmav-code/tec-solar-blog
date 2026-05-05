# Post 39 — Deye F17: Sobretensão do Barramento DC — Falha no Circuito de Pré-carga

---

[PALAVRA-CHAVE FOCO]
Deye F17 sobretensão barramento DC

---

[TÍTULO SEO — Title Tag]
Deye F17: Sobretensão do Barramento DC — Diagnóstico

---

[SLUG — URL do Post]
deye-f17-sobretensao-barramento-dc

---

[META DESCRIPTION]
O erro Deye F17 indica sobretensão no barramento DC. Saiba diagnosticar a falha no circuito de pré-carga antes de condenar o inversor.

---

[CATEGORIA]
Códigos de Erro e Falhas

---

[TAGS]
Deye F17, sobretensão barramento DC, circuito de pré-carga, inversor Deye com erro, diagnóstico inversor solar

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O erro **Deye F17** aparece no display e o técnico vai direto medir a string. Tensão dentro do limite, painéis funcionando, nada óbvio. O inversor continua parado. A suspeita migra para o equipamento em si e, sem uma investigação mais funda, o diagnóstico trava.

Na nossa bancada, esse erro chega com frequência associado a uma causa que raramente aparece no checklist de campo: falha no circuito de pré-carga. O barramento DC entra em sobretensão não por causa dos painéis, mas porque o circuito responsável por controlar a carga inicial dos capacitores deixou de funcionar. Essa distinção muda o diagnóstico do início ao fim.

## O que causa o erro Deye F17

O barramento DC é o link de tensão intermediário entre a entrada fotovoltaica e o estágio de inversão. Em inversores Deye de 5 a 15 kW, esse barramento opera tipicamente entre 350 V e 750 V. Os capacitores eletrolíticos de filtro conectados a esse ponto estabilizam a tensão e absorvem os transientes gerados pelas chaves IGBT durante a comutação.

O problema começa no momento em que o inversor tenta ligar. Os capacitores estão descarregados — tensão zero. Se a tensão da string for aplicada diretamente, a corrente de inrush pode destruir IGBTs e capacitores em milissegundos. O circuito de pré-carga resolve isso: insere um resistor em série temporariamente, limitando a taxa de crescimento da tensão no barramento. Quando a tensão do barramento se iguala à tensão de entrada, um relé de bypass curto-circuita o resistor e o inversor entra em operação.

O F17 dispara quando o firmware detecta tensão acima do limite máximo no barramento — geralmente 120% a 130% da tensão nominal. As causas:

1. **Relé de bypass com contatos abertos** — o relé que deveria fechar após a pré-carga permanece aberto. A corrente continua passando pelo resistor, gerando instabilidade de tensão no barramento.
2. **Resistor de pré-carga queimado ou com valor alterado** — muda a taxa de carga do barramento, gerando picos durante a inicialização que o firmware interpreta como sobretensão.
3. **Capacitores de barramento com ESR elevada** — capacitores degradados perdem a capacidade de absorver transientes. A tensão sobe mais rápido do que o controle consegue reagir.
4. **Circuito de medição de tensão com defeito** — divisor resistivo que alimenta o ADC da placa de controle fora de especificação. O inversor lê sobretensão mesmo com o barramento em nível normal.
5. **Tensão de string efetivamente alta** — em dias frios no sul do Brasil, especialmente em Santa Catarina e Rio Grande do Sul, a Voc dos painéis pode ultrapassar os limites de projeto. Inversores instalados no limite do MPPT máximo, sem margem para temperatura mínima, disparam F17 de manhã cedo — quando os painéis ainda estão frios — e normalizam antes do técnico chegar.
6. **Driver de IGBT com saída em estado anômalo** — driver travado em nível alto força condução incorreta no estágio de potência, gerando realimentação de tensão no barramento durante a tentativa de inicialização.

Falha no circuito de pré-carga é a causa raiz na maioria dos casos que chegam até nós. O resto é consequência.

## Como identificar na prática

O diagnóstico é sequencial. Pular etapas gera diagnóstico errado.

1. **Medir a tensão de string com o inversor desligado** — multímetro CAT III nas entradas CC. Comparar com a Voc máxima admissível do modelo específico conforme o manual do fabricante.
2. **Medir a tensão do barramento DC com o inversor em standby** — nos terminais dos capacitores de filtro ou nos pontos de teste do PCB. Acima de 750 V em modelos com barramento nominal de 600 V confirma sobretensão real.
3. **Verificar resistência do resistor de pré-carga** — com o equipamento desligado e capacitores completamente descarregados. Resistência típica: entre 10 Ω e 100 Ω dependendo da potência do modelo. Circuito aberto é falha confirmada.
4. **Testar o relé de bypass** — aplicar tensão de bobina e medir resistência nos contatos. Deve ficar abaixo de 1 Ω com bobina energizada. Contatos carbonizados muitas vezes ainda fecham parcialmente, gerando resistência residual que aquece o relé durante a operação.
   *Contatos parcialmente fundidos podem ser imperceptíveis na medição a frio — checar com carga aplicada quando possível.*
5. **Medir ESR dos capacitores de barramento** — com medidor LCR. ESR acima de 3x o valor nominal do datasheet indica degradação que justifica a substituição.
6. **Inspecionar a placa visualmente** — trilhas escurecidas próximas ao relé, componentes inchados, resíduo de eletrólito nos capacitores. Em inversores que chegam do Norte do país — Pará, Tocantins, Maranhão — a combinação de calor intenso e umidade acelera essa degradação de forma significativa.

Se resistor e relé estiverem íntegros e a string estiver dentro dos limites, investigar o divisor resistivo do circuito de medição de tensão do barramento.

## O erro mais comum do mercado

A maioria dos técnicos substitui a placa de potência inteira sem investigar o circuito de pré-carga.

O raciocínio é compreensível: F17, mediu a string, está normal, logo é defeito interno — placa de potência. Só que "defeito interno" não é diagnóstico. É uma categoria. Dentro dessa categoria, existe diferença enorme entre trocar o resistor de R$ 8 e substituir a placa inteira por R$ 2.800.

O segundo erro é não correlacionar o horário do alarme com a temperatura ambiente. Quando o F17 aparece sistematicamente entre 6h e 8h da manhã e desaparece depois, o problema provavelmente não está no circuito de pré-carga — está no dimensionamento da string para temperatura mínima do local. Esse diagnóstico não requer bancada. Requer atenção ao padrão temporal dos registros de falha.

Ainda não existe atalho para separar esses dois cenários sem medir. Depende do que você vai encontrar na placa.

## Quando o reparo é viável

Para o F17, a viabilidade de reparo é alta na maioria dos casos.

Falha no resistor de pré-carga é reparo direto — componente de baixo custo, substituição sem complexidade, desde que a especificação original seja recuperada (potência, valor ôhmico e coeficiente de temperatura). Falha no relé de bypass também é viável: relés de sinal com capacidade de 10 a 30 A têm boa disponibilidade no mercado nacional. Capacitores de barramento degradados são trocáveis quando o estágio de potência não foi danificado em cascata — capacitores eletrolíticos de alta tensão na faixa de 400 a 450 V com capacitância entre 1.000 e 4.700 µF são encontrados sem dificuldade.

Quando o IGBT queimou por inrush sem controle, o reparo fica mais complexo, mas continua viável em modelos com IGBTs discretos. Módulos integrados dependem de disponibilidade de sourcing específico para o modelo.

O único cenário que inviabiliza é dano em cascata extenso — múltiplos componentes da placa de controle afetados simultaneamente. Isso é exceção.

## Conclusão

O Deye F17 não exige troca de inversor. Na maior parte dos casos que chegam para diagnóstico, a causa está em um componente do circuito de pré-carga — um conjunto de peças de baixo custo que, sem diagnóstico, leva à substituição indevida da placa inteira.

Antes de qualquer decisão, meça o resistor, teste o relé e verifique os capacitores.

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

- Âncora: 'por que os IGBTs queimam' → URL: /por-que-os-igbts-queimam-em-inversores-solares → Contexto: seção "O que causa o erro Deye F17", item 6, após mencionar IGBT
- Âncora: 'capacitores eletrolíticos de filtro' → URL: /capacitores-eletrolíticos-inversores-vida-util-degradacao → Contexto: seção "O que causa o erro Deye F17", segundo parágrafo
- Âncora: 'driver de IGBT' → URL: /o-que-e-o-driver-de-igbt-falha-estagio-de-potencia → Contexto: seção "O que causa o erro Deye F17", item 6

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "Voc máxima admissível do modelo" → URL: https://www.aneel.gov.br/resolucoes-normativas → Fonte: ANEEL — referência regulatória para sistemas fotovoltaicos conectados à rede

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://unsplash.com/photos/solar-inverter-circuit-board (buscar por "solar inverter circuit board" em unsplash.com)
→ Por que foi escolhida: Mostra placa de circuito de inversor solar, relevante ao diagnóstico eletrônico do F17
→ Nome do arquivo: deye-f17-barramento-dc-placa-inversor.webp
→ Alt Text (máx. 125 caracteres): Placa de circuito de inversor solar Deye com componentes do barramento DC e relé de pré-carga
→ Legenda: Fig. 1 — Circuito do barramento DC em inversor solar — ponto crítico no erro Deye F17
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://unsplash.com/photos/multimeter-electronics-measurement (buscar por "multimeter electronics repair" em unsplash.com)
→ Por que foi escolhida: Técnico medindo componentes eletrônicos com multímetro, representando o diagnóstico prático do barramento DC
→ Nome do arquivo: diagnostico-barramento-dc-inversor-deye-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensão do barramento DC em inversor solar com multímetro durante diagnóstico do erro F17
→ Legenda: Fig. 2 — Medição sequencial do barramento DC e componentes de pré-carga no diagnóstico do Deye F17
→ Onde inserir: Após H2 "Como identificar na prática"
