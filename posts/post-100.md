# Post 100 — Fonte auxiliar (SMPS interna) do inversor: a falha que apaga o equipamento inteiro

---

[PALAVRA-CHAVE FOCO]
fonte auxiliar SMPS inversor solar

---

[TÍTULO SEO — Title Tag]
Fonte Auxiliar SMPS do Inversor: Falha que Apaga Tudo

---

[SLUG — URL do Post]
fonte-auxiliar-smps-inversor-solar-falha-apaga-equipamento

---

[META DESCRIPTION]
A falha da SMPS interna apaga o inversor inteiro sem deixar código de erro. Saiba como identificar e por que quase sempre tem conserto.

---

[CATEGORIA]
Análise Técnica de Componentes

---

[TAGS]
fonte auxiliar inversor solar, SMPS interna inversor, inversor solar sem display, falha fonte chaveada, diagnóstico inversor apagado

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Fonte auxiliar SMPS do inversor solar** é um dos componentes que menos aparece nos laudos de campo — e um dos que mais chegam aqui como causa raiz de inversores completamente apagados, sem display, sem LED, sem resposta nenhuma.

O padrão do problema é quase sempre o mesmo: o integrador vai até o local, mede tensão CC na entrada, verifica o disjuntor de AC, olha para fora e não encontra nada errado. O inversor simplesmente não liga. A conclusão que vem a seguir é automática: queimou o IGBT, o equipamento está perdido.

Na nossa bancada, essa conclusão raramente se confirma. O que a gente vê com frequência é o estágio de potência intacto, os IGBTs em condição normal, e uma fonte auxiliar que parou de gerar as tensões que a placa de controle precisa para inicializar. Sem essas tensões, o inversor não faz nada.

## O que causa esse problema

A SMPS de um inversor é um circuito flyback de pequeno porte. Ela converte a tensão do barramento CC — ou em alguns projetos a tensão de rede CA — em múltiplos níveis de baixa tensão que alimentam a placa de controle, os drivers de gate dos IGBTs, o ventilador, o display e os módulos de comunicação.

Quando essa fonte falha, o inversor fica sem energia para funcionar. Nada inicializa.

Os componentes que mais falham nesse estágio:

- Capacitores eletrolíticos no secundário — degradam com calor e ciclos repetidos de carga. No Brasil, inversores instalados em telhados metálicos sem ventilação adequada chegam com os capacitores da SMPS já abaulados antes de qualquer outro componente apresentar defeito visível
- MOSFET de chaveamento no primário — absorve transientes de tensão que chegam pelo barramento ou pela rede; cidades com fornecimento instável aceleram muito a degradação desse componente
- Opto-acoplador de realimentação — falha sem queimar nada, sem odor, sem nenhum sinal externo, mas derruba a regulação das tensões de saída de forma progressiva até o colapso
- Diodos do retificador secundário — curto interno resulta em tensão afundada ou oscilando no secundário, o que pode derrubar o inversor de forma intermitente antes de travá-lo definitivamente
- Transformador flyback — ruptura de isolamento entre primário e secundário, normalmente associada a surto severo; menos frequente, mas o mais difícil de localizar sem medição adequada
- Fusível do primário — o elemento de proteção mais simples; quando o surto é intenso o suficiente para abri-lo sem danificar os semicondutores, a troca resolve

O calor é o fator dominante. Inversores com ventilador nunca revisado, operando em ambientes com temperatura acima de 40°C no verão, chegam com a SMPS no limite — e o primeiro evento externo relevante finaliza o componente.

## Como identificar

O diagnóstico de SMPS não exige osciloscópio na primeira etapa. Começa assim:

1. Meça a tensão CC na entrada do inversor — dentro do range operacional descarta problema na string
2. Observe se há absolutamente nada no display ou em qualquer LED — ausência total de sinal é característica de SMPS sem saída
3. Abra o inversor e inspecione visualmente os capacitores da fonte auxiliar — abaulamento no topo do capacitor confirma degradação avançada
4. Cheire o interior assim que abrir — componente queimado tem odor específico que aponta a região do defeito antes de qualquer medição
5. Meça com multímetro nos pontos de teste da placa auxiliar as tensões de 5V, 12V e 15V — ausência dessas tensões com barramento CC presente confirma a SMPS como causa do problema
6. Verifique o fusível do primário — aberto com semicondutores intactos indica que o surto externo foi a causa, e o escopo do reparo é menor

Se as tensões no secundário estão ausentes e o primário tem tensão, o caminho está claro. O osciloscópio entra para identificar se o MOSFET está chaveando, se o opto-acoplador tem sinal de realimentação, e onde exatamente a cadeia quebrou. Mas muitas vezes o capacitor abaulado ou o MOSFET com junção em curto já entregam o diagnóstico visualmente.

## Quando é falha eletrônica interna

A SMPS raramente falha por causa externa isolada. O padrão mais comum é um componente que já estava próximo do limite da sua vida útil e um evento externo — surto, oscilação de rede, reinicialização frequente — que precipitou o colapso.

Três cenários frequentes na bancada:

