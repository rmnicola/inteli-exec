#!/usr/bin/env python3
"""Gera o learning-log.pdf do Essencial na Prática: quatro páginas preenchíveis, na identidade Inteli Exec.

O documento acompanha o dia inteiro, da abertura ao fechamento, e fica com a pessoa. Não há entrega,
devolução nem mentoria: cada parte é preenchida no momento indicado pelo selo, com cronômetro em sala.

Página 1  Desmistificando a IA: as palavras-chave do dia e a definição de cada uma, nas palavras de quem escreve.
Página 2  O projeto da dupla e o início da tabela de etapas do fluxo.
Página 3  Continuação da tabela de etapas.
Página 4  Fechamento: o que construímos, próximos passos e o que mudou de ideia.

Requer reportlab e pypdf. Os campos seguem o padrão de .agents/skills/pdf-preenchivel/formulario.py.

    uv run --with reportlab --with pypdf python gerar.py
"""
import sys
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
LOGO = RAIZ / "design-system/assets/img/logo-exec-escuro-coral.png"
FONTES = RAIZ / "design-system/assets/fonts/ttf"
SAIDA = AQUI / "learning-log.pdf"
sys.path.insert(0, str(RAIZ / ".agents/skills/pdf-preenchivel"))
from formulario import campo, centralizar, marca  # noqa: E402  padrão dos campos preenchíveis

for nome in ["Manrope-Regular", "Manrope-SemiBold", "Manrope-ExtraBold", "Platypi-Medium", "SpaceMono-Regular", "SpaceMono-Bold"]:
    pdfmetrics.registerFont(TTFont(nome, str(FONTES / f"{nome}.ttf")))

ROXO = HexColor("#2e2640")
CORAL = HexColor("#ff4545")
CORAL_TEXTO = HexColor("#d63333")
CINZA_CLARO = HexColor("#e6eaeb")
TEXTO_SUAVE = HexColor("#5d5870")

W, H = A4
M = 42  # margem
L = W - 2 * M  # largura útil

PROGRAMA = "AI FOR BUSINESS · ESSENCIAL NA PRÁTICA"
RODAPE = "Inteli Exec · AI for Business: Essencial na Prática"


PALAVRAS = 10
NIVEIS = [("nenhuma", "Nenhuma"), ("com-supervisao", "Com supervisão"), ("completa", "Completa")]
LINHA_ETAPA = 72  # altura de uma linha da tabela: cabe o nível de automação empilhado


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


def cabecalho(c, pagina):
    c.drawImage(str(LOGO), W - M - 84, H - M - 22, width=84, height=84 * 321 / 914, mask="auto")
    texto(c, M, H - M - 8, PROGRAMA, "SpaceMono-Bold", 7.5, CORAL_TEXTO)
    if pagina == 1:
        texto(c, M, H - M - 44, "Learning Log", "Platypi-Medium", 32, ROXO)
    else:
        texto(c, M, H - M - 30, "Learning Log", "Platypi-Medium", 18, ROXO)


def rodape(c, pagina):
    c.setStrokeColor(CINZA_CLARO)
    c.setLineWidth(1)
    c.line(M, M - 4, W - M, M - 4)
    texto(c, M, M - 16, RODAPE, "Manrope-Regular", 7.5, TEXTO_SUAVE)
    texto(c, W - M - 10, M - 16, str(pagina), "SpaceMono-Regular", 7.5, TEXTO_SUAVE)


