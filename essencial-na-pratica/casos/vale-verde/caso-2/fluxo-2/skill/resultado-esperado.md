# Resultado esperado: fluxo 2 (análise de fornecedor)

O que a skill `analise-de-fornecedor` deve entregar, com a data de referência de **03/10/2026**. A redação pode variar; os números, as marcações e as conclusões, não.

## Etapa 1 · Requisitos e propostas

### Requisitos

| # | Requisito | Problema que resolve | Origem |
|---|---|---|---|
| R1 | Entrega agendada com janela até as 10h nas 15 unidades de SP | A entrega chega no almoço e ninguém confere | Decidido na reunião (00:09:27 a 00:10:07); ocorrências entre 13h e 15h |
| R2 | Sem transbordo até a unidade | Atrasos de ~24h e a ruptura do Tatuapé nasceram no transbordo de Barueri | Ocorrências de 16/07, 07/08, 21/08 e 18/09; [SEM O CLIENTE] 00:13:56 |
| R3 | Motorista e rota estáveis | Motoristas substitutos; rota alterada sem aviso | Ocorrências de 28/07, 14/08 e 01/09; [SEM O CLIENTE] 00:13:56 |
| R4 | Visibilidade: rastreamento e dados para o relatório semanal | O cliente só sabe do atraso quando a loja liga | Reunião (00:10:10 a 00:10:55; 00:12:53 a 00:13:11) |
| R5 | Descarga na calçada (unidades de rua) e em doca de shopping | Falta de vaga em Pinheiros | Reunião (00:12:10); ocorrências de 09/07 e 11/09 |
| R6 | Cobertura de avaria e falta (comprovante com foto e seguro) | Caixas amassadas e volumes faltando | Reunião (00:02:12); ocorrências de 12/08, 21/08 e 09/09 |
| R7 | Cobertura fora da capital: Guarulhos, Osasco, ABC | Unidades com ocorrência fora da capital | Ocorrências |

Não é requisito: entrega aos sábados (recusada pelo cliente). Rastreamento em tempo real é desejável, não exigência.

### Propostas

| Item | A: Rodar Brasil (PDF) | B: Expresso Campinense (e-mail) | C: Irmãos Bertolini (foto) |
|---|---|---|---|
| Preço | R$ 62,00 por entrega, até 300 kg | **R$ 6,50 por km** ⚠️, VUC com até 18 entregas por rota, rota média de 210 km | R$ 58,00 por entrega, até 250 kg |
| Mínimos e multas | **Faturamento mínimo de 500 entregas/mês** ⚠️ (cláusula 7); multa de 1 mês na rescisão nos primeiros 12 meses ⚠️ (cláusula 9) | Sem volume mínimo | NÃO INFORMADO |
| Validade | 60 dias desde 29/09: até 28/11/2026 | 30 dias desde 28/09: até 28/10/2026 | 15 dias desde 20/08: **até 04/09/2026** ⚠️ |
| Capacidade | Mais de 6.000 entregas/mês | Até 700 entregas/mês | **Até 300 entregas/mês** ⚠️ |
| Cobertura | 39 municípios da Grande SP | Capital e região metropolitana | **"SP capital"** ⚠️ |
| Prazo e janela | D+1; agendamento com janela de 2h; rotas a partir das 7h | D+1 para pedido até 12h; entregas **entre 7h e 11h** ⚠️ | "Dia seguinte" |
| Transbordo | **Consolidação no cross-docking de Barueri** ⚠️ | Rota direta, sem transbordo | NÃO INFORMADO |
| Motorista e rota | Rotas montadas no dia, motoristas "disponíveis no dia" ⚠️ | Motorista fixo por rota | NÃO INFORMADO |
| Seguro | RCTR-C e RCF-DC, com apólices, até R$ 250 mil | **NÃO INFORMADO** ⚠️ | "Seguro incluso", sem apólice |
| Rastreamento e comprovante | Tempo real, portal e API; canhoto com foto | Rastreador nos VUCs; foto por WhatsApp; portal só no fim do ano | NÃO INFORMADO |

> Os requisitos e a tabela estão corretos?

## Etapa 2 · Análise

### Resumo

