# Post 21 — O que é o driver de IGBT e por que sua falha destrói o estágio de potência

---

[PALAVRA-CHAVE FOCO]

driver de IGBT inversor solar falha estágio de potência

---

[TÍTULO SEO — Title Tag]

Driver de IGBT: o que é e por que sua falha destrói o inversor

---

[SLUG — URL do Post]

driver-de-igbt-inversor-solar-falha-estagio-de-potencia

---

[META DESCRIPTION]

O driver de IGBT controla o chaveamento do estágio de potência. Entenda como sua falha destrói IGBTs e como diagnosticar antes de trocar o transistor.

---

[CATEGORIA]

Análise Técnica de Componentes

---

[TAGS]

driver de IGBT, falha gate driver inversor solar, diagnóstico IGBT, reparo inversor solar, estágio de potência fotovoltaico

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **driver de IGBT** é o circuito que fica entre a placa de controle e o transistor que processa toda a potência do inversor. Não é um componente auxiliar — sem ele, o IGBT não chavearia dentro do tempo necessário, operaria em saturação parcial por tempo demais e se destruiria em questão de ciclos de operação.

Na nossa bancada, inversores com IGBT queimado chegam todo mês. Em boa parte dos casos, o que disparou a falha não foi sobretensão externa nem sobrecarga de string. Foi o driver que perdeu capacidade de desligar o transistor de forma controlada. O IGBT foi a vítima. O driver estava com problema antes, e ninguém mediu.

## O que o driver de IGBT faz na prática

O gate do IGBT se comporta como um capacitor. A capacitância gate-emissor (Cge) varia de 2 nF a 20 nF dependendo do módulo — e para comutar esse capacitor em frequências de 10 kHz a 20 kHz com tempos de transição abaixo de 100 ns, é preciso corrente de pico entre 2 A e 5 A. A placa de controle gera um sinal PWM de 3,3 V ou 5 V com drive de alguns miliampères. Não chega nem perto. O driver amplifica esse sinal e entrega ao gate a corrente necessária para ligar e desligar o transistor dentro do tempo que a topologia exige.

Os CIs de driver presentes na maioria dos inversores de 1 kW a 15 kW que passam pela nossa bancada:

- IR2110 (Infineon): bootstrap simples, sem isolação galvânica — presente em topologias de barramento baixo
- HCPL-3120 (Broadcom): optoacoplamento com saída de 2 A — muito frequente em inversores nacionais e importados de 3 kW a 6 kW
- TLP250, TLP351 (Toshiba): pinagem e performance similares ao HCPL-3120, usados com frequência em equipamentos asiáticos da faixa de potência média
- 1ED020I12-F2 (Infineon EiceDRIVER): isolação por transformador de núcleo ar com proteção DESAT integrada — presente nas linhas mais recentes da SMA, Fronius e Deye. É o CI com maior rastreabilidade de falha porque gera sinal externo de fault ao detectar desaturação, o que facilita bastante o diagnóstico em bancada quando o CI sobrevive ao evento.
- 2SC0108T (Power Integrations): usado em módulos IGBT de alta potência acima de 10 kW

Cada canal de driver precisa de fonte de alimentação isolada — tipicamente +15 V / −8 V. Essa fonte é gerada por transformadores toroidais com oscilador push-pull ou por módulos DC-DC isolados. Quando a fonte perde a saída negativa, o driver continua parcialmente ativo mas não consegue aplicar tensão negativa no gate após o pulso de condução. O IGBT não desliga de forma limpa.

## Como a falha do driver destrói o estágio de potência

Três modos de falha convertem diretamente em destruição do transistor.

**Gate travado em condução.** Se o circuito de descarga do gate perde capacidade — por degradação do optoacoplador, falha na fonte de −8 V ou resistor de gate em circuito aberto —, o IGBT permanece parcialmente em condução após o sinal PWM encerrar. O transistor complementar do mesmo braço entra em condução. Os dois IGBTs conduzem simultaneamente e o barramento CC fecha em curto. A corrente sobe de zero a centenas de ampères em microssegundos. Sem proteção de desaturação funcional, o IGBT vai à avalanche.

**Shoot-through por perda de tempo morto.** A topologia de meia-ponte depende de um intervalo entre o desligamento do IGBT inferior e o acionamento do superior. Se o driver encurta esse intervalo — por variação de alimentação, degradação do timing interno ou parasita no sinal de enable —, os dois transistores do braço conduzem juntos por microssegundos. É suficiente para destruir o módulo e parte do barramento.

**Degradação silenciosa por CTR reduzido.** O CTR (Current Transfer Ratio) do optoacoplador cai com temperatura e envelhecimento. Com CTR baixo, o tempo de subida do pulso de gate aumenta. O IGBT passa mais tempo em cada transição, opera na região de saturação parcial e dissipa mais calor por ciclo. O sensor de temperatura do inversor não detecta nada anormal no início. O IGBT degrada de forma gradual até uma carga mais pesada finalizar o processo.

O técnico encontra o transistor destruído sem histórico de sobrecarga aparente. É o modo de falha que mais confunde o diagnóstico de campo — especialmente no Norte e no Centro-Oeste, onde ciclos de irradiância intensa combinados com variações de tensão frequentes aceleram o envelhecimento do optoacoplador.

## Como identificar na prática

Não tem outro caminho: osciloscópio.

