# Post 66 — Deye F23: Falha no Relé de Saída — relé de bypass com defeito, reparo possível?

---

[PALAVRA-CHAVE FOCO]
Deye F23 falha relé de saída

---

[TÍTULO SEO — Title Tag]
Deye F23: Falha no Relé de Saída — Diagnóstico e Reparo

---

[SLUG — URL do Post]
deye-f23-falha-rele-saida

---

[META DESCRIPTION]
Entenda o que causa o erro F23 no inversor Deye, como diagnosticar o relé de saída e quando o reparo é tecnicamente viável.

---

[CATEGORIA]
Códigos de Erro e Falhas

---

[TAGS]
Deye F23, falha relé de saída, inversor Deye, relé de bypass, diagnóstico inversor solar

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O erro **Deye F23** aparece no display e não vai embora. O inversor para de injetar energia, o cliente liga reclamando, e o técnico que chega ao local não sabe ao certo por onde começar. Parece simples — um relé. Mas o diagnóstico incorreto aqui costuma terminar em troca de inversor quando o problema estava em um componente de R$ 20.

Na nossa bancada, esse código chega com frequência em inversores Deye de 3 a 6 kW, especialmente de regiões com variação de rede mais agressiva — interior de Minas Gerais, Nordeste, áreas rurais com rede precária. O padrão que a gente vê é quase sempre o mesmo: o inversor funcionou bem por meses, a rede oscilou forte, o relé comutou repetidamente em curto intervalo de tempo, e o contato começou a deteriorar. Daí em diante, o F23 é só uma questão de tempo.

## O que causa o erro F23 no Deye

O F23 indica falha de detecção no circuito de controle do relé de saída CA. Para entender o que quebra, é preciso primeiro entender o que esse relé faz.

Em inversores on-grid, o relé de saída é o componente que conecta fisicamente o inversor à rede elétrica. Ele fica posicionado entre o estágio de potência e o ponto de conexão com a rede. Quando o firmware detecta condições fora dos limites — subtensão, sobretensão, frequência fora do padrão — esse relé abre e isola o sistema. A norma IEC 62116 exige que esse mecanismo opere em menos de 200 ms; o Deye cumpre isso via firmware combinado com o controle direto do relé.

O que o microcontrolador faz é simples: ele envia um sinal de comando ao relé e espera um sinal de retorno (feedback) confirmando que o contato está na posição correta. Quando esse retorno não corresponde ao comando, o inversor interpreta como falha e gera o F23.

As causas que chegam até nós com mais frequência:

1. Contato soldado (*welded contact*) — arco elétrico durante comutação sob carga funde os terminais metálicos, e o contato não abre mais
2. Bobina do relé com circuito aberto — ruptura no fio de enrolamento por fadiga térmica ou sobrecorrente
3. Transistor driver do relé em curto — o componente responsável por acionar a bobina queima e o relé perde o comando
4. Trilha do circuito de feedback interrompida — corrosão ou dano mecânico na PCB corta o sinal de retorno
5. Falso contato no conector da bobina — oxidação nos pinos do JST que alimenta o relé gera leituras inconsistentes
6. Mola de retorno fatigada — o contato não retorna à posição aberta mesmo sem sinal de acionamento

Nenhuma dessas causas aparece no display. O F23 só diz que o relé não está onde o firmware esperava.

## Como identificar na prática

Com o inversor desligado e desconectado da rede, comece pela inspeção visual.

1. Localize o relé de saída CA — em inversores Deye de 3 a 6 kW são geralmente um ou dois relés Omron ou TE Connectivity na região posterior da placa de potência
2. Inspecione os terminais de contato: escurecimento, marcas de arco e deformação visual indicam contato soldado
3. Meça a resistência da bobina com multímetro — valores abaixo de 5 Ω ou acima de 200 Ω (fora do especificado no datasheet do componente) indicam bobina comprometida
4. Teste o relé fora da placa com fonte DC na tensão nominal da bobina (tipicamente 12 V no Deye): clique audível e nítido confirma operação mecânica; ausência de clique confirma bobina aberta ou mola fatigada
5. Com o inversor energizado em bancada segura — sem conexão CA à rede — monitore com osciloscópio o sinal de controle do gate do transistor driver: ausência de pulso aponta falha no driver ou no microcontrolador, não no relé
6. Verifique continuidade no circuito de feedback: o sinal de retorno sai de um pino do relé e vai até o microcontrolador via resistor pull-up; qualquer interrupção nessa trilha mantém o F23 mesmo com relé novo
7. Inspecione o transistor driver (geralmente um NPN de coletor aberto, tipo BC817 ou equivalente SMD) em modo diodo — curto entre emissão e coletor confirma componente queimado

