# Post 12 — Growatt Erro 103: Falha de Aterramento — quando o problema está no cabo e quando está na placa

---

## [PALAVRA-CHAVE FOCO]

Growatt erro 103 falha de aterramento

---

## [TÍTULO SEO — Title Tag]

Growatt Erro 103: Falha de Aterramento — Cabo ou Placa?

---

## [SLUG — URL do Post]

growatt-erro-103-falha-de-aterramento-diagnostico

---

## [META DESCRIPTION]

Growatt exibe erro 103 de falha de aterramento? Veja como diferenciar problema no cabo, painel ou placa interna — diagnóstico técnico em nível de bancada.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Growatt erro 103, falha de aterramento inversor solar, diagnóstico aterramento fotovoltaico, resistência de isolamento CC, falha PE inversor Growatt

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Growatt erro 103 — falha de aterramento** aparece no display e o inversor trava. Geração zero, cliente no telefone, sistema parado. E o problema pode estar em três lugares completamente diferentes: no cabeamento CC, nos painéis fotovoltaicos, ou na própria placa interna do inversor.

Na nossa bancada, esse erro chega com uma história quase sempre igual: integrador fez a instalação, sistema funcionou por algumas semanas, chuva chegou, e o 103 apareceu. Ponto de atenção imediato — condições climáticas são gatilho frequente para falha de aterramento em instalações com conector MC4 mal crimpado ou cabo com isolamento deteriorado pela exposição solar intensa. No Norte e Nordeste do Brasil, a combinação de calor e umidade acelera esse processo de forma considerável.

---

## O que causa o erro 103 no Growatt

O Growatt erro 103 é uma proteção de aterramento — o inversor detecta que a resistência de isolamento entre os condutores CC (positivo e/ou negativo) e o terra (PE) caiu abaixo do limiar mínimo aceitável. Conforme IEC 62109-2 e os manuais técnicos Growatt, esse valor normalmente é de 1 MΩ para sistemas residenciais. Abaixo disso, o inversor desconecta automaticamente por segurança.

O que está acontecendo na prática: há um caminho de corrente se formando entre o circuito CC e a terra do sistema. Esse caminho pode vir de pontos distintos.

**Cabeamento CC com isolamento comprometido**

Cabos fotovoltaicos (norma IEC 62930 / NBR 16612) têm resistência ao UV e às variações de temperatura, mas envelhecem. Instalações com cabo roteado por eletroduto sem proteção mecânica adequada, ou pressionado por suportes metálicos, desenvolvem microfissuras no isolamento que se tornam caminhos condutores quando úmidas.

**Conectores MC4 com crimpagem inadequada**

A junta mal crimpada não veda completamente a entrada do cabo. Água penetra, oxida o contato, e a resistência entre o condutor e o corpo metálico do conector cai progressivamente. Em campo, a maioria desses casos não aparece com o cabo visivelmente danificado — o conector parece íntegro por fora.

**Módulos fotovoltaicos com laminação deteriorada**

O encapsulante EVA dos painéis absorve umidade com o tempo, especialmente em painéis expostos a temperatura elevada. Quando a umidade penetra entre as células e o vidro, a resistência de isolamento do painel em relação à estrutura cai. Um único painel com esse problema pode derrubar toda a string abaixo do limiar de operação do inversor.

**Sensor de isolamento interno com leitura falsa**

Esse caso é diferente dos anteriores: o sistema externo está íntegro, mas o circuito de medição dentro do inversor apresenta defeito. O sensor reporta resistência baixa mesmo quando ela está correta. É o caso mais difícil de identificar sem bancada — o técnico em campo mede tudo, encontra valores normais, e o inversor continua exibindo o erro 103.

---

## Como identificar na prática

O diagnóstico correto começa isolando as partes do sistema. Execute nesta ordem:

1. **Desligue o inversor pelo disjuntor CC e CA.** Aguarde o display apagar completamente — isso garante que os capacitores internos descarregaram. Nunca meça com o inversor energizado.

2. **Desconecte fisicamente os cabos CC das entradas do inversor** (terminais positivo e negativo de cada string). Isso isola o sistema externo do equipamento.

3. **Curto-circuite positivo e negativo de cada string separadamente** com um jumper adequado para a corrente da string. Isso permite medir o isolamento de cada string individualmente.

4. **Meça a resistência de isolamento com megôhmetro a 500 V DC** entre os dois condutores em curto e o aterramento do sistema (PE). Abaixo de 1 MΩ, aquela string tem falha de isolamento. Acima de 10 MΩ, o isolamento está íntegro.

5. **Se todas as strings medirem valor adequado**, reconecte apenas os cabos CC ao inversor e meça a resistência de isolamento entre os terminais CC e o PE diretamente nas entradas do equipamento. Se o valor cair com o inversor conectado, o problema está interno — o sensor de isolamento ou o circuito CC interno está com defeito.

6. **Inspecione visualmente os conectores MC4.** Conectores abertos, com ferrugem no contato ou com o cabo desalinhado dentro do corpo são pontos de falha frequentes. Em instalações com mais de 3 anos, vale crimpagem e substituição preventiva dos MC4 de toda a string com problema.

