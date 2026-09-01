# Post 124 — Deye e Growatt Híbrido: SOC Travado — Bateria Carregada mas o Sistema Não Usa

---

[PALAVRA-CHAVE FOCO]

SOC travado inversor híbrido bateria não descarrega

---

[TÍTULO SEO — Title Tag]

SOC Travado: Bateria Cheia e Inversor Não Usa Energia

---

[SLUG — URL do Post]

soc-travado-inversor-hibrido-bateria-nao-usa

---

[META DESCRIPTION]

SOC travado em Deye ou Growatt híbrido? Bateria mostra carga alta mas o sistema não usa. Veja causas reais e como diagnosticar na bancada.

---

[CATEGORIA]

Inversores Off-Grid e Híbridos

---

[TAGS]

SOC travado inversor híbrido, Deye bateria não descarrega, Growatt SPH diagnóstico, BMS comunicação CAN, inversor híbrido bateria solar

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

Quando o **SOC travado** aparece num inversor híbrido, o técnico entra num dos diagnósticos mais desorientadores do segmento: o display mostra bateria em 95%, o sol está gerando, mas o sistema continua comprando energia da rede como se a bateria não existisse. A conta de luz não cai. O cliente desconfia do equipamento, do instalador, de tudo.

Na nossa bancada, esse chamado chega com uma história quase sempre igual: o sistema funcionou bem por meses, o SOC travou num valor alto — normalmente entre 85% e 100% — e o inversor parou de despachar energia da bateria. Tentaram reiniciar, voltou por algumas horas. Depois travou de novo. Deye SUN-Xs e Growatt SPH são os dois modelos que chegam com maior frequência nessa condição, o que faz sentido: são os mais vendidos no mercado brasileiro e os mais comuns na bancada.

O comportamento é idêntico nas duas marcas porque a causa raiz é a mesma: ruptura em algum ponto da cadeia de leitura e controle do estado de carga.

## O que causa esse problema

SOC não é uma medição direta de quanto de energia está na bateria. É uma estimativa calculada em tempo real a partir de três fontes: corrente integrada no tempo (Coulomb counting), tensão do banco, e os dados transmitidos pelo BMS via protocolo de comunicação — geralmente CAN bus, RS485 ou RS232 dependendo do modelo e da bateria.

Quando o SOC trava, significa que uma dessas fontes falhou, foi perdida ou entrou em conflito com as demais.

As causas que chegam com mais frequência na bancada, em ordem decrescente:

1. **Falha de comunicação CAN ou RS485 entre a bateria e o inversor** — o inversor perde o contato com o BMS e congela o último valor de SOC recebido. A bateria pode estar perfeita; o canal de dados é que quebrou. Essa causa sozinha responde por mais da metade dos casos.
   O cabo pode ter continuidade no teste estático e falhar sob vibração ou temperatura — não confie no teste feito com o cabo parado e frio.

2. **Transceptor CAN degradado na placa de controle** — o CI responsável por traduzir o protocolo (TJA1050, SN65HVD230 ou equivalente) falha silenciosamente. O inversor não reporta erro de hardware porque o CI ainda recebe alimentação, mas os dados chegam corrompidos ou intermitentes. A reinicialização mascara o problema por algumas horas porque o barramento é reestabelecido do zero.

3. **Drift acumulado no Coulomb counting** — após muitos ciclos parciais sem atingir 0% ou 100%, o erro do contador de corrente se acumula. O inversor "acha" que a bateria está cheia quando não está. Esse padrão é mais comum em instalações no Nordeste e no Centro-Oeste, onde a irradiação alta gera mais ciclos por ano do que o fabricante projeta nos testes feitos na Europa — o equipamento envelhece antes do previsto nesse aspecto.

4. **Bloqueio de descarga pelo próprio BMS por desbalanceamento celular** — a bateria restringe saída de corrente por detectar divergência entre células ou temperatura fora do limite. O inversor vê SOC alto e descarga negada, interpreta como "bateria cheia em proteção" e não despacha — mas o motivo real é o BMS, não o inversor. O log do equipamento vai mostrar comunicação normal porque o BMS está respondendo; só que a permissão de descarga está bloqueada internamente.

