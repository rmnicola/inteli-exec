# Caso Vale Verde Distribuidora

Cenário fictício usado no projeto-gabarito do *Essencial na Prática*. Os dois casos acontecem na mesma empresa e usam os mesmos documentos institucionais.

> **Este arquivo é a referência do cenário.** Todo número, nome e regra que aparece nos insumos sai daqui. Para mudar um fato, mude aqui primeiro e depois nos documentos-fonte.

## Estrutura

```
vale-verde/
├── README.md                    ← este arquivo (referência do cenário)
├── build.py                     ← gera os PDFs, imagens e planilhas a partir das fontes
├── politicas-institucionais/    ← os documentos institucionais em PDF: tudo o que vai para o NotebookLM
│   └── fontes/
├── caso-1/                      ← perguntas e respostas (casos de teste) e o prompt da skill
└── caso-2/
    ├── fluxo-1/                 ← da transcrição a fatos e acionáveis: skill, transcrição e resultado esperado
    └── fluxo-2/                 ← da proposta ao match e ao risco
        ├── fontes/              ← Markdown editável das propostas, do relatório de pesquisa e das planilhas
        ├── insumos/             ← os arquivos gerados (PDF, PNG, XLSX, TXT)
        ├── skill/               ← o Gem/skill de análise e o resultado esperado
        └── agente/              ← a mesma análise como pasta de trabalho do Antigravity
```

Depois de editar qualquer arquivo em `fontes/`, gere os documentos de novo:

```
python3 build.py
```

Os PDFs de `politicas-institucionais/` são gerados na própria pasta; os do fluxo 2, em `caso-2/fluxo-2/insumos/`. O `build.py` também copia a base de conhecimento para `caso-2/fluxo-2/agente/base/`.

## Os dois casos

| # | Caso | Ferramentas | Termos que exercita |
|---|---|---|---|
| 1 | **Tira-dúvidas das políticas**: o time pergunta, a skill responde citando a fonte | NotebookLM + skill | Contexto, contexto longo, skill, hierarquia do prompt |
| 2 | **A nova transportadora**: da reunião tensa com o maior cliente às três propostas | Fluxo 1: skill de fatos e acionáveis. Fluxo 2: skill de análise de fornecedor ou agente no Antigravity | Contexto longo, pausas para validação, multimodal, saída de agente a verificar, critérios contra requisitos, ferramentas, o que a IA não decide |

## O que subir em cada ferramenta

| Caso | Arquivos de conhecimento (sobem uma vez) | Entra na conversa a cada uso | Gabaritos e roteiro |
|---|---|---|---|
| 1. Tira-dúvidas | No NotebookLM: todos os PDFs de `politicas-institucionais/` | As perguntas do time | `caso-1/perguntas-e-respostas.md`, `caso-1/skill-tira-duvidas-politicas.md` |
| 2. Fluxo 1 (skill `fatos-e-acionaveis`) | Nenhum | A transcrição (`caso-2/fluxo-1/`) | `caso-2/fluxo-1/skill-fatos-e-acionaveis.md`, `caso-2/fluxo-1/resultado-esperado.md` |
| 2. Fluxo 2 (skill `analise-de-fornecedor`) | `criterios-de-avaliacao-transportadora.pdf` e `politica-de-compras.pdf` (de `politicas-institucionais/`), `volumes-entrega-2026.xlsx` | O relatório final do fluxo 1, as 3 propostas, as ocorrências, o relatório de pesquisa e a data de hoje | `caso-2/fluxo-2/skill/` |

---

## Referência do cenário

### A empresa

- **Razão social:** Vale Verde Distribuidora Ltda. (fictícia)
- **O que faz:** distribui produtos de limpeza, higiene e descartáveis para empresas (restaurantes, hospitais, escritórios, condomínios). Vende só para empresas.
- **Sede e centro de distribuição:** Campinas (SP), Rodovia Anhanguera, km 98
- **Fundação:** 2004
- **Colaboradores:** cerca de 120
- **Faturamento:** cerca de R$ 80 milhões por ano
- **Clientes ativos:** cerca de 1.400
- **Entregas:**
  - Na Região Metropolitana de Campinas (RMC), com **frota própria**.
  - Na **Grande São Paulo**, por transportadora terceirizada: a **Rápido Interior Transportes**, com contrato desde 2023 a R$ 64,00 por entrega.

