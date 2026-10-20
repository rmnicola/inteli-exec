#!/usr/bin/env python3
"""Gera o learning-log.pdf do Ferramentas em Ação: cinco páginas preenchíveis, na identidade Inteli Exec.

O documento conta a história do agente de cada participante, do dia 1 ao ciclo de 90 dias. Cada parte
se preenche em 5 a 10 minutos, no momento indicado no selo, e é lida pelos colegas do trio.

Requer reportlab. Usa as fontes (Manrope, Platypi, Space Mono, OFL) do builder log do Essencial na Prática.
"""
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
LOGO = RAIZ / "design-system/assets/img/logo-exec-escuro-coral.png"
FONTES = RAIZ / "essencial-na-pratica/builder-log/fontes"
SAIDA = AQUI / "learning-log.pdf"

for nome in ["Manrope-Regular", "Manrope-SemiBold", "Manrope-ExtraBold", "Platypi-Medium", "SpaceMono-Regular", "SpaceMono-Bold"]:
    pdfmetrics.registerFont(TTFont(nome, str(FONTES / f"{nome}.ttf")))

ROXO = HexColor("#2e2640")
CORAL = HexColor("#ff4545")
CORAL_TEXTO = HexColor("#d63333")
VERDE = HexColor("#066d73")
CINZA_CLARO = HexColor("#e6eaeb")
CINZA_ESCURO = HexColor("#b2b6bf")
TEXTO_SUAVE = HexColor("#5d5870")
CAMPO = HexColor("#f6f7f8")

W, H = A4
M = 42  # margem
L = W - 2 * M  # largura útil

# Selos: quando cada parte é preenchida
DIA1 = ("DIA 1", VERDE)
DIA2 = ("DIA 2", ROXO)
CICLO = ("CICLO DE 90 DIAS", CORAL_TEXTO)


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
    """Etiqueta em Space Mono com o momento de preenchimento. y = base do texto."""
    tam = 7.5
    larg = pdfmetrics.stringWidth(rotulo, "SpaceMono-Bold", tam) + 10
    c.setFillColor(cor)
    c.roundRect(x, y - 3.5, larg, 13, 3, stroke=0, fill=1)
    texto(c, x + 5, y, rotulo, "SpaceMono-Bold", tam, white)
    return larg


def campo(c, nome, x, y, w, h, multilinha=False, dica=""):
    """Campo de texto preenchível. (x, y) = canto inferior esquerdo."""
    c.acroForm.textfield(
        name=nome, tooltip=dica or nome, x=x, y=y, width=w, height=h,
        borderStyle="solid", borderWidth=0.8, borderColor=CINZA_ESCURO, fillColor=CAMPO, textColor=ROXO,
        fontName="Helvetica", fontSize=9 if multilinha else 10,
        fieldFlags="multiline" if multilinha else "", forceBorder=True,
        maxlen=None,  # o padrão do reportlab é 100 caracteres
    )


def marca(c, grupo, valor, x, y, dica):
    """Um botão de opção (só um marcado por grupo). (x, y) = canto inferior esquerdo."""
    c.acroForm.radio(name=grupo, value=valor, x=x, y=y, size=12, buttonStyle="check", shape="square",
                     borderColor=ROXO, borderWidth=0.8, fillColor=white, textColor=ROXO, forceBorder=True, tooltip=dica)


def opcoes(c, grupo, x, y, valores):
    """Botões de opção em linha, com o rótulo ao lado."""
    for v in valores:
        marca(c, grupo, v.lower().replace(" ", "-"), x, y - 3, v)
        texto(c, x + 17, y, v, "Manrope-SemiBold", 10)
        x += 17 + pdfmetrics.stringWidth(v, "Manrope-SemiBold", 10) + 22


def cabecalho(c, pagina):
    c.drawImage(str(LOGO), W - M - 84, H - M - 22, width=84, height=84 * 321 / 914, mask="auto")
    texto(c, M, H - M - 8, "AI FOR BUSINESS · FERRAMENTAS EM AÇÃO · 23 E 24/10/2026", "SpaceMono-Bold", 7.5, CORAL_TEXTO)
    if pagina == 1:
        texto(c, M, H - M - 44, "Learning Log", "Platypi-Medium", 32, ROXO)
    else:
        texto(c, M, H - M - 30, "Learning Log", "Platypi-Medium", 18, ROXO)


def rodape(c, pagina):
    c.setStrokeColor(CINZA_CLARO)
    c.setLineWidth(1)
    c.line(M, M - 4, W - M, M - 4)
    texto(c, M, M - 16, "Inteli Exec · AI for Business: Ferramentas em Ação", "Manrope-Regular", 7.5, TEXTO_SUAVE)
    texto(c, W - M - 10, M - 16, str(pagina), "SpaceMono-Regular", 7.5, TEXTO_SUAVE)