Faro de bancada: se o relé clica mas o erro persiste após a substituição, o problema nunca foi o relé.

## O erro mais comum do mercado

O que a gente vê com regularidade é técnico substituindo o inversor inteiro com base no F23, sem ter aberto a placa. O raciocínio é direto: "relé soldado, inversor condenado". Não funciona assim.

Relé soldado é reparo de bancada. O componente custa entre R$ 8 e R$ 40 dependendo da especificação de corrente. A substituição em nível de placa, em mãos experientes, leva menos de duas horas. Condenar o inversor por isso é um erro técnico e financeiro ao mesmo tempo.

O segundo erro — menos óbvio, mas igualmente custoso — é trocar o relé sem verificar o transistor driver. Se o driver estava queimado, ele vai queimar o relé novo na primeira comutação. O inversor volta ao cliente, funciona dois dias, o F23 retorna. A culpa recai sobre a peça, mas o problema real nunca foi diagnosticado. Não existe reparo correto sem sequência correta.

## Quando o reparo é viável

Na maioria dos casos de F23 isolado, sem outros códigos associados, o reparo é tecnicamente viável.

Critérios que definem isso:

- Estágio de potência intacto: ausência de F24, F25 ou códigos de sobrecorrente junto ao F23 indica que os IGBTs provavelmente não foram comprometidos
- Placa de controle sem dano de umidade generalizado: manchas de corrosão extensas na PCB podem indicar comprometimento além do circuito do relé
- Microcontrolador respondendo: se o display funciona e o inversor inicializa normalmente até o ponto de falha, o microcontrolador está operacional — isso pesa a favor do reparo
- Componentes disponíveis: relés com especificação equivalente ao original estão disponíveis no mercado nacional, sem necessidade de importação direta

Inversores Deye de 3 a 8 kW fora de garantia, com F23 como código principal, têm alta taxa de reparo viável na bancada. O laudo define o escopo antes de qualquer investimento.

## Conclusão

O F23 trava o sistema completamente e não dá pista sobre o componente específico. Mas na maior parte dos casos, está apontando para um relé, um transistor driver ou uma trilha de feedback — nada que justifique substituir o equipamento inteiro.

A decisão de trocar um inversor de R$ 4.000 sem abrir a placa é uma decisão tomada sem informação suficiente.

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

- Âncora: 'por que os IGBTs queimam' → URL: /por-que-os-igbts-queimam-inversores-solares → Contexto: seção "O que causa o erro F23", ao mencionar o estágio de potência e IGBTs
- Âncora: 'o que é o driver de IGBT' → URL: /driver-igbt-falha-estagio-de-potencia → Contexto: seção "Como identificar na prática", ao citar o transistor driver do relé
- Âncora: 'placa de controle vs. placa de potência' → URL: /placa-controle-vs-placa-potencia-onde-esta-o-defeito → Contexto: seção "Quando o reparo é viável", ao diferenciar os estágios de dano
- Âncora: 'inversor fora de garantia' → URL: /inversor-fora-de-garantia-trocar-ou-reparar → Contexto: seção "Quando o reparo é viável", ao citar análise técnica e financeira

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62116" → URL: https://www.iec.ch/homepage → Fonte: IEC — norma internacional de anti-ilhamento para inversores conectados à rede

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=1200
→ Por que foi escolhida: Mostra placa eletrônica de inversor com componentes de potência em close, contexto direto ao diagnóstico de relé
→ Nome do arquivo: deye-f23-rele-saida-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Placa eletrônica de inversor solar com relé de saída CA — diagnóstico do erro Deye F23
→ Legenda: Fig. 1 — Relé de saída CA em placa de inversor solar: ponto de falha do erro F23
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Mostra componentes eletrônicos em bancada técnica, adequado para a seção de diagnóstico prático com multímetro e osciloscópio
→ Nome do arquivo: deye-f23-diagnostico-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Bancada de diagnóstico eletrônico com multímetro e placa de inversor solar — erro Deye F23
→ Legenda: Fig. 2 — Verificação do circuito de relé na bancada: medição da bobina e análise do driver
→ Onde inserir: Após H2 "Como Identificar na Prática"
