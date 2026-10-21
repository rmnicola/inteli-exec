#!/usr/bin/env python3
"""Gera o builder-log.pdf: uma folha frente e verso, preenchível, na identidade Inteli Exec.

Requer reportlab e pypdf. Os campos seguem o padrão de tools/formulario.py. As fontes (Manrope, Platypi, Space Mono, OFL) estão em fontes/,
convertidas dos woff2 do design-system.
"""
import sys
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

AQUI = Path(__file__).resolve().parent
LOGO = AQUI.parents[1] / "design-system/assets/img/logo-exec-escuro-coral.png"
SAIDA = AQUI / "builder-log.pdf"
sys.path.insert(0, str(AQUI.parents[1] / "tools"))
from formulario import campo, marca  # noqa: E402  padrão dos campos preenchíveis

for nome in ["Manrope-Regular", "Manrope-SemiBold", "Manrope-ExtraBold", "Platypi-Medium", "SpaceMono-Regular", "SpaceMono-Bold"]:
    pdfmetrics.registerFont(TTFont(nome, str(AQUI / "fontes" / f"{nome}.ttf")))

ROXO = HexColor("#2e2640")
CORAL = HexColor("#ff4545")
CORAL_TEXTO = HexColor("#d63333")
VERDE = HexColor("#066d73")
CINZA_CLARO = HexColor("#e6eaeb")
TEXTO_SUAVE = HexColor("#5d5870")

W, H = A4
M = 42  # margem


def texto(c, x, y, s, fonte="Manrope-Regular", tam=10, cor=ROXO):
    c.setFont(fonte, tam)
    c.setFillColor(cor)
    c.drawString(x, y, s)


def paragrafo(c, x, y, s, largura, fonte="Manrope-Regular", tam=9.5, cor=TEXTO_SUAVE, entrelinha=1.35):
    """Escreve texto com quebra de linha simples; devolve o y depois da última linha."""
    c.setFont(fonte, tam)
    c.setFillColor(cor)
    linha = ""
    for palavra in s.split():
        teste = (linha + " " + palavra).strip()
        if pdfmetrics.stringWidth(teste, fonte, tam) > largura:
            c.drawString(x, y, linha)
            y -= tam * entrelinha
            linha = palavra
        else:
            linha = teste
    if linha:
        c.drawString(x, y, linha)
        y -= tam * entrelinha
    return y


def selo(c, x, y, rotulo, cor):
    """Etiqueta em Space Mono: HOJE (verde) ou ANTES DA MENTORIA (coral). y = base do texto."""
    tam = 7.5
    larg = pdfmetrics.stringWidth(rotulo, "SpaceMono-Bold", tam) + 10
    c.setFillColor(cor)
    c.roundRect(x, y - 3.5, larg, 13, 3, stroke=0, fill=1)
    texto(c, x + 5, y, rotulo, "SpaceMono-Bold", tam, white)
    return larg


def opcoes(c, grupo, x, y, valores):
    """Botões de opção (só um marcado), com o rótulo ao lado."""
    for v in valores:
        marca(c, grupo, v.lower().replace(" ", "-"), x, y - 3, v)
        texto(c, x + 17, y, v, "Manrope-SemiBold", 10)
        x += 17 + pdfmetrics.stringWidth(v, "Manrope-SemiBold", 10) + 22


def cabecalho(c, pagina):
    c.drawImage(str(LOGO), W - M - 84, H - M - 22, width=84, height=84 * 321 / 914, mask="auto")
    texto(c, M, H - M - 8, "AI FOR BUSINESS · ESSENCIAL NA PRÁTICA · 03/10/2026", "SpaceMono-Bold", 7.5, CORAL_TEXTO)
    if pagina == 1:
        texto(c, M, H - M - 44, "Builder log", "Platypi-Medium", 32, ROXO)
    else:
        texto(c, M, H - M - 30, "Builder log", "Platypi-Medium", 18, ROXO)


def rodape(c, pagina):
    c.setStrokeColor(CINZA_CLARO)
    c.setLineWidth(1)
    c.line(M, M - 4, W - M, M - 4)
    texto(c, M, M - 16, "Inteli Exec · AI for Business", "Manrope-Regular", 7.5, TEXTO_SUAVE)
    texto(c, W - M - 10, M - 16, str(pagina), "SpaceMono-Regular", 7.5, TEXTO_SUAVE)


def titulo_secao(c, y, titulo, apoio=None):
    c.setFillColor(CORAL)
    c.rect(M, y - 2, 4, 16, stroke=0, fill=1)
    texto(c, M + 12, y, titulo, "Manrope-ExtraBold", 15, ROXO)
    if apoio:
        return paragrafo(c, M + 12, y - 16, apoio, W - 2 * M - 12) - 4
    return y - 22


