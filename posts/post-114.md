# Post 114 — MCU e DSP da placa de controle: quando o cérebro do inversor falha

---

[PALAVRA-CHAVE FOCO]
falha de MCU DSP inversor solar placa de controle

---

[TÍTULO SEO — Title Tag]
MCU e DSP do Inversor: Quando a Placa de Controle Falha

---

[SLUG — URL do Post]
mcu-dsp-placa-controle-inversor-solar

---

[META DESCRIPTION]
MCU ou DSP com defeito no inversor solar? Saiba identificar, diferenciar de firmware e quando o reparo é viável na bancada.

---

[CATEGORIA]
Análise Técnica de Componentes

---

[TAGS]
MCU inversor solar, DSP placa de controle, falha placa de controle, diagnóstico eletrônico inversor

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **MCU e o DSP da placa de controle** são os componentes que efetivamente comandam um inversor solar. Não é o IGBT que decide quando o circuito comuta — é o processador digital que lê os sensores, executa os algoritmos de MPPT, controla os drivers de gate e aciona as proteções. Quando esse processador falha, o inversor para. E o sintoma mais comum é justamente o que parece ser uma falha sem lógica: display em branco, inicialização incompleta, código de erro diferente a cada ciclo de energia.

Na nossa bancada, esse tipo de defeito costuma chegar mascarado por tentativas anteriores de software. O técnico já fez atualização de firmware. Já resetou de fábrica. Às vezes dois ou três ciclos de energia "resolveram" por alguns dias — até parar de resolver. O equipamento chega com a suspeita genérica de "placa queimada", sem que alguém tenha medido as tensões de alimentação do MCU ou verificado o sinal de clock na placa.

## O que causa esse problema

O MCU (Microcontroller Unit) e o DSP (Digital Signal Processor) são chips distintos com funções específicas. O MCU cuida da lógica de supervisão, da comunicação (RS485, Wi-Fi, CAN) e da interface com o usuário. O DSP executa os algoritmos de controle em tempo real — MPPT, formação de onda CA, sincronização com a rede. Em alguns modelos as funções estão integradas em um único chip; em outros, os dois coexistem na mesma placa com barramentos separados.

As causas de falha mais frequentes são:

- Subtensão na fonte auxiliar interna: se a SMPS entrega tensão abaixo do nominal — 3,3 V ou 5 V para o MCU, às vezes 1,8 V para o núcleo do DSP — o chip opera de forma errática antes de travar. Esse comportamento se confunde facilmente com bug de firmware.
- Descarga eletrostática (ESD): pinos de GPIO e interfaces RS485 sem proteção adequada são danificados durante manutenção em campo. A falha pode ser parcial — o periférico morre, o núcleo do processador continua ativo.
- Estresse térmico repetido: ciclos diários de aquecimento e resfriamento causam fadiga nas juntas de solda, especialmente em chips BGA com muitos pinos sob o encapsulamento. No Brasil, inversores instalados em ambientes sem controle térmico — galpões no Nordeste e no Centro-Oeste — chegam com esse padrão de falha com frequência bem acima da média.
- Sobretensão transitória: surtos vindos pela rede CA alcançam a placa de controle por acoplamento capacitivo ou por trilhas de sinal mal protegidas, danificando pinos de entrada do DSP.
- Corrosão por umidade: condensação em instalações costeiras penetra pelo conector de display e deposita resíduo iônico sobre os pinos do MCU, criando falha intermitente que piora com o tempo.

Firmware corrompido pode simular falha de MCU, mas é causa distinta. O chip pode estar íntegro e apenas um setor da memória flash estar danificado. A distinção é crítica — um diagnóstico errado aqui resulta em substituição de componente que não precisa ser trocado.

## Como identificar

O comportamento de boot revela muito antes de qualquer medição com instrumento:

1. **Display em branco imediato** — o inversor recebe energia mas não exibe nada: verifique a fonte auxiliar (5 V e 3,3 V nos pontos de test do esquemático) antes de qualquer outra medição
2. **Boot incompleto** — exibe a tela inicial mas trava antes de chegar ao modo de operação: o MCU inicializa mas não conclui o handshake com o DSP ou com o módulo de comunicação
3. **Códigos de erro inconsistentes** — erros diferentes a cada ciclo sem relação com as grandezas medidas: sinal claro de instabilidade no processamento dos sensores
4. **RS485 ou Wi-Fi ausentes sem falha no estágio de potência** — o inversor gera energia normalmente mas o datalogger não recebe dados: defeito parcial no periférico de comunicação do MCU
5. **MPPT travado em ponto fixo** — o DSP processa mas não rastreia o ponto de máxima potência; traçador de curva I-V confirma a falha no algoritmo de rastreamento
6. **Temperatura de chip acima de 80°C em standby** — o componente está puxando corrente anormal, indicativo de curto parcial interno detectável com câmera térmica

