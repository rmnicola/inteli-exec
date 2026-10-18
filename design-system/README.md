# Design system Inteli (apresentações em HTML)

Identidade visual extraída do `template/Template Apresentação - Inteli.pptx` e das telas oficiais da Educação Executiva (`PROJEÇÃO TELAS - Inteli Exec`). O mesmo design system atende a duas identidades; o deck escolhe uma e a mantém do começo ao fim:

| Identidade | Quando | Logo | Abre com | Fecha com |
|---|---|---|---|---|
| **Exec** | Programas da Educação Executiva (Exec, Pós, MBA) | `logo-exec-*.png` (inteli EXEC) | `boas-vindas` | `pesquisa` |
| **Inteli** | Graduação e eventos internos (aulas do M11, workshop de professores) | `logo-inteli-*.png` (inteli) | `capa` (painel roxo e triângulo coral) | o último conteúdo |

A cópia em `../m11-inteli-edge-computing/design-system` tem os mesmos arquivos.

```
design-system/
├── css/inteli-exec.css   ← variáveis da marca + layouts (a fonte da verdade visual)
├── js/deck.js            ← navegação pelo teclado e escala para a tela
├── assets/fonts/         ← Manrope, Platypi, Space Mono (OFL, do Google Fonts)
│   └── objetos/          ← EB Garamond, só para representar material impresso (não é fonte da marca)
├── assets/img/           ← logos inteli e inteli EXEC, 4 variantes cada, e esfera de pontos
├── tools/deck.mjs        ← gera o arquivo único, o PDF, as imagens e roda as verificações
├── exemplos/exemplo.html ← pontos de partida e um slide sob medida (#artigo-turing)
└── USO.md                ← quantas vezes cada tipo de slide foi usado (gerado pelo build)
```

## Como usar

1. Crie uma pasta para o deck, com nome sem espaços nem acentos. O deck de um curso fica em `<curso>/apresentacao/` (exemplo: `essencial-na-pratica/apresentacao/`). Não guarde versões antigas lado a lado: a versão anterior está no histórico do git.
2. Escreva `deck.html` nela, ligando o CSS e o JS do design system por caminho relativo (veja `exemplos/exemplo.html`).
3. Gere e verifique:

   ```
   node design-system/tools/deck.mjs <curso>/apresentacao/deck.html            # o deck inteiro
   node design-system/tools/deck.mjs <curso>/apresentacao/deck.html --slide 7  # só um slide
   ```

**O que o comando gera:**

| Arquivo | O que é |
|---|---|
| `dist/index.html` | **Arquivo único**, com CSS, JS, fontes e imagens embutidos. Funciona offline e serve direto no GitHub Pages |
| `dist/<pasta>.pdf` | Um slide por página, em 16:9 |
| `qa/slide-NN.png` | Uma imagem de cada slide, para revisão visual. Não publicar |
| `qa/relatorio.json` | Resultado das verificações |

**Para apresentar:** abra `dist/index.html` no navegador.

| Tecla | Ação |
|---|---|
| L, →, espaço | Avança: o próximo passo da animação ou o próximo slide |
| H, ← | Volta um passo |
| J, ↓ | Pula para o próximo slide, ignorando as animações (aparece completo) |
| K, ↑ | Pula para o slide anterior, ignorando as animações (aparece completo) |
| F | Tela cheia |
| `#N` no fim da URL | Abre no slide N |

**Slides interativos.** Um slide pode ter controles (botões, controles deslizantes, campos). Enquanto um campo ou controle deslizante está em foco, as teclas ficam com ele; `Esc` devolve o teclado à navegação. Marque os controles com `data-ajuda="o que é"`. Toda sigla num balão é explicada no próprio balão, mesmo que outro já explique, numa nota de rodapé em fonte menor ("TLB → translation lookaside buffer…"): defina `window.notasAjuda(texto)` no deck, com um glossário, e o texto do balão fica limpo. O build verifica que nenhum balão sai do slide. Use `data-ajuda-ordem` se a ordem do HTML não servir: o slide ganha um botão `?` no canto que percorre esses elementos com um balão explicativo. Um script do deck pode reagir aos passos observando o atributo `data-estado` do slide (veja `../m11-inteli-edge-computing/apresentacoes/encontro-07-paginacao/sims.js`).

