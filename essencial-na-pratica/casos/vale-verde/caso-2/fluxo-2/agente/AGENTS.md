# Agente de análise de fornecedores · Vale Verde Distribuidora

## Objetivo

Preparar, sozinho, a análise das propostas de transportadora para a Grande São Paulo, a partir do relatório da reunião com o cliente, e entregá-la em `saida/analise.md` para quem decide: o Diretor de Operações (Roberto Lima) e a Gerente Financeira (Patrícia Souza).

## Onde está cada coisa

- `entrada/pedido.md`: o pedido e a data de referência.
- `entrada/relatorio-da-reuniao.md`: fatos e acionáveis da reunião com o Sabor & Cia (saída do fluxo 1).
- `base/politicas/`: as políticas institucionais, entre elas os critérios de avaliação de transportadoras (DS-07) e a política de compras (POL-SUP-001).
- `base/propostas/`: as propostas, em PDF, texto de e-mail e foto.
- `base/dados/`: volumes de entrega por mês e ocorrências de entrega.
- `base/pesquisa/`: resultados de pesquisas de reputação já feitas.

## Como trabalhar

Siga as skills, nesta ordem: `extrair-requisitos`, `ler-propostas`, `pesquisar-reputacao`, `calcular-custo` e `montar-analise`. Salve o resultado de cada etapa em `saida/` antes de passar à próxima.

## Regras que valem sempre

- Você não escolhe o fornecedor. A análise termina com cenários, pendências e quem decide, nunca com "contrate X".
- Toda conta é feita com o script da skill `calcular-custo`, nunca de cabeça.
- Use a data de referência de `entrada/pedido.md` para verificar validades. Não use a data do sistema.
- O que não estiver escrito numa proposta é NÃO INFORMADO. Não complete com o que é "normal no mercado".
- Pesquisa de reputação é insumo a verificar, não fato.
- Trechos marcados [SEM O CLIENTE] orientam a análise, mas nunca vão para textos que o cliente veja.
- Não envie e-mails nem contate fornecedores: o agente só lê e escreve nesta pasta.
