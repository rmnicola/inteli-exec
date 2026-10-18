# Inteli Exec · cursos de Rodrigo Nicola

Apresentações e materiais dos cursos da Educação Executiva do Inteli. Cada curso é um produto, com pasta, página e senha próprias.

**Site:** https://rmnicola.github.io/inteli-exec/ — publicado automaticamente a cada push em `main`.

## Estrutura

```
cursos.json                      fonte única do site: cursos, senhas (hash) e materiais
essencial-na-pratica/            AI for Business: Essencial na Prática
  apresentacao/                  deck.html (fonte) e dist/index.html (build publicado)
  builder-log/                   folha preenchível (gerar.py → builder-log.pdf)
  casos/vale-verde/              caso fictício da manhã
ferramentas-em-acao/             AI for Business: Ferramentas em Ação (em preparação)
professores/apresentacao/        workshop de uso de IA para professores (página oculta)
design-system/                   identidade Inteli dos slides e ferramenta de build
site/                            design system das páginas do site (ver site/DESIGN.md)
tools/gerar_site.py              gera _site/ a partir de cursos.json
.agents/skills/                  skills (Claude Code, Codex, OpenCode, Gemini); .claude/skills é link para cá
```

## Fluxo de trabalho

1. Edite o deck do curso e gere o build:
   `node design-system/tools/deck.mjs essencial-na-pratica/apresentacao/deck.html`
2. Registre ou ajuste o curso em `cursos.json`. Enquanto estiver em andamento, use `"rascunho": true`.
3. Veja a prévia local, com rascunhos: `python3 tools/gerar_site.py --previa` e abra http://localhost:8000
4. Para publicar, faça commit e push em `main`.

Cada curso tem um deck só, atualizado no lugar. Para ver uma versão antiga, vá a um commit antigo: `git log -- essencial-na-pratica/apresentacao/deck.html`.

## Senhas e páginas ocultas

Cada curso tem a própria senha; só o hash SHA-256 fica em `cursos.json` (`senha_sha256`). Cursos com `"oculto": true` ficam fora do índice e pedem aos buscadores que não os indexem; só quem tem o link chega a eles.

As duas coisas são barreiras visuais: o repositório é público, e os arquivos (inclusive a pasta `professores/`) podem ser lidos aqui no GitHub.

## Fora do repositório

Ficam só na máquina do professor (ver `.gitignore`): dados de turma (`essencial-na-pratica/03-OUT/`), descritivos `.docx` e suas conversões, o Learning Log Toolkit, o template `.pptx` e os PDFs dos artigos de `referencias/artigos/`.

## Referências internas

- Skill de apresentações: [`.agents/skills/apresentacao-inteli/SKILL.md`](.agents/skills/apresentacao-inteli/SKILL.md)
- Skill do site: [`.agents/skills/cursos-site/SKILL.md`](.agents/skills/cursos-site/SKILL.md)
- Design system dos slides: [`design-system/README.md`](design-system/README.md)
- Caso Vale Verde: [`essencial-na-pratica/casos/vale-verde/README.md`](essencial-na-pratica/casos/vale-verde/README.md)
- Artigos do storytelling: [`referencias/artigos/README.md`](referencias/artigos/README.md)