## Paleta

| Variável | Cor | Uso |
|---|---|---|
| `--cinza-claro` | `#e6eaeb` | Fundo padrão |
| `--roxo` | `#2e2640` | Texto padrão. Fundo dos slides `.escuro` e dos painéis |
| `--verde-escuro` | `#066d73` | Cor do segmento MBA & EXEC. Fundo dos slides `.verde` |
| `--coral` | `#ff4545` | **Só formas:** moldura, seta, contornos |
| `--coral-texto` | `#d63333` | Coral como **texto** sobre fundo claro. O original tem contraste de 2,8 sobre o cinza, pouco para um projetor |
| `--verde` | `#89cea5` | Destaque de texto sobre o verde escuro |
| `--lilas`, cinzas | | Complementos |

Na identidade **Inteli** (segmento Graduação do template), a proporção é roxo, verde claro (`--verde`), branco e cinzas, com o coral de complemento. O verde escuro é a cor do Exec: evite-o.

## Tipografia

A Azurio é proprietária. No lugar dela vai a Platypi, como o próprio template orienta.

| Classe | Fonte | Tamanho | Uso |
|---|---|---|---|
| `.capitulo` | Platypi, maiúsculas | 96px | Aberturas e capítulos |
| `.titulo` | Manrope 700 | 64px | Título do slide |
| `.frase` (em `.ideia`) | Manrope 700 | 72px | A ideia única do slide |
| `.subtitulo` | Manrope 400 | 40px | |
| `.texto` | Manrope 400 | 34px | Texto corrido, curto |
| `.destaque` | Space Mono 700, maiúsculas, coral | 28px | Rótulo pontual. Não abusar |
| `.legenda` | Manrope | 28px | Fonte, data, autor |

**Nada na tela fica abaixo de 28px.** O número do slide é a única exceção.

## Composição dos slides

**A identidade é fixa e a diagramação é livre.** Há três caminhos:

**1. Pontos de partida.** São layouts recorrentes, prontos para usar ou ajustar. Cada um é uma classe em `<section class="slide …">`.

| Classe | Quando usar |
|---|---|
| `capa` | **Abertura da identidade Inteli:** painel roxo, triângulo coral, logo, `.titulo-capa` e `.autor` alinhados à direita |
| `boas-vindas` | **Abertura da identidade Exec:** a tela oficial de abertura (BEM-VINDOS! PROGRAMA …, com o wifi) |
| `pesquisa` | **Fechamento da identidade Exec:** o QR code da avaliação do encontro, que fecha o deck |
| `agenda` | A lista de itens da aula, que volta a cada parte com o item atual destacado (`data-agora`, a partir de 0). O marcador é o horário ou o número do item; `.curta` aumenta a fonte para listas de até 4 itens. Os itens vêm de uma fonte única no deck. Clicar num item leva ao slide de agenda daquele item |
| `capitulo-slide` | Abre uma parte da aula. Número em Space Mono e título com moldura |
| `ideia` | Uma frase só, grande |
| `termo` | Uma palavra grande com uma definição. **Não** use como slide de glossário: os termos da aula aparecem dentro da explicação, com `.rotulo-termo` |
| `painel` | Texto à esquerda e painel roxo (ou `.lado.verde`) à direita |
| `imagem` | Uma imagem ou figura ocupando o slide |
| `citacao` | Uma citação e o autor |