5. **Corrupção dos parâmetros de calibração na EEPROM** — os valores de referência para o cálculo de SOC ficam gravados em memória não-volátil. Uma queda de tensão durante uma regravação, ou desgaste natural dos setores do CI, faz o sistema usar referências que não correspondem mais à bateria instalada.

6. **Bug de firmware documentado** — Deye e Growatt lançaram versões corretivas exatamente para SOC travado em modelos específicos. Vale verificar o changelog antes de qualquer intervenção na bancada.

## Como identificar

Passos para confirmar que o SOC está travado e não é configuração errada dos parâmetros de carga e descarga:

1. Observe o display por 30 minutos com geração solar ativa e consumo real ligado. SOC que não varia mais que 1-2% nesse período está travado.

2. Conecte ao BMS diretamente pelo aplicativo do fabricante da bateria — Pylontech, BYD, Dyness, Growatt Battery conforme o modelo instalado. Compare o SOC que o BMS reporta com o que o inversor exibe. Divergência acima de 5% confirma falha de comunicação entre os equipamentos.

3. Leia o log de eventos do inversor. Em Growatt SPH, procure por "BMS communication lost" ou "battery offline". Em Deye, por "BMS timeout" ou "CAN fault". Qualquer registro desse tipo é o diagnóstico fechando.

4. Meça a tensão real do banco com multímetro nos terminais da bateria. Compare com o que o inversor exibe na tela de status. Divergência maior que 1V indica que o inversor está operando com dados congelados ou corrompidos.

5. Troque o cabo de comunicação CAN ou RS485 por um cabo novo. Use cabo blindado com resistência de terminação de 120Ω em ambas as extremidades — a ausência da resistência de terminação responde por uma parcela significativa dos casos que chegam aqui como "defeito no inversor".

6. Execute um ciclo forçado se o modelo permitir: descarregue até SOC baixo pelo painel do inversor e deixe carregar completamente. Se o SOC se recalibrar e o problema sumir por alguns dias, o diagnóstico aponta para drift de Coulomb counting — o problema vai voltar, mas a causa está identificada.

7. Atualize o firmware para a versão mais recente disponível e verifique o changelog específico do modelo.

Se nenhuma dessas etapas resolver, o defeito está dentro do inversor.

## Quando é falha eletrônica interna

Trocou o cabo. Verificou o BMS. Atualizou o firmware. O SOC continua congelado.

O defeito está na placa de controle. Três pontos aparecem com mais frequência na bancada:

**Transceptor CAN com degradação parcial**: o CI recebe alimentação e parece funcionar, mas a resistência diferencial do barramento está fora de especificação. O sinal chega distorcido e o microcontrolador descarta as mensagens. Diagnóstico confirma com osciloscópio no barramento CAN — o sinal ideal tem amplitude entre 2,5 V e 3,5 V no diferencial CAN-H e CAN-L; desvio expressivo indica o IC comprometido. Troca do componente resolve na maioria dos casos.

O componente custa entre R$5 e R$20 dependendo do modelo. O trabalho de diagnóstico e substituição com teste em carga leva de uma a três horas de bancada.

**EEPROM com setores defeituosos**: ao tentar regravar os parâmetros de calibração, o inversor falha silenciosamente porque os setores estão degradados. O equipamento opera com valores corrompidos que não correspondem à bateria instalada. Diagnóstico requer leitura direta do CI com programador externo e comparação com o mapa de memória do modelo — não tem como confirmar por software.

**DSP ou MCU com rotina de Coulomb counting comprometida**: menos comum, geralmente consequência de surto elétrico. O processador continua rodando todas as outras funções normalmente — gera energia, comunica com o monitoramento — mas a variável de acumulação de carga foi corrompida num registrador interno. Diagnóstico só é conclusivo com análise da execução do firmware em nível de barramento.

