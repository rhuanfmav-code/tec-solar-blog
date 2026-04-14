# Post 07 — Canadian Solar Falha 101: Tensão CC Elevada — String ou Sensor com Defeito?

---

## [PALAVRA-CHAVE FOCO]

canadian solar falha 101 tensão cc elevada diagnóstico inversor solar

---

## [TÍTULO SEO — Title Tag]

Canadian Solar Falha 101: Tensão CC Elevada — Diagnóstico

---

## [SLUG — URL do Post]

canadian-solar-falha-101-tensao-cc-elevada-diagnostico

---

## [META DESCRIPTION]

Canadian Solar exibindo Falha 101? Descubra se é string mal dimensionada ou falha no circuito de medição CC — diagnóstico em nível de placa.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Canadian Solar, Falha 101, tensão CC elevada, diagnóstico inversor solar, sobretensão CC

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

A **Falha 101 no inversor Canadian Solar** aparece no display como sobretensão CC e o sistema para na hora. O inversor pode voltar logo depois do reset — especialmente se o pico de tensão aconteceu cedo pela manhã e a temperatura dos painéis já subiu. O técnico fecha o chamado como instabilidade de rede, o cliente fica sem geração por mais uma manhã, e o problema se repete no ciclo seguinte.

Na nossa bancada, esse defeito chega de duas formas completamente distintas. A primeira é de projeto: string calculada sem considerar o coeficiente de temperatura negativo do painel, instalada em regiões onde a temperatura matinal cai abaixo de 0°C — e o Voc real ultrapassa o limite de entrada do inversor. A segunda é eletrônica: o circuito de medição de tensão CC está com deriva, reportando sobretensão onde fisicamente não existe. Tratar um sem entender qual é o problema não resolve. Só atrasa.

---

## O que causa a Falha 101 no Canadian Solar

A Falha 101 dispara quando a tensão CC nas entradas do inversor ultrapassa o limite máximo de entrada — geralmente 1000 V CC nas séries CSI-GHH e CSI-T, de acordo com as especificações técnicas publicadas pela Canadian Solar. No momento da detecção, o sistema de proteção de entrada abre e o inversor entra em fault com registro de evento.

Causas reais, em ordem de frequência:

1. **String com Voc calculado para 25°C sem correção de temperatura** — cada célula fotovoltaica monocristalina tem coeficiente de temperatura negativo entre −0,26%/°C e −0,35%/°C, especificado no datasheet do painel. Numa string de 18 painéis com Voc de 44 V a 25°C, a diferença entre calcular para 25°C e para −5°C representa mais de 85 V adicionais. Em projetos próximos ao limite de 1000 V, esse número derruba o sistema nas primeiras manhãs de inverno.
   — É o tipo de falha que ninguém percebe no comissionamento porque o dia de instalação quase sempre é ensolarado e quente.

2. **Resistores do divisor de alta tensão CC com deriva de resistência** — o circuito de medição de entrada usa uma cadeia de resistores SMD de alta impedância para escalonar a tensão CC até o nível de leitura do ADC no microcontrolador. Quando qualquer resistor dessa cadeia muda o valor por degradação térmica ou umidade nos terminais, a relação de divisão muda — e o inversor passa a enxergar uma tensão diferente da real.

3. **Op-amp de condicionamento com offset positivo** — o amplificador operacional que processa o sinal do divisor resistivo pode desenvolver deriva de offset com o tempo, especialmente em inversores que operam em ambientes com variação térmica intensa. O resultado é uma tensão reportada consistentemente acima da real, levando o inversor a proteger contra uma sobretensão que não existe na entrada.

4. **Painel substituído por modelo com Voc maior sem recalcular a string** — troca de painel em campo, muitas vezes por um modelo similar em potência mas com Voc diferente. O projeto original passa a estar fora dos limites sem que ninguém perceba.

5. **Varistor de proteção de entrada com degradação parcial** — um MOV envelhecido pode injetar ruído no barramento CC durante picos de irradiância. Esse ruído, dependendo da velocidade do circuito de amostragem, pode ser lido como pico de tensão e acionar a proteção.

6. **Inversores transformerless com aterramento inadequado do array** — a corrente de fuga entre string e terra distorce a referência de medição de tensão interna. Aparece com mais frequência em instalações onde o condutor de proteção do array fotovoltaico está mal conectado ou ausente.

---

## Como identificar na prática

Não recomenda, não troca, não reinicia — mede primeiro.

1. Registre o horário exato da Falha 101: manhãs frias com céu limpo apontam para problema de string; ocorrências aleatórias ao longo do dia apontam para circuito de medição
2. Meça a tensão CC real nas entradas do inversor com multímetro calibrado, categoria III mínimo 1000 V — o dado do monitoramento web não serve como referência primária
3. Calcule o Voc teórico da string para a temperatura ambiente no momento da medição: `Voc(T) = Voc(25°C) × [1 + α × (T − 25)]`, usando o coeficiente de temperatura (α) do datasheet do painel
4. Se a tensão medida nos bornes está dentro do limite do inversor: o problema está no circuito interno de medição
5. Se a tensão real ultrapassa o limite: o projeto de string precisa ser recalculado — nenhuma intervenção eletrônica no inversor vai resolver
6. Em bancada, aplique tensão CC controlada por fonte regulada na entrada e compare o valor aplicado com o valor reportado pelo display ou interface de comunicação serial do inversor — qualquer divergência consistente confirma deriva no circuito de medição
7. Localize os resistores do divisor de alta tensão no PCB de entrada; meça com inversor desenergizado e compare com valor nominal — desvio acima de 1% em resistores de precisão já justifica substituição

