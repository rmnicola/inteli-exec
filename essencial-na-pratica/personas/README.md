# Personas do Essencial na Prática

Três pessoas fictícias, de áreas diferentes, usadas nas práticas 2 e 3 da turma de 14/11/2026. A turma vota qual seguir em cada rodada.

> **Este arquivo é a referência do cenário.** Todo nome, número e regra que aparece nos documentos sai daqui. Para mudar um fato, mude aqui primeiro e depois na fonte correspondente.

Tudo é fictício: pessoas, empresas, clientes, preços e documentos.

## Estrutura

```
personas/
├── README.md            ← este arquivo
├── build.py             ← gera os documentos a partir das fontes e monta um .zip por persona
└── <persona>/
    ├── pratica-2/
    │   ├── fontes/              ← Markdown editável
    │   ├── arquivos/            ← o que o aluno baixa (PDF, PNG, XLSX, TXT)
    │   └── perguntas-e-respostas.md   ← casos de teste, com a resposta e o documento de origem
    └── pratica-3/
        ├── fontes/
        ├── arquivos/
        ├── skill.md                   ← o fluxo escrito como skill (gabarito do slide 36)
        └── resultado-esperado.md      ← o que uma execução boa produz
```

Depois de editar qualquer arquivo em `fontes/`, gere os documentos de novo:

```
python3 build.py
```

Os `.zip` saem em `personas/zips/` e são o que o site oferece para baixar.

## As três personas

| Persona | Área | Prática 2 (instruções e documentos) | Prática 3 (fluxo em várias etapas) |
|---|---|---|---|
| **Helena Prado** | varejo, gerente de três lojas | tira-dúvidas de procedimentos da loja | da reunião semanal ao e-mail de acompanhamento |
| **Diego Farias** | administrativo-financeiro | tira-dúvidas de um contrato de serviço | de três orçamentos a uma recomendação |
| **Beatriz Lemos** | arquitetura, autônoma | respostas a clientes no tom dela | da planilha do mês ao relatório do cliente |

Em cada prática 2 há **uma pergunta cuja resposta não está nos documentos**: o assistente bom diz que não sabe, em vez de inventar.

---

## Helena Prado

- **Quem é:** 38 anos, gerente das três lojas da **Casa Aurora**, rede de utilidades domésticas de Curitiba (Batel, Portão e Cabral). Cerca de 24 pessoas no total.
- **Como trabalha:** passa o dia entre as lojas e responde o time por mensagem.

### Prática 2 — "Meu time me pergunta as mesmas coisas o dia inteiro"

Documentos (três PDFs curtos, papel timbrado Casa Aurora):

| Documento | Código | O que traz |
|---|---|---|
| `escala-e-troca-de-turno.pdf` | PRO-LOJ-001 | horários das lojas, escala, regra de troca de turno, banco de horas, atestado |
| `trocas-e-devolucoes.pdf` | PRO-LOJ-002 | prazos de troca, o que não troca, vale-compra, defeito de fabricação |
| `abertura-e-fechamento-de-caixa.pdf` | PRO-LOJ-003 | fundo de caixa, sangria, conferência, quebra de caixa, fechamento |

Fatos de referência:

- **Horários:** Batel e Cabral das 10h às 20h de segunda a sábado; Portão das 9h às 19h. Domingo só o Batel, das 14h às 20h.
- **Troca de turno:** pedida com **48 horas** de antecedência, no grupo da loja, e vale só depois do "ok" escrito da Helena. Troca no mesmo dia só por emergência, e a Helena precisa ser avisada por ligação.
- **Banco de horas:** até **20 horas** acumuladas; o que passar disso é pago no mês seguinte. Compensação até o fim do trimestre.
- **Atestado:** entregue em até **48 horas**, foto no grupo e original na pasta da loja.
- **Troca de produto:** **30 dias** com nota fiscal, produto sem uso e com embalagem. **Defeito de fabricação: 90 dias.**
- **Não troca:** itens de uso pessoal (escova, tábua de carne já usada), produtos de promoção "ponta de estoque" (etiqueta amarela) e itens personalizados.
- **Vale-compra:** quando não há o mesmo produto, vale de **90 dias**, usado em qualquer uma das três lojas.
- **Troca entre lojas:** aceita. A loja que recebe registra com o código da loja de origem.
- **Fundo de caixa:** **R$ 300** por caixa, conferido na abertura por duas pessoas.
- **Sangria:** sempre que o caixa passar de **R$ 2.000** em dinheiro, e obrigatoriamente às 16h.
- **Quebra de caixa:** diferença de até **R$ 20** é registrada na planilha do dia; acima disso, a Helena é avisada no mesmo dia e o caso vai para o financeiro.
- **Fechamento:** conferência às cegas (conta primeiro, confere o sistema depois), envelope lacrado no cofre e foto do relatório no grupo até **30 minutos** depois do fechamento.