Ainda não existe resposta definitiva sem abrir o equipamento e medir. Depende do que você vai encontrar nos barramentos com o osciloscópio.

## Vale a pena consertar?

Depende do componente afetado.

Troca do transceptor CAN: com diagnóstico completo e teste em carga, o custo total fica entre R$250 e R$500. Representa menos de 10% do valor de um inversor híbrido de 5kW novo.

Regravação de EEPROM com parâmetros recalibrados: requer mapeamento do modelo específico e equipamento de programação dedicado. Custo de bancada entre R$400 e R$700.

Troca da placa de controle quando o processador está comprometido: Deye e Growatt têm boa disponibilidade de peças no mercado nacional. Custo entre R$700 e R$1.500 dependendo do modelo — ainda assim, uma fração do custo de um híbrido novo equivalente.

A taxa de aprovação para reparo desse tipo de defeito na bancada fica acima de 80%.

O que não faz sentido é condenar o equipamento com base no sintoma. Um inversor com **bateria de lítio não carrega** ou não descarrega por SOC travado não é um inversor destruído — é um equipamento com uma cadeia de comunicação quebrada ou um CI com defeito. Isso é uma realidade técnica e financeira completamente diferente da que o cliente está imaginando quando fala em "trocar tudo".

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

- Âncora: 'falha de comunicação CAN ou RS485 entre a bateria e o inversor' → URL: /deye-hibrido-bms-fault-falha-comunicacao-bateria → Contexto: H2 "O que causa esse problema", item 1 da lista
- Âncora: 'Growatt SPH' → URL: /growatt-sph-hibrido-erro-batvolt-high-low-bms-estagio-carga → Contexto: segundo parágrafo da introdução, referência aos modelos mais comuns
- Âncora: 'bateria de lítio não carrega' → URL: /bateria-litio-nao-carrega-inversor-hibrido → Contexto: H2 "Vale a pena consertar?", último parágrafo
- Âncora: 'BMS timeout' → URL: /deye-hibrido-bms-fault-falha-comunicacao-bateria → Contexto: H2 "Como identificar", item 3 do checklist (Deye)

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "CAN bus" → URL: https://www.aneel.gov.br/normas-tecnicas → Fonte: ANEEL — referência às normas técnicas de sistemas de geração distribuída (contextualiza o protocolo de comunicação no contexto regulatório nacional)
- Texto âncora: "Coulomb counting" → URL: https://www.iec.ch/homepage → Fonte: IEC — padrões internacionais para sistemas de armazenamento de energia (IEC 62619 para baterias de lítio em aplicações estacionárias)

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1620325867502-221cfb5faa5f?w=1200
→ Por que foi escolhida: Painel de bateria com display de SOC — representa o estado de carga congelado em inversor híbrido solar
→ Nome do arquivo: soc-travado-inversor-hibrido-bateria-nao-usa.webp
→ Alt Text (máx. 125 caracteres): Display de inversor híbrido com SOC travado — bateria carregada mas o sistema não descarrega por falha de comunicação BMS
→ Legenda: Fig. 1 — SOC travado: o display mostra bateria cheia, mas o sistema não usa a energia armazenada — o diagnóstico começa na cadeia de comunicação entre inversor e BMS
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=1200
→ Por que foi escolhida: Técnico medindo placa eletrônica com osciloscópio — representa o diagnóstico do transceptor CAN na bancada
→ Nome do arquivo: soc-travado-diagnostico-placa-controle-can-2.webp
→ Alt Text (máx. 125 caracteres): Técnico com osciloscópio medindo sinal CAN na placa de controle de inversor híbrido — diagnóstico de SOC travado
→ Legenda: Fig. 2 — Diagnóstico do barramento CAN: o sinal diferencial entre CAN-H e CAN-L revela se o transceptor está degradado ou se a comunicação com o BMS foi perdida
→ Onde inserir: Após H2 "Como identificar"