### Pessoas da Vale Verde

| Nome | Cargo |
|---|---|
| Antônio Ferraz | CEO e sócio fundador |
| **Carla Mendes** | **Diretora Comercial**: aprova descontos de 3% a 7% e prazos até 45 dias |
| Roberto Lima | Diretor de Operações e Logística |
| Patrícia Souza | Gerente Financeira |
| Lucas Andrade | Executivo de contas (key account) do Grupo Sabor & Cia |
| **Renata Alves** | **Coordenadora de Vendas (protagonista do caso 1)**: atende as dúvidas do time comercial sobre a política |
| Sílvia Rocha | Coordenadora de RH |
| Fábio Nunes | Comprador (área de Suprimentos, ligada a Operações) |

### O cliente: Grupo Sabor & Cia

- Rede de **35 restaurantes**: 20 na RMC, entregues pela frota própria, e **15 na Grande São Paulo**, entregues pela transportadora.
- O **maior cliente** da Vale Verde: cerca de **R$ 9,6 milhões por ano** (R$ 800 mil por mês), 12% do faturamento.
- Contrato anual que **vence em 31/10/2026**. Condições atuais: **4% de desconto** sobre a tabela e **prazo de pagamento de 35 dias**.
- **Margem de contribuição** da Vale Verde no cliente: **9%**. Informação interna, que nunca vai ao cliente.
- Contato: **Marcelo Duarte**, gerente de compras. Na operação do cliente há a **"Bia"** (Beatriz), citada só pelo primeiro nome; a transcrição não diz o cargo dela.
- **Problema:** atrasos de entrega nas 15 unidades da Grande SP.
  - O OTIF (entregas no prazo e completas) dessas unidades caiu de **96%** (janeiro a março) para **84%** (julho a setembro).
  - Em agosto e setembro houve **11 entregas atrasadas** e **2 rupturas**, em que faltou produto e itens saíram do cardápio.
- **Concorrente** que o cliente diz estar cotando: **Limpax Distribuidora** (fictícia).

### A reunião (contexto do caso 2)

- **Data:** 25/09/2026, às 10h, por Google Meet. Estava agendada para 40 minutos, mas durou cerca de 18, porque o Marcelo tinha outra reunião às 11h.
- **Participantes:**
  - Pela Vale Verde: Carla Mendes, Lucas Andrade e Roberto Lima (que entra no meio da reunião).
  - Pelo cliente: Marcelo Duarte.
- **O que o cliente pede:** desconto de **8%** (hoje são 4%) e prazo de **45 dias** na renovação.
- **O que de fato foi decidido**, com acordo explícito dos dois lados:
  1. A partir de 01/10, as entregas das 15 unidades da Grande SP passam a ter **agendamento com janela até as 10h**.
  2. A Vale Verde envia um **relatório semanal de entregas** das unidades da Grande SP, toda segunda-feira, a partir de 05/10. Responsável: Lucas.
  3. A Vale Verde apresenta um **plano de ação** para os atrasos até **15/10** (20 dias). Começou como "15 dias" e foi corrigido por Roberto para 20.
- **O que ficou pendente** (não foi decidido):
  - O desconto. Carla disse "vou ver se consigo chegar em uns 5%, preciso olhar com o financeiro". **Não é compromisso.** E é ambíguo: 5% no total, ou 5 pontos a mais?
  - O prazo de 45 dias, que ninguém respondeu.
  - O crédito pelas rupturas: "alguém precisa levantar os pedidos que tiveram ruptura para ver o crédito". **Sem responsável.**
  - A lista das unidades com mais problema: "a Bia te manda a lista". Pendência do lado do cliente.
- **Trecho interno capturado pela transcrição:** Marcelo sai da chamada uns 3 minutos para atender o telefone. Nesse intervalo, Carla e Roberto comentam:
  - que a margem no cliente é de 9% e que 8% de desconto "é pagar para entregar";
  - que a Rápido Interior "está enrolando";
  - que vão **cotar uma nova transportadora**. Responsável: Roberto. É o ponto de partida do caso 2.

### Alçadas e regras (políticas institucionais)

**Política Comercial, versão 3, vigente desde 01/03/2026.** Ela substitui a versão 2.

