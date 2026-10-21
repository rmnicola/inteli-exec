"""Padrão dos campos preenchíveis dos PDFs dos cursos (builder log, learning logs), sobre o reportlab.

- Cada campo de texto é uma caixa desenhada com uma margem interna; o campo fica dentro dela, sem borda própria.
- Nenhum campo tem limite de caracteres.
- Letra legível: 11 pt nos campos de uma linha e 10 pt nos de várias linhas, salvo `tam`.
- `centrado=True` centra o texto na horizontal. O reportlab não grava o alinhamento (/Q), então quem gera o PDF
  chama `centralizar(caminho)` depois de `c.save()`.
- Caixas de marcar e botões de opção: quadrados de 12 pt, com o rótulo à direita.

Uso, num gerar.py:
    sys.path.insert(0, str(RAIZ / "tools"))
    from formulario import campo, caixa, marca, centralizar

Requer reportlab e pypdf.
"""
from reportlab.lib.colors import HexColor, white

ROXO = HexColor("#2e2640")
CINZA_ESCURO = HexColor("#b2b6bf")
CAMPO = HexColor("#f6f7f8")

RECUO = 5  # margem interna da caixa
LADO = 12  # lado das caixas de marcar e dos botões de opção
CENTRALIZADOS = []


def campo(c, nome, x, y, w, h, multilinha=False, dica="", tam=None, centrado=False):
    """Campo de texto preenchível dentro de uma caixa com margem interna. (x, y) = canto inferior esquerdo da caixa."""
    c.saveState()
    c.setStrokeColor(CINZA_ESCURO)
    c.setFillColor(CAMPO)
    c.setLineWidth(0.8)
    c.rect(x, y, w, h, stroke=1, fill=1)
    c.restoreState()
    r = min(RECUO, h / 6)  # numa caixa baixa, a margem vertical encolhe para caber uma linha
    c.acroForm.textfield(
        name=nome, tooltip=dica or nome, x=x + RECUO, y=y + r, width=w - 2 * RECUO, height=h - 2 * r,
        borderStyle="solid", borderWidth=0, borderColor=CAMPO, fillColor=CAMPO, textColor=ROXO,
        fontName="Helvetica", fontSize=tam or (10 if multilinha else 11),
        fieldFlags="multiline" if multilinha else "",
        maxlen=None,  # o padrão do reportlab é 100 caracteres
    )
    if centrado:
        CENTRALIZADOS.append(nome)


def caixa(c, nome, x, y, dica):
    """Caixa de marcar independente. (x, y) = canto inferior esquerdo."""
    c.acroForm.checkbox(name=nome, x=x, y=y, size=LADO, buttonStyle="check", borderColor=ROXO, borderWidth=0.8,
                        fillColor=white, textColor=ROXO, forceBorder=True, tooltip=dica)


def marca(c, grupo, valor, x, y, dica):
    """Um botão de opção (só um marcado por grupo). (x, y) = canto inferior esquerdo."""
    c.acroForm.radio(name=grupo, value=valor, x=x, y=y, size=LADO, buttonStyle="check", shape="square",
                     borderColor=ROXO, borderWidth=0.8, fillColor=white, textColor=ROXO, forceBorder=True, tooltip=dica)


def centralizar(caminho):
    """Grava /Q 1 (texto centrado) nos campos criados com centrado=True."""
    if not CENTRALIZADOS:
        return
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import NameObject, NumberObject
    w = PdfWriter(clone_from=PdfReader(str(caminho)))
    for pagina in w.pages:
        for a in pagina.get("/Annots", []):
            a = a.get_object()
            if a.get("/T") in CENTRALIZADOS:
                a[NameObject("/Q")] = NumberObject(1)
    w.write(str(caminho))