O que o técnico vai ver na prática: multímetro comum não é suficiente para esse diagnóstico. A leitura de isolamento exige megôhmetro — a tensão de teste de 500 V DC é o que força o defeito a aparecer. Com multímetro em modo ohmímetro (tensão de teste de poucos volts), cabos com isolamento deteriorado podem parecer perfeitos.

---

## O erro mais comum do mercado

O técnico chega, vê o erro 103, descarta o cabeamento "visualmente" e concluiu que é defeito interno no inversor. Equipamento vai para reparo ou substituição. Sistema continua com o mesmo problema depois da troca.

Isso acontece com frequência. O cabo com isolamento fissura não aparece ao olho. O conector MC4 com água interna parece intacto. E como o técnico não carrega megôhmetro — às vezes porque não tem, às vezes porque não usaria de qualquer forma — o diagnóstico pula direto para o inversor.

Condenar o inversor sem medir a resistência de isolamento string por string é um erro técnico com consequência financeira real. Inversores Growatt residenciais de 3 a 5 kW custam entre R$ 2.500 e R$ 4.500 novos. A substituição de um conector MC4 ou de um trecho de cabo custa menos de R$ 80.

Tem um detalhe que poucos consideram: se o técnico troca o inversor sem corrigir o defeito no cabeamento, o inversor novo vai exibir o mesmo erro 103 em minutos após a partida. O cliente fica com dois inversores — um novo e um "defeituoso" — e o problema ainda não está resolvido.

---

## Quando o reparo é viável

Se o diagnóstico confirmou que o sistema externo está íntegro e o erro 103 persiste, o defeito é interno. Nesse ponto existem dois cenários.

**Sensor de isolamento com leitura falsa**

O circuito de medição de isolamento no Growatt é composto por resistores de alta precisão e um amplificador diferencial que compara as tensões entre os barramentos CC e o terra. Qualquer desvio de componente — resistor com tolerância deslocada por temperatura, capacitor de desacoplamento com ESR elevado — pode gerar leitura errada sem que o circuito esteja completamente danificado. Nesse caso, o reparo em nível de componente é tecnicamente viável e financeiramente mais sensato que a troca do inversor.

**Dano real no circuito CC interno**

Menos comum. Quando há sobretensão CC ou descarga eletrostática, o circuito de entrada CC pode ter componente danificado com baixa resistência para o terra. O diagnóstico diferencia as duas situações: no primeiro cenário, o sistema externo mede corretamente mas o inversor reporta erro; no segundo, o curto interno aparece na medição.

Para equipamentos com até 7 anos de uso, o reparo é justificável em ambos os cenários — especialmente quando o modelo não está descontinuado e as peças estão disponíveis. A relação custo-benefício é clara: reparo em bancada entre R$ 350 e R$ 700 versus inversor novo entre R$ 2.500 e R$ 4.500.

---

## Conclusão

O erro 103 do Growatt não é sentença de morte do inversor. Na maioria dos casos, o problema está fora do equipamento.

Antes de qualquer conclusão, meça. Megôhmetro, string por string, sistema isolado. Esse procedimento leva menos de 20 minutos e define se o problema é no cabo, no painel ou no inversor. Sem esse dado, qualquer decisão — trocar o inversor, trocar o cabeamento, chamar o técnico — é um chute com dinheiro do cliente.

Se o diagnóstico apontou para defeito interno, envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "falha de isolamento" → Link para: post sobre SMA 3501 – Falha de Isolamento (Post 04)
- Âncora: "IGBTs queimam em inversores solares" → Link para: post sobre causas de queima de IGBT (Post 10)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 62109-2" → Fonte: IEC — Safety of power converters for use in photovoltaic power systems (iec.ch)
- Texto âncora: "megôhmetro" → Fonte: Fluke — Understanding Insulation Resistance Testing (fluke.com)
- Texto âncora: "NBR 16612" → Fonte: ABNT — Cabos para sistemas fotovoltaicos (abntcatalogo.com.br)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Cabos e conectores de sistema fotovoltaico em instalação — representa diretamente o contexto de falha de aterramento por cabeamento CC comprometido
→ Nome do arquivo: growatt-erro-103-falha-aterramento-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Conectores MC4 e cabeamento CC de sistema fotovoltaico — diagnóstico do Growatt erro 103 falha de aterramento
→ Legenda: Fig. 1 — Cabeamento CC e conectores MC4 são os primeiros pontos a verificar no diagnóstico do Growatt erro 103
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=1200
→ Por que foi escolhida: Técnico com megôhmetro medindo resistência de isolamento — representa exatamente o procedimento de diagnóstico descrito na seção "Como Identificar na Prática"
→ Nome do arquivo: diagnostico-isolamento-inversor-growatt-megohmetro-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo resistência de isolamento CC com megôhmetro em sistema fotovoltaico — diagnóstico Growatt erro 103
→ Legenda: Fig. 2 — Medição de isolamento com megôhmetro a 500 V DC: único método confiável para identificar a origem do erro 103 no Growatt
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB
