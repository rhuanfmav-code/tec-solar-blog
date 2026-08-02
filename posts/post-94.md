# Post 94 — Driver de gate do IGBT: função, modos de falha e diagnóstico na bancada

---

[PALAVRA-CHAVE FOCO]
driver de gate IGBT inversor solar

---

[TÍTULO SEO — Title Tag]
Driver de Gate do IGBT: Falhas e Diagnóstico na Bancada

---

[SLUG — URL do Post]
driver-gate-igbt-falhas-diagnostico-bancada

---

[META DESCRIPTION]
O driver de gate do IGBT falha antes do transistor na maioria dos casos. Entenda como ele funciona, como identificar a falha e o que muda no reparo.

---

[CATEGORIA]
Análise Técnica de Componentes

---

[TAGS]
driver de gate IGBT, falha IGBT inversor solar, diagnóstico placa de potência, reparo inversor solar, CI driver IGBT

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **driver de gate do IGBT** não aparece nos manuais do integrador. Não vem no checklist de instalação. É um circuito que existe entre o sinal de controle do DSP e o gate do transistor de potência — e quando ele falha, o inversor para sem deixar rastro claro.

Na nossa bancada, esse padrão chega com frequência. O inversor vem rotulado como "IGBT queimado". Abrimos, medimos, e o IGBT está em curto — mas o CI de driver do mesmo braço está carbonizado. A pergunta correta nesse momento não é "onde está o componente para repor": é qual falhou primeiro, e o que causou o outro.

Essa distinção muda o reparo inteiro.

## O que causa esse problema

O IGBT não obedece diretamente ao sinal lógico do DSP. O controlador gera pulsos PWM em 3,3 V ou 5 V — mas o gate do transistor precisa de +15 V para conduzir de forma plena e de –8 V para bloquear com segurança. Sem tensão negativa de bloqueio, o IGBT não corta de forma confiável. Em barramento de 400 V ou 800 V CC, isso significa curto na meia-onda errada.

O driver faz quatro coisas ao mesmo tempo: eleva o nível do sinal, amplifica corrente para carregar a capacitância de gate (que pode chegar a 100 nC nos IGBTs de potência), isola galvanicamente o circuito de controle do circuito de potência, e monitora o estado do transistor para desarmar em caso de falha.

Quando falha, falha por quatro razões principais:

**Falta de alimentação isolada.** O driver tem sua própria fonte — uma SMPS auxiliar ou circuito bootstrap. Se essa tensão cai abaixo do UVLO (undervoltage lockout, tipicamente 13,5 V), o driver trava. O IGBT para de chavear. Em redes com quedas frequentes — e as redes de baixa tensão no interior do Brasil conhecem isso bem — esse mecanismo pode esgotar o bootstrap antes do tempo.

**Curto no IGBT que destrói o driver junto.** Quando o IGBT entra em curto, a corrente sobe em microssegundos. O driver detecta pelo circuito de desaturação: monitora a tensão VCE em condução e, se ela subir além do esperado, tenta o soft turn-off. O problema é que a energia do barramento, em um curto real, pode ultrapassar a capacidade de absorção do CI antes que o desligamento complete. O técnico que chega depois condena os dois sem saber qual provocou o quê.

**Degradação do optoacoplador.** A maioria dos drivers usa optoacopladores para isolar o sinal de PWM do lado de controle. Com ciclos térmicos e horas acumuladas, o LED interno perde eficiência — o CTR (current transfer ratio) cai, o sinal chega distorcido, e o IGBT passa a chavear de forma imprecisa. Não para o inversor imediatamente. Aumenta as perdas, aumenta o calor, desgasta o transistor por dentro.

**Resistor de gate alterado.** O Rg controla a velocidade de chaveamento. Um Rg aberto impede o chaveamento completamente. Um Rg com valor alterado por degradação acelera ou atrasa as bordas do gate — gerando spikes de tensão VCE no desligamento ou abrindo janela para que dois IGBTs do mesmo braço conduzam ao mesmo tempo.

## Como identificar

O diagnóstico do driver de gate não se faz com multímetro. Exige osciloscópio.

1. Medir a alimentação isolada do driver — pinos Vcc+ e Vcc– com multímetro. O valor típico é +15 V / –8 V ou +15 V / –5 V dependendo do projeto. Desvio acima de 10% indica problema na fonte auxiliar antes mesmo de tocar no CI de driver.
2. Com osciloscópio no par gate-emitter do IGBT: verificar se o sinal PWM está presente, se a forma de onda é quadrada, e se a amplitude bate com o projeto.
3. Verificar as bordas de chaveamento: subida e descida lentas (acima de 1 µs em IGBTs de potência padrão) indicam Rg alto, driver fraco ou optoacoplador degradado.
4. Medir o spike de tensão VCE no desligamento: valores acima de 150% da tensão nominal do IGBT indicam Rg baixo demais ou indutância parasita excessiva na trilha de gate.
5. Verificar o pino de fault do CI de driver — se ativo, o driver está em proteção; identificar qual condição ativou (UVLO, desaturação, sobrecorrente).
6. Testar o optoacoplador: injetar sinal de referência no lado de controle e medir o sinal no lado de potência. CTR menor que 50% do especificado indica degradação.
7. Medir os resistores de gate com LCR meter ou multímetro: desvio acima de 20% do valor de projeto muda o comportamento de chaveamento de forma relevante.
8. Inspecionar visualmente com lupa: CI de driver com marca de calor ou bolha na resina, trilhas levantadas ao redor do gate, componentes com alteração de cor.

