# Inteli Exec

Cursos de Rodrigo Nicola na Educação Executiva do Inteli. Cada curso é um produto, com pasta própria na raiz:

| Pasta | Curso |
|---|---|
| `essencial-na-pratica/` | AI for Business: Essencial na Prática |
| `ferramentas-em-acao/` | AI for Business: Ferramentas em Ação |
| `professores/` | workshop de uso de IA para professores (página oculta no site) |

Para criar, editar ou revisar apresentações, leia e siga `.agents/skills/apresentacao-inteli/SKILL.md` e `design-system/README.md`. Cada curso tem um deck só, em `<curso>/apresentacao/`, atualizado no lugar: não crie pastas datadas nem cópias para guardar versões. Uma versão antiga se recupera num commit antigo.

Este projeto é o repositório público github.com/rmnicola/inteli-exec; cada push em `main` publica o site (https://rmnicola.github.io/inteli-exec/). Para o site, as senhas, a prévia e a publicação, leia `.agents/skills/cursos-site/SKILL.md`. Mostre a prévia e só faça commit/push quando o professor pedir. Nunca adicione arquivos privados listados no `.gitignore` (lista de alunos, respostas de questionário, documentos internos).

O `learning-log-toolkit.md` é a fonte principal do Learning Log e prevalece sobre o descritivo do programa quando os dois divergem. Ele e os descritivos são de uso interno e ficam fora do repositório.

As skills ficam em `.agents/skills/`, lidas por Codex, OpenCode e Gemini; `.claude/skills` é um link para essa pasta e `GEMINI.md` é um link para este arquivo. Edite sempre `.agents/skills/` e não crie cópias por harness. Escreva skills sem recursos exclusivos de um harness (como `$ARGUMENTS` ou `argument-hint`).
