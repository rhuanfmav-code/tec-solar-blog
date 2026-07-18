# Post 11 — Inversor solar parou de funcionar: o checklist completo antes de chamar o técnico

---

## [PALAVRA-CHAVE FOCO]

inversor solar parou de funcionar

---

## [TÍTULO SEO — Title Tag]

Inversor solar parou: checklist antes de chamar o técnico

---

## [SLUG — URL do Post]

inversor-solar-parou-de-funcionar-checklist

---

## [META DESCRIPTION]

Inversor solar parado com sol batendo? Checklist técnico passo a passo — o que verificar antes de chamar o técnico ou enviar para bancada.

---

## [CATEGORIA]

Manutenção e Diagnóstico

---

## [TAGS]

inversor solar parado, diagnóstico inversor solar, checklist inversor fotovoltaico, inversor não liga, falha inversor solar

---

## [TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

**Inversor solar parou de funcionar** — e o sol está batendo. Os painéis estão no telhado, o sistema parece intacto, mas a geração está zerada. Display apagado, app sem atualização, cliente no telefone.

Na nossa bancada, o que a gente vê é diferente do que a maioria dos técnicos faz nessa hora. Boa parte dos inversores que chegam com o rótulo de "queimado" volta a funcionar após identificarmos uma causa externa que ninguém mediu antes de desmontar. Fusível fundido, disjuntor CC disparado, cabo de string solto. O problema não estava no inversor — estava fora dele, e ninguém verificou.

Este checklist foi construído a partir desses casos. Execute cada passo em ordem antes de qualquer conclusão.

---

## O que causa esse problema

Um inversor solar on-grid para porque foi projetado para parar. As proteções internas monitoram tensão CC, tensão CA, frequência de rede, temperatura, isolamento e corrente de fuga. Quando qualquer um desses parâmetros sai da faixa, o desligamento é automático.

A maior parte dos desligamentos tem origem externa ao equipamento:

- Disjuntor CC ou CA aberto ou disparado por sobrecorrente
- Tensão de rede CA fora da faixa operacional — abaixo de 191 V ou acima de 231 V conforme os limites da ANEEL para 220 V nominal
- Frequência fora do intervalo de operação (tipicamente 59,3 a 60,5 Hz no Brasil)
- Tensão CC no string abaixo do mínimo de partida por sombreamento parcial, painel com falha ou conector MC4 solto
- Falha de isolamento no cabeamento CC — a resistência de isolamento cai abaixo do limiar configurado e o GFCI interno bloqueia o equipamento conforme IEC 62109-2
- Fusível de string fundido na string box — causa zerar a produção inteira por um componente de R$ 8,00
- Sobretemperatura por ambiente fechado sem ventilação

As causas internas existem, mas são minoria:

- IGBT destruído no estágio de potência
- Driver de gate degradado ou com tensão de gate fora da faixa
- Placa de controle com defeito de DSP ou microcontrolador
- Capacitores de barramento com capacitância abaixo do mínimo operacional
- Relé de saída com contato soldado ou aberto

Saber de qual grupo vem o problema define se o inversor vai para bancada ou não.

---

## Como identificar

Execute esta sequência. Cada passo elimina uma hipótese antes de avançar para a próxima.

**1. Registre o código de erro no display.** Se houver qualquer indicação — piscada de LED, código alfanumérico, mensagem parcial — anote antes de qualquer ação. Esse código direciona o diagnóstico e reduz tempo de bancada.

**2. Meça a tensão CC na entrada do inversor.** Com multímetro nos terminais de entrada CC. A maioria dos on-grid residenciais exige pelo menos 100 a 150 V para inicializar. Tensão abaixo disso com sol pleno: o problema está no string ou nos disjuntores, não no inversor.

**3. Verifique os disjuntores CC e CA.** O disjuntor CC antes do inversor e o CA no quadro principal precisam estar fechados. Um disjuntor CC pode disparar por sobrecorrente, tensão reversa ou curto em um painel com defeito. Esse passo é esquecido com frequência.

**4. Meça a tensão CA na saída.** A rede elétrica pode estar fora dos parâmetros sem nenhuma indicação visual no local. Medir com multímetro CA diretamente no ponto de conexão descarta a concessionária como causa. Instalações em regiões com instabilidade crônica de tensão — como zonas rurais do Norte e do Nordeste — passam por isso com regularidade.

**5. Inspecione os fusíveis da string box.** Cada string tem um fusível individual. Fusível aberto em uma string pode zerar a produção ou criar desequilíbrio sem apagar o inversor completamente se houver outras strings operacionais. Medir continuidade com multímetro antes de qualquer conclusão visual — fusíveis com visual OK podem estar abertos eletricamente.

**6. Verifique a temperatura do local de instalação.** Se o inversor está em ambiente fechado sem circulação de ar, temperatura interna acima de 80 a 85°C provoca shutdown térmico automático. Encostar a mão na carcaça já dá informação. Esse detalhe resolve casos inteiros sem nenhum reparo eletrônico.

**7. Tente o reset via display ou botão.** Alguns inversores travam em estado de erro após acionamento de proteção e precisam de reset manual. O manual do fabricante indica a sequência exata. Growatt, Deye e Sungrow têm esse recurso documentado. Não é gambiarra — é procedimento previsto pelo fabricante.

