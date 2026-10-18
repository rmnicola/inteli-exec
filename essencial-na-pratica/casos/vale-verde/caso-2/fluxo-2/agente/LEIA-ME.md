# Agente de análise de fornecedores (Antigravity)

A mesma tarefa do Gem `analise-de-fornecedor`, montada para rodar sozinha num agente com ferramentas: o **Google Antigravity**. É a resposta "um agente com ferramentas" do slide do fluxo 2.

## O que mostrar à turma

Compare com o Gem. Lá, a pessoa cola o relatório, anexa as propostas e conduz cada etapa. Aqui, tudo de que o agente precisa já está na pasta:

```
agente/
├── AGENTS.md                ← as regras do workspace: objetivo, onde está cada coisa, o que o agente não pode fazer
├── .agents/skills/          ← uma skill por etapa, carregada só quando é usada
│   ├── extrair-requisitos/
│   ├── ler-propostas/          (+ o modelo da tabela)
│   ├── pesquisar-reputacao/    (+ o formato do relatório)
│   ├── calcular-custo/         (+ um script em Python que faz as contas)
│   └── montar-analise/         (+ o modelo da análise final)
├── entrada/                 ← o pedido do Roberto (com a data) e o relatório do fluxo 1
├── base/                    ← a base de conhecimento: políticas, propostas, planilhas e pesquisas já feitas
└── saida/                   ← onde o agente escreve cada etapa e a análise final
```

Os pontos para destacar:

- **`AGENTS.md` é o system prompt da pasta.** As regras críticas (não escolhe, conta só com script, usa a data do pedido) valem em todas as etapas.
- **As skills seguem o padrão que a turma já viu:** nome e descrição no topo, que ficam sempre na janela; o resto só entra quando a skill é usada.
- **O script de custo é a "IA com código"** do slide: a conta sai certa porque não é prevista pelo modelo. Dá para rodá-lo ao vivo:
  `python3 .agents/skills/calcular-custo/scripts/custo.py --por-km 6.50 --km-rota 210 --entregas-rota 18`
- **O que continua com a pessoa:** o agente não envia e-mail, não contata fornecedor e não escolhe. A decisão fica com Roberto e Patrícia.

## Por que não dá para testar de verdade

As transportadoras são fictícias: uma pesquisa real na web não acharia nada sobre elas. Por isso `base/pesquisa/` já traz o relatório de reputação, como se fosse uma pesquisa feita antes, e a skill `pesquisar-reputacao` começa por ele. Com fornecedores reais, a mesma skill faria a busca e guardaria o relatório ali.

## Como abrir

Abra a pasta `agente/` como workspace no Antigravity e peça: "Faça a análise pedida em entrada/pedido.md." O resultado esperado é o mesmo do Gem: `../skill/resultado-esperado.md`.

## De onde vêm os arquivos de `base/`

São cópias geradas pelo `build.py` do caso Vale Verde, a partir de `politicas-institucionais/fontes/` e de `caso-2/fluxo-2/`. Para mudar um documento, edite a fonte e rode `python3 build.py`.
