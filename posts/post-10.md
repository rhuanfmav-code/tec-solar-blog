# Post 10 — Por que os IGBTs queimam em inversores solares: as 6 causas reais

---

## [PALAVRA-CHAVE FOCO]

IGBT queimado inversor solar causas

---

## [TÍTULO SEO — Title Tag]

Por que o IGBT do inversor solar queima: 6 causas

---

## [SLUG — URL do Post]

igbt-queimado-inversor-solar-6-causas

---

## [META DESCRIPTION]

As 6 causas reais que destroem o IGBT de um inversor solar. Sobretensão, driver defeituoso, ciclos térmicos e mais — diagnóstico de bancada.

---

## [CATEGORIA]

Análise Técnica de Componentes

---

## [TAGS]

IGBT inversor solar, queima de IGBT, driver de gate inversor, diagnóstico inversor solar, reparo inversor solar

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **IGBT queimado em inversor solar** é a falha que mais custa na bancada. Quando o transistor de potência vai a curto, a corrente não tem controle — e o estrago atravessa a placa em frações de segundo. O inversor para, o sistema para, e a pergunta que surge raramente tem resposta simples.

Na nossa bancada, o IGBT destruído é a falha de estágio de potência que mais entra pela porta. E o padrão que a gente vê com frequência não é só o módulo queimado — é o mesmo módulo sendo substituído pela segunda vez no mesmo equipamento, porque a causa raiz não foi investigada na primeira intervenção. Módulo novo, inversor volta a funcionar. Semanas depois, mesmo sintoma, mesmo ponto de falha.

Antes de mandar buscar peça, é preciso entender por qual das seis causas aquele componente foi destruído.

---

## O que causa o IGBT queimar no inversor solar

O IGBT (Insulated Gate Bipolar Transistor) é o transistor de chaveamento de potência do inversor. Opera entre 10 e 20 kHz, comutando tensões de 400 a 800 V no barramento CC e conduzindo dezenas de ampères dependendo da potência do equipamento. Os limites críticos definidos pelo fabricante — Vces (tensão coletor-emissor), Ic (corrente de coletor) e Tj máx (temperatura de junção, tipicamente 150 a 175°C) — formam o envelope operacional. Qualquer cruzamento desses limites, mesmo por nanossegundos, pode ser fatal.

As seis causas que explicam a maior parte dos casos:

**1. Sobretensão por pico de comutação** — no momento em que o IGBT bloqueia, a corrente de coletor cai abruptamente. A indutância parasita do barramento CC gera um pico de tensão proporcional à taxa de variação: V = L × (dI/dt). Se esse pico ultrapassa o Vces do módulo, o IGBT sofre avalanche e o bloqueio se perde permanentemente. Os capacitores snubber e varistores do barramento CC existem para absorver esses picos — quando degradam, o módulo fica desprotegido.

**2. Falha no driver de gate** — o driver aplica tensão de gate para comandar condução (+15 V) e bloqueio (−8 V a −15 V). Se o optoacoplador degrada, a tensão em nível alto cai para 11 a 12 V. O IGBT entra em saturação parcial: a queda de tensão Vce(sat) aumenta, a dissipação de potência cresce. A temperatura sobe de forma acelerada sem que os sensores do inversor detectem a tempo. Já recebemos inversores com driver fornecendo 11 V no gate onde deveria ter 15 V — a diferença parece pequena na medição, o impacto térmico em horas de operação não é.

**3. Shoot-through — condução simultânea** — em topologias de meia-ponte, os dois IGBTs do mesmo braço operam em par complementar. O dead-time é o intervalo programado que impede a condução simultânea. Ruído elétrico no sinal de gate ou driver com falha pode eliminar esse intervalo. Quando ambos conduzem ao mesmo tempo, a tensão do barramento CC cai diretamente sobre eles. A corrente sobe para centenas de ampères em microssegundos. A proteção de desaturação tenta agir — mas o módulo frequentemente está destruído antes de conseguir bloquear.

