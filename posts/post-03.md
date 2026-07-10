# Post 03 — Deye F01/F02: Tensão de Rede Alta e Baixa — Causa e Diagnóstico

---

## [PALAVRA-CHAVE FOCO]

Deye F01 F02 tensão de rede inversor solar diagnóstico

---

## [TÍTULO SEO — Title Tag]

Deye F01/F02: Tensão de Rede Alta e Baixa — Causa Real

---

## [SLUG — URL do Post]

deye-f01-f02-tensao-rede-alta-baixa-diagnostico

---

## [META DESCRIPTION]

Inversor Deye com F01 ou F02? Entenda quando o problema é a rede, o cabo ou defeito interno na placa de controle. Diagnóstico técnico TEC Solar.

---

## [CATEGORIA]

Códigos de Erro e Falhas

---

## [TAGS]

Deye F01, Deye F02, sobretensão inversor solar, subtensão rede CA, diagnóstico placa Deye

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **inversor Deye com erro F01 ou F02** para o sistema e não retorna sem intervenção manual. F01 é sobretensão de rede — a tensão CA subiu acima do limite superior. F02 é subtensão — caiu abaixo do inferior. A confusão começa porque os dois códigos aparecem com causas completamente diferentes, e o mercado trata os dois da mesma forma: "problema na rede" ou "placa com defeito", sem medir nada.

Na nossa bancada, o padrão mais frequente chega assim: integrador relata que o sistema operava normal por meses, passou a acionar F01 entre 11h e 14h no verão, e o erro some quando o inversor reduz a geração ou quando a carga da casa aumenta. Já recebemos Deyes do interior de São Paulo e do sul de Minas com esse padrão quase idêntico. O diagnóstico completo leva menos de 20 minutos com um multímetro na mão. O que falta, na maioria dos casos, é saber o que medir e onde.

---

## O que causa o F01 e o F02 nos inversores Deye

Os inversores Deye da série SUN-K monitoram a tensão CA continuamente. O código **F01** dispara quando a tensão sobe acima do limite superior configurado. O **F02** dispara quando cai abaixo do inferior. Ambos acionam a desconexão automática imediata, conforme exige a ABNT NBR 16149.

A norma define para o Brasil: desconexão acima de 110% da tensão nominal (242V para redes de 220V) e abaixo de 80% (176V para 220V). Os limites padrão de fábrica nos inversores Deye podem vir configurados com base 230V — tensão europeia. Isso desloca o limite superior para 253V em vez de 242V. Em redes brasileiras com variação natural, a consequência depende de como a rede se comporta na instalação específica.

**Causas externas — as mais frequentes:**
- Tensão da distribuidora genuinamente fora dos limites do PRODIST Módulo 8
- Cabo CA de exportação subdimensionado: durante a geração, a corrente no condutor eleva a tensão nos próprios terminais do inversor
- Neutro com resistência elevada por conexão solta: desequilibra a tensão de referência e pode causar tanto F01 quanto F02, dependendo da fase afetada
- Parâmetros de proteção configurados com base europeia aplicados em instalação brasileira de 220V — o limite fica deslocado em relação à rede real

**Causa interna:**

O circuito de medição de tensão CA usa um divisor resistivo de alta impedância para escalar os 220V CA até um nível legível pelo ADC do processador. São resistores de centenas de kΩ a MΩ. Se qualquer um deles derivar por envelhecimento, corrosão ou sobretensão transitória, o inversor passa a "ver" uma tensão que não existe nos terminais. E dispara proteção em cima de uma leitura falsa.

Isso é menos frequente que a causa externa — mas é determinante no diagnóstico diferencial.

---

## Como identificar na prática

O diagnóstico começa com uma comparação obrigatória: o que o multímetro True RMS lê nos terminais CA do inversor versus o que o display ou o portal Solarman exibe. Essa medição precisa ser feita com o sistema gerando, nunca com ele desligado.

1. Conecte um multímetro True RMS (Fluke 87V ou equivalente) nos terminais L-N do inversor com o sistema em operação na potência máxima
2. Anote a leitura do instrumento
3. Anote a tensão exibida no display ou no Solarman
4. Compare: diferença acima de 5V aponta para defeito no circuito de medição interno

Se os dois valores batem, o problema é externo. O levantamento continua:

5. Meça a tensão no ramal de entrada ou no medidor da concessionária
6. Meça no quadro de distribuição do imóvel
7. Meça nos terminais CA do inversor com ele gerando na potência nominal
8. Calcule a queda de tensão no cabo: ΔV = 2 × ρ × L / S × I (onde ρ = 0,0175 Ω.mm²/m para cobre, L em metros, S em mm², I em Ampères)
9. Consulte o histórico de alarmes no portal Solarman: F01 aparece apenas no horário de pico de geração — ou também à noite ou com o inversor em stand-by?

Se F01 ou F02 dispara com os terminais CA fisicamente desconectados, a causa externa fica eliminada completamente. Isso é falha interna.

**Sinais físicos de defeito na placa de controle:**
- Resistores SMD do circuito de medição com coloração escurecida ou lascados
- Trilhas próximas ao conector CA com oxidação — especialmente comum em instalações no litoral nordestino e fluminense, onde umidade salina corrói os componentes ao longo de meses
- Capacitores no circuito de filtragem com inchaço ou eletrólito seco

---

## O erro mais comum do mercado

Medir a tensão da rede com o inversor desligado.

