# Post 111 — Solis (Ginlong): Os Erros Mais Frequentes e o Que É Reparável

---

[PALAVRA-CHAVE FOCO]
inversor Solis erros mais comuns

---

[TÍTULO SEO — Title Tag]
Solis (Ginlong): Erros Frequentes e o Que é Reparável

---

[SLUG — URL do Post]
solis-ginlong-erros-frequentes-reparavel

---

[META DESCRIPTION]
Os erros mais frequentes em inversores Solis (Ginlong), causas reais e o que é reparável na bancada. Diagnóstico antes da condenação.

---

[CATEGORIA]
Códigos de Erro e Falhas

---

[TAGS]
inversor Solis, Ginlong falha, erro F01 inversor solar, reparo inversor solar, diagnóstico inversor Solis

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

Os **inversores Solis da Ginlong** chegam cada vez mais à bancada técnica. Não por serem ruins — chegam porque estão por toda parte.

Desde que a marca ganhou fatia relevante no mercado brasileiro de instalações residenciais e pequenas empresas, o volume de falhas em campo cresceu na mesma proporção. Na nossa bancada, já passaram Solis de praticamente todas as séries — do monofásico de 3 kW ao trifásico de 25 kW. O padrão de falha é consistente o suficiente para reconhecer sem precisar de muita investigação inicial.

## O que causa as falhas mais comuns

Os inversores Solis operam com arquitetura de estágio duplo: um conversor CC-CC booster seguido por um inversor CC-CA baseado em IGBTs. Essa topologia é comum nas marcas chinesas de médio porte e distribui o estresse térmico entre dois estágios — mas cria pontos de falha em ambos.

O **F01 (Grid Fault)** é o erro que aparece com mais frequência nos relatórios de campo. Tensão ou frequência da rede fora dos parâmetros configurados no inversor. Em boa parte dos chamados, o problema está fora do equipamento: oscilação da concessionária, disjuntor mal calibrado na saída ou fiação CA com resistência de contato elevada. Mas há casos onde o relé de grid falhou internamente e o inversor está lendo mal a rede mesmo com ela estável.

O **F10 e F11 (Isolation Fault e Residual Current)** aparecem juntos com frequência. A causa mais comum é externa — cabo CC com isolamento degradado, conector MC4 oxidado, painel com microtrincas. Quando o técnico verifica todos os pontos externos, isola o campo e o erro persiste, o problema está no varistor (MOV) interno ou no circuito de medição de isolamento da placa de controle.

O **F21 (Fan Fault)** é o mais simples de resolver, mas o mais perigoso de ignorar. Um ventilador parado por rolamento travado ou driver PWM queimado vai forçar o inversor a limitar potência antes de desligar por sobretemperatura — às vezes sem chegar a exibir o código de fã no display.

O **F29 (Relay Check Fault)** indica que o relé de saída não comutou corretamente na inicialização. Pode ser o relé com bobina aberta, ou o driver que aciona a bobina com tensão insuficiente. Um multímetro e dois minutos de medição resolvem o diagnóstico.

O **F05 (PV Voltage High)** quase sempre vem de string mal dimensionada para a temperatura mínima local — problema de projeto, não de hardware. Mas há casos onde o sensor de tensão CC lê valor incorreto por falha no divisor resistivo da placa de controle.

Fora dos erros codificados, existe uma falha silenciosa frequente nos Solis: a fonte auxiliar interna (SMPS) entra em colapso e o inversor simplesmente não inicializa. Display apagado. Tensão CC nos bornes: normal. O equipamento não responde. Esse é o padrão clássico de SMPS com MOSFET ou diodo de saída danificado — e aparece com frequência crescente em equipamentos com mais de quatro anos de operação.

## Como identificar na prática

Antes de concluir por defeito interno, a verificação deve seguir esta sequência:

1. Medir tensão CC nos bornes de entrada — conferir se está dentro da faixa de operação do modelo
2. Verificar tensão e frequência na saída CA com multímetro true RMS
3. Testar isolamento do string CC com megôhmetro (mínimo 1 MΩ entre cada polo e o terra)
4. Inspecionar todos os conectores MC4: oxidação, crimpagem inadequada, sinal de queima ou infiltração de umidade
5. Verificar o ventilador com o equipamento aberto: gira livremente ao impulso manual? Rolamento com folga ou travado?
6. Com CC aplicado ao inversor: medir tensão nas saídas da fonte auxiliar (tipicamente 12 V e 5 V internos)
7. Display apagado com CC dentro da faixa correta: suspeitar da SMPS antes de qualquer outra hipótese — não partir direto para o estágio de potência

Para o F29, o procedimento é direto: medir resistência da bobina do relé e verificar a tensão de acionamento no driver. Relé com bobina aberta não vai comutar, independente do que o driver estiver fazendo.

## Quando é falha eletrônica interna

