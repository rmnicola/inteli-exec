#!/usr/bin/env python3
"""Gera o learning-log.pdf do workshop de professores: quatro páginas preenchíveis, em A4 deitado, na identidade Inteli.

Página 1, durante "Desmistificando a IA": palavras-chave e a definição de cada uma nas palavras do professor.
Páginas 2 e 3, na atividade "Desenhando um fluxo": no passo 1 (20 min), cada professor divide uma jornada em etapas e marca,
para cada etapa, se ela precisa de contexto ou de ferramenta específica e o nível de automação. No passo 2 (15 min),
escreve a ferramenta mais indicada para cada etapa.
Página 4, antes do segundo encontro: se conseguiu implementar o fluxo, que etapas foram ou não implementadas e por quê.

Requer reportlab e pypdf. Os campos seguem o padrão de tools/formulario.py. Usa as fontes (Manrope, Platypi, Space Mono, OFL) do builder log do Essencial na Prática.
"""
import sys
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
LOGO = RAIZ / "design-system/assets/img/logo-inteli-escuro-coral.png"
FONTES = RAIZ / "essencial-na-pratica/builder-log/fontes"
SAIDA = AQUI / "learning-log.pdf"
sys.path.insert(0, str(RAIZ / "tools"))
from formulario import campo, caixa, marca, centralizar  # noqa: E402  padrão dos campos preenchíveis

for nome in ["Manrope-Regular", "Manrope-SemiBold", "Manrope-ExtraBold", "Platypi-Medium", "SpaceMono-Regular", "SpaceMono-Bold"]:
    pdfmetrics.registerFont(TTFont(nome, str(FONTES / f"{nome}.ttf")))

ROXO = HexColor("#2e2640")
CORAL = HexColor("#ff4545")
CORAL_TEXTO = HexColor("#d63333")
CINZA_CLARO = HexColor("#e6eaeb")
TEXTO_SUAVE = HexColor("#5d5870")

W, H = landscape(A4)
M = 36  # margem
L = W - 2 * M  # largura útil

# Selos: em que passo da atividade cada coluna é preenchida
PASSO1 = ("PASSO 1 · 20 MIN", ROXO)
PASSO2 = ("PASSO 2 · 15 MIN", CORAL_TEXTO)

PALAVRAS = 8
ETAPAS_POR_PAGINA = 5
NIVEIS = ["Nenhuma", "Com supervisão", "Completa"]


def texto(c, x, y, s, fonte="Manrope-Regular", tam=10, cor=ROXO):
    c.setFont(fonte, tam)
    c.setFillColor(cor)
    c.drawString(x, y, s)


def centro(c, x, y, s, fonte="Manrope-ExtraBold", tam=8, cor=ROXO):
    c.setFont(fonte, tam)
    c.setFillColor(cor)
    c.drawCentredString(x, y, s)


def selo(c, x, y, rotulo, cor):
    """Etiqueta em Space Mono com o passo da atividade. y = base do texto."""
    tam = 7.5
    larg = pdfmetrics.stringWidth(rotulo, "SpaceMono-Bold", tam) + 10
    c.setFillColor(cor)
    c.roundRect(x, y - 3.5, larg, 13, 3, stroke=0, fill=1)
    texto(c, x + 5, y, rotulo, "SpaceMono-Bold", tam, white)
    return larg


def cabecalho(c, pagina):
    larg, alt = ImageReader(str(LOGO)).getSize()
    c.drawImage(str(LOGO), W - M - 64, H - M - 26, width=64, height=64 * alt / larg, mask="auto")
    texto(c, M, H - M - 8, "USO DE IA NOS PROCESSOS ACADÊMICOS · WORKSHOP PARA PROFESSORES", "SpaceMono-Bold", 7.5, CORAL_TEXTO)
    texto(c, M, H - M - 40, "Learning Log", "Platypi-Medium", 26, ROXO)
    if pagina == 1:
        x = M + 190
        texto(c, x, H - M - 38, "Nome", "Manrope-SemiBold", 9, TEXTO_SUAVE)
        campo(c, "nome", x + 32, H - M - 44, 300, 20)
    texto(c, W - M - 10, M - 16, str(pagina), "SpaceMono-Regular", 7.5, TEXTO_SUAVE)