def pagina_1(c):
    cabecalho(c, 1)
    y = H - M - 78
    # identificação
    texto(c, M, y, "Nome", "Manrope-SemiBold", 9, TEXTO_SUAVE)
    texto(c, M + 300, y, "Empresa", "Manrope-SemiBold", 9, TEXTO_SUAVE)
    campo(c, "nome", M, y - 26, 285, 20)
    campo(c, "empresa", M + 300, y - 26, W - 2 * M - 300, 20)

    # instruções
    y -= 46
    caixa_h = 66
    c.setFillColor(CINZA_CLARO)
    c.roundRect(M, y - caixa_h, W - 2 * M, caixa_h, 8, stroke=0, fill=1)
    texto(c, M + 14, y - 18, "Como usar esta folha", "Manrope-ExtraBold", 10.5, ROXO)
    larg = selo(c, M + 14, y - 36, "HOJE", VERDE)
    paragrafo(c, M + 22 + larg, y - 36, "Escreva as três perguntas e descreva seu projeto e o impacto esperado.", W - 2 * M - 40 - larg, "Manrope-Regular", 9.5, ROXO)
    larg = selo(c, M + 14, y - 56, "ANTES DA MENTORIA", CORAL_TEXTO)
    paragrafo(c, M + 22 + larg, y - 56, "Responda às perguntas e preencha a atualização do projeto.", W - 2 * M - 40 - larg, "Manrope-Regular", 9.5, ROXO)

    # três perguntas
    y -= caixa_h + 22
    resp_h = 88
    for i in range(1, 4):
        y -= 10
        c.setFillColor(ROXO)
        c.circle(M + 9, y + 3, 9, stroke=0, fill=1)
        texto(c, M + 6.2, y - 0.5, str(i), "SpaceMono-Bold", 10, white)
        texto(c, M + 26, y, "Pergunta", "Manrope-ExtraBold", 10.5, ROXO)
        selo(c, M + 84, y, "HOJE", VERDE)
        campo(c, f"pergunta_{i}", M + 26, y - 40, W - 2 * M - 26, 32, multilinha=True, dica=f"Pergunta {i}")
        y -= 56
        texto(c, M + 26, y, "Sua resposta", "Manrope-ExtraBold", 10.5, ROXO)
        selo(c, M + 112, y, "ANTES DA MENTORIA", CORAL_TEXTO)
        campo(c, f"resposta_{i}", M + 26, y - 8 - resp_h, W - 2 * M - 26, resp_h, multilinha=True, dica=f"Resposta à pergunta {i}")
        y -= resp_h + 26
    rodape(c, 1)


def pagina_2(c):
    cabecalho(c, 2)
    y = H - M - 72

    # o projeto
    y = titulo_secao(c, y, "Seu projeto")
    selo(c, M + 112, y + 22, "HOJE", VERDE)
    for nome, rotulo, apoio, h in [
        ("proposta", "Proposta de projeto", "Que tarefa do seu trabalho você quer automatizar com IA? Como ela é feita hoje e quem faz?", 128),
        ("impacto", "Impacto esperado", "O que significa sucesso para essa tarefa? O que você vai medir para dizer que deu certo?", 108),
    ]:
        texto(c, M, y, rotulo, "Manrope-ExtraBold", 10.5, ROXO)
        y = paragrafo(c, M, y - 14, apoio, W - 2 * M, tam=9)
        campo(c, nome, M, y - h + 4, W - 2 * M, h, multilinha=True, dica=rotulo)
        y -= h + 18

    # a atualização
    y -= 6
    y = titulo_secao(c, y, "Atualização do projeto")
    selo(c, M + 196, y + 22, "ANTES DA MENTORIA", CORAL_TEXTO)
    texto(c, M, y, "O projeto foi implementado?", "Manrope-ExtraBold", 10.5, ROXO)
    opcoes(c, "implementado", M, y - 22, ["Sim", "Em parte", "Não"])
    y -= 48
    texto(c, M, y, "Teve o impacto esperado?", "Manrope-ExtraBold", 10.5, ROXO)
    opcoes(c, "impacto_alcancado", M, y - 22, ["Sim", "Em parte", "Não", "Ainda não dá para saber"])
    y -= 48
    texto(c, M, y, "O que mudou?", "Manrope-ExtraBold", 10.5, ROXO)
    y = paragrafo(c, M, y - 14, "Desde o dia 03/10, você mudou de ideia sobre alguma coisa: a tarefa, a forma de usar a IA, o que medir? Se o projeto não andou ou não teve o impacto esperado, o que faltou?", W - 2 * M, tam=9)
    h = y - (M + 6)
    campo(c, "o_que_mudou", M, M + 6, W - 2 * M, h, multilinha=True, dica="O que mudou")
    rodape(c, 2)


def main():
    c = canvas.Canvas(str(SAIDA), pagesize=A4)
    c.setTitle("Builder log · AI for Business")
    c.setAuthor("Inteli Exec")
    pagina_1(c)
    c.showPage()
    pagina_2(c)
    c.showPage()
    c.save()
    print(SAIDA)


if __name__ == "__main__":
    main()
