# Post 14 — Deye F05: Frequência de Rede Fora do Limite — diagnóstico e solução definitiva

---

## [PALAVRA-CHAVE FOCO]

Deye F05 frequência de rede fora do limite

---

## [TÍTULO SEO — Title Tag]

Deye F05: Frequência Fora do Limite — Diagnóstico

---

## [SLUG — URL do Post]

deye-f05-frequencia-rede-fora-limite-diagnostico

---

## [META DESCRIPTION]

Deye F05: frequência de rede fora do limite. Saiba como separar falha da concessionária de defeito no circuito PLL — diagnóstico técnico completo.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Deye F05, frequência rede inversor solar, diagnóstico Deye SUN-5K, proteção anti-ilhamento solar, circuito PLL inversor

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **Deye F05** aparece no display, o inversor desconecta e a geração vai a zero. Para o técnico que chega no local, a tentação é reiniciar, esperar o inversor normalizar e registrar como "falha transitória de rede". O problema: nas próximas semanas, o cliente vai ligar de novo.

Na nossa bancada, esse código chega com um histórico quase invariável: três reinicializações feitas pelo instalador, uma ligação para a concessionária que disse que a rede "está normal", e o F05 voltando nos mesmos horários — geralmente entre 13h e 18h. Regiões do interior de Minas, Goiás e do Nordeste aparecem com mais frequência nesses casos. A rede nesses lugares oscila de verdade. Mas o inversor também pode estar mentindo.

A diferença entre esses dois cenários determina se o problema vai custar R$ 0 — uma solicitação à distribuidora — ou R$ 4.000 num inversor novo. Diagnosticar antes de concluir não é preciosismo técnico. É o procedimento mínimo correto.

---

## O que causa o Deye F05

O Deye monitora continuamente a frequência da rede CA por um circuito PLL (Phase-Locked Loop) que rastreia o cruzamento por zero da tensão CA. Esse circuito alimenta o DSP com o valor de frequência em tempo real. Se o valor medido ultrapassar os limites configurados de proteção, o F05 é disparado.

No Brasil, o PRODIST Módulo 8 (Resolução ANEEL 956/2021) define 60 Hz como frequência nominal. A NBR IEC 62116 exige desconexão em até 200 ms quando a frequência cai abaixo de 59,5 Hz ou supera 60,5 Hz. O Deye cumpre essa exigência — o F05 é essa proteção funcionando. O diagnóstico começa depois dessa constatação.

As causas se dividem em dois grupos distintos.

**Causas externas — a rede está realmente fora do padrão:**

- Perturbações na geração da concessionária: desligamento súbito de gerador ou rejeição de carga na usina causando queda momentânea de frequência no alimentador
- Chaveamento de cargas pesadas na mesma subestação: compressores de câmara fria, motores de irrigação, equipamentos industriais — eventos de 100 a 300 ms que não aparecem em medição RMS média de multímetro
- Rede de distribuição rural sobrecarregada com regulação deficiente, especialmente evidente no pico de demanda do final da tarde
- Geração distribuída descoordinada na mesma subestação, com resposta de frequência conflitante com o restante da rede

**Causas internas — o inversor está medindo errado:**

- Capacitor de filtro no circuito de detecção CA com capacitância reduzida ou ESR elevado, deslocando a fase detectada pelo zero-crossing detection e gerando leitura de frequência incorreta
- Resistores SMD de precisão no divisor de tensão do circuito PLL com tolerância desviada por ciclos térmicos, afetando o nível de entrada do comparador
- Optoacoplador do circuito de isolamento CA com ganho degradado, introduzindo ruído na detecção de cruzamento por zero
- Borne CA com resistência de contato variável sob carga — causa mais subestimada nos casos que chegam até nós

---

## Como identificar na prática

A ferramenta-chave aqui não é o multímetro. É o analisador de qualidade de energia com registro temporal.

1. **Instale um analisador de qualidade de energia** no ponto de conexão CA do inversor e configure registro contínuo de frequência com resolução de no mínimo 100 ms. Registre por 24 horas, priorizando os horários históricos de falha.

2. **Exporte o log de eventos do Deye** via SolarmanPV ou interface local. O inversor registra o timestamp, a frequência medida e a tensão CA no momento de cada desconexão.

3. **Cruze o horário exato do F05 com os dados do analisador externo.** Se a frequência registrada externamente estava dentro dos limites no momento da desconexão, o problema está no circuito interno de medição — não na rede.

4. **Com osciloscópio nos terminais de entrada CA internos**, verifique a forma de onda antes do circuito de medição. Sinal limpo de 60 Hz deve ser senoidal sem ruído superimposto. Distorção, picos ou assimetria indicam problema no filtro de entrada ou no zero-crossing detection.

5. **Meça o optoacoplador do circuito CA com multímetro em modo diodo** e compare o ganho com o especificado no datasheet. Optoacoplador degradado é silencioso — não gera falha óbvia, mas corrompe gradualmente o sinal de detecção de frequência.