Duas propostas válidas (A e B); a C está eliminada. A atende melhor o que é formal (seguro, SLA, rastreamento), mas repete o transbordo de Barueri, de onde vieram os atrasos. A B resolve o transbordo e o motorista, mas não declara seguro e é mais cara enquanto o volume fica perto de 500.

### Eliminatórias

| Condição | A | B | C |
|---|---|---|---|
| Validade em 03/10/2026 | ✅ | ✅ | ❌ venceu em 04/09 |
| Capacidade de 490/mês (445 × 1,1) | ✅ | ✅ | ❌ 300 |
| Cobertura da Grande SP | ✅ | ✅ | ❌ só a capital |

### Requisitos

| | A | B |
|---|---|---|
| R1 Janela até 10h | ✅ | ⚠️ confirmar (diz 7h a 11h) |
| R2 Sem transbordo | ❌ Barueri | ✅ |
| R3 Motorista estável | ❌ | ✅ |
| R4 Visibilidade | ✅ | ⚠️ parcial |
| R5 Descarga na calçada | ✅ | ✅ |
| R6 Avaria e falta | ✅ | ❌ sem seguro declarado |
| R7 Fora da capital | ✅ | ✅ |

### Reputação

- **Descartar** a citação [5] da Rodar Brasil: a fonte é a "Rodar Bem Mudanças", outra empresa.
- **Não comparar** 312 reclamações com 23: a Rodar opera mais de 6.000 entregas por mês. Valem os temas.
- **Aproveitar:** as reclamações da Rodar sobre carga parada e volume perdido em Barueri confirmam o risco do R2; as da Expresso sobre avaria sem ressarcimento confirmam que o seguro é condição.
- **Ignorar a conclusão** do relatório: a Bertolini tem só 4 avaliações e já está eliminada.

### Custo (só Grande SP; contrato atual a R$ 64,00 por entrega)

| Cenário | A | B | Atual |
|---|---|---|---|
| Setembro (445 entregas) | 500 × 62 = **R$ 31.000** (R$ 69,66/entrega, +8,8%) | 25 rotas × 210 km × 6,50 = **R$ 34.125** (R$ 76,69, +19,8%) | R$ 28.480 |
| Média abr–set (2.462 entregas em 6 meses) | R$ 186.000 (R$ 75,55, +18,0%) | R$ 189.735 (R$ 77,07, +20,4%) | R$ 157.568 |
| Sem o Sabor & Cia (250 entregas) | o mínimo continua: **R$ 31.000 (R$ 124,00, +93,8%)** | 14 rotas: R$ 19.110 (R$ 76,44, +19,4%) | — |

As duas propostas válidas custam mais que o contrato atual: a troca se justifica pelo serviço, não pelo preço.

### Notas (critérios DS-07)

| Cenário | A | B, seguro pendente | B, seguro comprovado |
|---|---|---|---|
| Sabor fica (setembro) | **4,70** | 3,25 | 3,85 |
| Sabor sai | 3,80 | 3,25 | **3,85** |

### Onde a nota e os requisitos discordam

A nota favorece a A, mas a A repete o transbordo de Barueri e não garante motorista fixo, justamente as causas das reclamações que estão fazendo o cliente ouvir a concorrência. Os critérios da empresa não têm uma linha para isso.

### Pendências

- **Expresso Campinense:** apólice do seguro de carga (RCTR-C, de preferência RCF-DC) e confirmação da janela até as 10h nas 15 unidades.
- **Rodar Brasil:** rota direta, sem cross-docking, para as unidades do Sabor; mínimo menor que 500 ou nenhum; detalhe da multa da cláusula 9.
- **Terceira cotação válida:** a Bertolini atualizada (que ainda não atende capacidade e cobertura) ou outra transportadora.

### Quem decide

Valor anual entre R$ 50 mil e R$ 500 mil (A ≈ R$ 372 mil; B ≈ R$ 379 mil): pela política de compras, exige **3 cotações válidas** (há só duas) e aprovação do **Diretor de Operações (Roberto Lima) e da Gerente Financeira (Patrícia Souza)**.

**O que a skill não pode fazer:** terminar com "contrate a A" (ou a B). A escolha depende de o Sabor renovar e das respostas das transportadoras.
