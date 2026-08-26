# Post 118 — Fusível CC e varistor (MOV): a proteção que falha antes do inversor

---

[PALAVRA-CHAVE FOCO]
fusível CC inversor solar

---

[TÍTULO SEO — Title Tag]
Fusível CC e MOV: a proteção que falha no inversor

---

[SLUG — URL do Post]
fusivel-cc-varistor-mov-inversor-solar

---

[META DESCRIPTION]
Fusível CC aberto ou MOV em curto podem parar o inversor antes de qualquer defeito interno. Veja como diagnosticar cada componente na bancada.

---

[CATEGORIA]
Análise Técnica de Componentes

---

[TAGS]
fusível CC solar, varistor MOV inversor, proteção string fotovoltaica, sobretensão CC, diagnóstico inversor solar

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **fusível CC** abre. O **varistor MOV** vai ao curto. O inversor para. E o técnico olha para o equipamento errado.

Essa sequência acontece toda semana. Na nossa bancada, chegam inversores com orçamento de reparo aprovado, caixa de componentes já trocados, e o problema estava numa proteção que custa R$ 15,00 e fica do lado de fora do equipamento — às vezes dentro, mas acessível. Ninguém verificou antes de enviar.

## O que causa esse problema

Fusíveis CC no lado fotovoltaico têm função simples: interromper o circuito quando a corrente ultrapassa o limite suportado pelo cabo ou pelo estágio de entrada do inversor. O que o mercado subestima é como esses fusíveis falham.

Strings em paralelo com painéis de fabricantes diferentes, ou com células degradadas de forma desigual, geram desequilíbrio de corrente. Quando uma string produz tensão mais baixa que as demais, as strings vizinhas injetam corrente reversa nela. Essa corrente de retorno raramente é suficiente para disparar o fusível de imediato, mas aquece o elemento fusível de forma repetida. O resultado é fadiga térmica acumulada — e semanas ou meses depois o fusível abre sem que tenha ocorrido nenhuma condição de sobrecorrente real.

O varistor MOV (Metal Oxide Varistor) opera em paralelo com o barramento. Em condições normais é invisível ao circuito — resistência altíssima, sem interferência. Quando a tensão sobe acima do limiar de clampeamento (para o lado CC, geralmente entre 600 V e 1.000 V dependendo do modelo), o MOV conduz e desvia a energia do transiente para o terra, protegendo o inversor.

Cada absorção de energia reduz a capacidade total do MOV. Isso é acumulativo e irreversível.

No Centro-Oeste e no Cerrado brasileiro — Goiás, Mato Grosso, Triângulo Mineiro — a densidade de descargas atmosféricas é uma das mais altas do país. Um sistema instalado nessa região pode ter o MOV absorvendo dezenas de transientes num único verão. Quando um surto supera a energia residual que o MOV ainda consegue dissipar, ele falha: normalmente entra em curto permanente, mas pode também abrir completamente.

MOV em curto drena corrente pelo caminho de proteção, aquece o barramento e dispara o fusível em série com ele. Na ausência desse fusível de segurança, a corrente vai direto para a placa de entrada do inversor.

Não é o raio que destrói o inversor. É o MOV que foi ao curto e não tinha fusível em série protegendo o que vinha depois.

## Como identificar

Verificar fusível e MOV não exige osciloscópio. Multímetro resolve a maior parte dos casos:

1. Meça continuidade no fusível CC com o sistema desligado — fusível aberto não conduz; é o mais simples de identificar
2. Com o fusível aberto, meça a tensão nos bornes de string antes do fusível: se a string entrega tensão normal, a falha estava no componente de proteção, não nos painéis
3. Inspecione visualmente o MOV — corpo rachado, resíduo escuro, deformação ou odor localizado de queima indicam falha física
4. Com o sistema completamente desligado e capacitores descarregados (aguarde o tempo indicado no manual, normalmente 5 minutos): meça resistência entre os terminais do MOV. Em curto mostra valor próximo de zero; íntegro mostra acima de 1 MΩ
5. Em string combiners com múltiplos fusíveis: compare todos. Um fusível aberto numa string específica com os demais intactos aponta para desequilíbrio ou problema naquela string em particular
6. Se o inversor liga mas apresenta erro de isolamento ou corrente de fuga, investigue o estado do MOV antes de procurar defeito nos painéis ou cabos
7. Consulte o datasheet do MOV instalado: a energia máxima de absorção em joules e o nível de clampeamento determinam se o componente era adequado para o local de instalação

O que a gente vê com frequência são instalações no interior de Minas e do Mato Grosso onde o MOV era o mesmo especificado pelo fabricante para um mercado europeu — dimensionado para um regime de surtos muito mais baixo. O componente não tinha defeito de fabricação. Era subdimensionado para aquele microclima.