### Prática 3 — "Saio da reunião semanal e ninguém sabe quem ficou com o quê"

- **Arquivo:** `reuniao-semanal-2026-11-09.txt`, transcrição de cerca de 1.200 palavras da reunião de segunda-feira, 09/11/2026, com Helena, Rafael (Batel), Juliana (Portão), Marcos (Cabral) e Tatiane (financeiro).
- **Fluxo:** receber a transcrição → separar fatos de opiniões → listar pendências com responsável e prazo → marcar o que ficou sem dono → redigir o e-mail de acompanhamento.
- **Armadilhas plantadas:**
  1. A conferência do estoque de Natal fica **sem responsável** ("alguém vai ter que olhar isso").
  2. Marcos diz como fato que "o pessoal do Cabral vende mais no sábado porque o shopping ao lado lota" — é **opinião**, não há número na reunião.
  3. O prazo do novo horário de fim de ano aparece **de duas formas**: "até o fim da semana" e, mais adiante, "quinta". A quinta-feira é 12/11.

---

## Diego Farias

- **Quem é:** 31 anos, analista administrativo-financeiro da **Núcleo Engenharia**, empresa de 60 pessoas em Belo Horizonte. É quem todo mundo procura quando a pergunta envolve contrato, nota ou compra.

### Prática 2 — "Ninguém lê o contrato, e todo mundo me pergunta o que ele diz"

- **Documento:** `contrato-limpeza-asseio-total.pdf`, contrato de prestação de serviço de limpeza predial, **sete páginas**, entre a Núcleo Engenharia (contratante) e a **Asseio Total Serviços** (contratada).

Fatos de referência:

- **Vigência:** 12 meses, de **01/02/2026 a 31/01/2027**, renovação automática por igual período se nenhuma das partes avisar.
- **Valor:** **R$ 18.400,00 por mês**, pagos até o **dia 10** do mês seguinte ao da prestação.
- **Reajuste:** anual, na data-base, pelo **IPCA** acumulado em 12 meses. Se o IPCA for negativo, o valor fica o mesmo.
- **Aviso de não renovação:** **60 dias** antes do fim da vigência, por escrito.
- **Rescisão imotivada:** qualquer parte, com aviso de **30 dias**, e **multa de 20% sobre o saldo restante** do contrato.
- **Rescisão por justa causa** (descumprimento não sanado em 10 dias após notificação): **sem multa**.
- **Atraso no pagamento:** multa de **2%** mais juros de **1% ao mês**, proporcionais aos dias.
- **Falha na prestação:** desconto proporcional no mês, mais multa de **5% do valor mensal** se o problema se repetir três vezes no mesmo trimestre.
- **Equipe:** 4 auxiliares de limpeza e 1 encarregado, de segunda a sexta, das 6h às 15h.
- **Serviços extras** (limpeza pós-obra, vidros externos, sábados): cobrados à parte, **conforme a tabela do Anexo II**.
- **Anexo I** (escopo e frequência) está no contrato. **O Anexo II (tabela de preços dos serviços extras) é citado mas não foi enviado** — é a armadilha da pergunta 5.
- **Foro:** Belo Horizonte. **Reajuste de pessoal por dissídio** não altera o valor fora da data-base.

### Prática 3 — "Recebo três orçamentos, cada um de um jeito, e preciso recomendar um"

Compra: **30 cadeiras de escritório** para a nova sala do time de projetos. Data de hoje no exercício: **14/11/2026**.

- **Critérios de compra** (`criterios-de-compra.pdf`, POL-NUC-002): três cotações válidas acima de R$ 10 mil; proposta precisa ter **validade vigente**, **prazo de entrega declarado** e **preço com frete até o endereço da empresa**; garantia mínima de **12 meses**; pagamento em até 30 dias; peso: custo 40%, prazo 25%, garantia 20%, atendimento ao pedido 15%.