1. Com o inversor desligado e capacitores descarregados, identificar os terminais de gate e emissor de cada IGBT na placa de potência
2. Iniciar operação em condição controlada — sem carga ou com carga reduzida
3. Medir a forma de onda gate-emissor com ponteiras diferenciais: sinal deve ser quadrado, com +12 V a +18 V no pulso positivo e −5 V a −15 V no estado de repouso
4. Verificar tempo de subida e descida: acima de 500 ns para IGBTs de até 600 V indica degradação no driver ou resistor de gate fora da especificação
5. Comparar a amplitude entre canais do mesmo braço: assimetria acima de 2 V indica drivers com comportamento diferente — o canal mais fraco falha primeiro
6. Medir a tensão das fontes isoladas com o circuito em operação, nunca em vazio — a fonte de 15 V pode apresentar valor correto sem carga e cair 3 V a 4 V com o driver sob demanda real
7. Com o inversor desligado, medir resistência dreno-source de cada IGBT: valor abaixo de 10 Ω confirma curto por falha catastrófica — o driver foi comprometido junto com o transistor, mesmo sem sinal externo visível

Em inversores com proteção DESAT ativa (HCPL-314J ou 1ED020I12-F2), o pino de fault registra o evento de desaturação. Se esse pino ficou flutuante ou o CI de lógica foi destruído junto, a informação se perdeu — mas a topologia do circuito ainda pode indicar o que aconteceu.

## O erro mais comum do mercado

Trocar o IGBT sem avaliar o driver.

O módulo queimado é o sinal visível: capacitor explodido, arco na resina, curto entre dreno e fonte. O driver danificado fica na placa sem qualquer marca externa. O IGBT novo entra em operação com o mesmo driver comprometido. O ciclo se repete.

O segundo erro é medir a tensão da fonte isolada fora do circuito. A leitura em vazio não revela o problema. Só sob demanda real a queda de tensão aparece — e essa diferença entre o valor medido e o valor real em operação já foi o que nos fez refazer diagnósticos mais de uma vez.

O terceiro erro é atribuir a falha à rede. Um transitório externo pode ter dado início ao processo, mas o que propagou a destruição ao IGBT foi a incapacidade do driver de desligar o transistor de forma controlada. Resolver o transitório sem inspecionar o driver é deixar a cadeia de falha em aberto.

## Quando o reparo é viável

O CI de driver tem custo baixo. Um HCPL-3120 original fica entre R$ 12 e R$ 35. O 1ED020I12-F2 da Infineon, dependendo do canal e do fornecedor nacional, entre R$ 45 e R$ 90. O transformador de fonte isolada, quando danificado, pode ser substituído por módulo DC-DC equivalente entre R$ 60 e R$ 150.

Reparo completo do estágio de driver — CIs, fontes isoladas, resistores de gate, optoacopladores — raramente ultrapassa R$ 500 em um inversor de 5 kW a 10 kW. Somado ao custo do módulo IGBT (R$ 80 a R$ 250 dependendo do modelo), o total ainda fica bem abaixo do custo de um inversor novo de mesma potência, entre R$ 4.000 e R$ 15.000.

O que inviabiliza o reparo não é o driver. É o dano colateral quando a falha destrói a placa de controle junto. Isso acontece com menos frequência, mas acontece — e o diagnóstico precisa mapear o que foi comprometido antes de qualquer orçamento.

## Conclusão

O driver é o elo entre lógica e potência. Quando ele falha, o IGBT não tem como se defender.

Antes de substituir qualquer transistor de potência, o driver precisa ser verificado. Não como item secundário — como ponto de partida do diagnóstico.

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

- Âncora: 'O IGBT foi a vítima' → URL: /por-que-os-igbts-queimam-em-inversores-solares → Contexto: Introdução — referência cruzada com Post 10 que analisa as 6 causas reais de queima de IGBT em inversores solares
- Âncora: 'o transistor que processa toda a potência do inversor' → URL: /por-que-os-igbts-queimam-em-inversores-solares → Contexto: Introdução — reforça a relação entre driver e IGBT tratada no Post 10
- Âncora: 'O técnico encontra o transistor destruído sem histórico de sobrecarga aparente' → URL: /inversor-solar-parou-de-funcionar-checklist-completo → Contexto: Seção "Como a falha do driver destrói o estágio de potência" — referência cruzada com Post 11 sobre o checklist completo antes de chamar o técnico

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "proteção DESAT ativa" → URL: https://www.infineon.com → Fonte: Infineon — fabricante dos CIs EiceDRIVER com proteção de desaturação integrada para IGBTs em conversores de potência fotovoltaicos
- Texto âncora: "módulos DC-DC isolados" → URL: https://www.iec.ch → Fonte: IEC — referência para especificações de isolação galvânica em circuitos de acionamento de transistores de potência (IEC 60747-9)

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Placa de circuito eletrônico com componentes SMD em close — representa o estágio de driver de IGBT em nível de placa, contexto direto do diagnóstico descrito no post
→ Nome do arquivo: driver-igbt-inversor-solar-placa-de-potencia.webp
→ Alt Text (máx. 125 caracteres): Placa de circuito eletrônico com driver de IGBT — diagnóstico em nível de componente em inversor solar
→ Legenda: Fig. 1 — O driver de IGBT fica na placa de potência e controla cada pulso de gate do transistor
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092787765-e3feb951d987?w=1200
→ Por que foi escolhida: Técnico com osciloscópio analisando forma de onda em circuito eletrônico — representa o processo de diagnóstico do driver de IGBT descrito na seção "Como identificar na prática"
→ Nome do arquivo: driver-igbt-diagnostico-osciloscopio-inversor-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo forma de onda gate-emissor com osciloscópio para diagnóstico de driver de IGBT em inversor solar
→ Legenda: Fig. 2 — O osciloscópio é o único instrumento que revela degradação do driver de IGBT antes da falha catastrófica
→ Onde inserir: Após H2 "Como identificar na prática"
