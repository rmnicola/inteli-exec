# Skill: da planilha do mês ao relatório do cliente

Gabarito do fluxo da Beatriz (slide 36 e prática 3). Os cinco campos são os mesmos em qualquer aplicativo: **nome, quando usar, etapas, formato da saída e o que nunca fazer sozinho**.

```markdown
---
name: relatorio-de-andamento
description: Transforma a planilha de horas do mês no relatório de andamento do cliente, no formato do relatório do mês anterior. Use quando houver uma planilha de horas e um relatório anterior na pasta.
---

# Relatório de andamento do cliente

## Quando usar
No fim do mês, quando a planilha de horas daquele mês estiver em `entrada/` e o relatório do
mês anterior estiver em `base/`. Um cliente por vez.

## Etapas

1. **Ler a planilha inteira, as três abas** (Horas, Etapas, Pendências do cliente) e o
   relatório do mês anterior, que é o **modelo de formato**: mesmos títulos, mesma ordem,
   mesmas tabelas.

2. **Somar as horas.** Some linha a linha, nunca estime nem arredonde "de cabeça":
   - total do mês;
   - total por etapa;
   - acumulado do projeto = acumulado do relatório anterior + total do mês.
   **Mostre a conta do acumulado** no rascunho, para a Beatriz conferir.

3. **Calcular o andamento** pelas etapas: quantas concluídas, quantas em andamento, quantas
   não iniciadas, e o que mudou desde o relatório anterior.

4. **Destacar os atrasos.** Etapa com previsão já vencida e sem data de entrega está
   **ATRASADA**. Para cada atraso, procure a causa nas pendências do cliente e diga qual é,
   com a data em que a pendência foi pedida e há quantos dias está em aberto.

5. **Listar as pendências do cliente** em aberto, com a data do pedido e o que cada uma trava.

6. **Redigir o relatório** com os mesmos títulos do mês anterior, preenchidos com os números
   deste mês.

7. **Listar o que a Beatriz precisa conferir antes de enviar** — uma seção separada, que não
   faz parte do relatório.

8. **Gravar** em `saida/relatorio-<mes>-<ano>.md`.

## Formato da saída

O relatório segue exatamente o modelo do mês anterior:

1. Cabeçalho: projeto, cliente, período, data de emissão.
2. `## 1. Onde o projeto está` — parágrafo curto e a tabela de etapas.
3. `## 2. Horas do mês` — total do mês, acumulado e tabela por etapa.
4. `## 3. Atrasos` — cada atraso com a causa. Se não houver, escreva que não houve.
5. `## 4. O que depende de vocês` — tabela das pendências em aberto.
6. `## 5. Próximo mês`.
7. `## 6. Financeiro` — repetido do mês anterior, com **a atualizar** onde não houver dado novo.

Depois do relatório, fora dele:

8. `## Antes de enviar — conferir` — lista do que a Beatriz precisa checar.

## O que nunca fazer sozinho

- **Nunca estimar horas.** Se um lançamento estiver sem valor, escreva SEM HORAS e aponte.
- **Nunca inventar número financeiro**: o que não estiver na planilha nem no relatório
  anterior vai como **a atualizar**.
- **Nunca cobrar o cliente nem escrever em tom de cobrança.** Pendência em aberto é
  informada com a data e o efeito, sem adjetivo.
- **Nunca enviar o relatório.** Quem envia é a Beatriz.
- Se a planilha e o relatório anterior se contradisserem, aponte os dois valores.
```