- Descontos sobre a tabela:
  - Vendedor ou executivo de contas: até **3%**.
  - Diretora Comercial: até **7%**.
  - Acima de 7%: **CEO, com parecer do Financeiro**.
- Renovação de contrato anual com mudança de desconto: exige **análise de margem** pelo Financeiro, qualquer que seja o percentual.
- Prazo de pagamento:
  - Padrão: **28 dias**.
  - Até **45 dias**, com aprovação da Diretora Comercial.
  - Acima de 45 dias: CEO.
- Frete: grátis para pedidos a partir de **R$ 1.500** na RMC e a partir de R$ 3.000 na Grande SP. Abaixo disso, a taxa de entrega é de **R$ 85** (RMC) ou **R$ 140** (Grande SP).
- Bonificação em produto: até 2% do volume do pedido, com aprovação da Diretora Comercial.

**Política Comercial, versão 2, de 2024. REVOGADA.** Saiu do caso em out/2026: não vai mais para a pasta do caso.

- Descontos: vendedor até **5%**, diretor comercial até **10%**.
- Prazo padrão de **30 dias**.
- A versão 3 ainda cita, no cabeçalho, que substituiu a versão 2.

**Política de Compras e Contratação de Fornecedores** (vale para o caso 2):

| Valor da compra ou valor anual do contrato | Cotações | Aprovação |
|---|---|---|
| Até R$ 10 mil | 1 | Gestor da área |
| R$ 10 mil a R$ 50 mil | 2 | Diretor da área |
| Acima de R$ 50 mil | **3 válidas** | **Diretor da área + Gerente Financeira** |
| Acima de R$ 500 mil por ano | 3 válidas | CEO |

- Para serviço de transporte, a proposta precisa trazer: **seguro de carga (RCTR-C)**, **validade vigente** e prazo de entrega (SLA) declarado.
- Uma proposta vencida ou incompleta **não conta** como cotação válida.

**Nível de serviço de entrega e devoluções:**

- Prazos de entrega:

| Destino | Prazo |
|---|---|
| RMC, pedido até as 14h | D+1 |
| Grande SP e interior até 150 km | D+2 |
| Demais cidades de SP | D+3 |
| Outros estados | D+5 |

- Meta de OTIF: **95%**.
- Avaria deve ser comunicada em até **48h**. A devolução sem avaria é aceita em até **7 dias**, com o frete por conta do cliente. O crédito é dado em até **10 dias úteis**.

**Viagens e despesas** (volume para o contexto longo):

- Quilometragem: R$ 1,20/km.
- Hotel: teto de R$ 350 no interior e de R$ 450 nas capitais.
- Alimentação: R$ 120 por dia.
- Passagem aérea com 14 dias de antecedência.
- Prestação de contas em até 5 dias úteis.

**Perguntas frequentes de RH** (volume para o contexto longo):

- Férias pedidas com 30 dias de antecedência.
- Home office: 2 dias por semana para o administrativo. A operação não tem home office.
- Auxílio-educação: 50% da mensalidade, até R$ 600 por mês, depois de 6 meses de casa.
- Vale-refeição: R$ 45 por dia.

### As transportadoras (caso 2)

**Escopo da cotação:** entregas fracionadas de Campinas para a **Grande São Paulo**, com contrato de 12 meses.

**Volume de entregas na Grande SP:**

| Mês (2026) | Entregas | Do Sabor & Cia |
|---|---|---|
| Abril | 380 | 175 |
| Maio | 395 | 180 |
| Junho | 410 | 185 |
| Julho | 402 | 182 |
| Agosto | 430 | 190 |
| Setembro | 445 | 195 |

- Peso médio: 175 kg por entrega.
- Valor médio da nota fiscal: R$ 1.900 por entrega.
- Distância Campinas–São Paulo: cerca de 95 km.
- Contrato atual com a Rápido Interior: R$ 64,00 por entrega.

**Valor anual estimado:** cerca de 410 entregas × R$ 64 × 12 meses ≈ **R$ 315 mil**.

- Pela Política de Compras, isso exige **3 cotações válidas** e aprovação de **Roberto + Patrícia**.
- O valor fica abaixo de R$ 500 mil, então não precisa do CEO.

