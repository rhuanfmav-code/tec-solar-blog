# Post 11 — Inversor solar parou de funcionar: o checklist completo antes de chamar o técnico

---

## [PALAVRA-CHAVE FOCO]

inversor solar parou de funcionar

---

## [TÍTULO SEO — Title Tag]

Inversor Solar Parou? Checklist Antes de Chamar o Técnico

---

## [SLUG — URL do Post]

inversor-solar-parou-de-funcionar-checklist

---

## [META DESCRIPTION]

Inversor solar parado com o sol batendo? Execute este checklist completo antes de condenar o equipamento. Diagnóstico em nível de placa — TEC Solar.

---

## [CATEGORIA]

Manutenção e Diagnóstico

---

## [TAGS]

inversor solar parado, checklist diagnóstico inversor, inversor solar sem gerar energia, diagnóstico fotovoltaico, falha de inversor solar

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Inversor solar parou de funcionar** — e o sol está batendo forte. O painel está no telhado, o sistema parece intacto, mas a geração é zero. Display apagado, app sem dados, cliente no telefone.

O que a gente vê na prática é diferente do que a maioria dos técnicos faz nessa hora. Na nossa bancada, recebemos inversores toda semana com o diagnóstico "queimado" — e muitos voltam a funcionar após identificarmos um fusível fundido na string box ou um disjuntor CC disparado. O problema não estava no inversor. Estava no sistema externo.

Este checklist foi construído a partir desses casos. Execute cada passo em ordem antes de qualquer conclusão sobre defeito interno.

---

## O que pode fazer um inversor solar parar de funcionar

O inversor é um equipamento com múltiplas proteções automáticas. Ele desliga porque foi projetado para desligar — quando detecta uma condição fora do padrão. Esse desligamento pode ter origem externa ao inversor ou interna.

Causas externas (sistema, não o inversor):

1. Disjuntor CC disparado ou desligado manualmente
2. Disjuntor CA no quadro de distribuição aberto
3. Tensão de rede fora do intervalo operacional — a ANEEL Resolução 1000/2021 define a faixa de 191 V a 231 V para tensão nominal de 220 V; inversores fora disso desconectam por proteção automática
4. Tensão CC abaixo do mínimo de operação (string com sombra parcial, painel em curto, disjuntor CC de string individual aberto)
5. Falha de isolamento detectada — o inversor mede continuamente a resistência entre os condutores CC e o aterramento; abaixo do limiar configurado, o shutdown é automático conforme IEC 62109-2
6. Sobretemperatura por ambiente sem ventilação — instalações em caixas metálicas fechadas, como acontece frequentemente no Nordeste e Centro-Oeste, disparam o shutdown térmico com regularidade no verão, sem nenhum defeito eletrônico real
7. Fusível CC fundido na string box — um fusível de R$ 8,00 pode zerar a produção de uma string inteira

Causas internas (falha eletrônica real):

1. IGBT danificado no estágio de potência
2. Driver de gate com falha ou tensão de gate fora da faixa correta
3. Capacitor de bulk com capacitância degradada abaixo do mínimo operacional
4. Placa de controle com defeito (DSP ou microcontrolador)
5. Sensor de isolamento com leitura falsa — causa shutdown mesmo sem falha real de isolamento
6. Relé de saída com contato aberto ou soldado

Saber de qual grupo vem o problema define se o inversor vai para bancada ou não.

---

## Como identificar na prática

Execute esta sequência. Cada passo elimina uma hipótese antes de avançar.

**1. Anote o código de erro no display**
Se houver qualquer indicação — piscada de LED, código alfanumérico, mensagem parcial — registre antes de qualquer outra ação. Isso direciona o diagnóstico imediatamente e reduz o tempo de bancada.

**2. Meça a tensão CC na entrada do inversor**
Com multímetro nos terminais de entrada CC (positivo e negativo). A maioria dos inversores residenciais opera entre 150 V e 1000 V DC. Abaixo de 100 V, o problema está na string ou nos disjuntores, não no inversor.

**3. Verifique os disjuntores CC e CA**
O disjuntor CC (instalado antes do inversor) e o disjuntor CA (no quadro principal) devem estar fechados. Um disjuntor CC pode disparar por sobretensão, corrente reversa ou curto em um painel com defeito. A maioria dos técnicos esquece de checar o CC.

**4. Meça a tensão CA na saída**
A rede elétrica pode estar fora dos parâmetros sem nenhuma indicação visual no local. Medir com multímetro CA direto no ponto de conexão do inversor descarta a concessionária como causa — especialmente em regiões com instabilidade de tensão.

**5. Meça o isolamento CC**
Com megôhmetro a 500 V DC entre os condutores CC (positivo e negativo) e o aterramento, com o inversor desconectado. Abaixo de 1 MΩ, há falha de isolamento. O ponto pode ser um conector MC4 mal crimpado, um cabo com isolamento rompido por roedor, ou um painel com laminação deteriorada pela umidade.

