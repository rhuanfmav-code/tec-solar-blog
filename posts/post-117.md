# Post 117 — SAJ: erros comuns, perfil de falha e viabilidade de reparo

---

[PALAVRA-CHAVE FOCO]
inversor SAJ falha diagnóstico

---

[TÍTULO SEO — Title Tag]
SAJ: Erros Comuns, Diagnóstico e Viabilidade de Reparo

---

[SLUG — URL do Post]
saj-inversor-erros-comuns-reparo

---

[META DESCRIPTION]
Conheça os erros mais frequentes nos inversores SAJ, como diagnosticar cada falha na bancada e quando o reparo é tecnicamente viável.

---

[CATEGORIA]
Manutenção e Diagnóstico

---

[TAGS]
inversor SAJ, SAJ R5 falha, diagnóstico inversor solar, SAJ reparo, perfil de falha SAJ

---

[TEXTO DO POST — VERSÃO HUMANIZADA FINAL]

O **inversor SAJ** chegou no Brasil com força. Preço competitivo, linha diversificada, presença crescente no mercado residencial e comercial. E, junto com isso, chegou o volume de equipamentos com defeito.

Na nossa bancada, a SAJ já ocupa uma fatia relevante dos equipamentos que recebemos. O padrão é curioso: a primeira fase é de erros de comunicação e falhas intermitentes que o técnico de campo consegue resetar. A segunda fase — que vem alguns meses depois — é a parada total. E aí o técnico já não consegue mais resolver no campo.

## O que causa as falhas nos inversores SAJ

A linha R5, a mais comum no mercado brasileiro, usa arquitetura transformerless com estágio boost duplo. O estágio de potência é construído ao redor de módulos IGBT com drivers de gate em módulo dedicado — topologia padrão nos inversores chineses de médio porte.

O ponto mais fraco da plataforma é o circuito de bootstrap do driver. Ele alimenta a parte alta do gate a partir do barramento CC via capacitor de bootstrap. Quando esse capacitor degrada — coisa que acontece entre dois e quatro anos em ambientes com temperatura elevada — o IGBT superior começa a receber sinal de gate incompleto. O disparo irregular gera sobretensão de comutação, e o IGBT queima em modo de curto.

Inversores instalados em telhas metálicas no Nordeste e Centro-Oeste chegam antes dos outros. A temperatura interna passa de 70 °C com facilidade nessas condições, e o fabricante não dimensionou os componentes para esse regime térmico contínuo.

A outra causa frequente é falha na fonte auxiliar interna (SMPS). Essa fonte alimenta a placa de controle, o DSP e o ventilador. Quando ela começa a oscilar — entregando tensão fora do range mas sem desligar completamente — o DSP opera com alimentação instável e registra erros sem causa aparente. O inversor entra e sai de fault. O técnico vai ao campo, reseta e volta sem diagnóstico.

Isso se repete por semanas até a segunda fase.

## Como identificar os erros mais comuns

Os erros que chegam com mais frequência nos SAJ que a gente atende:

1. **Err 003 / Err 004** — Falha de isolamento CC. Pode ser painel com dano no backsheet, cabo CC com isolamento rompido ou capacitor Y de filtro com fuga — esse último é o mais comum e o que menos se suspeita primeiro.
2. **Err 006** — Tensão CC muito alta. Geralmente string mal dimensionada, mas pode ser sensor de tensão com leitura errática.
3. **Err 013** — Frequência de rede fora do limite. Na maioria dos casos, é instabilidade da concessionária. Quando persiste com rede estável, o transformador de corrente (CT) de saída merece atenção.
4. **Err 022** — Falha de IGBT. O de maior custo. Implica abertura completa e substituição do módulo ou reparo do estágio discreto.
5. **Err 030** — Temperatura interna alta. Ventilador parado, pasta térmica seca ou sensor de temperatura com leitura incorreta.
6. **Falha de comunicação Wi-Fi (eSolar Air)** — O módulo integrado tem taxa de falha elevada após exposição ao calor. O módulo descola internamente da placa e a comunicação cai. O inversor continua funcionando, mas o monitoramento some.
7. **Standby sem saída** — Inversor que inicializa mas não entra em operação. Sintoma clássico de SMPS com problema: a placa de controle sobe, mas o DSP não recebe tensão suficiente para completar o boot.

A verificação na bancada segue esta sequência:

1. Medir tensão CC nos terminais de entrada e conferir contra a string real
2. Medir resistência de isolamento string-terra com megôhmmetro (mínimo 1 MΩ a 500 V)
3. Checar tensão de saída da fonte auxiliar: 15 V para o gate, 3,3 V e 5 V para o DSP
4. Verificar forma de onda do gate com osciloscópio — disparo assimétrico aponta driver com problema
5. Medir temperatura do dissipador com termopar durante operação — limite da linha R5 está em 85 °C
6. Verificar ventilador: tensão de alimentação, rotação e corrente de partida

## Quando é falha eletrônica interna

O técnico de campo costuma ler erro de comunicação como problema de rede ou configuração. Às vezes é isso mesmo. Mas quando o SAJ entra em fault e não sai com reset, o problema já está dentro.

