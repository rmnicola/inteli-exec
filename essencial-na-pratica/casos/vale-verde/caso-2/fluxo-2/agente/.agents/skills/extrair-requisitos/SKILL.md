---
name: extrair-requisitos
description: Transforma o relatório de uma reunião com o cliente e as ocorrências de entrega numa lista de requisitos que um novo fornecedor precisa atender. Use no início da análise de propostas de fornecedor.
---

# Extrair requisitos

1. Leia `entrada/relatorio-da-reuniao.md` e `base/dados/ocorrencias-entrega-sabor-2026.csv`.
2. Liste os requisitos: só o que o cliente pediu, o que foi decidido com ele ou o que se repete nas ocorrências. Sugestão recusada não é requisito; "seria bom" é desejável, não exigência.
3. Para cada requisito, diga o problema que ele resolve e a origem (horário da reunião ou data da ocorrência).
4. Fatos [SEM O CLIENTE] podem revelar a causa de um problema; use-os, mantendo a marcação.
5. Salve em `saida/1-requisitos.md`, numa tabela: # | requisito | problema que resolve | origem.