def secao(c, y, numero, titulo, quando, apoio=None):
    """Título de seção com número, selo do momento e uma linha de apoio. Devolve o y seguinte."""
    c.setFillColor(CORAL)
    c.rect(M, y - 2, 4, 16, stroke=0, fill=1)
    t = f"{numero}. {titulo}"
    texto(c, M + 12, y, t, "Manrope-ExtraBold", 15, ROXO)
    selo(c, M + 22 + pdfmetrics.stringWidth(t, "Manrope-ExtraBold", 15), y + 2, *quando)
    if apoio:
        return paragrafo(c, M + 12, y - 16, apoio, L - 12) - 6
    return y - 24


def pergunta(c, y, nome, rotulo, apoio, h):
    """Rótulo, uma linha de apoio e o campo. Devolve o y seguinte."""
    texto(c, M, y, rotulo, "Manrope-ExtraBold", 10.5, ROXO)
    y = paragrafo(c, M, y - 14, apoio, L, tam=9) if apoio else y - 8
    campo(c, nome, M, y - h + 4, L, h, multilinha=True, dica=rotulo)
    return y - h - 16


def pagina_1(c):
    cabecalho(c, 1)
    y = H - M - 78
    texto(c, M, y, "Nome", "Manrope-SemiBold", 9, TEXTO_SUAVE)
    texto(c, M + 300, y, "Empresa", "Manrope-SemiBold", 9, TEXTO_SUAVE)
    campo(c, "nome", M, y - 26, 285, 20)
    campo(c, "empresa", M + 300, y - 26, L - 300, 20)

    # como usar
    y -= 46
    caixa_h = 104
    c.setFillColor(CINZA_CLARO)
    c.roundRect(M, y - caixa_h, L, caixa_h, 8, stroke=0, fill=1)
    texto(c, M + 14, y - 18, "Como usar este documento", "Manrope-ExtraBold", 10.5, ROXO)
    paragrafo(c, M + 14, y - 34, "Ele conta a história do seu agente, do primeiro dia ao ciclo de 90 dias. Os colegas do trio vão lê-lo: "
              "escreva para quem não conhece o seu processo. Cada parte leva de 5 a 10 minutos.", L - 28, tam=9.5, cor=ROXO)
    x = M + 14
    for rotulo, cor in [DIA1, DIA2, CICLO]:
        x += selo(c, x, y - 70, rotulo, cor) + 8
    paragrafo(c, x + 2, y - 70, "indicam quando preencher cada parte.", L - (x - M) - 16, tam=9.5, cor=ROXO)
    paragrafo(c, M + 14, y - 90, "Não há resposta certa: escreva o que você decidiu e por quê.", L - 28, tam=9.5)

    y -= caixa_h + 30
    y = secao(c, y, 1, "O processo", DIA1, "Na abertura do dia 1. Descreva para alguém de fora da sua empresa.")
    y = pergunta(c, y, "processo", "Que processo você trouxe?", "Quem faz, com que frequência, a partir de que entrada e para produzir que saída.", 110)
    y = pergunta(c, y, "valor", "Por que vale a pena automatizá-lo?", "O que se ganha, e para quem: tempo, erro, custo, prazo. Se puder, com um número de hoje.", 110)
    rodape(c, 1)


def pagina_2(c):
    cabecalho(c, 2)
    y = H - M - 72
    y = secao(c, y, 2, "A abordagem", DIA1, "No fim da manhã do dia 1, depois das cinco abordagens.")
    y = pergunta(c, y, "abordagem", "Que abordagem você escolheu, e por quê?",
                 "Assistente, automação, job, agente ou uma combinação. O que você considerou e deixou de lado?", 96)

    y -= 8
    y = secao(c, y, 3, "O plano, etapa por etapa", DIA1, "Na tarde do dia 1, junto com o Blueprint. Uma linha por etapa do processo.")
    # cabeçalho da tabela
    col_etapa, col_marca, col_onde = 150, 56, L - 150 - 3 * 56
    xs = [M + col_etapa + i * col_marca for i in range(3)]
    texto(c, M, y, "Etapa", "Manrope-ExtraBold", 9, ROXO)
    for x, (l1, l2) in zip(xs, [("Pessoa", "faz"), ("Agente, com", "aprovação"), ("Agente", "sozinho")]):
        c.setFont("Manrope-ExtraBold", 8)
        c.setFillColor(ROXO)
        c.drawCentredString(x + col_marca / 2, y + 4, l1)
        c.drawCentredString(x + col_marca / 2, y - 6, l2)
    texto(c, M + col_etapa + 3 * col_marca + 6, y, "Onde pode dar errado", "Manrope-ExtraBold", 9, ROXO)
    y -= 16
    linha_h = 30
    for i in range(1, int((y - M - 10) / linha_h) + 1):
        y -= linha_h
        campo(c, f"etapa_{i}", M, y + 4, col_etapa - 8, linha_h - 8, multilinha=True, dica=f"Etapa {i}")
        for x, v in zip(xs, ["pessoa", "agente-com-aprovacao", "agente-sozinho"]):
            marca(c, f"quem_{i}", v, x + col_marca / 2 - 6, y + 9, f"Etapa {i}: {v.replace('-', ' ')}")
        campo(c, f"onde_{i}", M + col_etapa + 3 * col_marca + 6, y + 4, col_onde - 6, linha_h - 8, multilinha=True, dica=f"Etapa {i}: onde pode dar errado")
    rodape(c, 2)