A falha eletrônica interna nos SAJ tem progressão. Primeiro a SMPS começa a oscilar levemente — imperceptível pelo display, mas visível no osciloscópio no barramento de 15 V. Depois o DSP começa a registrar erros intermitentes porque os dados dos sensores chegam corrompidos. Então o inversor começa a falhar na inicialização mas ainda volta com reset. Por fim, para completamente.

Quando o equipamento está na segunda fase, o técnico acha que resolveu ao resetar. Não resolveu. A SMPS estabilizou transitoriamente. O defeito está instalado e vai evoluir.

Outro sinal claro de falha interna: inversor que desliga nas primeiras horas da manhã, quando a irradiância ainda está subindo e a tensão CC está abaixo do pico. Esse comportamento aponta para IGBT com disparo instável ou sensor de corrente com leitura incorreta no range baixo. Ainda não existe resposta definitiva para qual dos dois falhou primeiro. Depende do que você vai encontrar na placa.

## Vale a pena consertar?

A linha R5 da SAJ, nas potências de 3 a 10 kW, é reparável na maioria dos casos que chegam até nós. O custo médio de reparo — troca de driver e IGBT, pasta térmica renovada, fonte auxiliar recondicionada — fica entre 30% e 45% do preço de um equipamento novo equivalente.

O que não tem reparo econômico é o SAJ que sofreu sobretensão severa no barramento CC por surto de raio sem proteção adequada. Nesses casos, o dano se espalha por múltiplas partes da placa e o custo de componentes ultrapassa o viável.

A linha HS (híbrido) tem complexidade maior. Quando a falha está no estágio de inversão, o reparo é comparável ao on-grid. Quando está na comunicação com a bateria — CAN ou RS485 — o diagnóstico precisa de interface serial com a bateria para rastrear o ponto real de falha.

A maioria dos SAJ que chegam com laudo de "placa queimada" tem um componente discreto danificado: um transistor do driver, um capacitor de bootstrap, um regulador de tensão da fonte auxiliar. O equipamento inteiro não queimou. O diagnóstico é que estava faltando.

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

- Âncora: 'IGBT queima em modo de curto' → URL: /por-que-os-igbts-queimam-em-inversores-solares → Contexto: Seção "O que causa as falhas nos inversores SAJ", parágrafo sobre bootstrap
- Âncora: 'drivers de gate em módulo dedicado' → URL: /driver-de-gate-do-igbt-funcao-modos-de-falha-diagnostico → Contexto: Seção "O que causa as falhas", primeiro parágrafo
- Âncora: 'fonte auxiliar interna (SMPS)' → URL: /fonte-auxiliar-smps-interna-inversor → Contexto: Seção "O que causa as falhas", quarto parágrafo
- Âncora: 'temperatura do dissipador com termopar durante operação' → URL: /superaquecimento-inversor-solar-causas-consequencias → Contexto: Seção "Como identificar", item 5 da lista de verificação
- Âncora: 'diagnóstico em nível de componente' → URL: /o-que-e-diagnostico-em-nivel-de-placa → Contexto: Seção "Vale a pena consertar?", parágrafo final

---

[LINKS EXTERNOS SUGERIDOS]

- Texto âncora: "resistência de isolamento string-terra com megôhmmetro" → URL: https://www.aneel.gov.br/resolucoes-normativas → Fonte: ANEEL — resolução normativa sobre requisitos de conexão de microgeração e minigeração distribuída
- Texto âncora: "temperatura interna passa de 70 °C" → URL: https://www.iec.ch/homepage → Fonte: IEC 62109-1 — norma de segurança para conversores de potência em sistemas fotovoltaicos

---

[IMAGEM PRINCIPAL — USE ESTA]

IMAGEM PRINCIPAL:
→ Buscar em: unsplash.com — termo de busca: "solar inverter circuit board repair"
→ Por que foi escolhida: Placa eletrônica de inversor solar em bancada de diagnóstico
→ Nome do arquivo: saj-inversor-placa-diagnostico.webp
→ Alt Text: Placa de controle de inversor SAJ em bancada de diagnóstico eletrônico com multímetro e osciloscópio
→ Legenda: Fig. 1 — Diagnóstico em nível de componente na placa do inversor SAJ
→ Onde inserir: Topo do post, antes da introdução

---

[IMAGEM SECUNDÁRIA — USE NO MEIO DO POST]

IMAGEM SECUNDÁRIA:
→ Buscar em: unsplash.com — termo de busca: "IGBT transistor electronic component"
→ Por que foi escolhida: Componente IGBT ou módulo de potência, relevante para seção de identificação de falhas
→ Nome do arquivo: saj-inversor-igbt-modulo-potencia.webp
→ Alt Text: Módulo IGBT de inversor solar com sinal de gate medido em osciloscópio durante diagnóstico de falha
→ Legenda: Fig. 2 — Verificação do sinal de gate do IGBT com osciloscópio na bancada da TEC Solar
→ Onde inserir: Após H2 "Como identificar os erros mais comuns"