**6. Cheque a temperatura do local de instalação**
Se o inversor está em ambiente fechado sem circulação de ar, encosta a mão na lateral da carcaça. Temperatura interna acima de 80–85°C provoca shutdown térmico por proteção. Esse detalhe resolve casos inteiros sem nenhum reparo eletrônico.

**7. Inspecione os fusíveis da string box**
Se o sistema tem string box, cada string tem um fusível individual. Fusível aberto em uma string pode zerar a produção se for a única string conectada — ou criar desequilíbrio sem apagar o inversor completamente, caso haja mais strings operacionais.
— Fusíveis com marcas de calor ou escurecimento na ponteira confirmam sobrecorrente. Meça continuidade antes de qualquer conclusão visual.

**8. Tente o reset via display ou botão**
Alguns inversores travam em estado de erro após proteção e precisam de reset manual. O manual do fabricante indica a sequência exata. Não é gambiarra — é procedimento padrão previsto pelo fabricante. Growatt, Deye e Sungrow têm esse recurso documentado.

---

## O erro mais comum do mercado

Técnico chega, vê o inversor apagado, não mede nada, emite o parecer: "precisa trocar".

Já recebemos equipamentos com esse exato laudo. O inversor chega na bancada, ligamos — funciona. O que havia era um fusível fundido na string box. Componente de R$ 8,00.

O problema não é só técnico. O cliente foi orientado a comprar um inversor novo de R$ 4.500 por um problema que não existia no inversor. Isso não é diagnóstico — é um chute com custo alto.

Condenar um inversor sem medir tensão CC, tensão CA, isolamento e estado dos disjuntores é um erro técnico documentável. Qualquer laudo emitido sem essas medições não tem base de sustentação.

---

## Quando o reparo é viável

Se o checklist foi executado por completo e o inversor continua parado, o problema é interno. Nesse ponto a análise de viabilidade entra em jogo.

O reparo faz sentido quando o dano está isolado: falha de IGBT sem propagação para o driver, ou falha de driver sem destruição da placa de controle. Nesses casos, o custo de reparo em nível de componente fica entre 15% e 35% do valor de um inversor novo equivalente — normalmente entre R$ 400 e R$ 900 para equipamentos residenciais de 3 a 10 kW.

O reparo não se justifica quando há dano múltiplo em cascata: IGBT + driver + placa de controle ao mesmo tempo. Ou quando o equipamento tem mais de 10 anos com capacitores de bulk no fim da vida útil, sem peças disponíveis para o modelo.

Para inversores com até 8 anos de uso e dano isolado, o reparo em nível de placa quase sempre é mais econômico que a substituição. A decisão, no entanto, depende do diagnóstico real — não do display apagado.

---

## Conclusão

Execute o checklist antes de qualquer conclusão. Meça antes de condenar.

Na maioria dos casos que chegam à nossa bancada como "inversor queimado", o problema estava fora do inversor. E nos que tinham defeito eletrônico real, o diagnóstico em nível de placa mudou completamente a decisão — reparo viável, custo menor, sistema voltando a gerar.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "falha de IGBT" → Link para: post sobre as 6 causas de queima do IGBT (Post 10)
- Âncora: "tensão CC fora do range" → Link para: post sobre Fronius State 102 – Tensão CC Muito Alta (Post 02)

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ANEEL Resolução 1000/2021" → Fonte: ANEEL — Resolução Normativa 1000/2021 (aneel.gov.br)
- Texto âncora: "IEC 62109-2" → Fonte: IEC — Safety of power converters for use in photovoltaic power systems (iec.ch)
- Texto âncora: "megôhmetro" → Fonte: Fluke — Megohmmeter Guide for Solar PV Systems (fluke.com)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Técnico medindo painel solar com multímetro em campo — representa o contexto de diagnóstico prático descrito no checklist do post
→ Nome do arquivo: inversor-solar-parou-de-funcionar-checklist-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Técnico realizando diagnóstico de inversor solar parado com multímetro — checklist antes de chamar o técnico especializado
→ Legenda: Fig. 1 — Diagnóstico sistemático com multímetro é o primeiro passo antes de concluir por defeito interno no inversor solar
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200
→ Por que foi escolhida: Técnico em bancada com equipamentos de medição — representa o processo de diagnóstico eletrônico em nível de placa descrito na seção de identificação prática
→ Nome do arquivo: diagnostico-inversor-solar-bancada-medição-2.webp
→ Alt Text (máx. 125 caracteres): Técnico em bancada eletrônica medindo tensão CC e isolamento de inversor solar parado — diagnóstico em nível de placa TEC Solar
→ Legenda: Fig. 2 — Bancada de diagnóstico: medição de tensão CC, isolamento e estado dos disjuntores antes de qualquer desmontagem do inversor
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB
