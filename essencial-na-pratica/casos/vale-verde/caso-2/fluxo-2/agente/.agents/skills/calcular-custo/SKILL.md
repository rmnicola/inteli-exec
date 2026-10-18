---
name: calcular-custo
description: Calcula o custo mensal e por entrega de propostas de transporte (preço por entrega com mínimo faturado, ou preço por km com rotas) em vários cenários de volume, rodando um script. Use sempre que a análise precisar de números de custo.
---

# Calcular custo

Nunca calcule de cabeça: rode `scripts/custo.py`, que lê `base/dados/volumes-entrega-2026.csv`, usa só a Grande SP e mostra três cenários (último mês, média de 6 meses e sem o principal cliente).

- Preço por entrega, com mínimo faturado:
  `python3 .agents/skills/calcular-custo/scripts/custo.py --por-entrega 62 --minimo 500`
- Preço por km, com rotas (arredondadas para cima):
  `python3 .agents/skills/calcular-custo/scripts/custo.py --por-km 6.50 --km-rota 210 --entregas-rota 18`
- O contrato atual, para comparar:
  `python3 .agents/skills/calcular-custo/scripts/custo.py --por-entrega 64`

Use os parâmetros da tabela de `saida/2-propostas.md`. Não calcule propostas eliminadas. Salve em `saida/4-custo.md` os comandos rodados, as saídas e a comparação com o contrato atual.