**2. Sob medida.** É um slide desenhado do zero para uma ideia específica.
- O `<section>` recebe um `id` e um `data-modelo="nome-curto"`.
- O CSS vai no `<style>` do próprio deck, com seletores pelo `#id`.
- Ele usa as variáveis e os ingredientes abaixo.

**3. Objeto.** É algo de fora representado no slide, como a página de um artigo ou uma tela de sistema, dentro de um `.objeto`. Dentro do objeto valem a aparência e o tamanho de texto do original, e as verificações de tamanho, contraste e palavras não se aplicam. Em volta, o slide continua Inteli.

**Ingredientes para qualquer slide:**

| Ingrediente | Para quê |
|---|---|
| Fundos `escuro`, `verde`, `branco` | Acrescentados à classe do slide. Trocam as cores de texto e de destaque. O `verde` usa o verde escuro, cor do segmento Exec; na identidade Inteli prefira `escuro` e `branco` |
| Classes de texto | `.capitulo`, `.titulo`, `.subtitulo`, `.destaque`, `.legenda`, `.texto` |
| `.rotulo-termo` | O nome de um conceito, discreto, no slide em que ele acontece (Space Mono, maiúsculas, coral) |
| `.moldura` | Contorno coral em volta de uma palavra-chave. No máximo uma por slide |
| `.bloco-cinza` | Retângulo translúcido, grafismo do template |
| `img.esfera` | Textura de pontos, para slides verdes |
| `.sangra` | Marca um elemento decorativo que pode passar da borda do slide |
| `img.logo` | Canto superior direito. Fundo claro: `logo-*-escuro-coral.png`; fundo escuro: `logo-*-branco-coral.png`, com `*` = `exec` ou `inteli` conforme a identidade |
| `aside.notas` | O que o professor vai falar. **Nunca aparece no slide** |

Os logos não podem ser deformados nem recoloridos. Use só os arquivos de `assets/img/`.

**Registro de uso.** Todo build completo atualiza o `USO.md`.
- Um `data-modelo` sob medida que aparece 2 vezes ou mais é marcado como candidato a template.
- Um ponto de partida que nunca aparece é candidato a sair.
- A decisão é sempre do professor. Ao promover, acrescente o nome à lista `LAYOUTS` em `tools/deck.mjs`.

## Verificações automáticas (`tools/deck.mjs`)

**Erros** (o comando sai com código 1):
- elemento fora da área do slide;
- texto vazando da caixa ou da área útil;
- fonte abaixo de 28px;
- fonte que não carregou;
- textos sobrepostos;
- imagem que não carregou;
- contraste abaixo de 3 (texto grande) ou de 4,5 (texto menor).

- caixa que passa da borda do slide antes do transform: quebraria o PDF (ex.: `top: 50%` + `translateY(-50%)`; centralize com flexbox).

**Avisos** (a regra dos 30 segundos e o registro):
- mais de 30 palavras no slide (ajustável por slide com `data-max-palavras`);
- mais de 4 blocos de conteúdo;
- slide sob medida sem `data-modelo`.

As verificações não substituem a revisão visual das imagens em `qa/`.

## Publicação no GitHub Pages

O `dist/` de cada deck já está pronto para publicar: é um `index.html` que não depende de nada de fora, mais o PDF. Num repositório de aulas, basta copiar a pasta para lá (por exemplo, `aulas/2026-10-03-essencial-na-pratica/`) e adicionar um link na página inicial. **Nunca publique `qa/` nem materiais com dados de alunos.**

## Documentos impressos

Roteiros, questionários, gabaritos e folhas usam `css/inteli-doc.css` (A4, mesma paleta e fontes) e são gerados por `tools/doc.sh <documento.html> [páginas esperadas]`, que imprime o PDF com o Chromium e salva uma imagem por página em `qa/`. Exemplo: `../m11-inteli-edge-computing/apresentacoes/encontro-07-paginacao/impressos/`, e a skill `documento-inteli` daquele repositório descreve os componentes.
