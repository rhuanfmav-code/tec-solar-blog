# Post 22 — Inversor on-grid vs. off-grid: os defeitos são diferentes — saiba por quê

---

[PALAVRA-CHAVE FOCO]
defeitos inversor on-grid vs off-grid

---

[TÍTULO SEO — Title Tag]
Inversor On-Grid vs. Off-Grid: Por Que os Defeitos Diferem

---

[SLUG — URL do Post]
inversor-on-grid-vs-off-grid-defeitos-diferentes

---

[META DESCRIPTION]
Inversor on-grid e off-grid falham por razões distintas. Entenda a diferença de arquitetura e como diagnosticar cada tipo corretamente.

---

[CATEGORIA]
Manutenção e Diagnóstico

---

[TAGS]
inversor on-grid, inversor off-grid, diagnóstico inversor solar, reparo inversor solar, on-grid vs off-grid

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Inversor on-grid e off-grid** têm funções diferentes, arquiteturas eletrônicas diferentes — e quando quebram, falham por razões completamente distintas. Usar o mesmo checklist de diagnóstico para os dois é o caminho mais rápido para um laudo errado e uma substituição desnecessária.

Na nossa bancada, essa confusão chega de forma parecida: o integrador aparece com um off-grid dizendo que "parou igual ao on-grid que vocês consertaram semana passada". O sintoma no display pode até ser semelhante. Mas o circuito responsável não tem nada a ver com o outro.

## Por que os defeitos são diferentes entre on-grid e off-grid

O inversor on-grid tem uma função central: sincronizar a saída CA com a rede da concessionária. Para isso, ele usa um circuito PLL (Phase-Locked Loop) que monitora em tempo real a frequência e a fase da rede. Esse circuito fica sob estresse contínuo — qualquer oscilação na rede chega direto nele.

Além disso, todo inversor on-grid tem proteção antiilhamento, obrigatória pela ABNT NBR 16149, que monitora tensão, frequência e variação de potência para desligar o equipamento quando a rede some. O relé responsável por esse desligamento é acionado dezenas de vezes por mês em redes instáveis. Em áreas rurais do Nordeste e do interior de Minas Gerais, não é incomum ver esse relé com registros de centenas de operações em poucos meses.

O inversor off-grid ou híbrido não depende da rede para funcionar. Ele gera sua própria referência de frequência e tensão internamente, e ainda precisa gerenciar o ciclo completo de carga e descarga da bateria. Isso exige componentes que o on-grid simplesmente não tem: conversor DC-DC bidirecional, relé de transferência (bypass), interface com o BMS da bateria e lógica de prioridade de carga.

Cada um desses pontos adiciona um modo de falha que não existe no on-grid.

## Como identificar o tipo de falha em cada arquitetura

Para o inversor on-grid, os padrões mais recorrentes na bancada são:

1. Erro de sincronização com a rede — o display exibe "grid fault" ou frequência fora do padrão sem que a rede esteja realmente fora de especificação
2. IGBT do estágio de inversão com curto — geralmente após pico da concessionária ou retorno brusco de energia depois de uma queda
3. Driver de gate com falha parcial — o IGBT recebe tensão de gate incorreta e opera no limite por semanas até queimar sem nenhum novo evento externo
4. Relé de antiilhamento travado ou com resistência de contato elevada — o inversor sincroniza mas não entrega potência
5. Capacitor do barramento DC fora de especificação — tensão instável antes do estágio de inversão, identificável com osciloscópio nas condições de carga real
6. Sensor de corrente ou tensão com leitura falsa — o inversor exibe código de erro mas o estágio de potência está íntegro; trocar o conjunto seria desperdiçar o equipamento

Para o inversor off-grid e híbrido, o diagnóstico começa em pontos completamente diferentes:

1. Relé de transferência (bypass) com resistência de contato elevada ou travado em uma posição — o sistema não comuta corretamente entre modo bateria e modo rede
2. MOSFET ou IGBT do conversor DC-DC bidirecional queimado — a bateria não carrega mesmo com tensão CA presente e disjuntores fechados
3. Perda de comunicação com o BMS — o inversor desliga sem evento aparente; o log interno mostra falha no protocolo CAN ou RS485
4. Falha no oscilador interno de referência — a saída CA apresenta frequência ou tensão instável, o que num on-grid seria impossível porque ele usa a rede como referência
5. Placa de controle com defeito no setor de gerenciamento de energia — mais difícil de isolar sem o diagrama do modelo específico; cada fabricante tem lógica proprietária
6. Relé de carga da bateria queimado — tensão de bateria presente no barramento, corrente de carga zerada

