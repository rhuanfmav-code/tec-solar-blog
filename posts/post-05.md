# Post 05 — Sungrow Grid Lost: Perda de Rede — Disjuntor, Cabeamento ou Defeito Interno?

---

## [PALAVRA-CHAVE FOCO]

sungrow grid lost perda de rede diagnóstico inversor solar

---

## [TÍTULO SEO — Title Tag]

Sungrow Grid Lost: Perda de Rede — Causa e Diagnóstico

---

## [SLUG — URL do Post]

sungrow-grid-lost-perda-de-rede-diagnostico

---

## [META DESCRIPTION]

Inversor Sungrow com Grid Lost? Veja se o problema está no disjuntor, cabeamento ou relé interno — diagnóstico em nível de componente. TEC Solar.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Sungrow Grid Lost, perda de rede inversor solar, relé saída CA, diagnóstico Sungrow, alarme 010 Sungrow

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Sungrow Grid Lost** aparece no display, o inversor desliga, e o integrador começa o checklist clássico: disjuntor, cabeamento, reset. Na metade dos casos, o equipamento volta. Na outra metade, não volta — e aí começa a divergência de diagnóstico.

Na nossa bancada, esse alarme chega com dois perfis bem distintos. No primeiro, o inversor estava saudável mas houve um evento de rede — pico de frequência, subtensão momentânea da concessionária, oscilação durante comutação de cargas pesadas. O equipamento travou, mas o problema estava fora dele. No segundo perfil, o grid está completamente normal e o inversor continua reportando Grid Lost. Nesse caso, o problema está dentro da caixa.

O Grid Lost no Sungrow (também identificado como Alarm 010 ou variantes de "No Grid" em alguns modelos) é a mensagem do inversor dizendo que não consegue detectar tensão CA na saída. As causas podem ser banais ou graves. O diagnóstico é o que decide qual.

---

## O que causa esse erro no Sungrow

O circuito de supervisão de rede nos inversores Sungrow (famílias SG, SH e SG-RT) monitora continuamente tensão, frequência e, nos modelos trifásicos, a simetria de fases. Quando qualquer desses parâmetros sai dos limites configurados — ou some completamente — o equipamento abre o relé de saída, desconecta da rede e registra o alarme.

A proteção anti-ilhamento nos modelos Sungrow homologados para o Brasil segue a ABNT NBR 16149, que exige desconexão em menos de 2 segundos quando a frequência sai de 55–65 Hz ou a tensão ultrapassa 10% da nominal. Isso é correto e obrigatório. O problema começa quando o inversor dispara fora dessas condições — e continua reportando Grid Lost com a rede presente.

Causas reais, em ordem de frequência:

1. **Disjuntor AC com mau contato ou subdimensionado** — micro-abertura cíclica que o técnico não detecta sem medição direta no barramento de saída
2. **Cabos AC com queda de tensão excessiva** — o inversor não enxerga a tensão mínima no borne AC mesmo com rede presente no quadro
3. **Terminal de conexão AC com aperto insuficiente** — vibração e ciclos térmicos afrouxam terminais de cobre progressivamente; o contato piora durante picos de geração
4. **Relé de saída CA com falha de fechamento** — contato oxidado ou carbonizado que não fecha com confiabilidade, gerando leitura intermitente no circuito de supervisão. Isso acontece mais do que o integrador imagina.
5. **Circuito de amostragem de tensão CA com deriva** — divisor resistivo ou amplificador operacional na placa de controle com leitura distorcida por corrosão ou variação de temperatura
6. **Instabilidade da rede da concessionária** — frequência fora dos limites (±0,5 Hz do padrão 60 Hz conforme ANEEL) ou queda de tensão momentânea de 200 ms, suficiente para disparar a proteção dependendo da parametrização do firmware

Sem separar causa externa de interna, o diagnóstico não começa.

---

## Como identificar na prática

O diagnóstico começa do ponto mais externo e vai entrando. Não o contrário.

1. Meça a tensão CA no barramento do QDC com carga real ligada — não em tomada
2. Meça na saída do disjuntor dedicado do inversor
3. Meça diretamente nos bornes de conexão AC do inversor com o equipamento em standby
4. Calcule a queda de tensão entre o ponto 2 e o ponto 3: qualquer valor acima de 3V com o inversor desligado indica resistência elevada no cabeamento ou nos terminais
5. Com o inversor desenergizado, meça a resistência de cada condutor CA entre o QDC e o inversor — limite prático: máximo 0,3 Ω por condutor em cabos até 15 m
6. Verifique o torque de aperto dos terminais: 1,5 a 2,5 N·m para bornes AC residenciais Sungrow
7. Com a rede confirmada e o disjuntor íntegro, ligue o inversor e observe — o Grid Lost aparece imediatamente ou após tentativa de sincronização?

Se o alarme aparece antes de qualquer tentativa de sincronizar, o circuito de medição interno é o suspeito principal.

Sinais físicos que apontam falha interna:
- No osciloscópio, forma de onda CA ausente nos pinos de leitura da placa de controle mesmo com tensão presente nos terminais de saída
- Resistores do divisor de tensão CA com mudança de coloração (marrom-escuro ou deformação leve) — sobrecarga pontual no circuito de medição
- Relé com marcas de queima ou resíduo escuro nos contatos visíveis durante abertura mecânica

Não é sempre que esses sinais estão visíveis. Às vezes só a medição de resistência revela o defeito.