Quando o inversor está em stand-by, não há corrente no cabo CA. A tensão no quadro e nos terminais é praticamente a mesma. O técnico lê 232V, conclui que a rede está dentro do limite e parte para trocar a placa de controle.

O que ele não mediu: o que acontece quando o inversor injeta 5 kW na rede por um cabo de 2,5mm² com 25 metros. Nessa condição, a corrente é de aproximadamente 22,7A. A resistência do condutor ida e volta é 2 × 0,0175 × 25 / 2,5 = 0,35Ω. A elevação de tensão nos terminais é 22,7 × 0,35 = 7,9V. Uma rede de 234V no quadro aparece como 242V nos terminais durante a geração. Se o limite de desconexão está configurado para 240V, o F01 vai acionar toda vez que o inversor trabalhar próximo da potência nominal.

No interior do Nordeste e em partes do Centro-Oeste, é comum a rede oscilar entre 237V e 243V nos horários de maior demanda. Com cabo subdimensionado, o F01 fica contínuo durante o verão.

O segundo erro frequente: ajustar os limites de proteção para "tolerar" tensões mais altas sem confirmar a causa. Isso pode resolver o sintoma mas mantém o sistema operando fora da norma. O passivo de segurança passa a ser do integrador.

---

## Quando o reparo é viável

**Sem necessidade de intervenção no inversor:**
- Tensão da distribuidora fora do PRODIST Módulo 8: registre as medições com data e hora, correlacione com o histórico de alarmes do Solarman e abra chamado formal na distribuidora
- Cabo CA subdimensionado identificado: recalcule a bitola para a potência e comprimento do trecho e substitua
- Parâmetros configurados com base europeia: acesse o menu de proteção com senha de instalador e ajuste os limites conforme a NBR 16149 para redes de 220V

**Reparo eletrônico indicado quando:**
- Display mostra tensão sistematicamente diferente do multímetro em mais de 5V
- F01 ou F02 dispara com os terminais CA fisicamente desconectados
- Inspeção visual confirma componentes danificados próximos ao circuito de medição CA

O reparo envolve a substituição dos resistores do divisor de alta tensão e, se necessário, dos capacitores de filtragem. São componentes de alta estabilidade, tolerância de 1%, mínimo 1W. Os valores precisos dependem da revisão de placa e requerem o esquema elétrico do modelo específico. Um reparo feito com valores aproximados pode corrigir o sintoma mas deixar a leitura imprecisa — o que é tecnicamente pior do que não reparar, porque o inversor vai operar sem a proteção de tensão funcionando corretamente.

Um inversor Deye residencial novo custa entre R$ 3.500 e R$ 5.000. O reparo em nível de componente no circuito de medição fica em R$ 350 a R$ 600, dependendo do grau de dano e do acesso ao material técnico do fabricante.

---

## Conclusão

F01 e F02 no Deye têm causa raiz identificável — na maioria dos casos em menos de 20 minutos de medição. A comparação entre o que o multímetro lê e o que o display mostra, feita com o sistema gerando, separa o problema externo do interno. O que atrasa o diagnóstico não é a falta de equipamento. É partir para troca sem medir.

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

- Âncora: "falha de isolamento" → URL: /growatt-erro-102-falha-isolamento-string-leakage → Contexto: mencionar no H2 "O que causa o F01 e o F02" ao falar de causas internas, como comparação com outros tipos de falha eletrônica interna
- Âncora: "inversor solar parou de funcionar" → URL: /inversor-solar-parou-checklist-completo → Contexto: inserir no H2 "O erro mais comum do mercado" ao citar o checklist como referência antes de condenar o equipamento
- Âncora: "cabo CA subdimensionado" → URL: /fronius-state-102-tensao-cc-alta-diagnostico → Contexto: inserir no H2 "Quando o reparo é viável" ao mencionar a bitola correta do cabo como solução

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16149" → URL: https://www.abnt.org.br → Fonte: ABNT — Norma Técnica de Sistemas Fotovoltaicos, Interface de Conexão com a Rede Elétrica de Distribuição
- Texto âncora: "PRODIST Módulo 8" → URL: https://www.aneel.gov.br/prodist → Fonte: ANEEL — Procedimentos de Distribuição de Energia Elétrica no Sistema Elétrico Nacional, Módulo 8: Qualidade da Energia Elétrica

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1621905251918-48416bd8575a?w=1200
→ Por que foi escolhida: Técnico analisando placa eletrônica de inversor — contexto direto do diagnóstico de circuito de medição de tensão descrito no post
→ Nome do arquivo: deye-f01-f02-diagnostico-tensao-rede-placa.webp
→ Alt Text (máx. 125 caracteres): Técnico diagnosticando erro F01 F02 em inversor Deye com multímetro na placa de controle
→ Legenda: Fig. 1 — Diagnóstico do circuito de medição de tensão CA na placa de controle de inversor Deye
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Multímetro em uso com equipamento eletrônico — ilustra o procedimento de medição de tensão CA descrito no H2 de diagnóstico
→ Nome do arquivo: medicao-tensao-ca-inversor-deye-multimetro-2.webp
→ Alt Text (máx. 125 caracteres): Multímetro True RMS medindo tensão CA nos terminais de inversor Deye durante geração solar
→ Legenda: Fig. 2 — Medição de tensão CA com o sistema gerando. A comparação entre o instrumento e o display é o primeiro passo do diagnóstico
→ Onde inserir: Após H2 "Como identificar na prática"