| | A: Mobicorp | B: Ergoline | C: Cadeiras & Cia |
|---|---|---|---|
| Formato | PDF formal | e-mail em texto | foto de orçamento manuscrito |
| Preço unitário | R$ 1.280,00 | R$ 1.190,00 | R$ 1.090,00 |
| Frete | **incluso** | **"frete a combinar"** | R$ 780 no total |
| Prazo | **25 dias úteis** | **20 dias corridos** | "umas 3 semanas" |
| Garantia | 36 meses | 12 meses | 12 meses |
| Validade | emitida 05/11/2026, válida 30 dias | enviada 07/11/2026, válida 15 dias | emitida **26/09/2026, válida 15 dias** (vencida) |
| Pagamento | 30 dias | 28 dias | 50% na entrada |

- **Armadilhas plantadas:** o preço da **B não tem frete**; a **C está vencida**; os prazos vêm em **unidades diferentes** (dias úteis, dias corridos, "umas 3 semanas").
- **Conta:** A = 30 × 1.280 = **R$ 38.400** com frete. B = 30 × 1.190 = R$ 35.700 **mais frete não informado**. C = 30 × 1.090 + 780 = R$ 33.480, **mas está vencida**.
- **Decisão:** não há resposta única. A é a mais cara e a única completa; B pode ganhar se o frete for informado e couber; C precisa de proposta nova. Como só duas cotações são válidas hoje, **a política de três cotações não está cumprida**.

---

## Beatriz Lemos

- **Quem é:** 34 anos, arquiteta autônoma em Florianópolis. Trabalha sozinha, com dois estagiários por projeto. Atende de reforma de apartamento a projeto de loja.

### Prática 2 — "Passo a noite respondendo cliente, e as respostas são sempre parecidas"

- **Documentos:** `respostas-anteriores.pdf` (oito respostas antigas dela, que mostram o tom) e `tabela-de-servicos-e-precos.pdf`.

Fatos de referência (tabela de serviços):

| Serviço | Preço | Prazo |
|---|---|---|
| Visita técnica com relatório | R$ 450 (abatido do projeto se fechar em 30 dias) | relatório em 5 dias |
| Projeto de interiores, apartamento até 90 m² | R$ 230/m², mínimo de R$ 16.000 | 8 semanas |
| Projeto de interiores, acima de 90 m² | R$ 210/m² | 10 semanas |
| Projeto de loja ou consultório | R$ 280/m², mínimo de R$ 22.000 | 10 semanas |
| Acompanhamento de obra | R$ 1.900 por visita quinzenal | ao longo da obra |
| Projeto de marcenaria isolado | R$ 4.800 por ambiente | 4 semanas |

- **Pagamento:** 30% na assinatura, 40% na entrega do preliminar, 30% na entrega do executivo. Parcelamento em até 4 vezes sem juros.
- **Revisões:** duas rodadas de ajuste incluídas em cada etapa. A terceira em diante é cobrada a R$ 900 por rodada.
- **Desconto:** a tabela **não prevê desconto**. Beatriz decide caso a caso. O assistente nunca promete desconto: anota o pedido e passa para ela.
- **Tom das respostas anteriores:** direta, cordial, sem jargão, primeira pessoa, sempre com um próximo passo claro e uma pergunta no fim. Nunca usa "prezado" nem "venho por meio desta".

### Prática 3 — "Todo mês monto na mão o relatório de andamento de cada cliente"

- **Arquivos:** `horas-novembro-2026.xlsx` (horas por etapa, etapas concluídas, pendências do cliente, do projeto do apartamento da família Tavares) e `relatorio-outubro-2026.pdf` (o relatório do mês anterior, que serve de modelo).
- **Fluxo:** ler a planilha → calcular horas e andamento → destacar atrasos e pendências do cliente → redigir o relatório no formato do modelo → listar o que ela precisa conferir antes de enviar.
- **Armadilhas plantadas:**
  1. A etapa **"Projeto executivo — marcenaria"** está **atrasada**: previsão de 31/10 e ainda em andamento.
  2. O total de horas **não está na planilha**: precisa ser somado, não estimado (são **47,5 horas** em novembro; 126,0 acumuladas).
  3. Uma pendência do cliente (a escolha do porcelanato) está parada desde **16/10** e é a causa do atraso da marcenaria.