def secao(c, y, titulo, apoio):
    """Título de seção com a barra coral e uma linha de apoio. Devolve o y seguinte."""
    c.setFillColor(CORAL)
    c.rect(M, y - 2, 4, 16, stroke=0, fill=1)
    texto(c, M + 12, y, titulo, "Manrope-ExtraBold", 15, ROXO)
    texto(c, M + 12, y - 16, apoio, "Manrope-Regular", 9.5, TEXTO_SUAVE)
    return y - 40


def pagina_1(c):
    cabecalho(c, 1)
    y = secao(c, H - M - 80, "Desmistificando a IA", "Anote as palavras-chave da conversa e defina cada uma com as suas palavras.")
    larg_palavra = 200
    texto(c, M + 18, y, "Palavra-chave", "Manrope-ExtraBold", 9.5, ROXO)
    texto(c, M + 18 + larg_palavra, y, "O que é, nas minhas palavras", "Manrope-ExtraBold", 9.5, ROXO)
    y -= 10
    linha_h = (y - M) / PALAVRAS
    for i in range(1, PALAVRAS + 1):
        y -= linha_h
        texto(c, M, y + linha_h / 2 - 4, str(i), "SpaceMono-Bold", 10, CORAL_TEXTO)
        h = linha_h - 10
        campo(c, f"palavra_{i}", M + 18, y + 5, larg_palavra - 10, h, dica=f"Palavra-chave {i}", tam=15, centrado=True)
        campo(c, f"definicao_{i}", M + 18 + larg_palavra, y + 5, L - 18 - larg_palavra, h, multilinha=True, dica=f"Palavra-chave {i}: definição", tam=11, centrado=True)


def pagina_etapas(c, pagina, primeira):
    """Uma página da tabela de etapas, a partir da etapa `primeira`."""
    cabecalho(c, pagina)
    apoio = "Uma jornada de trabalho, etapa por etapa." if primeira == 1 else "Continuação."
    y = secao(c, H - M - 80, "Desenhando um fluxo", apoio)

    # colunas da tabela: (rótulo, apoio, largura); o nível de automação vem logo depois das ferramentas, com as opções empilhadas
    n_larg = 18
    cols = [
        ("Etapa", "Uma ação pequena e concreta.", 170),
        ("Contexto", "Marque se precisa e diga qual.", 140),
        ("Ferramentas", "Marque se precisa e diga quais.", 140),
    ]
    larg_auto = 100
    xs, x = [], M + n_larg
    for _, _, larg in cols:
        xs.append(x)
        x += larg
    x_auto = x
    x_ind = x_auto + larg_auto + 10
    larg_ind = M + L - x_ind

    # selos por passo, sobre as colunas
    c.setStrokeColor(ROXO)
    c.setLineWidth(1.2)
    c.line(xs[0], y - 6, x_ind - 10, y - 6)
    selo(c, xs[0], y + 2, *PASSO1)
    c.setStrokeColor(CORAL_TEXTO)
    c.line(x_ind, y - 6, M + L, y - 6)
    selo(c, x_ind, y + 2, *PASSO2)

    # cabeçalho da tabela: todos os rótulos na mesma linha, e os apoios na linha de baixo
    y -= 24
    for (rotulo, apoio, _), x in zip(cols, xs):
        texto(c, x, y, rotulo, "Manrope-ExtraBold", 9.5, ROXO)
        texto(c, x, y - 12, apoio, "Manrope-Regular", 8, TEXTO_SUAVE)
    texto(c, x_auto, y, "Nível de automação", "Manrope-ExtraBold", 9.5, ROXO)
    texto(c, x_auto, y - 12, "Marque um.", "Manrope-Regular", 8, TEXTO_SUAVE)
    texto(c, x_ind, y, "Ferramenta mais indicada", "Manrope-ExtraBold", 9.5, ROXO)
    texto(c, x_ind, y - 12, "Chat, Gem, projeto, harness...", "Manrope-Regular", 8, TEXTO_SUAVE)

    # linhas
    y -= 18
    linha_h = (y - M) / ETAPAS_POR_PAGINA
    for i in range(primeira, primeira + ETAPAS_POR_PAGINA):
        y -= linha_h
        c.setStrokeColor(CINZA_CLARO)
        c.setLineWidth(0.8)
        c.line(M, y, M + L, y)
        meio = y + linha_h / 2
        texto(c, M, meio - 4, str(i), "SpaceMono-Bold", 10, CORAL_TEXTO)
        h = linha_h - 8
        campo(c, f"etapa_{i}", xs[0], y + 4, cols[0][2] - 10, h, multilinha=True, dica=f"Etapa {i}")
        for x, (chave, rotulo) in zip(xs[1:3], [("contexto", "contexto"), ("ferramenta", "ferramentas")]):
            caixa(c, f"precisa_{chave}_{i}", x, meio - 6, f"Etapa {i}: precisa de {rotulo}")
            campo(c, f"{chave}_{i}", x + 18, y + 4, cols[1][2] - 28, h, multilinha=True, dica=f"Etapa {i}: {rotulo} necessário(s)")
        # os três níveis empilhados: a primeira caixa alinhada ao topo dos campos da linha, a última à base
        base, passo_v = y + 4, (h - 12) / 2
        for k, (v, rotulo) in enumerate(zip(["nenhuma", "com-supervisao", "completa"], NIVEIS)):
            yk = base + h - 12 - k * passo_v
            marca(c, f"automacao_{i}", v, x_auto, yk, f"Etapa {i}: automação {rotulo.lower()}")
            texto(c, x_auto + 17, yk + 3, rotulo, "Manrope-SemiBold", 9, ROXO)
        campo(c, f"indicada_{i}", x_ind, y + 4, larg_ind, h, multilinha=True, dica=f"Etapa {i}: ferramenta mais indicada")