**As três propostas:**

| | A: Rodar Brasil Logística | B: Expresso Campinense | C: Transportes Irmãos Bertolini |
|---|---|---|---|
| Perfil | Grande, nacional | Regional, 12 anos de mercado | Pequena, 3 anos de mercado |
| Formato | PDF formal, 4 páginas | E-mail em texto corrido | **Foto de um orçamento escrito à mão** |
| Preço | **R$ 62,00 por entrega** | **R$ 6,50 por km rodado** (veículo urbano de carga, até 18 entregas por rota; rota média de 210 km ida e volta) | **R$ 58,00 por entrega** |
| Armadilha | **Mínimo de 500 entregas por mês** cobrado mesmo que o volume seja menor (cláusula 7). Reajuste anual pelo IPCA + 2% | **Não menciona seguro de carga.** O preço por km não pode ser comparado direto com o preço por entrega | **Validade vencida** (emitida em 20/08/2026, válida por 15 dias). **Capacidade de até 300 entregas por mês.** Atende só a capital, sem Guarulhos ou Osasco. "Seguro incluso", sem número de apólice |
| Prazo | D+1 | D+1 para pedido até as 12h | "Entrega no dia seguinte" |
| Seguro | RCTR-C e RCF-DC incluídos | Não menciona | "Seguro incluso" |

**Datas das propostas:**

- A: emitida em 29/09/2026, válida por 60 dias.
- B: enviada em 28/09/2026, válida por 30 dias.
- C: emitida em **20/08/2026**, válida por 15 dias. É um orçamento antigo, que o comprador Fábio tinha pedido em agosto e que ficou na gaveta.

**Critérios de avaliação de transportadora:**

- Pesos:

| Critério | Peso |
|---|---|
| Prazo e nível de serviço | 30% |
| Custo | 30% |
| Seguro e risco | 15% |
| Capacidade e cobertura | 15% |
| Histórico e referências | 10% |

- Condições que precisam ser atendidas antes de pontuar a proposta:
  - validade vigente;
  - capacidade de pelo menos o maior volume mensal dos últimos 6 meses mais 10% (445 × 1,1 ≈ **490 entregas por mês**);
  - cobertura de toda a Grande SP.
- Uma proposta sem seguro de carga declarado **não é descartada automaticamente**, mas precisa ser complementada antes da decisão.

**Conta que a análise deve fazer** (com execução de código ou na planilha), com o volume de setembro (445 entregas):

| Proposta | Cálculo | Custo mensal | Por entrega |
|---|---|---|---|
| A | 500 (mínimo) × R$ 62 | **R$ 31.000** | R$ 69,66 |
| B | 25 rotas (445 ÷ 18, arredondando para cima) × 210 km × R$ 6,50 | **R$ 34.125** | R$ 76,69 |
| C | 445 × R$ 58 | R$ 25.810 | R$ 58,00 |

A proposta C, porém, é **desclassificada**: a validade venceu, a capacidade não comporta o volume e a cobertura é incompleta.

**A virada:** e se o Sabor & Cia sair? O volume cai para cerca de 250 entregas por mês (445 − 195).

| Proposta | Cálculo | Custo mensal | Por entrega |
|---|---|---|---|
| A | o mínimo continua valendo: 500 × R$ 62 | R$ 31.000 | **R$ 124,00** |
| B | 14 rotas × 210 km × R$ 6,50 | R$ 19.110 | **R$ 76,44** |

**Não existe uma resposta certa única. É uma decisão humana:**

- A proposta A vale se o Sabor ficar e se der para negociar o mínimo.
- A proposta B vale se houver risco de perder o cliente, desde que ela comprove o seguro.
- Em qualquer caso, como a C não é uma cotação válida, **a política de 3 cotações não está cumprida**. Falta pedir uma nova proposta à Bertolini ou cotar outra transportadora.

### Requisitos do cliente e reputação (caso 2)

- **Requisitos que saem da reunião e das ocorrências** (gabarito em `caso-2/fluxo-2/skill/resultado-esperado.md`):
  - entrega agendada com janela até as 10h;
  - sem transbordo: os atrasos de 24h e a ruptura do Tatuapé nasceram no transbordo de Barueri da Rápido Interior;
  - motorista e rota estáveis;
  - visibilidade (rastreamento e dados para o relatório semanal);
  - descarga na calçada;
  - cobertura de avaria e falta;
  - cobertura fora da capital.
