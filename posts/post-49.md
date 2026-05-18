[PALAVRA-CHAVE FOCO]
placa de controle inversor solar defeito

─────────────────────────────────────
[TÍTULO SEO — Title Tag]
─────────────────────────────────────
Placa de Controle vs. Potência: Como Diferenciar o Defeito

─────────────────────────────────────
[SLUG — URL do Post]
─────────────────────────────────────
placa-controle-vs-potencia-como-diferenciar-defeito-inversor-solar

─────────────────────────────────────
[META DESCRIPTION]
─────────────────────────────────────
Como diferenciar defeito na placa de controle e na placa de potência do inversor solar. Protocolo de bancada com multímetro e osciloscópio.

─────────────────────────────────────
[CATEGORIA]
─────────────────────────────────────
Análise Técnica de Componentes

─────────────────────────────────────
[TAGS]
─────────────────────────────────────
placa de controle inversor solar, placa de potência inversor solar, diagnóstico inversor solar, falha IGBT inversor, reparo inversor solar bancada

─────────────────────────────────────
[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]
─────────────────────────────────────

# Post 49 — Placa de controle vs. placa de potência: como diferenciar onde está o defeito

A decisão mais importante no diagnóstico de um inversor parado é essa: **placa de controle ou placa de potência**. Errar aqui significa trocar o componente errado, gastar mais do que o necessário e, pior, devolver o equipamento ainda com falha.

Na nossa bancada, esse erro chega com uma história quase sempre igual: o técnico trocou os IGBTs, o inversor ligou por três dias e parou de novo. O defeito estava no driver da placa de controle, que continuava enviando pulsos fora de sequência. A placa de potência era consequência, não causa. O IGBT novo queimou no ciclo seguinte.

Saber onde olhar antes de tocar em qualquer componente define se o reparo vai custar R$ 400 ou R$ 2.000.

## O que diferencia a placa de controle da placa de potência

O inversor solar opera com dois estágios funcionalmente distintos. Eles trabalham juntos, mas as falhas têm origens e sintomas completamente diferentes.

A **placa de controle** (também chamada de placa lógica ou placa de sinal) contém o DSP ou microcontrolador principal, os circuitos de comunicação (RS485, Wi-Fi, CAN), os sensores de tensão e corrente de baixa energia, e os drivers de gate que disparam os IGBTs. É ela quem decide quando e como a energia vai fluir. Quando falha, os sintomas costumam ser menos óbvios: erros de comunicação, leituras de sensor inconsistentes, comportamento intermitente, ou o inversor travando sem mostrar nenhuma falha clara no display.

A **placa de potência** contém os IGBTs ou MOSFETs, os capacitores do barramento CC, os indutores de filtragem e os sensores de corrente de alta potência. É ela quem converte a energia dos painéis em CA para a rede. Quando falha, os sinais geralmente aparecem: cheiro de queimado, componente carbonizado, fusível aberto, tensão ausente no barramento.

O problema é que uma falha em uma pode destruir a outra.

Um IGBT em curto eleva o potencial no barramento e pode queimar o driver da placa de controle. Um driver disparando fora de fase pode colocar dois IGBTs em condução simultânea — curto direto no barramento CC. Isso é chamado de *shoot-through*, e quando acontece, normalmente leva as duas placas juntas.

Por isso, diagnosticar sem isolar a origem é apostar na sorte.

## Como identificar onde está o defeito

O protocolo segue esta sequência. Nenhuma etapa pode ser pulada sem justificativa técnica.

1. **Aguardar descarga dos capacitores** — mínimo de 10 minutos após desligar. Capacitores de barramento em equipamentos acima de 5 kW mantêm tensão residual acima de 400 V por vários minutos. Trabalhar antes disso é risco real de choque elétrico.

2. **Inspeção visual antes de qualquer medição** — componente carbonizado, trilha levantada, capacitor com cúpula abaulada ou vazamento de eletrólito. Dano visível aponta para a placa de potência. Sem nada visível, o problema provavelmente está na placa de controle ou na interface entre elas.

3. **Teste de continuidade nos IGBTs com multímetro em modo diodo** — medir junção coletor-emissor em ambas as polaridades. IGBT íntegro comporta-se como diodo em uma direção (queda de 0,4 a 0,7 V) e como circuito aberto na outra. Leitura próxima de zero nas duas direções confirma curto. Defeito na placa de potência confirmado.

4. **Verificação da fonte auxiliar** — a maioria dos inversores tem uma fonte auxiliar independente (flyback ou linear) que alimenta a placa de controle, geralmente fornecendo 12 V, 15 V ou 24 V. Se essa tensão está presente e estável, a placa de controle tem alimentação. Se está ausente, o problema começa na fonte auxiliar — que fica na placa de potência — antes de qualquer outra medição.

5. **Leitura dos sinais PWM com osciloscópio** — com o inversor em tentativa de inicialização, medir os sinais de gate na saída do driver. Sinais limpos e simétricos indicam que a placa de controle está gerando os comandos corretamente. Sinais ausentes, assimétricos ou com ruído excessivo apontam para falha no driver ou no DSP.

6. **Medição de resistência de isolamento CC-terra** — com megôhmímetro entre os terminais CC positivo/negativo e o terra do gabinete. Valor abaixo de 1 MΩ pode indicar capacitor Y de filtro de modo comum com vazamento, componente da placa de potência, mesmo sem sinal visual.

7. **Análise do padrão de erro no histórico** — erros de temperatura, tensão de rede, corrente de fuga e comunicação têm origem em sensores ou no processamento da placa de controle. Erros de overcurrent seguidos de componente queimado têm origem no estágio de potência.