Não existe checklist único que funcione para os dois tipos. Quem aplica o mesmo protocolo em ambos vai errar em pelo menos um deles.

## Quando a falha é eletrônica interna

No on-grid, a maioria dos casos que chegam até nós tem falha eletrônica interna depois de um evento externo: pico de tensão, queda e retorno brusco da rede, curtocircuito momentâneo na string. O cabeamento e os painéis podem estar intactos. O problema está dentro.

Os componentes mais afetados são os IGBTs do estágio de inversão e o driver de gate entre a placa de controle e o IGBT. Esse driver é frequentemente ignorado no diagnóstico de mercado. Quando falha parcialmente — sem evidência visual de queima — o IGBT passa a operar fora das condições nominais de tensão de gate e vai ao curto em semanas, sem nenhum novo evento externo perceptível.

Já no off-grid e híbrido, a falha eletrônica interna costuma aparecer depois de ciclos intensos de carga e descarga. O Norte e o Nordeste do Brasil têm esse perfil: sistema trabalhando no limite durante horas de sol e com demanda concentrada à noite. Os MOSFETs do conversor DC-DC bidirecional são os mais estressados nesse regime.

Quando o defeito não é óbvio? Medir. Com o equipamento aberto, alimentado em bancada e sob carga controlada.

Ainda não existe atalho que substitua isso.

## Vale a pena consertar os dois tipos?

Em inversores on-grid de 3 a 15 kW, o reparo em nível de componente costuma representar entre 15% e 35% do valor de um equipamento novo equivalente. Se o IGBT ou o driver queimou de forma isolada, sem dano extenso na placa de controle, o reparo é direto e o resultado é durável.

No off-grid e híbrido, a conta muda porque o equipamento novo custa consideravelmente mais. Um inversor híbrido de 5 kW sai entre R$ 8.000 e R$ 20.000 dependendo da marca e da capacidade integrada. Reparar o conversor DC-DC ou o relé de transferência por uma fração desse valor é, na maioria dos casos, a decisão economicamente evidente.

O que inviabiliza o reparo em qualquer um dos dois tipos é dano extenso na placa de controle: microcontrolador queimado por sobretensão sem repositório de firmware disponível, rastreadores do DSP com dano irreversível, memória de configuração corrompida sem procedimento documentado de reprogramação. Esses casos existem. São a minoria do que chega na bancada.

A maioria chega consertável.

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

- Âncora: 'IGBTs do estágio de inversão' → URL: /por-que-igbts-queimam-inversores-solares → Contexto: H2 "Como identificar o tipo de falha em cada arquitetura", item 2 da lista on-grid
- Âncora: 'driver de gate entre a placa de controle e o IGBT' → URL: /o-que-e-driver-igbt-falha-estagio-potencia → Contexto: H2 "Quando a falha é eletrônica interna", segundo parágrafo
- Âncora: 'Inversor solar parou de funcionar' → URL: /inversor-solar-parou-de-funcionar-checklist → Contexto: introdução, ao mencionar diagnóstico inicial

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16149" → URL: https://www.abnt.org.br/normalizacao/lista-de-publicacoes/abnt → Fonte: ABNT — norma técnica de conexão de microgeração ao sistema de distribuição
- Texto âncora: "ciclo completo de carga e descarga da bateria" → URL: https://www.aneel.gov.br/resolucoes-normativas → Fonte: ANEEL — resoluções sobre armazenamento de energia e sistemas híbridos

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Painel solar com inversor visível, representa sistema fotovoltaico completo
→ Nome do arquivo: inversor-on-grid-vs-off-grid-diagnostico.webp
→ Alt Text (máx. 125 caracteres): Inversor solar instalado — diferença entre on-grid e off-grid no diagnóstico eletrônico de falhas
→ Legenda: Fig. 1 — Inversores on-grid e off-grid têm arquiteturas distintas e modos de falha diferentes
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: Técnico com multímetro realizando diagnóstico em equipamento eletrônico
→ Nome do arquivo: diagnostico-inversor-solar-bancada-2.webp
→ Alt Text (máx. 125 caracteres): Técnico realizando diagnóstico de inversor solar em bancada com multímetro e osciloscópio
→ Legenda: Fig. 2 — Diagnóstico em nível de componente exige abordagens diferentes para on-grid e off-grid
→ Onde inserir: Após H2 "Como identificar o tipo de falha em cada arquitetura"
