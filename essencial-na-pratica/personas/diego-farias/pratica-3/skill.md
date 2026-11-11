# Skill: de três orçamentos a uma recomendação

Gabarito do fluxo do Diego (slide 36 e prática 3). Os cinco campos são os mesmos em qualquer aplicativo: **nome, quando usar, etapas, formato da saída e o que nunca fazer sozinho**.

```markdown
---
name: comparar-orcamentos
description: Lê orçamentos em formatos diferentes (PDF, e-mail, foto), coloca tudo na mesma tabela, confere contra os critérios de compra e escreve uma recomendação. Use quando houver dois ou mais orçamentos na pasta de entrada.
---

# Comparar orçamentos e recomendar

## Quando usar
Quando chegarem orçamentos para uma mesma compra em `entrada/`, em qualquer formato: PDF,
texto de e-mail ou foto de papel.

## Etapas

1. **Ler cada orçamento inteiro**, inclusive a foto do manuscrito. Para cada um, extraia:
   fornecedor, data de emissão, validade, preço unitário, quantidade, frete, montagem,
   prazo de entrega, garantia e condição de pagamento.
   - Se um campo não estiver no documento, escreva **NÃO INFORMADO**. Nunca preencha por
     semelhança com os outros orçamentos.
   - Se a foto estiver ilegível em algum ponto, diga qual campo não deu para ler.

2. **Colocar tudo na mesma tabela**, uma linha por fornecedor, com as colunas da etapa 1.
   - Converta os prazos para **dias corridos** e mostre a conversão: "25 dias úteis → 35 dias
     corridos". Prazo escrito de forma vaga ("umas 3 semanas") fica como **PRAZO VAGO**,
     com o texto original ao lado.
   - Calcule o **custo total posto na empresa** = unitário × quantidade + frete + instalação.
     Mostre a conta. Se o frete não estiver informado, o custo total é **INCOMPARÁVEL**:
     escreva o subtotal e diga o que falta.

3. **Conferir contra os critérios de compra** (`base/criterios-de-compra.pdf`), um a um,
   para cada orçamento. Use a data de hoje para checar a validade e mostre a conta:
   "emitida em 26/09, válida 15 dias → venceu em 11/10".
   Classifique cada proposta em **VÁLIDA**, **INCOMPLETA** (falta um dado) ou **VENCIDA**.

4. **Listar o que falta perguntar a cada fornecedor**, em frases prontas para copiar no e-mail.

5. **Recomendar**, com justificativa curta, dizendo em que condição a recomendação muda.
   Se o número de cotações válidas for menor que o exigido pela política, **diga isso antes
   da recomendação**: a compra não pode ser fechada assim.

6. **Gravar** em `saida/comparacao-<objeto-da-compra>.md` e resumir na conversa, em três
   linhas, o que precisa de ação humana.

## Formato da saída

1. `## Tabela comparativa` — uma linha por fornecedor, com a conversão de prazo e a conta do
   custo total visíveis.
2. `## Conferência dos critérios` — tabela: fornecedor | validade | prazo declarado | frete |
   garantia | pagamento | situação (VÁLIDA / INCOMPLETA / VENCIDA).
3. `## O que falta perguntar` — por fornecedor, em frases prontas.
4. `## Recomendação` — até 150 palavras, com a condição que a faria mudar.
5. `## Alerta de política` — quantas cotações válidas existem hoje e quantas a política exige.

## O que nunca fazer sozinho

- **Nunca estimar um preço que não está no documento**, nem usar a média de um intervalo
  ("entre R$ 600 e R$ 1.200"). Frete não informado é NÃO INFORMADO.
- **Nunca comparar preços com e sem frete** na mesma coluna de total.
- **Nunca tratar uma proposta vencida como válida**, mesmo que seja a mais barata.
- **Nunca fechar a compra, enviar e-mail ou contatar fornecedor.** A saída é um rascunho.
- Se a política exigir mais cotações válidas do que existem, diga isso em primeiro lugar.
```