**Surto externo puro:** fusível do primário aberto, MOSFET e diodos intactos. Troca do fusível mais verificação do MOV resolve. Cenário mais simples e mais rápido.

**Degradação interna progressiva:** capacitores com ESR alto, MOSFET com junção degradada, opto-acoplador com CTR reduzido pelo envelhecimento. O inversor foi dando sinais antes de apagar — instabilidades no monitoramento, reinicializações esporádicas que o integrador atribuiu a oscilações de rede. O sistema parou de forma definitiva quando o componente mais degradado chegou ao limite.

**Dano colateral na placa de controle:** quando a SMPS colapsa de forma violenta, pode levar tensão incorreta para o microcontrolador ou para os drivers de gate. Não é o cenário mais comum, mas acontece. Esse é o caso que exige diagnóstico mais amplo, porque o escopo do reparo muda.

A distinção importa antes de qualquer orçamento. SMPS isolada: custo de componentes baixo, tempo de reparo curto. SMPS com dano colateral na placa de controle: mais trabalho antes de fechar o valor.

## Vale a pena consertar?

Na quase totalidade dos casos em que o diagnóstico confirma falha restrita ao estágio auxiliar: sim.

Componentes para reconstrução de uma SMPS de inversor raramente ultrapassam R$ 150,00. Mesmo com bancada especializada e processo de teste, o reparo fica muito abaixo do custo de um inversor novo. Um equipamento de 5 kWp custa entre R$ 3.000 e R$ 6.000 novo. Reconstruindo a fonte auxiliar, o mesmo equipamento volta a funcionar por uma fração disso.

O que muda o cenário é dano no estágio de potência. Se os IGBTs foram afetados pela falha ou se a placa de controle tem componentes queimados além da fonte auxiliar, o custo sobe. Mas isso só se sabe depois do diagnóstico em nível de placa — não antes de abrir e medir o equipamento.

Condenar o inversor sem medir as tensões de saída da SMPS é erro técnico. A gente recebe equipamentos toda semana com laudo de campo dizendo "defeito irreparável" que voltam da bancada funcionando depois da reconstrução da fonte auxiliar. O estágio de potência estava intacto.

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

- Âncora: 'drivers de gate dos IGBTs' → URL: /driver-de-gate-igbt-funcao-modos-de-falha-diagnostico-bancada → Contexto: seção "O que causa esse problema", ao listar o que a SMPS alimenta
- Âncora: 'os IGBTs foram afetados pela falha' → URL: /por-que-os-igbts-queimam-inversores-solares → Contexto: seção "Vale a pena consertar?", ao citar dano colateral no estágio de potência
- Âncora: 'diagnóstico em nível de placa' → URL: /o-que-e-diagnostico-nivel-placa-por-que-muda-tudo-reparo → Contexto: seção "Vale a pena consertar?", ao explicar que o escopo só se define após abertura e medição
- Âncora: 'Capacitores eletrolíticos no secundário' → URL: /capacitores-eletrolíticos-inversores-vida-util-degradacao-quando-trocar → Contexto: seção "O que causa esse problema", primeiro item da lista de componentes vulneráveis
- Âncora: 'Condenar o inversor sem medir' → URL: /por-que-maioria-inversores-condenados-mercado-ainda-tem-conserto → Contexto: último parágrafo da seção "Vale a pena consertar?"

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "circuito flyback" → URL: https://www.iec.ch/homepage → Fonte: IEC — norma IEC 62040 sobre sistemas de alimentação ininterrupta e fontes chaveadas, base técnica para circuitos flyback em eletrônica de potência
- Texto âncora: "temperatura acima de 40°C no verão" → URL: https://www.inmetro.gov.br/qualidade/portarias/inversores-fotovoltaicos → Fonte: INMETRO — portaria de requisitos de eficiência para inversores fotovoltaicos, que inclui faixas de temperatura de operação e teste de vida útil de componentes

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: placa eletrônica em close técnico mostrando componentes SMD — representa o nível de diagnóstico necessário para identificar falha na fonte auxiliar SMPS do inversor
→ Nome do arquivo: fonte-auxiliar-smps-inversor-solar-diagnostico-placa.webp
→ Alt Text (máx. 125 caracteres): Placa eletrônica de inversor solar em diagnóstico de bancada — falha na fonte auxiliar SMPS identificada em nível de componente
→ Legenda: Fig. 1 — A SMPS interna do inversor é um circuito flyback de pequeno porte; quando falha, apaga o equipamento inteiro sem deixar código de erro no display
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=1200
→ Por que foi escolhida: técnico com multímetro em bancada eletrônica — representa o processo de medição das tensões de saída da SMPS para confirmar o diagnóstico
→ Nome do arquivo: fonte-auxiliar-smps-diagnostico-multimetro-bancada.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensões de saída da fonte auxiliar SMPS de inversor solar com multímetro em bancada de diagnóstico
→ Legenda: Fig. 2 — A medição das tensões de 5V, 12V e 15V no secundário da SMPS com barramento CC presente é o passo que confirma a fonte auxiliar como causa do inversor apagado
→ Onde inserir: Após H2 "Como identificar"
