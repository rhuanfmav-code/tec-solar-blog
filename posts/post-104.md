# Post 104 — Inversor híbrido não entra em modo ilha (off-grid) na queda de energia — EPS/backup

---

[PALAVRA-CHAVE FOCO]
inversor híbrido modo ilha EPS não ativa

---

[TÍTULO SEO — Title Tag]
Inversor híbrido não entra em modo ilha: EPS e backup

---

[SLUG — URL do Post]
inversor-hibrido-nao-entra-modo-ilha-eps-backup

---

[META DESCRIPTION]
Inversor híbrido não entra em EPS na queda de rede? Relé, detecção ou configuração: veja as causas e quando o defeito é eletrônico interno.

---

[CATEGORIA]
Inversores Off-Grid e Híbridos

---

[TAGS]
inversor híbrido modo ilha, EPS backup solar, relé de grid inversor, falha modo off-grid híbrido, diagnóstico inversor híbrido

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **inversor híbrido modo ilha** parece simples de entender: a rede elétrica cai, o sistema detecta a queda, comuta em menos de 20 milissegundos e as cargas prioritárias continuam funcionando com a bateria. Na prática, uma série de coisas pode impedir essa transição de acontecer.

Na nossa bancada, essa reclamação chega com uma consistência que já é familiar: o técnico instalou o sistema com bateria, configurou o EPS (ou achou que tinha configurado), e na primeira queda real de energia, as cargas foram junto. Não comutou. Ou comutou tarde demais, reiniciando os equipamentos conectados. Já recebemos inversores vindos do interior do Nordeste e do Centro-Oeste — regiões onde a rede oscila com frequência — e o cliente contou que nunca tinha visto o modo ilha ativar uma única vez desde a instalação.

Isso não é problema do conceito. Em muitos casos é defeito eletrônico com conserto viável. Em outros, é configuração incorreta que ninguém verificou.

## O que causa esse problema

A comutação para modo EPS não é um evento único. É uma sequência que depende de vários componentes funcionando em sincronia, dentro de uma janela de tempo curtíssima.

O primeiro elo é o circuito de detecção de rede. Esse bloco monitora tensão e frequência da CA de entrada de forma contínua. Quando a tensão cai abaixo do limiar configurado — geralmente 80% do nominal — ou a frequência sai do intervalo permitido, o circuito dispara o processo de comutação. Se o optoacoplador ou o divisor resistivo desse bloco estiver com deriva, o inversor não identifica a queda de rede e permanece no modo normal sem reagir.

Identificada a perda de rede, o inversor precisa abrir o relé de grid. Essa desconexão é obrigatória pela ABNT NBR 16149 e pela REN 482 da ANEEL — sem ela, o inversor criaria uma ilha com a rede presente, risco direto para quem trabalha na rede da concessionária. Se esse relé não abre, a transição não acontece.

Depois, o relé de bypass EPS precisa fechar, conectando as cargas ao barramento interno alimentado pela bateria. Um relé com bobina deteriorada ou contato oxidado não fecha quando precisa.

Mas nem toda falha no modo ilha é eletrônica. O que chega até nós com mais frequência são estas situações:

- SOC da bateria abaixo do limiar mínimo de EPS — a maioria dos fabricantes bloqueia o modo ilha com bateria abaixo de 20%
- Falha de comunicação com o BMS: sem confirmação do estado da bateria, o inversor bloqueia a descarga como medida de proteção
- Carga no circuito EPS acima da potência nominal do backup — e esse valor é menor que a potência total do inversor em vários modelos
- Modo EPS desabilitado por padrão: Deye, Growatt e Sungrow têm equipamentos que saem de fábrica com essa função inativa
- Temperatura da bateria fora do intervalo operacional — abaixo de 5°C o BMS bloqueia descarga independente do SOC, e isso é comum no Sul do Brasil durante o inverno
- Circuito EPS conectado na saída errada: em modelos com saída EPS dedicada e saída AC principal separadas, a confusão na fiação é mais comum do que parece

Tudo isso antes de considerar qualquer defeito nos componentes internos.

## Como identificar

A investigação começa no app de monitoramento e no painel de configuração, não no multímetro.

1. Verifique se o EPS está habilitado nas configurações do inversor — não assuma que está ativo
2. Confira o SOC atual e o limiar mínimo de EPS configurado: se o SOC está em 17% e o limiar em 20%, o sistema não ativa por projeto
3. Confirme que as cargas de backup estão conectadas na saída correta — em modelos com saída EPS separada, isso define tudo
4. Simule uma queda de rede: abra o disjuntor de entrada CA e observe se o inversor comuta para modo ilha. Se comuta no teste manual mas não comuta nas quedas reais, o problema está no circuito de detecção de tensão — ele não está lendo corretamente o que acontece na rede.
   *(Esse teste separa falha de configuração de falha eletrônica em menos de dois minutos.)*
5. Consulte o log de eventos: entradas como "EPS fault", "relay fault" ou "grid relay fail" apontam diretamente para componente interno
6. Meça a tensão na saída EPS com multímetro durante queda simulada — ausência de tensão com bateria carregada e EPS habilitado confirma falha de relé ou problema no estágio de saída
7. Verifique se há mensagem de sobrecarga no log: se a carga conectada ao circuito EPS excede a capacidade nominal, o inversor pode desabilitar o modo automaticamente como proteção

Um único ponto pode fechar o diagnóstico. Às vezes são dois.