**4. Superaquecimento crônico** — ventilador parado, dissipador obstruído por poeira, pasta térmica ressecada entre o módulo e o alumínio. Qualquer um desses fatores eleva a temperatura de junção gradualmente, sem alarme visível. O módulo não queima na hora — ele envelhece de forma acelerada. Em galpões sem climatização, em inversores instalados diretamente ao sol ou em ambientes fechados, condições comuns em instalações de baixo custo espalhadas pelo Brasil, a temperatura ambiente já consome boa parte da margem de segurança térmica disponível.

**5. Fadiga de bond wire por ciclos térmicos** — cada ciclo de geração aquece e resfria os materiais internos do módulo em proporções diferentes: o silício (~2,6 ppm/°C), o alumínio dos fios de bonding (~23 ppm/°C) e o substrato cerâmico (~7 ppm/°C) não se expandem juntos. O estresse mecânico se acumula nas interfaces. Publicações do IEEE Transactions on Power Electronics apontam a amplitude ΔTj por ciclo como principal preditor de vida útil dos bond wires. Em regiões do semiárido nordestino, o delta de temperatura entre madrugada e pico do dia pode superar 35°C — isso acelera o processo de forma considerável. Módulos com oito, dez anos de operação nessas condições começam a apresentar resistência de contato crescente antes de falhar.

**6. Surto de corrente por falha na saída CA** — curto em carga conectada, cabo de saída mal fixado ou neutro subdimensionado geram um surto de corrente que o circuito de proteção precisa interceptar. Se a proteção está degradada, o IGBT conduz a corrente toda antes de ser bloqueado. Rápido.

---

## Como identificar

O diagnóstico começa com o equipamento completamente desenergizado e os capacitores de barramento descarregados — aguardar no mínimo cinco minutos após desligar a tensão CC antes de tocar na placa:

1. Medir em modo diodo entre coletor e emissor de cada IGBT nos dois sentidos. IGBT em curto: resistência próxima de zero em ambas as polaridades, sem preferência direcional.
2. Verificar o diodo de retorno. Ausência de condução em ambas as direções indica IGBT aberto — bond wire rompida internamente.
3. Com o inversor energizado pela CC (CA desabilitado), medir a tensão de saída do driver. Gate em nível alto deve estar entre +14 V e +16 V. Abaixo de 13 V é suspeito antes de qualquer conclusão sobre o módulo.
4. Inspecionar os capacitores snubber e varistores do barramento CC. Tampa abaulada ou marcas de arco confirmam sobretensão como causa provável.
5. Verificar o ventilador: girar manualmente para detectar travamento, medir continuidade das bobinas. Ventilador que gira lento não gera alarme — mas é suficiente para elevar Tj acima do limite ao longo de semanas.
6. Examinar a pasta térmica entre o módulo e o dissipador. Pasta fragmentada, ressecada ou ausente é causa isolada de queima progressiva — e é invisível sem abrir o equipamento.
7. Com osciloscópio nos pinos de gate do driver, verificar temporização dos pulsos PWM. Borda de subida lenta indica resistor de gate com valor incorreto ou optoacoplador degradado — não necessariamente o IGBT em si.

---

## Quando é falha eletrônica interna

Nem todo IGBT queimado indica problema no componente em si.

Quando o shoot-through ocorre, o dano se estende: módulo, driver, fusível CC — às vezes múltiplos componentes em cascata. Quando a causa é superaquecimento crônico, o módulo falhou mas o driver e a placa de controle podem estar intactos.

Identificar até onde o dano chegou é o que define a viabilidade do reparo — e impede que o módulo novo queime pelo mesmo motivo. O que a gente vê com frequência: IGBT substituído, driver não verificado, pasta térmica não trocada, snubbers não checados. O módulo novo chega à bancada com o mesmo padrão de falha do anterior.

