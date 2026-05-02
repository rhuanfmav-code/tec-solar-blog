[PALAVRA-CHAVE FOCO]
growatt erro 117 tensão CC alta inversor solar

─────────────────────────────────────
[TÍTULO SEO — Title Tag]
─────────────────────────────────────
Growatt Erro 117: Tensão CC Alta — Causa e Diagnóstico

─────────────────────────────────────
[SLUG — URL do Post]
─────────────────────────────────────
growatt-erro-117-tensao-cc-alta

─────────────────────────────────────
[META DESCRIPTION]
─────────────────────────────────────
Growatt Erro 117 indica sobretensão no barramento CC. Veja como separar string mal configurada de falha no circuito de medição interno.

─────────────────────────────────────
[CATEGORIA]
─────────────────────────────────────
Códigos de Erro e Falhas

─────────────────────────────────────
[TAGS]
─────────────────────────────────────
Growatt Erro 117, tensão CC alta inversor solar, string fotovoltaica, circuito de medição, diagnóstico Growatt

─────────────────────────────────────
[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]
─────────────────────────────────────

# Post 36 — Growatt Erro 117: Tensão CC Alta Demais — string mal configurada ou falha no circuito de medição?

O **Growatt Erro 117** aparece no display quando a tensão no barramento CC interno ultrapassa o limite operacional definido pelo firmware. Inversor travado, sistema sem geração, cliente ligando. Para o técnico que recebe o chamado, o pressuposto quase imediato é: problema na string — módulos em série demais.

Na nossa bancada, esse erro chega com dois perfis completamente distintos. O primeiro é o inversor com string genuinamente mal dimensionada, tensão de circuito aberto acima do Vmax do equipamento. O segundo é o inversor com a string dentro dos limites, tensão medida no terminal dentro do esperado, mas com o circuito de medição interno com defeito — reportando um valor que não existe na prática. Quem não mede antes de concluir vai embora com o problema intacto.

---

## O que causa o Erro 117 nos inversores Growatt

O Erro 117 nos modelos Growatt corresponde a "Bus Voltage High" — sobretensão no barramento CC interno. O barramento DC é o estágio intermediário entre a entrada fotovoltaica e o estágio de inversão: é onde a energia CC dos painéis é estabilizada antes de virar CA para a rede.

Duas causas raiz explicam esse erro, e elas não têm nada em comum.

A primeira é a string mal dimensionada. Quando a quantidade de módulos em série gera uma tensão de circuito aberto (Voc) acima do Vmax do inversor, o barramento CC opera além do limite tolerado. O problema é amplificado pela variação de temperatura: a tensão de circuito aberto aumenta conforme a temperatura cai — efeito do coeficiente térmico negativo de tensão, descrito no datasheet de qualquer módulo fotovoltaico. Uma string calculada para condição NOCT pode ter Voc corrigido excedendo o limite nas manhãs de julho em Santa Catarina ou no Rio Grande do Sul, enquanto a mesma string funciona sem erro nenhum em Mato Grosso o ano inteiro. A região importa para o cálculo.

A segunda causa é eletrônica interna. O inversor mede a tensão do barramento CC através de um divisor resistivo ligado a um conversor analógico-digital (ADC) na placa de controle. Quando um dos resistores desse divisor deriva significativamente do valor nominal por envelhecimento, calor ou umidade absorvida — ou quando o próprio ADC apresenta leitura incorreta — o firmware interpreta uma tensão que não existe. O inversor acusa o Erro 117. A string está correta. O problema está dentro da caixa.

---

## Como identificar na prática

O protocolo de campo começa por separar as duas causas antes de qualquer conclusão:

1. Com o inversor desligado, meça a tensão CC nos terminais de entrada com multímetro calibrado. Registre o valor real.
2. Calcule o Voc corrigido por temperatura para a string instalada: Voc_corrigido = Voc_STC × [1 + (coeficiente de temperatura × (T_ambiente − 25))]. O coeficiente está no datasheet do módulo — geralmente entre −0,25%/°C e −0,40%/°C.
3. Compare com o Vmax do inversor. Modelos Growatt de 3 kW a 10 kW costumam ter Vmax entre 450 V e 600 V; modelos de string acima de 15 kW chegam a 1000 V. Consulte o manual.
4. Se a tensão medida está acima do Vmax, a string está fora do limite. O caminho é reconfigurar — remover um módulo da string ou revisar o projeto.
5. Se a tensão medida está dentro do limite, compare o valor que o display ou o monitoramento do inversor reporta com o que o multímetro indica nos terminais físicos. Divergência significativa entre os dois aponta diretamente para falha no circuito de medição.
6. Um sinal adicional: o erro aparece de forma intermitente, especialmente logo após a inicialização, sem correlação com hora do dia ou irradiância. Esse padrão é característico de componente com falha elétrica na placa — não de string com tensão real elevada.