Inversores Sungrow instalados no litoral nordestino — especialmente nos modelos SG5KTL e SG8KTL em Pernambuco, Alagoas e Sergipe — chegam com os terminais CA com oxidação severa por névoa salina. O Grid Lost nesse contexto é frequentemente um problema de resistência de contato, não falha eletrônica interna.

---

## O erro mais comum do mercado

O técnico mede a tensão na tomada mais próxima do quadro, vê 220V, e conclui que a rede está normal. Fecha o chamado como "falha transitória da concessionária" e reseta o inversor.

Isso não é diagnóstico. É exclusão com uma variável só.

Ninguém mediu os bornes AC do inversor. Ninguém verificou o disjuntor dedicado sob carga. Ninguém apertou os terminais. O inversor volta, funciona por uma semana, e o Grid Lost reaparece — normalmente no horário de pico de geração, quando a corrente AC está no máximo e a queda de tensão nos cabos atinge o valor mais alto. Não é coincidência. É física: corrente alta em cabo subdimensionado gera queda de tensão que empurra a leitura do inversor para fora do envelope da ABNT NBR 16149.

O Sungrow armazena log de eventos com timestamp. Se o Grid Lost ocorreu entre 13h e 14h num dia de calor extremo, cruzar com os dados de demanda da concessionária local pode revelar o padrão. Em regiões do sertão nordestino e do interior do Sudeste, inversores desligam no pico da tarde por subtensão de rede — o barramento da concessionária afunda quando os equipamentos de ar-condicionado entram simultaneamente. A instalação está correta. A rede que falhou.

Condenar o inversor sem olhar o log de eventos é o erro mais caro do mercado.

---

## Quando o reparo é viável

Para causas externas, não há reparo no inversor. A correção é na instalação.

Para causas internas, o critério é direto:

- Relé de saída CA com falha de contato: componente substituível em bancada. O relé é geralmente um modelo padronizado (Omron G2R ou equivalente), com especificação rastreável no datasheet da placa. Custo do componente: R$ 30 a R$ 80.
- Divisor resistivo com deriva por corrosão: troca dos resistores de precisão, custo de componente abaixo de R$ 20.
- Amplificador de condicionamento com drift: identificação e substituição em nível SMD — custo de componente baixo, o que determina o valor é a hora de bancada.
- Placa de controle com dano extenso por raio, surto ou infiltração de água: o reparo depende do mapeamento do dano. Pode ser viável, pode não ser.

Um inversor Sungrow residencial novo de 5 kW está entre R$ 3.200 e R$ 4.800. Um de 8 kW, entre R$ 4.500 e R$ 6.500. Reparo do relé de saída na bancada: R$ 300 a R$ 600.

A conta é simples.

---

## Conclusão

Grid Lost não é sentença de morte do inversor. Na maioria dos casos que chegam até nós, o equipamento está eletronicamente saudável — o problema estava no disjuntor mal fixado, no cabo CA com terminal frouxo, ou na rede da concessionária que oscilou e ninguém registrou.

Nos casos em que o defeito é interno, o relé de saída CA é o suspeito principal. Um componente de R$ 60 que, sem diagnóstico, vira justificativa para troca de inversor novo.

Antes de condenar, diagnostica.

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

- Âncora: 'proteção anti-ilhamento' → URL: /growatt-erro-102-falha-de-isolamento → Contexto: seção "O que causa", ao mencionar a desconexão automática por segurança
- Âncora: 'falha de isolamento em inversor solar' → URL: /sma-erro-3501-falha-isolamento-diagnostico-fotovoltaico → Contexto: seção "O que causa", ao mencionar diagnóstico em nível de placa como método comum
- Âncora: 'instabilidade da rede da concessionária' → URL: /deye-f01-f02-tensao-de-rede-alta-e-baixa → Contexto: seção "O erro mais comum do mercado", ao mencionar oscilação de rede como causa não identificada

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16149" → URL: https://www.abnt.org.br → Fonte: ABNT — Sistemas fotovoltaicos — Requisitos de conexão à rede elétrica de distribuição
- Texto âncora: "padrão 60 Hz conforme ANEEL" → URL: https://www.aneel.gov.br/distribuicao4 → Fonte: ANEEL — Módulo 8 do PRODIST, Qualidade da Energia Elétrica

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Painel de distribuição elétrica residencial com disjuntores — contexto direto do diagnóstico de perda de rede descrito no post
→ Nome do arquivo: sungrow-grid-lost-perda-de-rede-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Quadro de distribuição elétrica com disjuntor AC de inversor Sungrow — diagnóstico de erro Grid Lost perda de rede
→ Legenda: Fig. 1 — Ponto de medição no disjuntor dedicado do inversor: primeiro passo no diagnóstico do Grid Lost
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=1200
→ Por que foi escolhida: Técnico usando multímetro em equipamento eletrônico — representa a medição de tensão nos bornes AC e o diagnóstico do circuito de supervisão
→ Nome do arquivo: medicao-bornes-ac-inversor-sungrow-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo tensão nos bornes AC de inversor Sungrow com multímetro para diagnóstico de erro Grid Lost
→ Legenda: Fig. 2 — Medição direta nos bornes AC do inversor em standby. Queda de tensão entre QDC e borne indica problema no cabeamento ou nos terminais
→ Onde inserir: Após H2 "Como identificar na prática"
