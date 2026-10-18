---
name: apresentacao-inteli
description: "Cria ou edita apresentações (slides, deck, aula, encontro, workshop) do professor no padrão Inteli, em HTML de arquivo único com exportação para PDF, na identidade Exec (logo inteli EXEC, boas-vindas e pesquisa) ou Inteli (logo inteli, capa triangular). Use sempre que o pedido envolver montar, alterar ou revisar slides de uma aula ou apresentação neste repositório."
---

# Apresentações Inteli

O design system está em `design-system/`. Leia `design-system/README.md` antes do primeiro slide: lá estão a paleta, a tipografia, os pontos de partida, os ingredientes e os comandos. Cada curso tem um deck só, em `<curso>/apresentacao/deck.html` (por exemplo, `essencial-na-pratica/apresentacao/`; o workshop de professores fica em `professores/apresentacao/`).

## Identidade: Exec ou Inteli

Todo deck tem uma identidade só, do primeiro ao último slide. Se o pedido não deixar claro qual é, pergunte.

| | **Exec** | **Inteli** |
|---|---|---|
| Quando | programas da Educação Executiva (Exec, Pós, MBA), como o *AI for Business* | graduação (aulas do M11) e eventos internos, como o workshop de professores |
| Logo | `logo-exec-escuro-coral.png` em fundo claro, `logo-exec-branco-coral.png` em fundo escuro | `logo-inteli-escuro-coral.png` em fundo claro, `logo-inteli-branco-coral.png` em fundo escuro |
| Abre com | `boas-vindas` (tela oficial, com o wifi) | `capa` (painel roxo e triângulo coral) |
| Fecha com | `pesquisa` (QR code da avaliação do encontro) | o último conteúdo; sem tela de pesquisa |
| Paleta | todas as variáveis, inclusive o verde escuro (`--verde-escuro`, fundo `.verde`), que é a cor do Exec | roxo, verde claro (`--verde`), branco e cinzas, com coral de complemento; evite o verde escuro |

Na identidade Inteli, a capa leva o título em `.titulo-capa` e o autor em `.autor`. Nas aulas do M11, o título é `M11 EC - <tema>` (sem número de encontro) e o autor é `Prof. Nicola`:

```html
<section class="slide capa sem-numero">
  <img class="logo" src="../../design-system/assets/img/logo-inteli-escuro-coral.png" alt="inteli">
  <div class="conteudo">
    <h1 class="titulo-capa">M11 EC - Paginação</h1>
    <p class="autor">Prof. Nicola</p>
  </div>
</section>
```

## Quem conduz

- **O professor é o guia da apresentação.** Ele decide o que entra em cada slide. Proponha, não decida. Se faltar orientação para um slide, sugira uma ou duas opções curtas e pergunte.
- **O slide não compete com o professor.** Apresentações minimalistas: pouca coisa na tela, uma ideia por slide. O que ele vai falar vai em `<aside class="notas">`, nunca no slide.
- **Termos aparecem dentro da explicação, nunca num slide só para eles.** A turma engaja na fala e extrai sozinha os termos importantes. O termo surge no slide em que ele acontece, com destaque discreto: a classe `.rotulo-termo` (Space Mono, maiúsculas, coral) ou um rótulo do próprio diagrama. Exemplos: "atenção" junto dos arcos, "tokens" sobre a frase cortada, "quantum" sobre a barra de tempo. Não use o ponto de partida `termo` para isso.
- **Regra dos 30 segundos:** em até 30 segundos qualquer pessoa da plateia consome tudo o que está na tela e volta a olhar para o professor. Na prática:
  - até ~30 palavras;
  - até 4 blocos;
  - nenhuma lista longa;
  - nenhum parágrafo.

  Se não couber, divida em dois slides ou leve o excedente para as notas.

## Composição: identidade fixa, desenho livre

**Fixo, sempre:**
- a paleta Inteli: só as variáveis do CSS, sem nenhuma cor nova, na proporção da identidade do deck;
- as fontes da marca (Manrope, Platypi, Space Mono);
- o logo da identidade do deck, sem deformação, na variante certa para o fundo e sempre que o slide for "da casa";
- nada abaixo de 28px fora de objetos;
- as verificações automáticas;
- a abertura e o fechamento da identidade (tabela acima);
- **a agenda** (ponto de partida `agenda`, com `.curta` para até 4 itens): o slide volta antes de cada item com o atual destacado (`data-agora`, a partir de 0). Os itens vêm de uma fonte única no script do deck; o marcador é o horário (num dia com grade, como no Exec) ou o número do item, `01`, `02`… Clicar num item leva ao slide de agenda daquele item. Não faça slides de "hoje em ciclos" ou de dinâmica: o professor conduz isso na fala.

**Livre:** a diagramação de cada slide. Há três caminhos, e o critério é a ideia que o slide precisa mostrar, não o modelo que já existe:

1. **Ponto de partida.** Use um layout pronto (`agenda`, `ideia`, `termo`, `painel`, `capitulo-slide`, `imagem`, `citacao`) quando ele servir de verdade. Pode ajustá-lo no slide.
2. **Sob medida.** Desenhe o slide do zero quando a ideia pedir algo próprio: um diagrama, uma linha do tempo, uma comparação visual, uma composição única.
   - Dê ao `<section>` um `id` e um `data-modelo="nome-curto"`, por exemplo `data-modelo="pagina-de-artigo"`.
   - Escreva o CSS no `<style>` do próprio `deck.html`, com seletores começando pelo `#id` do slide.
   - Use as variáveis e os ingredientes do design system: `.moldura`, `.bloco-cinza`, `.esfera`, fundos `escuro`, `verde` (só no Exec), `branco`, e as classes de texto.
   - Não altere o design system para atender a um slide só.
3. **Objeto.** Quando o slide representa algo de fora (a página de um artigo, a tela de um sistema, a saída de um terminal, um documento), o objeto vai dentro de um elemento `.objeto`.
   - Dentro dele valem a aparência e o tamanho de texto do original. Para material impresso, use as fontes de `design-system/assets/fonts/objetos/` (Courier Prime serve bem para terminal e código).
   - Em volta, o slide continua Inteli: fundo, logo e paleta da marca.
   - Mostre só o suficiente para dar a impressão do original, sem virar texto para ler. Pode apagar o excesso em cinza e destacar com a moldura coral.

Veja `design-system/exemplos/exemplo.html`: os slides `capa` e `boas-vindas` abrem um deck de cada identidade, e `#artigo-turing` é um slide sob medida com objeto.

**Conteúdo que se repete vem de uma fonte única.** Quando o mesmo conteúdo aparece em vários slides, o deck guarda esse conteúdo uma vez só, num `<script>` antes do `deck.js`, e monta todos os slides a partir dele. Cada slide declara só o próprio estado, por exemplo `data-ate="1950"`. Assim um título nunca diverge entre as versões. Isso vale, por exemplo, para a agenda, para uma linha do tempo que volta preenchida aos poucos ou para um diagrama que ganha partes. Veja `MARCOS` e `AGENDA` no deck do Essencial na Prática.

**Para contar uma história dentro de um slide,** use passos em vez de duplicar o slide.
- Marque os elementos com `class="passo"` e `data-passo="N"`: o elemento entra no passo N.
- `data-sai="N"` faz o elemento sair no passo N. Use `data-passo="0"` para um elemento que começa visível.
- Para **trocar uma coisa por outra** (uma figura, uma pergunta), ponha as duas no mesmo lugar: a primeira com `data-sai="N"` e a segunda com `data-passo="N"`.
- A seta avança um passo por vez e só depois troca de slide.
- O PDF mostra o último estado de cada slide, e o `qa/` traz uma imagem de cada estado (`slide-NN-passo-K.png`).

Veja o slide `#jogo-da-imitacao` no deck do Essencial na Prática.

**Para mudar o estilo de um elemento a cada passo** (grifar, desfocar, destacar), em vez de fazê-lo entrar ou sair:
- o slide recebe `data-estado="K"` do `deck.js`;
- o CSS do deck usa seletores como `#id[data-estado="2"] .t2`;
- marcadores invisíveis (`<i class="passo" data-passo="1">` … `"N"`) criam os N passos.

**Grifos se acumulam.** Num texto grifado em passos (a página de um artigo, o resumo de uma capa), cada grifo que aparece se junta aos anteriores, que continuam grifados. Não há passo de recapitulação ("todos juntos"): o último grifo já deixa todos à vista. Trechos que a fala apresenta juntos entram no mesmo passo (a mesma classe `.tN`). Veja `.corpo-artigo` e `.resumo-grifos` em `professores/apresentacao/deck.html`.

**Para centralizar na vertical, use flexbox, nunca `top: 50%` + `translateY(-50%)`.** O navegador decide onde quebrar a página do PDF antes de aplicar o transform, então um bloco que começa no meio do slide e passa da borda é cortado entre duas páginas. Use `top: 0; bottom: 0; display: flex; flex-direction: column; justify-content: center`. A verificação acusa esse caso como "caixa passa da borda antes do transform".

**Slides interativos (simuladores).** Prefira um simulador que o professor e a turma exploram livremente a uma sequência de passos que só muda valores. Quando dois slides mostram o mesmo sistema sob ângulos diferentes, eles compartilham o estado: o segundo mostra a situação em que o primeiro parou. Números que mudam com os controles têm casas decimais fixas, para a linha não mudar de largura. Ações viram ícones pequenos perto do que elas afetam, e não botões com texto. Num simulador com vários controles, cada controle e cada parte leva `data-ajuda="o que é"`: o slide ganha o botão `?`, que percorre esses elementos com balões. Uma interação simples (clicar num ponto, digitar uma frase e apertar Enter, trocar entre duas opções) não leva `data-ajuda` nem botão `?`: o professor explica na fala. **Toda sigla num balão é explicada no próprio balão**, mesmo que outro balão já tenha explicado, mas sem poluir o texto: a sigla fica no meio da frase e, embaixo, numa nota de rodapé em fonte menor, vem "SIGLA → significado". O deck define `window.notasAjuda` com o glossário. O build acusa balão de ajuda que saia do slide e exceções de JavaScript, porque um simulador quebrado deixa o slide vazio sem outro sintoma. Exemplo: `../m11-inteli-edge-computing/apresentacoes/encontro-07-paginacao/sims.js`.

## Fluxo: um slide por vez, com o professor no loop

1. Para um curso novo, crie `<curso>/apresentacao/` com um `deck.html` que liga `../../design-system/css/inteli-exec.css` e `../../design-system/js/deck.js` por caminho relativo (copie o esqueleto de `design-system/exemplos/exemplo.html`, ajustando os `../` para a nova profundidade).
2. Escreva **um** slide (ou o pequeno grupo que o professor pediu).
3. Rode a verificação daquele slide:
   `node design-system/tools/deck.mjs <curso>/apresentacao/deck.html --slide N`
4. Corrija todo **erro** e trate todo **aviso** antes de seguir.
5. **Abra a imagem `qa/slide-NN.png` e revise com olhos frescos**, porque as verificações automáticas não pegam tudo:
   - alinhamento e respiro;
   - hierarquia;
   - se a moldura ou a esfera atrapalham o texto;
   - o logo certo para a identidade e para o fundo;
   - se dá para ler em 30 segundos.
6. **Mostre ao professor e peça aprovação** antes de passar ao próximo slide. Diga em uma linha o que o slide faz, se é ponto de partida ou sob medida, e o que ficou nas notas.
7. Ao final, rode o comando sem `--slide` para gerar o `dist/index.html` (o que o site publica) e o PDF, e revise todas as imagens de novo. O CI não gera decks: o `dist/index.html` precisa ser commitado atualizado. Para publicar, siga a skill `cursos-site`.

## Registro de uso e evolução dos templates

Todo build completo atualiza `design-system/USO.md`, que conta quantas vezes cada ponto de partida e cada `data-modelo` sob medida aparecem nos decks.

- **Um slide sob medida que se repete vira candidato a template.** Quando um `data-modelo` aparecer em 2 ou mais slides (marcado com ⭐), sugira ao professor transformá-lo em ponto de partida. Só promova com aprovação. Para promover:
  1. mova o CSS do deck para a seção "Pontos de partida" de `design-system/css/inteli-exec.css`, trocando o `#id` por uma classe;
  2. acrescente o nome à lista `LAYOUTS` de `design-system/tools/deck.mjs`;
  3. documente no `design-system/README.md`;
  4. atualize os slides que o usavam.
- **Um ponto de partida que nunca é usado,** depois de alguns decks, também deve ser mencionado ao professor, que decide se ele sai.
- Use o mesmo `data-modelo` para slides que seguem a mesma ideia de composição, para que a repetição apareça no registro.
- O design system existe em duas cópias com os mesmos arquivos (`exec-inteli-ai-for-business/design-system` e `m11-inteli-edge-computing/design-system`). Ao mudar uma, avise o professor para levar a mudança à outra.

## Regras fixas

- **Pastas e nomes:** um deck por curso, em `<curso>/apresentacao/`, com nomes sem espaços e sem acentos. Não crie pastas datadas nem cópias para versões: o deck é atualizado no lugar, e uma versão antiga se recupera num commit antigo do repositório. Os caminhos são sempre relativos.
- **Coral:** o `--coral` é só para formas. Texto coral usa `--destaque` ou `--coral-texto`, porque o coral puro tem pouco contraste sobre o cinza num projetor.
- **QR codes:** gere-os com `qrencode -s 20 -m 0` a partir do link certo (no Exec, o link oficial da pesquisa do dia) e confira com `zbarimg` que decodificam para ele. Nunca reaproveite a imagem de outro deck ou de outro dia.
- **Privacidade:** nunca coloque em slide nem em nota nomes de alunos, notas, respostas de questionário, de prova ou de formulário, nem dados de empresas da turma ou de parceiros de projeto que não sejam públicos. O repositório é público e o `dist/` é publicado no site: a senha é só uma barreira visual.