---

## O erro mais comum do mercado

O diagnóstico mais frequentemente errado com o Growatt Erro 117 é assumir que a string está errada sem medir nada.

O instalador estima o número de módulos, faz uma conta rápida e conclui que "devia estar fora do limite". Remove um módulo. O erro some. E ele vai embora achando que resolveu.

O que aconteceu na prática: ao reduzir a string, a tensão caiu bem abaixo do limiar onde o circuito de medição com defeito apresentava leitura errática. O problema eletrônico continua lá dentro. Vai se manifestar de novo — talvez em outro código, talvez com dano maior.

Condenar a string sem confirmar o circuito de medição é o caminho mais caro.

---

## Quando o reparo é viável

Se a causa é a string, o reparo do inversor não entra na equação — o trabalho é de projeto, não de bancada.

Se a causa é eletrônica interna, o diagnóstico determina a extensão:

- Resistores do divisor de tensão com deriva: substituição pontual, reparo simples com custo baixo
- ADC danificado no circuito de aquisição: substituição do componente, viável na maioria dos modelos Growatt, desde que não haja dano em cascata
- Microcontrolador da placa de controle afetado: complexidade aumenta — depende do modelo e da disponibilidade do componente
- Dano em cascata no estágio de potência por operação prolongada com sobretensão real: IGBT ou módulo de potência comprometido, custo sobe, mas costuma ser inferior ao inversor novo

Um Growatt de 5 kW custa entre R$ 2.500 e R$ 4.000 no mercado atual. O reparo de um circuito de medição com defeito, sem dano em cascata, fica em torno de R$ 400 a R$ 800 dependendo do componente afetado. A conta não é difícil de fazer.

Ainda não existe resposta definitiva sobre o que vai ser encontrado sem abrir o equipamento. Depende do que está na placa.

---

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
- Âncora: "por que os IGBTs queimam" → Link para: post sobre causas de falha de IGBT (Post 10)
- Âncora: "o que é o driver de IGBT" → Link para: post sobre driver de IGBT e falha no estágio de potência (Post 21)
- Âncora: "Growatt Erro 102" → Link para: post sobre Growatt Erro 102 falha de isolamento (Post 01)

─────────────────────────────────────
[LINKS EXTERNOS SUGERIDOS]
─────────────────────────────────────
- Texto âncora: "coeficiente térmico negativo de tensão" → Fonte: datasheet do fabricante do módulo fotovoltaico (ex: Canadian Solar, BYD, Jinko — seção Electrical Characteristics)
- Texto âncora: "NBR 16274" → Fonte: ABNT NBR 16274 — Sistemas fotovoltaicos conectados à rede elétrica: requisitos mínimos para documentação, ensaios de comissionamento, inspeção e avaliação de desempenho

─────────────────────────────────────
[IMAGEM PRINCIPAL — USE ESTA]
─────────────────────────────────────
IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?w=1200
→ Por que foi escolhida: placa de circuito eletrônico com componentes SMD visíveis, representando o circuito de medição interno do inversor
→ Nome do arquivo: circuito-medicao-inversor-growatt-erro-117.webp
→ Alt Text (máx. 125 caracteres): Placa de controle de inversor solar com circuito de medição de tensão CC — diagnóstico do Growatt Erro 117
→ Legenda: Fig. 1 — O circuito de medição interno: divisor resistivo e ADC que reportam a tensão do barramento CC ao firmware
→ Onde inserir: Topo do post, antes da introdução

─────────────────────────────────────
[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]
─────────────────────────────────────
IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: painel solar com string de módulos em série visível, representando o contexto de string fotovoltaica
→ Nome do arquivo: string-fotovoltaica-tensao-cc-alta.webp
→ Alt Text (máx. 125 caracteres): String de painéis solares em série com tensão CC elevada — causa externa do Growatt Erro 117 em inversores
→ Legenda: Fig. 2 — String com módulos em série: o Voc corrigido por temperatura é o primeiro ponto de verificação no campo
→ Onde inserir: Após H2 "Como identificar na prática"