def pagina_retorno(c):
    """Página 4: preenchida antes do segundo encontro, depois de tentar implementar o fluxo."""
    cabecalho(c, 4)
    y = secao(c, H - M - 80, "Antes do segundo encontro",
              "Depois de tentar implementar o fluxo, volte a este Learning Log. O encontro começa pela leitura destes registros.")
    texto(c, M, y, "Você conseguiu implementar o fluxo?", "Manrope-ExtraBold", 10.5, ROXO)
    x = M + pdfmetrics.stringWidth("Você conseguiu implementar o fluxo?", "Manrope-ExtraBold", 10.5) + 20
    for rotulo in ["Sim", "Em parte", "Não"]:
        marca(c, "implementou", rotulo.lower().replace(" ", "-").replace("ã", "a"), x, y - 3, rotulo)
        texto(c, x + 17, y, rotulo, "Manrope-SemiBold", 10)
        x += 17 + pdfmetrics.stringWidth(rotulo, "Manrope-SemiBold", 10) + 22
    y -= 30

    perguntas = [
        ("implementadas", "Quais etapas foram implementadas?", "Com que ferramenta e com que nível de automação."),
        ("nao_implementadas", "Quais etapas não foram implementadas?", "Inclua as que você tirou ou passou para uma pessoa."),
        ("por_que", "Por que essas etapas não foram implementadas?", "Contexto que faltou, ferramenta que não serviu, resultado ruim."),
    ]
    gap = 28
    alt = (y - M - 2 * gap) / 3
    for k, (nome, rotulo, apoio) in enumerate(perguntas):
        topo = y - k * (alt + gap)
        texto(c, M, topo, rotulo, "Manrope-ExtraBold", 10.5, ROXO)
        texto(c, M + pdfmetrics.stringWidth(rotulo, "Manrope-ExtraBold", 10.5) + 10, topo, apoio, "Manrope-Regular", 9, TEXTO_SUAVE)
        campo(c, nome, M, topo - alt, L, alt - 10, multilinha=True, dica=rotulo, tam=10)


def main():
    c = canvas.Canvas(str(SAIDA), pagesize=(W, H))
    c.setTitle("Learning Log · Uso de IA nos processos acadêmicos")
    c.setAuthor("Inteli")
    pagina_1(c)
    c.showPage()
    for pagina, primeira in [(2, 1), (3, 1 + ETAPAS_POR_PAGINA)]:
        pagina_etapas(c, pagina, primeira)
        c.showPage()
    pagina_retorno(c)
    c.showPage()
    c.save()
    centralizar(SAIDA)
    print(SAIDA)


if __name__ == "__main__":
    main()