Os erros F01, F10 e F11 têm causa externa na maioria dos chamados. A proporção muda quando o sistema operou sem falhas por meses e o erro surgiu de forma súbita — isso indica degradação interna, não erro de instalação. Muda também quando o técnico já isolou o campo fotovoltaico fisicamente e o erro persiste no display.

Surtos são a principal causa de dano eletrônico interno nos Solis. A placa de controle, o circuito de medição e o estágio de gate dos IGBTs absorvem o transitório antes que os fusíveis CC atuem — a proteção não reage rápido o suficiente. No Brasil, com alta incidência de raios e qualidade de rede variável por região, esse cenário se repete com mais frequência do que o esperado.

O surto não avisa.

O superaquecimento crônico é a segunda causa mais recorrente. Inversores instalados em locais fechados, sem ventilação adequada, com camada de poeira sobre o dissipador — chegam com IGBT com solda de ball bond rompida ou capacitores de barramento com ESR fora da especificação.

Ainda não existe uma regra universal que diga se o dano é reparável só pelo sintoma. Depende do que você vai encontrar na placa.

## Vale a pena consertar?

A Solis tem boa disponibilidade de componentes no mercado nacional. IGBTs das séries mais comuns usam encapsulamentos TO-247 ou módulos discretos com equivalência em fabricantes como Infineon e ON Semiconductor. Relés, capacitores de barramento e MOVs também têm reposição viável.

Um Solis de 5 kW monofásico novo custa entre R$ 2.000 e R$ 2.800. Um reparo completo com troca de IGBT, driver e capacitores de barramento fica entre R$ 600 e R$ 900 — dependendo do que a bancada encontrar.

Para os modelos trifásicos de 10 kW a 25 kW, a lógica favorece ainda mais o reparo. Um trifásico de 15 kW novo pode custar de R$ 8.000 a R$ 12.000. O reparo raramente passa de R$ 2.000, mesmo em falhas severas no estágio de potência.

A exceção são os casos de surto intenso com dano múltiplo simultâneo: placa de controle, estágio de potência e módulo de comunicação atingidos juntos. Nesses casos, o custo de componentes pode superar o ponto de retorno. O laudo técnico serve de base para a decisão — seja para acionar seguro, negociar com o fabricante ou optar pela substituição.

A marca tem potencial de reparo. O que define é o diagnóstico.

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

- Âncora: 'por que os IGBTs queimam' → URL: /por-que-os-igbts-queimam-em-inversores-solares → Contexto: seção "O que causa as falhas mais comuns", ao mencionar IGBT com solda de ball bond rompida
- Âncora: 'fonte auxiliar interna' → URL: /fonte-auxiliar-smps-interna-inversor → Contexto: seção "O que causa as falhas mais comuns", parágrafo sobre SMPS com display apagado
- Âncora: 'superaquecimento crônico' → URL: /superaquecimento-inversor-solar → Contexto: seção "Quando é falha eletrônica interna", parágrafo sobre temperatura e poeira
- Âncora: 'falha de isolamento' → URL: /falha-isolamento-sistemas-fotovoltaicos → Contexto: seção "O que causa as falhas mais comuns", ao descrever F10 e F11
- Âncora: 'quanto custa consertar' → URL: /quanto-custa-consertar-inversor-solar → Contexto: seção "Vale a pena consertar?", ao citar valores de reparo vs. equipamento novo

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "qualidade de rede variável por região" → URL: https://www.aneel.gov.br/qualidade-do-fornecimento-de-energia-eletrica → Fonte: ANEEL — Módulo 8 do PRODIST (Qualidade da Energia Elétrica)
- Texto âncora: "mínimo 1 MΩ entre cada polo e o terra" → URL: https://www.iec.ch/homepage → Fonte: IEC 62109-1: Safety for power converters for use in photovoltaic power systems

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ Buscar em: unsplash.com — termos de busca: "solar inverter electronics repair" ou "power electronics circuit board"
→ Por que foi escolhida: placa eletrônica de inversor solar representando diagnóstico em bancada
→ Nome do arquivo: solis-inversor-erros-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Placa eletrônica de inversor solar Solis em bancada de diagnóstico com multímetro e componentes visíveis
→ Legenda: Fig. 1 — Diagnóstico eletrônico em nível de componente em inversor Solis (Ginlong)
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ Buscar em: pexels.com — termos de busca: "technician measuring voltage" ou "electronics repair multimeter"
→ Por que foi escolhida: técnico medindo tensão em placa eletrônica, representando o checklist de verificação
→ Nome do arquivo: solis-inversor-verificacao-campo-2.webp
→ Alt Text (máx. 125 caracteres): Técnico usando multímetro para verificar tensão em inversor solar durante diagnóstico de falha eletrônica
→ Legenda: Fig. 2 — Sequência de verificação antes de concluir por defeito interno no inversor Solis
→ Onde inserir: Após H2 "Como identificar na prática"