6. **Aperte os bornes CA com torque especificado no manual do modelo.** Borne frouxo gera resistência de contato variável sob carga — não aparece em inspeção visual, não aparece no multímetro com o inversor desligado.

---

## O erro mais comum do mercado

O técnico reinicia o inversor, o F05 desaparece, e o caso é dado como resolvido.

Reinicialização não elimina nenhuma causa. Se a rede estava instável, vai ficar instável de novo. Se o circuito interno está degradado, vai falhar de novo na próxima variação de temperatura. O que muda com a reinicialização é o contador de falhas — não o problema que gerou o F05.

Um Deye SUN-5K novo custa entre R$ 3.500 e R$ 5.000. O aluguel de um analisador de qualidade de energia por dois dias sai por menos de R$ 300. A diferença entre "problema da concessionária" e "componente interno com defeito" vale esse investimento antes de qualquer outra decisão.

---

## Quando o reparo é viável

Se o diagnóstico confirmou origem interna, o componente identificado define o prognóstico.

**Capacitor de filtro CA com ESR elevado** — componente passivo, substituição direta, reparo viável entre R$ 250 e R$ 500. Esse é o cenário mais frequente nos casos com esse código.

**Optoacoplador do circuito de isolamento CA** — componente de sinal, substituição com equivalente listado no datasheet. Custo similar ao do capacitor. Requer identificação do circuito exato no esquema do modelo.

**Resistores SMD de precisão no divisor de tensão PLL** — resistores de 0,1% ou 0,5% de tolerância. Substituição possível com rastreamento correto no esquema. Viável em bancada com equipamento adequado.

**Falha no DSP ou na placa de controle** — o único cenário em que o reparo pode não ser financeiramente viável. Placa de controle de reposição para modelos mais antigos pode não estar disponível no mercado. Só o diagnóstico em bancada define isso — não há como concluir antes de abrir o equipamento e medir os pontos certos.

---

## Conclusão

Deye F05 é um código de proteção. Ele aparece quando o inversor detectou frequência fora do limite — real ou medida incorretamente. Não é uma falha definitiva. Mas precisa de diagnóstico antes de qualquer conclusão.

A rede elétrica no interior do Brasil oscila. Isso é documentado, é real, e dispara proteções legítimas de anti-ilhamento. Mas um capacitor de R$ 2,00 envelhecido no circuito PLL faz o mesmo — com muito menos dignidade.

Envie seu inversor para a TEC Solar. Realizamos diagnóstico eletrônico completo em nível de placa e devolvemos um laudo técnico detalhado — mesmo que o reparo não seja viável. Atendemos todo o Brasil via logística reversa. [Falar com a TEC Solar no WhatsApp](https://wa.me/5538998891587) | [@tec_solar_moc](https://www.instagram.com/tec_solar_moc/)

---

## [LINKS INTERNOS SUGERIDOS]

- Âncora: "proteções legítimas de anti-ilhamento" → Link para: post sobre Fronius State 108: Oscilação de Rede (Post 13)
- Âncora: "frequência da rede" → Link para: post sobre Deye F01/F02: Tensão de Rede Alta e Baixa (Post 03) — se publicado

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "PRODIST Módulo 8" → Fonte: ANEEL — Procedimentos de Distribuição de Energia Elétrica (gov.br/aneel)
- Texto âncora: "NBR IEC 62116" → Fonte: ABNT — Procedimento de ensaio de anti-ilhamento para inversores de sistemas fotovoltaicos conectados à rede elétrica (abnt.org.br)

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Inversor solar instalado em parede com painel de distribuição CA — representa diretamente o ponto de conexão de rede onde a frequência é monitorada e onde o F05 é disparado
→ Nome do arquivo: deye-f05-frequencia-rede-fora-limite-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Inversor solar Deye instalado com conexão CA — diagnóstico do F05 por frequência de rede fora do limite
→ Legenda: Fig. 1 — Deye F05 pode indicar rede elétrica instável ou defeito interno no circuito PLL de medição de frequência CA
→ Onde inserir: Topo do post, antes da introdução
→ Converter para WebP — máximo 150 KB

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581093458791-9f3c3250a8b0?w=1200
→ Por que foi escolhida: Técnico com osciloscópio medindo sinal elétrico em placa eletrônica — representa o procedimento de diagnóstico com análise de forma de onda CA descrito na seção "Como Identificar na Prática"
→ Nome do arquivo: diagnostico-deye-f05-osciloscópio-circuito-pll-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo forma de onda CA com osciloscópio em placa de inversor — diagnóstico do Deye F05 circuito PLL
→ Legenda: Fig. 2 — Osciloscópio e analisador de qualidade de energia são as ferramentas para diferenciar falha externa de defeito no circuito PLL interno do Deye
→ Onde inserir: Após H2 "Como identificar na prática"
→ Converter para WebP — máximo 150 KB