## Quando é falha eletrônica interna

Quando configuração, cabeamento e bateria estão corretos e o EPS ainda não ativa, o defeito está dentro do equipamento.

O relé de grid é o candidato mais frequente. Em redes com oscilações constantes — situação típica em municípios do interior do Nordeste servidos por linhas de distribuição longas — o número de ciclos de comutação acumula rápido. O contato pode se desgastar, oxidar ou, em casos de arco elétrico durante abertura sob carga, soldar (welded contact). A bobina também deteriora ao longo do tempo. Medir resistência da bobina e verificar abertura do contato fecha esse diagnóstico.

O circuito de detecção de tensão CA é o segundo ponto. Optoacopladores com ganho reduzido podem funcionar em condições normais e falhar nas quedas rápidas — exatamente quando o EPS precisaria atuar. Esse modo de falha é traiçoeiro porque o sistema parece operar normalmente até o momento em que mais importa.

Há casos menos comuns onde o driver do estágio de saída está comprometido: os relés comutam corretamente, o log registra "EPS active", mas o IGBT não gera a forma de onda CA e a carga não recebe tensão. Esses casos exigem bancada com gerador de carga e osciloscópio para fechar.

Nenhum desses diagnósticos é possível sem abrir o equipamento e medir.

## Vale a pena consertar?

Na maioria dos casos, sim.

Substituição de relé de grid ou de bypass EPS: entre R$ 400 e R$ 900 com componente e mão de obra, dependendo do modelo do inversor e da especificação do relé. É o cenário mais frequente e o mais direto.

Quando o problema está no circuito de detecção de tensão ou no driver de gate, o custo de bancada sobe. Mesmo assim, fica bem abaixo do custo de substituição: um inversor híbrido de 5 kW parte de R$ 8.000, e os modelos de 8 a 10 kW passam de R$ 15.000 com facilidade.

Um ponto técnico que vale mencionar: se o relé falhou por acúmulo de ciclos em rede instável, só trocar o relé resolve o problema imediato mas não o padrão de falha. Avaliar a instalação de supressor de surto e contator externo de proteção reduz o estresse sobre o relé interno e estende a vida útil do reparo.

O que definitivamente não tem saída é deixar o modo EPS inativo por falta de diagnóstico. Um sistema híbrido sem comutação funcionando é um solar on-grid com uma bateria cara que não faz nada quando a energia falta. O investimento não se justifica.

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

---

[LINKS INTERNOS SUGERIDOS]

- Âncora: 'relés de bypass em inversores solares' → URL: /reles-bypass-inversores-solares-falha-silenciosa → Contexto: seção "O que causa esse problema", ao descrever o relé de bypass EPS e seu mecanismo de falha
- Âncora: 'Falha de comunicação com o BMS' → URL: /sungrow-sh-hibrido-falha-comunicacao-bms → Contexto: seção "O que causa esse problema", no item sobre BMS bloqueando a descarga
- Âncora: 'Deye F45' → URL: /deye-f45-falha-bateria-inversor-hibrido-bms → Contexto: seção "Quando é falha eletrônica interna", ao tratar de falhas relacionadas à comunicação com bateria em inversores Deye
- Âncora: 'diagnóstico em nível de placa' → URL: /o-que-e-diagnostico-nivel-placa-reparo-inversor → Contexto: seção "Quando é falha eletrônica interna", ao mencionar que o diagnóstico exige abertura e medição do equipamento
- Âncora: 'trocar ou consertar inversor solar' → URL: /trocar-ou-consertar-inversor-solar-analise → Contexto: seção "Vale a pena consertar?", ao comparar custo de reparo com substituição do inversor híbrido

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "ABNT NBR 16149" → URL: https://www.abnt.org.br → Fonte: ABNT — norma que define requisitos de conexão de microgeração distribuída à rede, incluindo exigência de antiilhamento e desconexão automática da rede CA
- Texto âncora: "REN 482 da ANEEL" → URL: https://www.aneel.gov.br → Fonte: ANEEL — resolução que regulamenta a microgeração e minigeração distribuída, estabelecendo requisitos de proteção e desconexão do sistema fotovoltaico

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1593941707882-a5bba14938c7?w=1200
→ Por que foi escolhida: painel de controle de inversor híbrido com bateria ao fundo — representa diretamente o contexto do post sobre comutação para modo ilha
→ Nome do arquivo: inversor-hibrido-modo-ilha-eps-backup.webp
→ Alt Text (máx. 125 caracteres): Inversor híbrido com sistema de bateria — diagnóstico de falha no modo ilha EPS e comutação de backup
→ Legenda: Fig. 1 — O modo ilha (EPS) depende de uma sequência precisa de relés e circuitos de detecção funcionando em sincronia
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200
→ Por que foi escolhida: técnico com multímetro medindo equipamento eletrônico em bancada — representa o processo de diagnóstico de relé e circuito de detecção descrito na seção de identificação
→ Nome do arquivo: diagnostico-rele-eps-inversor-hibrido-bancada.webp
→ Alt Text (máx. 125 caracteres): Técnico medindo relé de grid em inversor híbrido na bancada — diagnóstico de falha no modo EPS e backup
→ Legenda: Fig. 2 — A medição direta do relé de grid e do circuito de detecção de rede é o único caminho para fechar o diagnóstico de falha no modo EPS
→ Onde inserir: Após H2 "Como identificar"