def secao(c, y, numero, titulo, apoio=None):
    """Título de seção com número e uma linha de apoio. Devolve o y seguinte."""
    c.setFillColor(CORAL)
    c.rect(M, y - 2, 4, 16, stroke=0, fill=1)
    texto(c, M + 12, y, f"{numero}. {titulo}", "Manrope-ExtraBold", 15, ROXO)
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
    y = H - M - 80
    texto(c, M, y, "Nome", "Manrope-SemiBold", 9, TEXTO_SUAVE)
    texto(c, M + 300, y, "Empresa ou área", "Manrope-SemiBold", 9, TEXTO_SUAVE)
    campo(c, "nome", M, y - 26, 285, 20, dica="Nome")
    campo(c, "empresa", M + 300, y - 26, L - 300, 20, dica="Empresa ou área")
    y -= 26

    # como usar
    y -= 40
    caixa_h = 76
    c.setFillColor(CINZA_CLARO)
    c.roundRect(M, y - caixa_h, L, caixa_h, 8, stroke=0, fill=1)
    texto(c, M + 14, y - 18, "Como usar este documento", "Manrope-ExtraBold", 10.5, ROXO)
    paragrafo(c, M + 14, y - 34,
              "Ele acompanha o dia inteiro e fica com você: não há entrega nem correção. Não há resposta certa: "
              "escreva o que você entendeu e decidiu. Preencheu no computador? Salve o arquivo (Ctrl+S, ou Cmd+S "
              "no Mac) num leitor de PDF — a pré-visualização do Drive e do Teams não salva o que você digitou.",
              L - 28, tam=9.5, cor=ROXO)

    y -= caixa_h + 30
    y = secao(c, y, 1, "Desmistificando a IA",
              "Enquanto a conversa acontece, anote só as palavras-chave. A definição vem depois, com os colegas.")
    larg_palavra = 150
    texto(c, M + 18, y, "Palavra-chave", "Manrope-ExtraBold", 9.5, ROXO)
    texto(c, M + 18 + larg_palavra, y, "O que é, nas minhas palavras", "Manrope-ExtraBold", 9.5, ROXO)
    y -= 8
    linha_h = (y - M - 4) / PALAVRAS
    for i in range(1, PALAVRAS + 1):
        y -= linha_h
        texto(c, M, y + linha_h / 2 - 4, str(i), "SpaceMono-Bold", 10, CORAL_TEXTO)
        h = linha_h - 8
        campo(c, f"palavra_{i}", M + 18, y + 4, larg_palavra - 10, h, dica=f"Palavra-chave {i}", tam=11, centrado=True)
        campo(c, f"definicao_{i}", M + 18 + larg_palavra, y + 4, L - 18 - larg_palavra, h,
              multilinha=True, dica=f"Palavra-chave {i}: definição", tam=10)
    rodape(c, 1)


def tabela_etapas(c, y, primeira):
    """Tabela do fluxo: etapa, contexto, ferramentas, nível de automação e quem confere.
    Preenche o espaço até o rodapé; devolve o número da próxima etapa."""
    n_larg, larg_auto, vao = 16, 84, 8
    campo_larg = (L - n_larg - larg_auto - 4 * vao) / 4
    cols = [("Etapa", "Uma ação pequena e concreta."),
            ("Contexto", "Que informação ela precisa."),
            ("Ferramentas", "Chat, assistente, agente."),
            ("Quem confere", "Nome de uma pessoa.")]
    xs, x = [], M + n_larg
    for k in range(4):
        xs.append(x)
        x += campo_larg + vao
        if k == 2:  # o nível de automação entra entre "Ferramentas" e "Quem confere"
            x_auto = x
            x += larg_auto + vao
    for (rotulo, apoio), x in zip(cols, xs):
        texto(c, x, y, rotulo, "Manrope-ExtraBold", 9.5, ROXO)
        paragrafo(c, x, y - 11, apoio, campo_larg + vao - 2, tam=7.5)
    texto(c, x_auto, y, "Automação", "Manrope-ExtraBold", 9.5, ROXO)
    texto(c, x_auto, y - 11, "Marque um.", "Manrope-Regular", 7.5, TEXTO_SUAVE)
    y -= 26
    i = primeira
    while y - LINHA_ETAPA >= M + 4:
        y -= LINHA_ETAPA
        c.setStrokeColor(CINZA_CLARO)
        c.setLineWidth(0.8)
        c.line(M, y, M + L, y)
        h = LINHA_ETAPA - 8
        base = y + 4
        texto(c, M, base + h / 2 - 4, str(i), "SpaceMono-Bold", 10, CORAL_TEXTO)
        for x, (chave, rotulo) in zip(xs, [("etapa", "etapa"), ("contexto", "contexto"),
                                           ("ferramenta", "ferramentas"), ("confere", "quem confere")]):
            campo(c, f"{chave}_{i}", x, base, campo_larg, h, multilinha=True, dica=f"Etapa {i}: {rotulo}", tam=9)
        # os três níveis empilhados: a primeira caixa alinhada ao topo dos campos da linha, a última à base
        passo_v = (h - 12) / 2
        for k, (v, rotulo) in enumerate(NIVEIS):
            yk = base + h - 12 - k * passo_v
            marca(c, f"automacao_{i}", v, x_auto, yk, f"Etapa {i}: automação {rotulo.lower()}")
            texto(c, x_auto + 17, yk + 3, rotulo, "Manrope-SemiBold", 8.5, ROXO)
        i += 1
    return i