**8. Inspecione visualmente o interior.** Com o equipamento completamente desligado e tensão CC desconectada por pelo menos cinco minutos: abra a tampa de acesso disponível e observe. Cheiro de queimado, capacitor com tampa abaulada, trilha escurecida ou componente com marca de arco são sinais diretos. Sem sinais visíveis, isso não descarta falha interna.

---

## Quando é falha eletrônica interna

Se o checklist externo não identificou nada, o problema está dentro do inversor.

Os sinais que apontam para isso sem ambiguidade: display apagado com tensão CC e CA presentes e dentro dos limites; código de erro de hardware (IGBT, placa de controle, relé de saída); inversor que inicializa e desliga em segundos independente das condições externas.

Nesse ponto o diagnóstico passa para a bancada. O que vale levantar antes de enviar: qual código de erro estava registrado no display ou no log; se houve evento climático próximo ao momento da falha (raio, surto de tensão na rede); se o inversor apresentou comportamento anômalo nos dias anteriores — reinicializações frequentes, geração caindo progressivamente, ruído incomum.

Essas informações mudam o ponto de partida da diagnose e reduzem o tempo de reparo.

---

## Vale a pena consertar?

Depende do que está destruído. Não existe resposta genérica aqui.

Problemas externos resolvidos pelo instalador: custo zero, inversor volta a operar. Fusível de string, disjuntor CC, conector MC4 com mau contato — ficam nessa categoria.

Falha eletrônica de média complexidade — driver de gate degradado, ventilador parado, relé de saída com contato aberto — em geral viável com custo entre 15% e 30% do valor do equipamento novo.

IGBT destruído com placa de controle intacta: reparável na maioria dos casos. Um módulo IGBT para inversor residencial de 5 a 10 kW sai entre R$ 300 e R$ 700. O inversor novo equivalente sai entre R$ 3.500 e R$ 6.000. A diferença justifica o diagnóstico antes de qualquer outra decisão.

Dano em cascata — IGBT, driver e placa de controle destruídos juntos — precisa de avaliação individual. Depende do que está destruído e da disponibilidade de componentes para o modelo específico. Sem abrir e medir, não tem como saber.

Um inversor de 10 kW parado custa geração todo dia. Um laudo leva um ou dois dias úteis.

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

## [LINKS INTERNOS SUGERIDOS]

- Âncora: 'IGBT destruído no estágio de potência' → URL: /igbt-queimado-inversor-solar-6-causas → Contexto: seção "O que causa esse problema", lista de causas internas — o Post 10 detalha as 6 causas de queima de IGBT em bancada
- Âncora: 'falha de isolamento no cabeamento CC' → URL: /growatt-erro-102-falha-isolamento-string-leakage → Contexto: seção "O que causa esse problema", causas externas — o Post 01 cobre falha de isolamento com análise de string leakage no Growatt
- Âncora: 'Tensão de rede CA fora da faixa operacional' → URL: /sungrow-grid-lost-perda-de-rede-diagnostico → Contexto: seção "O que causa esse problema", causas externas — o Post 05 aborda perda de rede CA com análise de causa externa vs. interna
- Âncora: 'tensão CC no string abaixo do mínimo de partida' → URL: /weg-e001-sobretensao-cc-diagnostico → Contexto: seção "O que causa esse problema" — o Post 06 analisa os limites de tensão CC e o circuito de medição no WEG

---

## [LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "limites da ANEEL para 220 V nominal" → URL: https://www.aneel.gov.br/qualidade-da-energia-eletrica → Fonte: ANEEL — Resolução Normativa 1000/2021, que define os limites de tensão e frequência para conexão à rede de distribuição
- Texto âncora: "GFCI interno bloqueia o equipamento conforme IEC 62109-2" → URL: https://www.iec.ch/standards/iec-standards → Fonte: IEC — IEC 62109-2: Safety of power converters for use in photovoltaic power systems, norma que define os requisitos de proteção de corrente de fuga em inversores fotovoltaicos

---

## [IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ URL para download: https://images.unsplash.com/photo-1509391366360-2e959784a276?w=1200
→ Por que foi escolhida: Técnico com equipamentos de medição próximo a painéis solares — representa o contexto de diagnóstico externo antes de acionar reparo de inversor
→ Nome do arquivo: inversor-solar-parou-de-funcionar-checklist.webp
→ Alt Text (máx. 125 caracteres): Técnico verificando inversor solar parado com multímetro — checklist de diagnóstico passo a passo antes de chamar o técnico especializado
→ Legenda: Fig. 1 — Diagnóstico externo sistemático: o checklist elimina as causas mais comuns antes de concluir por defeito eletrônico interno
→ Onde inserir: Topo do post, antes da introdução

---

## [IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ URL para download: https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=1200
→ Por que foi escolhida: Multímetro e ferramentas sobre bancada de diagnóstico eletrônico — representa a etapa de medição de tensão CC e isolamento descrita no checklist
→ Nome do arquivo: checklist-inversor-solar-medicao-tensao-2.webp
→ Alt Text (máx. 125 caracteres): Medição de tensão CC e isolamento em inversor solar parado — diagnóstico passo a passo com multímetro antes de envio para bancada
→ Legenda: Fig. 2 — Medição de tensão CC, isolamento e estado dos disjuntores: etapas 2 a 5 do checklist eliminam a maioria das causas externas
→ Onde inserir: Após H2 "Como identificar"
