# Post 68 — Sungrow Err 059: Sobretensão do Barramento DC — falha no circuito de descarga

---

[PALAVRA-CHAVE FOCO]
Sungrow Err 059 sobretensão barramento DC

---

[TÍTULO SEO — Title Tag]
Sungrow Err 059: Sobretensão Barramento DC — Diagnóstico

---

[SLUG — URL do Post]
sungrow-err-059-sobretensao-barramento-dc

---

[META DESCRIPTION]
Entenda o que causa o Err 059 no inversor Sungrow, como diagnosticar a falha no circuito de descarga e quando o reparo eletrônico é viável.

---

[CATEGORIA]
Códigos de Erro e Falhas

---

[TAGS]
Sungrow Err 059, sobretensão barramento DC, circuito de descarga inversor, diagnóstico inversor Sungrow, falha barramento CC

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **Sungrow Err 059** aparece, o inversor desliga e a geração vai a zero. O display mostra o código, às vezes sem nenhum detalhe adicional, e o instalador que chega ao local não encontra nada óbvio: strings aparentemente dentro da tensão esperada, temperatura razoável, nenhum barulho suspeito. O diagnóstico de mercado, nesse ponto, tende para "placa queimada" e o equipamento segue para descarte ou substituição.

Na nossa bancada, esse erro chega com frequência em modelos SG da Sungrow com dois a cinco anos de operação, vindos principalmente do interior de Minas Gerais e do Centro-Oeste, onde a rede da concessionária tem variações mais pronunciadas durante o pico de carga do verão. O padrão que a gente vê é sempre o mesmo: sistema funcionando por meses, início do verão com irradiância alta e produção no limite, primeiro desligamento com Err 059, e o inversor nunca mais sobe depois disso.

## O que causa o Err 059

No firmware dos inversores Sungrow, o Err 059 indica sobretensão no barramento CC intermediário — o que a documentação técnica descreve como "DC Bus Overvoltage, discharge circuit fault". O barramento CC é o estágio de alta tensão entre o lado fotovoltaico e o estágio de potência CA. Nos modelos SG monofásicos, essa tensão opera tipicamente entre 350 e 800 V. Nos modelos trifásicos, pode chegar a 1000 V em configurações de alta tensão.

O circuito de descarga tem duas funções. Na partida, ele controla a velocidade de carga do banco de capacitores do barramento através de um resistor de pré-carga — sem esse controle, o inrush de corrente destrói o banco no primeiro ciclo. No desligamento, ele fornece um caminho para que os capacitores se descarreguem até tensões seguras. A IEC 62109-1 exige descarga abaixo de 60 VDC em menos de 1 segundo em partes acessíveis do equipamento. Sem esse circuito operacional, o inversor não cumpre a norma de segurança.

As causas que chegam até nós com mais frequência:

1. Resistor de pré-carga aberto — tipicamente um resistor de potência cerâmico ou bobinadosem de 50 a 200 Ω, 25 a 100 W; quando abre, o banco de capacitores não carrega de forma controlada e a tensão dispara nos primeiros milissegundos da partida
2. MOSFET de bypass com falha em circuito aberto — esse componente deveria derivar o resistor de pré-carga depois que o barramento estabiliza; se falha em aberto, o resistor passa a conduzir carga contínua, aquece progressivamente e em semanas ou meses abre também
3. Banco de capacitores com capacitância reduzida — capacitores eletrolíticos com ESR elevado ou capacitância abaixo de 70% do valor nominal não conseguem amortecer picos durante transientes de produção; a tensão no barramento ultrapassa o limiar do comparador e o Err 059 é disparado
4. Divisor de tensão de medição com deriva — o circuito que monitora a tensão do barramento usa um divisor resistivo de alta impedância seguido de um amplificador operacional; se qualquer resistor nesse divisor deriva mais de 5% da tolerância, o controlador recebe leituras incorretas e registra sobretensão quando o barramento ainda está dentro do limite real
5. Retorno de energia pelo lado CA — durante distúrbios na rede com elevação súbita de tensão, energia pode fluir de volta pelo estágio de saída para o barramento CC; se o tempo de resposta da proteção não acompanha a transição, a tensão no barramento escala e o código é registrado
6. Sinal de gate ausente para o MOSFET de bypass — a placa de controle pode falhar ao gerar o pulso de comando correto por problema no driver de gate, mantendo o MOSFET desligado quando deveria comutar; o resultado prático é idêntico ao do MOSFET com falha em aberto, mas a causa está na lógica de controle, não no componente de potência