O padrão que a gente vê com mais frequência: IGBT em curto, CI de driver carbonizado, Rg com resistência aberta. Os três no mesmo braço, chegando na bancada como se fossem um único defeito.

## Quando é falha eletrônica interna

A maior parte das falhas de driver não tem causa externa identificável. O CI chegou ao fim da vida útil, ou foi destruído por um transitório que o barramento gerou em algum momento de carga irregular.

Mas há situações com causa raiz fora do inversor:

- String superdimensionada sobe a tensão do barramento além do projeto, gera spike de desligamento que supera o suporte do driver — o CI vai queimando progressivamente até parar
- Ambiente com temperatura de gabinete acima de 60–70 °C em barracões fechados no Nordeste ou Centro-Oeste no verão reduz a vida do optoacoplador e dos capacitores da fonte auxiliar do driver de forma acelerada
- Cabo de gate longo ou mal roteado cria indutância parasita na malha, piora o perfil de chaveamento e aumenta o stress no CI
- Rede elétrica instável com quedas e retornos frequentes cicla o bootstrap além da especificação, desgastando a fonte isolada antes do prazo

Quando a causa é externa e não é corrigida, trocar o CI de driver resolve por meses. O problema volta pelo mesmo caminho.

## Vale a pena consertar?

Se o diagnóstico mostrou que o dano está restrito ao driver — CI queimado, optoacoplador degradado, Rg aberto — o reparo é tecnicamente simples e o custo é baixo. Os CIs mais comuns em inversores solares (HCPL-314J, ISO5500, 1EDC20I12AH, ACPL-P343) custam entre R$ 30 e R$ 150 por unidade. A soldagem é SMD de complexidade média. Com o componente certo e execução correta, o resultado é equipamento operando igual ao original.

A variável que complica: disponibilidade. Alguns desses CIs têm lead time longo no mercado nacional, ou chegam apenas via importação direta com custo de frete que altera a equação.

Se o IGBT também foi destruído junto, o conjunto IGBT + driver + Rg em inversores de 5 kW a 15 kW sai entre R$ 400 e R$ 1.500 dependendo do modelo — frente a um inversor novo na mesma faixa de R$ 4.000 a R$ 14.000, a diferença ainda é expressiva.

O único cenário onde não compensa: dano em cascata que atingiu múltiplos braços, a placa de controle e a fonte auxiliar ao mesmo tempo. Aí o custo de peças se aproxima do equipamento novo, e a conta precisa ser refeita.

O driver de gate é barato. O que é caro é chegar na bancada sem saber que ele existia.

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

- Âncora: 'por que os IGBTs queimam' → URL: /por-que-igbts-queimam-inversores-solares → Contexto: seção "O que causa esse problema", ao descrever o IGBT em curto destruindo o driver junto
- Âncora: 'driver de IGBT' → URL: /driver-igbt-falha-estagio-potencia → Contexto: introdução, ao apresentar o driver de gate como componente crítico entre controle e potência
- Âncora: 'placa de controle' → URL: /placa-controle-vs-placa-potencia-como-diferenciar-defeito → Contexto: seção "Vale a pena consertar?", ao descrever dano em cascata que atinge múltiplos componentes
- Âncora: 'logística reversa' → URL: /logistica-reversa-reparo-inversores-como-funciona → Contexto: bloco CTA, reforçando o atendimento nacional via envio
- Âncora: 'a maioria dos inversores condenados pelo mercado ainda tem conserto' → URL: /inversores-condenados-mercado-ainda-tem-conserto → Contexto: seção "Vale a pena consertar?", ao argumentar que defeitos pontuais no driver são reparáveis

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IGBTs de potência" → URL: https://www.iec.ch/homepage → Fonte: IEC 60747-9 — norma internacional para transistores bipolares de gate isolado (IGBT), referência para parâmetros de gate, tensão de saturação VCE e capacitância de gate usados no diagnóstico
- Texto âncora: "tensão negativa de bloqueio" → URL: https://www.aneel.gov.br → Fonte: ANEEL — Resolução Normativa 1000/2021 define requisitos de qualidade da energia e parâmetros de rede que impactam diretamente o comportamento do barramento CC e o stress no driver de gate

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: placa eletrônica de potência com componentes SMD visíveis, representando a análise de bancada de um circuito de driver de gate em inversor solar
→ Nome do arquivo: driver-gate-igbt-placa-potencia-inversor.webp
→ Alt Text (máx. 125 caracteres): Placa de potência de inversor solar com CI driver de gate IGBT — diagnóstico eletrônico em nível de componente na bancada
→ Legenda: Fig. 1 — O driver de gate fica na placa de potência, entre o sinal de controle do DSP e o gate do IGBT: pequeno, mas responsável por manter o transistor vivo
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=1200
→ Por que foi escolhida: técnico com osciloscópio medindo sinal em placa eletrônica, representando a etapa de diagnóstico da forma de onda de gate no IGBT
→ Nome do arquivo: diagnostico-driver-gate-igbt-osciloscopio.webp
→ Alt Text (máx. 125 caracteres): Técnico usando osciloscópio para diagnosticar sinal de gate do IGBT em inversor solar — verificação de forma de onda e amplitude
→ Legenda: Fig. 2 — Sem osciloscópio no par gate-emitter, não é possível saber se o driver está enviando o sinal correto ou se o IGBT está recebendo tensão fora da especificação
→ Onde inserir: Após H2 "Como identificar"
