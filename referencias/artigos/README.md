# Artigos do storytelling (Bloco 1)

Artigos usados como fio narrativo da abertura. Eles não são estudados em detalhe: cada um marca um momento da história da IA e introduz um termo.

| Ano | Artigo | Momento da história | Termo que ancora | PDF |
|---|---|---|---|---|
| 1950 | Turing, A. M. *Computing Machinery and Intelligence*. Mind, 59(236), 433–460 | A pergunta "máquinas podem pensar?" e o Jogo da Imitação. A computação vista como mais do que uma ferramenta de especialistas | Inteligência como comportamento observável | [pdf](1950-turing-computing-machinery-and-intelligence.pdf) |
| 1955 | McCarthy, J., Minsky, M., Rochester, N., Shannon, C. *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence* | Nasce o termo "inteligência artificial" e a aposta de que a inteligência pode ser descrita a ponto de uma máquina simulá-la | Inteligência artificial | [pdf](1955-mccarthy-et-al-dartmouth-proposal.pdf) |
| 1958 | Rosenblatt, F. *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain*. Psychological Review, 65(6), 386–408 | A máquina que aprende com exemplos em vez de seguir regras escritas à mão | Aprendizado, rede neural, pesos | [pdf](1958-rosenblatt-the-perceptron.pdf) |
| 1990 | Elman, J. L. *Finding Structure in Time*. Cognitive Science, 14(2), 179–211 | A rede ganha memória do que veio antes (rede recorrente). Treinada só para prever a próxima palavra, ela descobre sozinha categorias como substantivo e verbo | Modelo de sequência, prever o próximo item | [pdf](1990-elman-finding-structure-in-time.pdf) |
| 2003 | Bengio, Y., Ducharme, R., Vincent, P., Jauvin, C. *A Neural Probabilistic Language Model*. JMLR, 3, 1137–1155 | O primeiro modelo de linguagem neural. Cada palavra vira um vetor de números, e palavras parecidas ficam próximas | Modelo de linguagem, embedding, token | [pdf](2003-bengio-et-al-neural-probabilistic-language-model.pdf) |
| 2017 | Vaswani, A. et al. *Attention Is All You Need*. NeurIPS | O Transformer. Modelos de sequência que leem o texto inteiro de uma vez e ponderam o que importa | Token, janela de contexto, atenção | [pdf](2017-vaswani-et-al-attention-is-all-you-need.pdf) |
| 2020 | Brown, T. et al. *Language Models are Few-Shot Learners* (GPT-3). NeurIPS | Um único modelo faz tarefas novas a partir de instruções e exemplos no prompt, sem fine-tuning para cada tarefa | Prompt, contexto, few-shot | [pdf](2020-brown-et-al-language-models-are-few-shot-learners.pdf) |
| 2020 | Dosovitskiy, A. et al. *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale* (ViT). ICLR 2021 | O Transformer sai do texto: a imagem é cortada em quadradinhos de 16×16 pixels, e cada quadradinho vira um token. Citado no slide dos tokens do workshop de professores | Tokens de imagem (patches), multimodalidade | [pdf](2020-dosovitskiy-et-al-an-image-is-worth-16x16-words.pdf) |
| 2022 | Yao, S. et al. *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023 | O modelo deixa de só responder e passa a agir: raciocina, usa uma ferramenta, observa o resultado e continua | Agente, ferramenta | [pdf](2022-yao-et-al-react.pdf) |

Skill e harness não têm um artigo clássico de origem. São conceitos da prática da indústria (2024–25), e o melhor é apresentá-los mostrando uma ferramenta.

## Origem dos arquivos

- Turing: cópia aberta hospedada pela UMBC (`redirect.cs.umbc.edu/courses/471/papers/turing.pdf`)
- Dartmouth: site de John McCarthy em Stanford (`jmc.stanford.edu/articles/dartmouth/dartmouth.pdf`)
- Rosenblatt: cópia aberta hospedada pela UIC (`homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf`)
- Elman: cópia aberta em gwern.net (`gwern.net/doc/ai/nn/rnn/1990-elman.pdf`)
- Bengio: JMLR, acesso aberto (`jmlr.org/papers/volume3/bengio03a/bengio03a.pdf`)
- Vaswani, Brown, Dosovitskiy e Yao: arXiv (1706.03762v7, 2005.14165v4, 2010.11929v1, 2210.03629)

Elman e Bengio são elos de pesquisa e não precisam entrar todos na apresentação.

Turing (*Mind*), Rosenblatt (*Psychological Review*) e Elman (*Cognitive Science*) são cópias de material publicado por editoras. Use-as como referência pessoal e de aula. Para distribuir aos alunos, prefira o link da fonte original.