- **Proposta A (Rodar Brasil):** consolida as cargas no **cross-docking de Barueri**, com rotas montadas no dia e motoristas "disponíveis no dia". Atende bem o formal (SLA, seguro, rastreamento), mas repete a causa dos atrasos.
- **Proposta B (Expresso Campinense):** rota direta do CD, sem transbordo, com motorista fixo. Os VUCs saem às 5h e entregam entre 7h e 11h, o que não garante a janela até as 10h. Continua sem seguro declarado.
- **Levantamento de reputação** (`levantamento-reputacao-transportadoras.pdf`), no formato de um relatório de deep research (plano, resumo, seções com citações numeradas, lista de fontes), sem revisão humana:
  - Rodar Brasil: nota 6,1 e 312 reclamações (atraso 41%, extravio 18%), com relatos de carga parada no cross-docking de Barueri. A citação [5] é de uma empresa de mudanças homônima, o que só aparece na lista de fontes.
  - Expresso Campinense: nota 7,8 e 23 reclamações, 6 delas de avaria sem ressarcimento ("o seguro era por conta do embarcador").
  - Irmãos Bertolini: nota 9,0 com só 4 avaliações.
  - A conclusão do relatório recomenda a Bertolini, que está eliminada pelas regras da empresa.

### Fatos acrescentados na escrita dos insumos

São detalhes que não estavam nesta referência e foram criados ao escrever os insumos. Nenhum a contradiz.

- **Políticas institucionais:**
  - Códigos dos documentos: POL-COM-003 (comercial v3), POL-COM-002 (comercial v2), POL-SUP-001 (compras), POL-OPE-002 (nível de serviço), POL-ADM-004 (viagens) e RH-FAQ-2026.
  - Cliente-chave é quem fatura mais de R$ 2 milhões por ano ou tem contrato anual.
  - A análise de margem deve ser pedida 20 dias úteis antes da renovação. No caso do Sabor, o prazo cai por volta de 02/10, então já está no limite.
  - O frete é calculado sobre o valor líquido do pedido. A tabela de preços é revista a cada trimestre.
  - A POL-OPE-002 §5.3 pede um plano de ação interno em 10 dias úteis quando o OTIF de um cliente-chave fica abaixo de 90%. **Não é o mesmo** plano de 20 dias prometido ao Sabor na reunião.
- **A versão 2 da política comercial (2024)**, além das alçadas e do prazo, diverge da v3 em:
  - frete grátis a partir de R$ 1.200 (RMC) e R$ 2.500 (Grande SP), com taxas de R$ 70 e R$ 120;
  - frete calculado sobre o valor bruto;
  - bonificação de até 3%;
  - revisão semestral da tabela de preços.
- **Sabor & Cia:**
  - Cliente desde 2017.
  - OTIF de 91% no 2º trimestre.
  - Uma 36ª unidade em Valinhos (RMC) está em implantação, com inauguração em 10/10.
  - A planilha lista só as ocorrências com reclamação formal: 4 atrasos em julho; 11 atrasos, 2 rupturas e 1 "sem recebimento" (falha do cliente) em agosto e setembro.
  - A Rápido Interior faz transbordo em Barueri.
- **Transportadoras e volumes (caso 2):**
  - RMC: frota própria, com custo interno de R$ 38,50 por entrega.
  - Interior de SP: atendido pela Via Oeste Cargas, a R$ 71,00 por entrega.
  - Proposta A: limite de 300 kg por entrega, capacidade de mais de 6.000 entregas por mês.
  - Proposta B: capacidade de até 700 entregas por mês, sem volume mínimo.
  - Proposta C: limite de 250 kg por entrega, pagamento em 30 dias. O contato é Sérgio Bertolini e a empresa existe desde 2023.
  - Nota de custo: definida pela diferença em relação aos R$ 64,00 do contrato atual.
  - Notas ponderadas no gabarito:

| Cenário | A | B, seguro pendente | B, seguro comprovado |
|---|---|---|---|
| Sabor fica | 4,70 | 3,25 | 3,85 |
| Sabor sai | 3,80 | 3,25 | 3,85 |