Trocar o módulo sem investigar a causa raiz não é reparo. É adiamento.

---

## Vale a pena consertar?

Depende do que acompanhou o IGBT na destruição.

IGBT em curto, driver e placa de controle intactos: reparo direto. Um módulo IGBT de inversor residencial de 5 kW fica entre R$ 200 e R$ 600 dependendo do fabricante — uma fração do custo de um inversor novo equivalente, que sai entre R$ 3.000 e R$ 6.000. A diferença justifica o diagnóstico antes de qualquer outra decisão.

Driver destruído junto com o módulo: custo sobe, mas na maioria dos modelos ainda compensa. O problema de viabilidade real aparece quando a trilha de potência sofreu dano extenso — arco que carbonizou a PCB, múltiplos componentes em cascata. Nesse caso, a viabilidade precisa ser avaliada componente a componente antes de qualquer compromisso.

O pior cenário não é o IGBT queimado. É condenar o equipamento sem abrir.

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

- Âncora: 'capacitores snubber e varistores do barramento CC' → URL: /weg-e001-sobretensao-cc-diagnostico → Contexto: seção "O que causa", item 1 — o Post 06 aborda sobretensão CC com análise dos componentes de proteção do barramento
- Âncora: 'tensões de 400 a 800 V no barramento CC' → URL: /fronius-state-102-tensao-cc-alta-diagnostico → Contexto: seção "O que causa", parágrafo introdutório — o Post 02 detalha os limites de tensão CC em inversores e as causas de ultrapassagem
- Âncora: 'sobretensão por pico de comutação' → URL: /abb-f003-tensao-cc-alta-string-defeito-medicao → Contexto: seção "O que causa", item 1 — o Post 09 cobre sobretensão CC em inversores ABB com análise do circuito de medição
- Âncora: 'Publicações do IEEE Transactions on Power Electronics' → URL: /canadian-solar-falha-101-tensao-cc-elevada-diagnostico → Contexto: seção "O que causa", item 5 — o Post 07 referencia o mesmo contexto de normas técnicas aplicadas a falhas de componentes em sistemas fotovoltaicos

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "Publicações do IEEE Transactions on Power Electronics" → URL: https://ieeexplore.ieee.org/document/6175576 → Fonte: IEEE Xplore — "Prediction of Bond Wire Lift-Off Failure for Automotive IGBTs", estudo de fadiga de bond wire com análise de ΔTj como preditor de vida útil
- Texto âncora: "temperatura de junção" → URL: https://www.aneel.gov.br/qualidade-da-energia-eletrica → Fonte: ANEEL — Qualidade da Energia Elétrica, referência para limites de temperatura operacional e requisitos de qualidade para equipamentos conectados à rede

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Close de placa de circuito eletrônico de potência com componentes visíveis — representa o ambiente de bancada e o foco em diagnóstico em nível de componente descrito no post
→ Nome do arquivo: igbt-queimado-inversor-solar-placa-potencia.webp
→ Alt Text (máx. 125 caracteres): Placa de potência de inversor solar com módulo IGBT — diagnóstico das 6 causas reais de queima em nível de componente eletrônico
→ Legenda: Fig. 1 — Estágio de potência de inversor solar: o módulo IGBT opera no limite térmico e elétrico do circuito — qualquer cruzamento de limite pode ser fatal
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=1200
→ Por que foi escolhida: Técnico com equipamento de medição em bancada eletrônica — representa a etapa de diagnóstico com multímetro e osciloscópio descrita na seção "Como identificar"
→ Nome do arquivo: diagnostico-igbt-inversor-solar-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Técnico realizando diagnóstico de IGBT em bancada eletrônica — medição de tensão de gate e verificação do driver de inversor solar
→ Legenda: Fig. 2 — Diagnóstico de IGBT na bancada: medição da tensão de gate do driver precede qualquer decisão de substituição do módulo
→ Onde inserir: Após H2 "Como identificar"