Resistores com coloração escurecida próxima às trilhas, varnish com microfissuras ou terminais com sinal de oxidação são indicativos visuais diretos de degradação térmica.

---

## O erro mais comum do mercado

O técnico reseta e o inversor volta. Certo? Nem sempre.

O que acontece na maior parte dos casos: o sol já subiu, os painéis aqueceram, o Voc caiu para dentro do limite e o sistema volta sozinho. O chamado é fechado sem medição. Uma semana depois, nova Falha 101. Novo reset. Novo fechamento de chamado.

Depois de várias ocorrências, a conclusão que o mercado tira é que o inversor tem "defeito de fábrica" — e começa a pressão por substituição em garantia. O Canadian Solar novo sobe ao telhado. A string continua com os mesmos 18 painéis dimensionados sem correção de temperatura. Na primeira manhã fria: Falha 101. O ciclo reinicia com equipamento novo.

O que ninguém contabilizou é o custo oculto: cada ciclo de fault por sobretensão real estressou os capacitores do barramento CC e os IGBTs do estágio de potência. Componentes que têm vida útil medida em horas de operação dentro de especificação. O problema de projeto gerou desgaste eletrônico real.

---

## Quando o reparo é viável

Se a causa for dimensionamento incorreto da string, a solução está em campo:

- Reduzir o número de painéis em série
- Substituir por painel com Voc compatível com a temperatura mínima do local
- Custo: recalculo de projeto e eventual ajuste de cabeamento

Se a causa for falha no circuito de medição interno:

- Resistores do divisor: R$ 3 a R$ 15 por componente, requer estação de solda SMD com ponta fina ou ar quente
- Op-amp de condicionamento: R$ 8 a R$ 45 dependendo do encapsulamento e especificação de offset
- PCB de entrada com corrosão generalizada: substituição do conjunto, R$ 280 a R$ 550 incluindo mão de obra
- Inversor Canadian Solar CSI 3–5 kW novo: a partir de R$ 3.200. Séries de maior potência: R$ 6.000 a R$ 12.000

O reparo é financeiramente viável quando o diagnóstico aponta para o componente específico. Sem isso, não tem como estimar — e o mercado tende a trocar o inversor sem saber o que estava errado.

Ainda não existe resposta definitiva sobre viabilidade sem abrir o inversor e medir o circuito de medição. Depende do que você vai encontrar na placa.

---

## Conclusão

A Falha 101 no Canadian Solar não é um defeito de inversor na maioria dos casos — é um problema de interface entre o projeto fotovoltaico e os limites elétricos do equipamento. Quando é eletrônico, se resolve na bancada com componentes acessíveis. Quando é de projeto, se resolve no campo sem tocar no inversor.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

Recalcule o Voc da string para a temperatura mínima do local antes de qualquer outra coisa.

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "coeficiente de temperatura negativo do painel" → Link para: post sobre Growatt Erro 102 – Falha de Isolamento (Post 01)
- Âncora: "tensão CC muito alta no inversor Fronius" → Link para: post sobre Fronius State 102 – Tensão CC Muito Alta (Post 02)
- Âncora: "sobretensão CC no inversor WEG" → Link para: post sobre WEG E001 – Sobretensão CC (Post 06)
- Âncora: "Voc calculado sem correção de temperatura" → Link para: post sobre inversor solar parado – checklist completo (Post 11)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "coeficiente de temperatura do painel" → Fonte: Canadian Solar – Datasheet módulos HiDM e HiKu (canadiansolar.com)
- Texto âncora: "limite máximo de tensão CC" → Fonte: Canadian Solar – Manual de Instalação CSI-GHH / CSI-T Series (canadiansolar.com)
- Texto âncora: "IEC 62109" → Fonte: IEC – Safety of power converters for use in photovoltaic power systems (iec.ch)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?w=1200
→ Por que foi escolhida: Inversor solar instalado com conexões CC visíveis — representa o ponto de medição de tensão nos bornes de entrada descrito no diagnóstico da Falha 101
→ Nome do arquivo: canadian-solar-falha-101-tensao-cc-elevada.webp
→ Alt Text (máx. 125 caracteres): Inversor on-grid Canadian Solar — diagnóstico da Falha 101 tensão CC elevada, verificação de Voc da string e circuito de medição
→ Legenda: Fig. 1 — Bornes de entrada CC do inversor Canadian Solar CSI: primeiro ponto de medição no diagnóstico da Falha 101 por sobretensão
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=1200
→ Por que foi escolhida: Técnico com multímetro em bancada eletrônica — representa a etapa de medição do circuito de medição CC e comparação de valores descrita no diagnóstico
→ Nome do arquivo: diagnostico-circuito-medicao-cc-canadian-solar-falha101-2.webp
→ Alt Text (máx. 125 caracteres): Técnico com multímetro medindo tensão CC em inversor Canadian Solar — diagnóstico de deriva no circuito de medição da Falha 101
→ Legenda: Fig. 2 — Medição nos bornes CC com multímetro calibrado: discrepância entre tensão real e valor reportado pelo inversor confirma deriva no divisor resistivo
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB
