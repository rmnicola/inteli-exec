# Skill: da reunião semanal ao e-mail de acompanhamento

Gabarito do fluxo da Helena (slide 36 e prática 3). É o arquivo que o agente deve criar na pasta da persona. Os cinco campos são os mesmos em qualquer aplicativo: **nome, quando usar, etapas, formato da saída e o que nunca fazer sozinho**.

```markdown
---
name: acompanhamento-da-reuniao
description: Transforma a transcrição da reunião semanal das lojas em fatos, pendências com dono e prazo, e um e-mail de acompanhamento. Use quando houver um arquivo de transcrição de reunião na pasta.
---

# Acompanhamento da reunião semanal

## Quando usar
Quando chegar um arquivo de transcrição de reunião na pasta `entrada/`. Uma reunião por vez.

## Etapas

1. **Ler a transcrição inteira antes de escrever qualquer coisa.** Anote o horário de cada
   trecho relevante: ele vai em todas as tabelas.

2. **Separar fatos de opiniões.**
   - É **fato**: número relatado, decisão tomada com acordo das pessoas, acontecimento descrito.
   - É **opinião**: impressão, explicação sem dado, previsão, "eu acho".
   - Uma frase dita com voz de fato mas sem número na reunião é **opinião**. Não promova
     opinião a fato e não apague a opinião: ela vai numa lista à parte, com o motivo.

3. **Listar as pendências.** Para cada uma: o que é, **quem** ficou responsável e **até quando**.
   - Se a reunião não disse quem, escreva **SEM RESPONSÁVEL** em maiúsculas. Nunca chute.
   - Se não disse quando, escreva **SEM PRAZO**.
   - Quando o mesmo prazo aparecer de duas formas na conversa, registre as duas e marque
     **PRAZO AMBÍGUO**, com os dois horários da transcrição. Não escolha por conta própria.
   - Converta "quinta", "fim da semana" e afins para a data real, usando a data da reunião,
     e mostre a conta: "quinta → 12/11/2026".

4. **Destacar o que ficou sem dono.** Uma seção própria, antes do e-mail, só com as pendências
   SEM RESPONSÁVEL e as de PRAZO AMBÍGUO. É o que a Helena precisa resolver hoje.

5. **Redigir o e-mail de acompanhamento** para quem participou, no formato abaixo.

6. **Gravar o resultado** em `saida/acompanhamento-<data-da-reuniao>.md` e dizer, na conversa,
   o que ficou sem dono.

## Formato da saída

Um arquivo com quatro partes, nesta ordem:

1. `## Fatos` — tabela: fato | horário.
2. `## Opiniões (fora da lista de fatos)` — tabela: frase | quem disse | por que não é fato.
3. `## Pendências` — tabela: pendência | quem | até quando | horário.
4. `## Precisa de decisão da Helena` — lista do que está SEM RESPONSÁVEL ou com PRAZO AMBÍGUO.
5. `## E-mail de acompanhamento` — assunto em uma linha e corpo de até 200 palavras:
   abertura de uma frase, a lista das pendências com dono e prazo, e um último parágrafo
   com o que ainda precisa de dono. Tom direto, sem "venho por meio desta".

## O que nunca fazer sozinho

- **Nunca inventar responsável ou prazo.** Faltou, escreve SEM RESPONSÁVEL ou SEM PRAZO.
- **Nunca escolher entre dois prazos** que a reunião deixou ambíguos.
- **Nunca transformar opinião em fato**, mesmo quando ela parece razoável.
- **Nunca enviar o e-mail.** O arquivo é um rascunho: quem envia é a Helena.
- Se a transcrição parecer ter errado um nome ou um número, aponte, não corrija em silêncio.
```