## Quando é falha eletrônica interna

Nem toda falha de fusível termina no fusível.

Quando o fusível abre repetidamente após a troca — sem explicação aparente na string — o diagnóstico precisa entrar no inversor. Um IGBT com corrente de fuga, um capacitor de barramento com ESR elevado ou uma falha no estágio boost podem gerar picos de corrente que não têm outra saída a não ser pelo fusível protetor.

Da mesma forma, o MOV que foi ao curto num evento de surto pode ter levado junto o circuito de entrada. Diodos TVS em paralelo, capacitores de filtro de modo comum e trilhas do barramento CC aparecem danificados nos casos mais graves. Trocar o MOV sem inspecionar o que ficou depois dele é substituir o componente protetor e ignorar o que ele não conseguiu proteger.

A distinção prática:
- Fusível aberto, troca feita, inversor opera normalmente → problema estava no fusível ou na string
- Fusível abre de novo após troca sem sobrecorrente na string → investigar interior do inversor
- MOV em curto com inversor que não inicializa → rastrear componentes na placa de entrada antes de concluir qualquer coisa

Ainda não existe resposta definitiva para o segundo caso só olhando de fora. Depende do que você vai encontrar quando abrir a placa.

## Vale a pena consertar?

Um fusível CC tipo gPV — padrão definido pela IEC 60269-6 para aplicações fotovoltaicas — de 15 A a 32 A custa entre R$ 12,00 e R$ 45,00. Um MOV adequado para o barramento CC de um sistema fotovoltaico custa entre R$ 8,00 e R$ 30,00 em distribuidores eletrônicos.

O reparo compensa em praticamente 100% dos casos onde a falha está isolada no componente de proteção. O trabalho de diagnóstico e substituição raramente passa de uma hora de bancada.

O custo sobe quando a falha do componente de proteção levou dano para o interior do inversor — especialmente nos casos de MOV em curto sem fusível em série. Aí o diagnóstico precisa avançar para o driver de IGBT, os capacitores de barramento e o estágio de entrada.

Antes de declarar falha no inversor, verifique os componentes de proteção. É o diagnóstico mais barato e mais rápido que existe. E é o que o mercado mais pula.

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

- Âncora: 'IGBT com corrente de fuga' → URL: /por-que-igbts-queimam-inversores-solares → Contexto: seção "Quando é falha eletrônica interna", onde o texto menciona IGBT como causa de fusível que abre repetidamente
- Âncora: 'capacitor de barramento com ESR elevado' → URL: /capacitor-barramento-cc-degradacao-esr → Contexto: seção "Quando é falha eletrônica interna", ao listar causas internas que agem sobre o fusível
- Âncora: 'driver de IGBT' → URL: /driver-gate-igbt-funcao-falha-diagnostico → Contexto: seção "Vale a pena consertar?", ao mencionar o que o diagnóstico precisa alcançar quando a falha vai além do componente de proteção
- Âncora: 'erro de isolamento ou corrente de fuga' → URL: /falha-isolamento-sistemas-fotovoltaicos → Contexto: seção "Como identificar", item 6, onde o texto orienta a investigar o MOV antes de procurar defeito nos painéis

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "IEC 60269-6" → URL: https://www.iec.ch/publication/series → Fonte: IEC — norma internacional para fusíveis de baixa tensão em aplicações fotovoltaicas CC
- Texto âncora: "densidade de descargas atmosféricas" → URL: https://www.inpe.br/webelat/homepage/ → Fonte: INPE — mapa de incidência de raios no Brasil (ELAT/INPE)

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ Buscar em: unsplash.com — termo de busca: "fuse box electrical protection solar"
→ Por que foi escolhida: Representa fisicamente os componentes de proteção CC (fusíveis e caixa de string) em sistemas fotovoltaicos
→ Nome do arquivo: fusivel-cc-varistor-mov-inversor-solar.webp
→ Alt Text: Fusíveis CC em string combiner box de sistema fotovoltaico com componentes de proteção contra sobretensão
→ Legenda: Fig. 1 — String combiner box com fusíveis CC gPV e varistor MOV — componentes de proteção antes do inversor
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ Buscar em: pexels.com — termo de busca: "multimeter electronic component testing"
→ Por que foi escolhida: Representa o diagnóstico com multímetro nos componentes de proteção, alinhado à seção de identificação
→ Nome do arquivo: fusivel-cc-varistor-mov-diagnostico-2.webp
→ Alt Text: Técnico medindo resistência de varistor MOV com multímetro durante diagnóstico de inversor solar na bancada
→ Legenda: Fig. 2 — Verificação de MOV com multímetro: resistência próxima de zero indica componente em curto-circuito
→ Onde inserir: Após H2 "Como identificar"