Com osciloscópio, verifique o sinal de clock do MCU no pino XTAL ou no barramento CLK. Clock ausente ou com jitter excessivo confirma falha no oscilador interno ou no núcleo do processador.

## Quando é falha eletrônica interna

A diferença entre firmware corrompido e defeito físico no chip tem um marcador claro.

Firmware corrompido: o chip responde ao programador (JTAG, SWD, UART bootloader). É possível acessar a memória, apagar e regravar. Após o processo, o equipamento retorna ao funcionamento normal sem nenhuma intervenção física.

MCU ou DSP com defeito físico: o chip não responde ao programador mesmo com tensões corretas e linhas de reset ativas. Ou responde, aceita o firmware, mas falha novamente após alguns ciclos de operação. Em alguns casos, parte das periféricas funciona enquanto outra está morta — o processador executa, mas não aciona determinado canal de saída digital.

O teste mais direto: medir corrente de consumo do chip durante o boot. Um MCU típico no padrão STM32 consome menos de 150 mA na inicialização. Um chip com curto interno puxa corrente desproporcional e aquece de forma localizada.

Esse diagnóstico não é feito quando o suporte do fabricante diz "tente atualizar o firmware mais uma vez".

## Vale a pena consertar?

Depende do encapsulamento do chip e do acesso ao firmware original.

MCUs em LQFP ou TQFP — pinos externos visíveis: a substituição é direta. O componente é identificável pelo datasheet, está disponível no mercado e a remoção exige estação de ar quente com ponta adequada. Processo factível em qualquer bancada minimamente equipada.

DSPs em BGA — pinos na parte inferior do chip, invisíveis: o retrabalho exige estação de reflow com perfil de temperatura controlado, stencil de solda e inspeção por raios-X após a substituição. Sem esse equipamento, o processo não tem confiabilidade. Não é uma limitação de habilidade — é uma limitação de infraestrutura.

O firmware é o outro fator. Alguns fabricantes gravam a memória com criptografia e proteção contra leitura. A substituição do chip nesses casos exige regravação com firmware original, que nem sempre está disponível fora do suporte oficial da marca. Growatt e Sungrow são os casos mais frequentes nessa categoria.

Quando o reparo é viável, o argumento financeiro é direto: uma placa de controle nova no fabricante custa entre 40% e 70% do valor de um inversor equivalente novo. O reparo eletrônico do chip ou do circuito de alimentação que o antecede custa uma fração disso. O que falta, na maioria dos casos que chegam até nós, é o diagnóstico preciso antes de qualquer compra ser feita.

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

- Âncora: 'fonte auxiliar interna' → URL: /fonte-auxiliar-smps-interna-inversor → Contexto: no H2 "O que causa esse problema", ao mencionar subtensão na fonte auxiliar como causa de falha do MCU
- Âncora: 'placa de controle vs. placa de potência' → URL: /placa-de-controle-vs-placa-de-potencia → Contexto: na introdução, como referência cruzada ao explicar a função da placa de controle no contexto do inversor
- Âncora: 'diagnóstico em nível de placa' → URL: /o-que-e-diagnostico-em-nivel-de-placa → Contexto: no H2 "Vale a pena consertar?", ao mencionar bancada equipada para o retrabalho de componentes
- Âncora: 'driver de gate' → URL: /o-que-e-o-driver-de-igbt → Contexto: na introdução, ao explicar que o MCU controla os drivers de gate dos IGBTs

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "algoritmos de MPPT" → URL: https://www.aneel.gov.br/resolucoes-normativas → Fonte: ANEEL — resoluções normativas sobre requisitos de rastreamento de ponto de máxima potência em sistemas fotovoltaicos
- Texto âncora: "NBR IEC 62109" → URL: https://www.abnt.org.br → Fonte: ABNT — norma técnica de segurança para conversores de potência utilizados em sistemas fotovoltaicos

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200
→ Por que foi escolhida: Mostra placa eletrônica com microprocessador em close — contexto direto do tema de MCU e DSP
→ Nome do arquivo: mcu-dsp-placa-controle-inversor-solar.webp
→ Alt Text (máx. 125 caracteres): Placa de controle de inversor solar com MCU e DSP — diagnóstico de falha no processador digital de controle
→ Legenda: Fig. 1 — MCU e DSP da placa de controle: os chips que comandam o inversor e os primeiros a serem subestimados no diagnóstico
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1200
→ Por que foi escolhida: Técnico com equipamento de medição eletrônica — representa o diagnóstico prático com osciloscópio e multímetro descrito no H2
→ Nome do arquivo: diagnostico-mcu-dsp-inversor-bancada.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo sinal de clock em MCU de inversor solar — diagnóstico de falha na placa de controle
→ Legenda: Fig. 2 — Verificação de sinal de clock no MCU: clock ausente ou com jitter excessivo confirma falha no oscilador ou no núcleo do processador
→ Onde inserir: Após H2 "Como identificar"
