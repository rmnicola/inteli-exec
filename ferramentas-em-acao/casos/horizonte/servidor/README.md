# Servidor da Companhia Horizonte

Uma API fictícia de reembolsos e um servidor MCP na frente dela, para o bloco 6 do *AI for Business: Ferramentas em Ação*. Os dados são os arquivos fictícios da oficina do dia 1: a política de reembolso (R1 a R6) e os pedidos da semana (R-101 a R-108). O pedido R-109 foi acrescentado para a demonstração de prompt injection.

O servidor roda no Cloudflare Workers, no plano gratuito. Quem participa do curso não instala nada: só cola a URL do MCP no aplicativo.

## As duas camadas

Tudo está em `src/index.js`, separado de propósito:

| Camada | Caminho | Para quem | O que faz |
|---|---|---|---|
| API REST | `/api/...` | programadores | devolve os pedidos, a política e o cadastro de fornecedores em JSON |
| MCP | `/mcp` | a IA | descreve a API como ferramentas, com nome, descrição e parâmetros, e repassa cada chamada para a API |

O MCP não tem dados próprios: cada ferramenta vira um pedido à API (veja `pedidoParaApi`).

| Ferramenta MCP | Rota da API | Observação |
|---|---|---|
| `listar_pedidos` | `GET /api/pedidos?categoria=` | |
| `obter_pedido` | `GET /api/pedidos/R-103` | |
| `ler_politica` | `GET /api/politica` | |
| `consultar_fornecedor` | `GET /api/fornecedores/<cnpj>` | para o verificador conferir o comprovante; o CNPJ do R-106 está baixado |
| `registrar_decisao` | `POST /api/pedidos/R-103/decisao` | ação de escrita, simulada: nada é gravado, e todos veem sempre o mesmo estado |

## Ligar no aplicativo

Endereço publicado: `https://horizonte-reembolsos.rmnicola.workers.dev/mcp`.

**Claude Code:** na pasta do projeto, um `.mcp.json`:

```json
{ "mcpServers": { "horizonte": { "type": "http", "url": "https://horizonte-reembolsos.rmnicola.workers.dev/mcp" } } }
```

Ou, na linha de comando: `claude mcp add --transport http horizonte https://horizonte-reembolsos.rmnicola.workers.dev/mcp`.

**Codex:** no `.codex/config.toml` do projeto (em pasta marcada como confiável) ou no `~/.codex/config.toml`:

```toml
[mcp_servers.horizonte]
url = "https://horizonte-reembolsos.rmnicola.workers.dev/mcp"
```

## Rodar e publicar (professor)

Requer Node. Na primeira vez, `npx wrangler login` abre o navegador para entrar na conta da Cloudflare.

```sh
npx wrangler dev      # roda em http://127.0.0.1:8787, sem publicar
npx wrangler deploy   # publica em https://horizonte-reembolsos.rmnicola.workers.dev
```

A raiz do servidor (`/`) lista as rotas. Todos os nomes, valores e CNPJs são fictícios.