def pagina_2(c):
    cabecalho(c, 2)
    y = H - M - 72
    y = secao(c, y, 2, "O projeto da dupla",
              "Com a sua dupla, antes de construir. É um registro, não um plano.")
    y = pergunta(c, y, "tarefa", "Qual é a tarefa que vocês escolheram?",
                 "Uma tarefa que se repete, com entrada e saída claras, que cabe numa tarde.", 72)
    y = pergunta(c, y, "hoje", "Como ela é feita hoje, e por quem?", "Quanto tempo leva e onde costuma travar.", 72)
    y = pergunta(c, y, "dar_certo", "O que é dar certo?", "O sinal concreto de que funcionou. Se der, com um número.", 64)
    y -= 2
    y = secao(c, y, 3, "O fluxo, etapa por etapa",
              "Uma linha por etapa do fluxo que vocês desenharam.")
    proxima = tabela_etapas(c, y, 1)
    rodape(c, 2)
    return proxima


def pagina_3(c, primeira):
    cabecalho(c, 3)
    y = secao(c, H - M - 72, 3, "O fluxo, etapa por etapa",
              "Continuação. No meio da tarde, pare a construção e volte aqui: risque, acrescente e corrija o que mudou.")
    tabela_etapas(c, y, primeira)
    rodape(c, 3)


def pagina_4(c):
    cabecalho(c, 4)
    y = H - M - 72
    y = secao(c, y, 4, "Fechamento", "Os últimos quinze minutos do dia. Escreva para você, daqui a um mês.")
    y = pergunta(c, y, "construimos", "O que construímos?",
                 "O que existe agora e não existia de manhã: o assistente, os documentos, a skill, o fluxo.", 104)
    y -= 4
    texto(c, M, y, "Próximos passos para implementar", "Manrope-ExtraBold", 12, ROXO)
    y = paragrafo(c, M, y - 15, "Três perguntas, três campos. Sem ciclo, sem prazo imposto: o que você de fato "
                                "pretende fazer.", L, tam=9) - 4
    passos = [("falta", "O que falta?", "Dado, acesso, autorização, tempo, alguém."),
              ("quando", "A partir de quando?", "Uma data ou um gatilho concreto."),
              ("sinal", "Que sinal mostra que funcionou?", "O que você vai observar para saber.")]
    alt = 76
    for nome, rotulo, apoio in passos:
        texto(c, M, y, rotulo, "Manrope-SemiBold", 10, ROXO)
        texto(c, M + pdfmetrics.stringWidth(rotulo, "Manrope-SemiBold", 10) + 10, y, apoio, "Manrope-Regular", 9, TEXTO_SUAVE)
        campo(c, nome, M, y - alt + 4, L, alt - 10, multilinha=True, dica=rotulo)
        y -= alt + 8
    y -= 4
    pergunta(c, y, "mudei_de_ideia", "O que eu pensava sobre IA de manhã e penso diferente agora?",
             "A frase que você diria para quem chegou aqui hoje de manhã.", y - M - 30)
    rodape(c, 4)


def main():
    c = canvas.Canvas(str(SAIDA), pagesize=(W, H))
    c.setTitle("Learning Log · AI for Business: Essencial na Prática")
    c.setAuthor("Inteli Exec")
    pagina_1(c)
    c.showPage()
    proxima = pagina_2(c)
    c.showPage()
    pagina_3(c, proxima)
    c.showPage()
    pagina_4(c)
    c.showPage()
    c.save()
    centralizar(SAIDA)
    print(SAIDA)


if __name__ == "__main__":
    main()