def pagina_3(c):
    cabecalho(c, 3)
    y = H - M - 72
    y = secao(c, y, 4, "A revisão do plano", DIA2, "No dia 2, depois dos casos de falha. Volte à tabela da parte 3.")
    texto(c, M, y, "O que mudou no plano", "Manrope-ExtraBold", 10.5, ROXO)
    y = paragrafo(c, M, y - 14, "Para cada risco que você encontrou: mudou a estratégia, passou a etapa para uma pessoa ou criou uma verificação?", L, tam=9) - 4
    cols = [("Etapa", 120), ("O risco", 190), ("O que mudou", L - 310)]
    x = M
    for rotulo, larg in cols:
        texto(c, x, y, rotulo, "Manrope-ExtraBold", 9, ROXO)
        x += larg
    y -= 8
    linha_h = 40
    for i in range(1, int((y - M - 190) / linha_h) + 1):
        y -= linha_h
        x = M
        for j, (rotulo, larg) in enumerate(cols):
            campo(c, f"revisao_{i}_{j}", x, y + 4, larg - 8, linha_h - 8, multilinha=True, dica=f"Linha {i}: {rotulo}")
            x += larg
    y -= 24

    texto(c, M, y, "Em uma frase", "Manrope-ExtraBold", 10.5, ROXO)
    y = paragrafo(c, M, y - 14, "A mudança mais importante, do jeito que você contaria a um colega.", L, tam=9) - 6
    for nome, rotulo in [("antes", "Antes, eu deixaria o agente"), ("agora", "Agora,"), ("porque", "porque")]:
        larg = pdfmetrics.stringWidth(rotulo, "Manrope-SemiBold", 10) + 10
        texto(c, M, y - 12, rotulo, "Manrope-SemiBold", 10, ROXO)
        campo(c, f"frase_{nome}", M + larg, y - 18, L - larg, 22, multilinha=True, dica=rotulo)
        y -= 34
    rodape(c, 3)


def pagina_4(c):
    cabecalho(c, 4)
    y = H - M - 72
    y = secao(c, y, 5, "Para levar adiante", DIA2, "No fim do dia 2, junto com o Pacto de Implantação.")
    y = pergunta(c, y, "marco_30", "O que vai estar rodando em 30 dias?", "E como alguém da sua empresa vai perceber que está.", 250)
    pergunta(c, y, "para_a_turma", "O que da sua solução vale contar para a turma?", "Uma decisão que deu certo ou uma falha que ensinou alguma coisa.", y - M - 26 - 14 - 4)
    rodape(c, 4)


def pagina_5(c):
    cabecalho(c, 5)
    y = H - M - 72
    y = secao(c, y, 6, "Atualizações", CICLO, "Antes de cada encontro do ciclo. O encontro começa pela leitura destes registros.") - 10
    bloco_h = (y - M - 16) / 3
    for dias in (30, 60, 90):
        topo = y
        texto(c, M, y, f"Encontro de {dias} dias", "Manrope-ExtraBold", 12, ROXO)
        texto(c, M + 160, y, "O agente está rodando?", "Manrope-SemiBold", 9.5, TEXTO_SUAVE)
        opcoes(c, f"rodando_{dias}", M + 280, y, ["Sim", "Em parte", "Não"])
        y -= 20
        y = paragrafo(c, M, y, "O que mudou desde o último registro: no processo, no agente ou no plano? Se travou, o que faltou?", L, tam=9) - 2
        h = bloco_h - (topo - y) - 14
        campo(c, f"atualizacao_{dias}", M, y - h + 4, L, h, multilinha=True, dica=f"Atualização de {dias} dias")
        y -= h + 14
    rodape(c, 5)


def main():
    c = canvas.Canvas(str(SAIDA), pagesize=A4)
    c.setTitle("Learning Log · AI for Business: Ferramentas em Ação")
    c.setAuthor("Inteli Exec")
    for pagina in (pagina_1, pagina_2, pagina_3, pagina_4, pagina_5):
        pagina(c)
        c.showPage()
    c.save()
    print(SAIDA)


if __name__ == "__main__":
    main()
