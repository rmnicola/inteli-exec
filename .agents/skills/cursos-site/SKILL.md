---
name: cursos-site
description: "Mantém o site dos cursos Inteli Exec publicado no GitHub Pages a partir deste repositório: registra cursos em cursos.json, define a senha de cada curso, esconde cursos (como o de professores), lista materiais para baixar, ajusta o estilo do site com as regras de contraste, mostra a prévia local e publica com commit e push quando o professor pedir. Use sempre que o pedido envolver o site, a página de um curso, senhas, materiais para os alunos, prévia, publicação, commit ou push deste projeto."
---

# Site dos cursos

Este projeto é o repositório público https://github.com/rmnicola/inteli-exec. Cada push em `main` publica https://rmnicola.github.io/inteli-exec/ pelo workflow `.github/workflows/pages.yml`, que verifica o contraste e roda `tools/gerar_site.py`.

O site reúne vários produtos do Inteli Exec. Cada curso tem a própria página, em `/<slug>/`, e a própria senha.

## Regra principal: discutir antes de publicar

Commit e push publicam. Trabalhe localmente, mostre a prévia e só faça commit/push quando o professor pedir. Na dúvida, pergunte.

```sh
python3 tools/gerar_site.py --previa     # inclui rascunhos; serve em http://localhost:8000
```

Rode a prévia em segundo plano e não inicie um segundo servidor: os dois disputam `_site/`.

## Onde fica cada coisa

| Caminho | Papel |
|---|---|
| `cursos.json` | fonte única do site: dados gerais e lista de cursos, cada um com o hash da sua senha |
| `<curso>/apresentacao/` | `deck.html` (fonte) e `dist/index.html` (build publicado). Um deck por curso, atualizado no lugar |
| `<curso>/…` | materiais do curso (por exemplo, `essencial-na-pratica/builder-log/builder-log.pdf`) |
| `site/estilo.css`, `site/DESIGN.md` | design system das páginas: tokens, componentes, regras de contraste |
| `tools/gerar_site.py` | gera `_site/`: índice, página de cada curso, preparação, tela de senha |
| `tools/verificar_contraste.py` | regras C1–C4 e T1; falha bloqueia a publicação |

## Sem versões lado a lado

Não crie pastas datadas nem cópias de decks ou materiais para guardar versões. O curso tem um deck só, que é atualizado; uma versão antiga se recupera num commit antigo (`git log -- <curso>/apresentacao/deck.html`, `git show <commit>:<caminho>`).

## Registrar um curso

Em `cursos.json`, cada curso tem:

| Campo | Uso |
|---|---|
| `slug` | URL: `/<slug>/`. Não mude depois de divulgado |
| `pasta` | pasta do curso na raiz do repositório. Curso sem `pasta` aparece como "em breve" |
| `senha_sha256` | hash da senha do curso (veja "Senhas") |
| `oculto` | `true`: fora do índice, com `noindex` em todas as páginas. Só quem tem o link chega |
| `rascunho` | `true` enquanto estiver em andamento: fica fora do site publicado, aparece na prévia |
| `titulo`, `subtitulo` | textos do índice e da página |
| `proposito`, `objetivos` | frase de propósito e objetivos de aprendizagem (aceitam `código`, **forte**, *ênfase*) |
| `apresentacao` | arquivo relativo à pasta, normalmente `apresentacao/dist/index.html`; vira `apresentacao.html` |
| `materiais` | lista de `{rotulo, tipo, arquivo}` (arquivo da pasta, baixado) ou `{rotulo, tipo, link}` |

Um `preparacao.json` na pasta do curso vira `/<slug>/preparacao/`, um passo a passo com comandos copiáveis (formato no docstring de `gerar_preparacao` e no projeto `pecege-ons`).

O CI não roda o build dos decks (precisa de Chromium): `dist/index.html` precisa estar atualizado e commitado.

## Senhas

Só o hash SHA-256 fica em `cursos.json`. Nunca escreva uma senha em texto em nenhum arquivo do repositório, que é público: pergunte ao professor quando precisar dela. A comparação ignora maiúsculas e espaços nas pontas, então gere o hash da senha em minúsculas:

```sh
printf %s '<senha>' | sha256sum
```

Cada curso guarda a liberação no navegador pela chave do próprio hash: entrar num curso não libera os outros.

A tela é uma barreira visual: o repositório e os links diretos dos arquivos continuam públicos, e a pasta `professores/` aparece no GitHub. Diga isso ao professor sempre que o assunto for privacidade.

## Estilo do site

Minimalista e monoespaçado, o mesmo do site `pecege-ons`. Leia `site/DESIGN.md` antes de mexer. Toda cor nova vira token em `site/estilo.css`, ganha um par em `PARES` no verificador e deve passar em:

```sh
python3 tools/verificar_contraste.py
```

Confira as páginas na prévia em 1280px e 390px. Para capturar uma página atrás da senha, digite a senha no campo `#portao-senha` antes da captura.

## Publicar (somente quando o professor pedir)

1. Retire `"rascunho"` do curso, se for o caso, e confira a prévia.
2. `python3 tools/verificar_contraste.py` e `python3 tools/gerar_site.py` sem erros.
3. `git status`: confirme que nada privado entra (lista de alunos, respostas de questionário, `.docx`, `.pptx`, `.xlsx`, `qa/`, PDFs de `dist/`, toolkit e artigos são ignorados). Use `git add` com caminhos explícitos quando houver alterações fora do escopo.
4. Commit em português, descrevendo o que muda para quem usa o site, com a linha de coautoria da sessão. Autor: Rodrigo Nicola.
5. `git push origin main` e confira o workflow (API pública: `https://api.github.com/repos/rmnicola/inteli-exec/actions/runs`).