O ponto de fronteira entre as duas placas é o gate do IGBT. Se o sinal está correto e o IGBT não responde, a falha é na placa de potência. Se o sinal está incorreto ou ausente, a falha está antes — no driver ou no DSP.

## O erro que mais custa: trocar sem medir

Trocar o IGBT sem verificar o driver antes é o erro mais frequente e mais caro que a gente vê passando pela bancada.

O componente novo queima no ciclo seguinte. O técnico conclui que a peça era de qualidade ruim, ou que o inversor não tem conserto, e a causa real segue intacta. Retrabalho garantido.

O segundo padrão: diagnosticar a placa de controle como defeituosa com base no comportamento externo, sem medir os sinais de gate. Reinicialização aleatória, erros de comunicação, comportamento intermitente — tudo isso pode ser sintoma de placa de potência com degradação lenta, não de problema na lógica de controle. Sem o osciloscópio no ponto de fronteira, o diagnóstico é estimativa.

Condenar o equipamento inteiro quando apenas uma placa falhou fecha a conta errada. Um inversor de 10 kW pode custar acima de R$ 8.000 novo. Uma placa de potência com IGBT em curto e driver comprometido, com placa de controle intacta, sai por fração disso.

Abrir e medir antes de decidir não é preciosismo técnico. É o que define se o reparo compensa.

## Vale a pena consertar?

Depende de quantas peças da cadeia foram comprometidas.

**IGBT com curto simples, driver intacto, placa de controle funcionando** — reparo direto, custo menor, alta viabilidade. É o cenário mais comum quando há histórico de surto único sem histórico de sobretemperatura.

**IGBT e driver comprometidos, placa de controle intacta** — viável, custo intermediário, bem abaixo do valor de um inversor novo. O módulo IGBT varia entre R$ 150 e R$ 500 dependendo do fabricante e da potência; o driver IC custa consideravelmente menos.

**Dano em cascata que alcançou a placa de controle** — análise individual por modelo. DSPs proprietários com código gravado são o maior obstáculo. Quando disponíveis no mercado de reposição, o reparo ainda pode fechar. Quando não estão, define o inviável.

**Carbonização severa em ambas as placas** — custo total ultrapassa 60% do valor de um inversor novo. O laudo entrega esse número antes de qualquer componente ser comprado.

No Norte e Nordeste do Brasil, onde inversores operam com temperatura ambiente acima de 40°C por meses consecutivos, o dano em cascata é mais frequente. O estágio de potência envelhece mais rápido nessas condições, e quando falha, tende a comprometer a placa de controle junto com mais regularidade do que em instalações com temperatura controlada.

Ainda não existe resposta antes de abrir e medir. O que você vai encontrar na placa é que define.

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

─────────────────────────────────────
[LINKS INTERNOS SUGERIDOS]
─────────────────────────────────────
- Âncora: 'por que os IGBTs queimam' → URL: /por-que-os-igbts-queimam-em-inversores-solares → Contexto: seção "O que diferencia a placa de controle da placa de potência", ao mencionar IGBT em curto e dano em cascata
- Âncora: 'driver de IGBT' → URL: /o-que-e-o-driver-de-igbt-e-por-que-sua-falha-destroi-o-estagio-de-potencia → Contexto: seção "O erro que mais custa", no parágrafo sobre trocar IGBT sem verificar o driver
- Âncora: 'capacitores eletrolíticos' → URL: /capacitores-eletrolíticos-em-inversores-vida-util-degradacao-e-quando-trocar → Contexto: seção "Vale a pena consertar?", ao mencionar degradação no estágio de potência
- Âncora: 'custo de reparo' → URL: /quanto-custa-reparar-um-inversor-vs-comprar-um-novo-a-conta-real → Contexto: seção "O erro que mais custa", ao comparar valor de reparo com equipamento novo
- Âncora: 'logística reversa' → URL: /como-funciona-a-logistica-reversa-de-equipamento-eletronico-no-brasil → Contexto: parágrafo do CTA, ao mencionar atendimento via logística reversa

─────────────────────────────────────
[LINKS EXTERNOS SUGERIDOS]
─────────────────────────────────────
- Texto âncora: "resistência de isolamento" → URL: https://www.abnt.org.br → Fonte: ABNT — NBR 16149 e NBR 16274, normas técnicas para sistemas fotovoltaicos conectados à rede
- Texto âncora: "IEC 62109" → URL: https://www.iec.ch/homepage → Fonte: IEC — norma internacional de segurança para conversores de energia em sistemas fotovoltaicos

─────────────────────────────────────
[IMAGEM PRINCIPAL — USE ESTA]
─────────────────────────────────────
IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Placa eletrônica com componentes visíveis de perto — representação direta do tema de diagnóstico em nível de placa de inversores
→ Nome do arquivo: placa-controle-potencia-inversor-solar-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Placa eletrônica de inversor solar com componentes SMD e capacitores — diagnóstico de placa de controle versus potência
→ Legenda: Fig. 1 — Placa de controle e placa de potência têm funções distintas; identificar qual falhou define todo o diagnóstico
→ Onde inserir: Topo do post, antes da introdução

─────────────────────────────────────
[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]
─────────────────────────────────────
IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=1200
→ Por que foi escolhida: Técnico com multímetro medindo componente eletrônico — ilustra diretamente o protocolo de verificação de IGBT descrito na seção de identificação
→ Nome do arquivo: diagnostico-multimetro-igbt-inversor-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo IGBT com multímetro em modo diodo em bancada de reparo de inversor solar fotovoltaico
→ Legenda: Fig. 2 — Teste de continuidade nos terminais do IGBT: leitura próxima de zero nas duas direções confirma curto na placa de potência
→ Onde inserir: Após H2 "Como identificar onde está o defeito"