Nenhuma dessas falhas é visível de fora do gabinete.

## Como identificar na prática

Com o inversor desligado, strings desconectadas e pelo menos 5 minutos de espera para descarga passiva:

1. Descarregue ativamente o barramento antes de tocar em qualquer componente — conecte um resistor de 1 kΩ / 10 W com pontas isoladas entre os bornes do barramento e aguarde a tensão cair abaixo de 30 V no multímetro antes de prosseguir
2. Localize o resistor de pré-carga — nos modelos SG-S e SG-TL fica próximo ao bloco de entrada CC, geralmente com marcas de calor na cerâmica ou no substrato; meça com o multímetro na faixa de resistência: circuito aberto confirma a falha
3. Verifique o MOSFET de bypass em modo diodo: próximo de zero Ω nos dois sentidos indica falha em curto; resistência elevada nos dois sentidos indica falha em aberto
4. Inspecione o banco de capacitores: tampas abauladas, resíduo de eletrólito na base ou descoloração da PCB em volta do can indicam degradação; meça com medidor LCR quando disponível — capacitância abaixo de 70% do nominal ou ESR acima de 200 mΩ confirmam o diagnóstico
5. Meça os resistores do divisor de tensão na placa de controle com a placa sem alimentação — deriva superior a 5% em qualquer resistor suspeita o circuito de medição como causa raiz
6. Monitore a tensão do barramento com osciloscópio durante uma partida controlada a partir de uma fonte CC de bancada limitada a 400 VDC — a tensão deve subir linearmente na fase de pré-carga e estabilizar quando o MOSFET de bypass comuta; qualquer pico não amortecido ou ausência da comutação aponta a fase exata onde o circuito falhou
7. Verifique o sinal de gate no MOSFET de bypass durante a partida controlada: sinal presente mas MOSFET não comutando confirma falha do componente; ausência do sinal direciona o diagnóstico para o driver ou para a lógica de controle

Se o resistor está intacto e o MOSFET está intacto, o problema está no banco de capacitores ou no divisor de tensão. Ainda não existe resposta definitiva sem medir — depende do que você vai encontrar na placa.

## O erro mais comum do mercado

O que a gente vê com mais frequência: os capacitores são trocados sem que ninguém tenha verificado o MOSFET de bypass. A lógica parece razoável — "sobretensão no barramento, capacitores devem estar ruins". O banco é substituído (custo alto em modelos com banco de capacitância elevada), o sistema volta a funcionar por algumas semanas, e o Err 059 retorna. O MOSFET que deveria ter sido diagnosticado na primeira intervenção continuou danificado e passou a degradar os capacitores novos progressivamente.

O segundo erro é trocar o resistor de pré-carga sem entender por que ele abriu. Se o MOSFET de bypass estava em aberto e o resistor ficou conduzindo carga contínua por meses, ele queimou como efeito secundário. Trocar só o resistor e manter o MOSFET danificado resolve o sintoma por um período curto. Em duas a oito semanas, o resistor novo queima pelo mesmo mecanismo — e o técnico volta ao ponto de partida sem saber o porquê.

O diagnóstico tem que mapear a causa raiz, não apenas o componente visivelmente danificado.

## Quando o reparo é viável

O Err 059 como código primário, sem eventos associados de curto no estágio de potência ou falha de IGBT, é um dos cenários com melhor taxa de recuperação que chegam até nós.

Critérios que pesam a favor do reparo:

- Resistor de pré-carga aberto sem dano térmico secundário na PCB — reparo de componente único, componentes disponíveis no mercado nacional sem necessidade de importação
- MOSFET de bypass com falha isolada sem dano no circuito de gate drive — substituição por componente equivalente com os mesmos parâmetros de tensão e corrente
- Banco de capacitores degradado com estágio de potência preservado — troca do banco com verificação de ESR e capacitância pós-reparo antes de religar
- Firmware inicializando normalmente até o ponto de desligamento — microcontrolador e memória operacionais indicam que o dano está no circuito de potência, não na lógica de controle

Inversores Sungrow série SG de 3 a 15 kW com Err 059 como código único, sem histórico de falha de IGBT ou surto por descarga atmosférica, têm prognóstico favorável na bancada. O laudo define o escopo real antes de qualquer comprometimento financeiro.

## Conclusão

O Err 059 registra que a tensão do barramento CC ultrapassou o limite — mas não diz qual componente falhou. Resistor aberto, MOSFET em aberto, banco degradado, divisor desviado: o código é o mesmo para todos. Às vezes é um resistor de cinco reais. Às vezes é o banco inteiro. Sem abrir a placa e medir, não tem como saber.

Condenar o equipamento com base no código, sem diagnóstico, é jogar fora um inversor que provavelmente tem reparo.

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

- Âncora: 'capacitores eletrolíticos em inversores' → URL: /capacitores-eletrolíticos-inversores-vida-util-degradacao → Contexto: seção "O que causa o Err 059", ao mencionar banco de capacitores com capacitância reduzida
- Âncora: 'por que os IGBTs queimam' → URL: /por-que-os-igbts-queimam-inversores-solares → Contexto: seção "Quando o reparo é viável", ao diferenciar falha do circuito de descarga de falha no estágio de potência
- Âncora: 'placa de controle vs. placa de potência' → URL: /placa-controle-vs-placa-potencia-onde-esta-o-defeito → Contexto: seção "Como identificar na prática", ao redirecionar o diagnóstico para lógica de controle vs. componente de potência
- Âncora: 'relés de bypass em inversores solares' → URL: /reles-bypass-inversores-solares-falha-silenciosa → Contexto: seção "O que causa o Err 059", ao introduzir a função do MOSFET de bypass no circuito de pré-carga
- Âncora: 'inversor fora de garantia' → URL: /inversor-fora-de-garantia-trocar-ou-reparar → Contexto: seção "Quando o reparo é viável", ao avaliar a análise técnica e financeira do reparo

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62109-1" → URL: https://www.iec.ch/homepage → Fonte: IEC — norma internacional de segurança para conversores de energia fotovoltaica, requisito de descarga abaixo de 60 VDC
- Texto âncora: "descarga abaixo de 60 VDC" → URL: https://www.gov.br/inmetro/pt-br → Fonte: INMETRO — certificação de inversores fotovoltaicos no Brasil com base nas normas IEC 62109

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=1200
→ Por que foi escolhida: Placa eletrônica de potência com capacitores e componentes de alta tensão visíveis, contexto direto ao barramento CC e circuito de descarga
→ Nome do arquivo: sungrow-err-059-barramento-dc-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Placa de inversor Sungrow com banco de capacitores do barramento DC — diagnóstico do Err 059
→ Legenda: Fig. 1 — Circuito do barramento CC em inversor Sungrow: banco de capacitores e circuito de pré-carga, componentes centrais do Err 059
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Componentes eletrônicos em bancada com multímetro e osciloscópio, adequado para a seção de diagnóstico prático
→ Nome do arquivo: sungrow-err-059-diagnostico-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Bancada de diagnóstico eletrônico com multímetro e placa de inversor — verificação do circuito de descarga Sungrow
→ Legenda: Fig. 2 — Diagnóstico do circuito de descarga na bancada: medição do resistor de pré-carga e verificação do MOSFET de bypass
→ Onde inserir: Após H2 "Como identificar na prática"
