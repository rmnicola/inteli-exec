#!/usr/bin/env python3
"""Gera os documentos das personas a partir das fontes editáveis e monta um .zip por persona.

Convenção de nomes em <persona>/<pratica>/fontes/:
  nome.pdf.md         -> arquivos/nome.pdf   (documento formatado, com papel timbrado)
  nome.manuscrito.md  -> arquivos/nome.png   (foto de papel escrito à mão)
  nome.xlsx.csv       -> arquivos/nome.xlsx  (planilha; separador ';')
  qualquer outro      -> copiado para arquivos/ como está (.txt, .md...)

Nos .pdf.md, a primeira linha escolhe o papel timbrado:
  <!-- timbre: aurora -->   Casa Aurora (Helena)
  <!-- timbre: nucleo -->   Núcleo Engenharia (Diego)
  <!-- timbre: asseio -->   Asseio Total Serviços
  <!-- timbre: mobicorp --> Mobicorp Mobiliário
  <!-- timbre: beatriz -->  Beatriz Lemos Arquitetura
  <!-- timbre: nenhum -->

Uso:  python3 build.py            (tudo)
      python3 build.py helena     (só uma persona)
"""
import csv
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown
import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

ROOT = Path(__file__).resolve().parent
CHROMIUM = shutil.which("chromium") or shutil.which("google-chrome")
RODAPE = "Material didático Inteli · empresa e pessoas fictícias"

PERSONAS = ["helena-prado", "diego-farias", "beatriz-lemos"]
PRATICAS = ["pratica-2", "pratica-3"]


def _timbre(classe, logo, nome, linha, endereco):
    return (f"<header class='timbre {classe}'><div class='marca'><span class='logo'>{logo}</span>"
            f"<div><strong>{nome}</strong><small>{linha}</small></div></div>"
            f"<div class='end'>{endereco}</div></header>")


TIMBRES = {
    "aurora": _timbre("aurora", "◉", "Casa Aurora", "Utilidades domésticas · Curitiba",
                      "Batel · Portão · Cabral"),
    "nucleo": _timbre("nucleo", "▦", "Núcleo Engenharia Ltda.", "Projetos e gerenciamento de obras",
                      "Av. do Contorno, 6.480 · Belo Horizonte/MG"),
    "asseio": _timbre("asseio", "✦", "ASSEIO TOTAL SERVIÇOS LTDA.", "Limpeza e conservação predial",
                      "Rua Rio Grande do Norte, 1.055 · Belo Horizonte/MG"),
    "mobicorp": _timbre("mobicorp", "■", "MOBICORP MOBILIÁRIO CORPORATIVO", "Cadeiras, estações e armários",
                        "Rod. Fernão Dias, km 12 · Contagem/MG"),
    "beatriz": _timbre("beatriz", "△", "Beatriz Lemos", "Arquitetura e interiores · Florianópolis",
                       "contato@beatrizlemos.arq.br"),
    "nenhum": "",
}

CSS = """
@page { size: A4; margin: 18mm 18mm 20mm; }
body { font-family: 'Alegreya Sans', 'Adwaita Sans', sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1d2320; }
.timbre { display: flex; justify-content: space-between; align-items: flex-end; padding-bottom: 8px; margin-bottom: 18px; }
.timbre .marca { display: flex; gap: 10px; align-items: center; }
.timbre strong { display: block; font-size: 13pt; letter-spacing: .02em; }
.timbre small { color: #5b6660; font-size: 8.5pt; }
.timbre .end { font-size: 8.5pt; color: #5b6660; }
.aurora { border-bottom: 2px solid #9a5b2d; } .aurora .logo { color: #9a5b2d; font-size: 22pt; }
.nucleo { border-bottom: 2px solid #1f4e79; } .nucleo .logo { color: #1f4e79; font-size: 20pt; }
.asseio { border-bottom: 3px solid #0f7a6a; } .asseio .logo { color: #0f7a6a; font-size: 18pt; }
.mobicorp { border-bottom: 3px solid #4b4b4b; } .mobicorp .logo { color: #4b4b4b; font-size: 16pt; }
.beatriz { border-bottom: 1px solid #b08968; } .beatriz .logo { color: #b08968; font-size: 20pt; }
h1 { font-size: 16pt; margin: 0 0 4px; } h2 { font-size: 12.5pt; margin: 18px 0 6px; } h3 { font-size: 11pt; margin: 14px 0 4px; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 12px; font-size: 9.5pt; }
th, td { border: 1px solid #c9d1cc; padding: 4px 7px; text-align: left; vertical-align: top; }
th { background: #eef3f0; }
blockquote { margin: 8px 0; padding: 6px 12px; border-left: 3px solid #9fb5a8; background: #f6f8f7; }
.rodape { position: fixed; bottom: -12mm; left: 0; right: 0; font-size: 7.5pt; color: #8a948f; text-align: center; }
"""

MANUSCRITO_CSS = """
body { margin: 0; background: #d9d4c7; }
.folha { width: 820px; min-height: 860px; margin: 40px auto; padding: 50px 60px 60px 90px; background:
  repeating-linear-gradient(#fbf8ef 0 33px, #a9c4dd 33px 34px); position: relative;
  transform: rotate(-1.2deg); box-shadow: 0 8px 24px rgba(0,0,0,.25);
  font-family: 'Grape Nuts', cursive; font-size: 23px; line-height: 34px; color: #1f2a6b; }
.folha::before { content: ''; position: absolute; left: 70px; top: 0; bottom: 0; width: 2px; background: #e39a9a; }
.folha h1, .folha h2, .folha h3 { font-size: 30px; line-height: 34px; margin: 0; font-weight: normal; text-decoration: underline; }
.folha p, .folha ul, .folha ol { margin: 0; } .folha table { border-collapse: collapse; }
.folha td, .folha th { border: none; padding: 0 18px 0 0; font-weight: normal; text-align: left; }
.folha strong { font-weight: normal; text-decoration: underline; }
"""


def md_html(text):
    return markdown.markdown(text, extensions=["tables", "sane_lists"])


def chromium(args):
    subprocess.run([CHROMIUM, "--headless=new", "--disable-gpu", "--no-sandbox", *args],
                   check=True, capture_output=True)


def build_pdf(src, dst):
    text = src.read_text(encoding="utf-8")
    m = re.match(r"\s*<!--\s*timbre:\s*(\w+)\s*-->\s*", text)
    timbre = TIMBRES[m.group(1) if m else "nenhum"]
    if m:
        text = text[m.end():]
    html = (f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head>"
            f"<body>{timbre}{md_html(text)}<div class='rodape'>{RODAPE}</div></body></html>")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
    chromium(["--no-pdf-header-footer", f"--print-to-pdf={dst}", f"file://{f.name}"])


def build_manuscrito(src, dst):
    html = (f"<!doctype html><html><head><meta charset='utf-8'><style>{MANUSCRITO_CSS}</style></head>"
            f"<body><div class='folha'>{md_html(src.read_text(encoding='utf-8'))}</div></body></html>")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
    chromium(["--hide-scrollbars", "--window-size=1000,1020", f"--screenshot={dst}", f"file://{f.name}"])


def build_xlsx(src, dst):
    """Uma planilha por CSV. Uma linha `#aba: Nome` comeca uma nova aba."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = src.name.split(".")[0][:31]
    primeira = True
    with src.open(encoding="utf-8") as f:
        for row in csv.reader(f, delimiter=";"):
            if row and row[0].startswith("#aba:"):
                titulo = row[0].removeprefix("#aba:").strip()[:31]
                ws = ws if primeira else wb.create_sheet()
                ws.title = titulo
                primeira = False
                cabecalho = True
                continue
            if primeira:
                primeira, cabecalho = False, True
            ws.append([_num(c) for c in row])
            if cabecalho:
                for c in ws[ws.max_row]:
                    c.font = Font(bold=True)
                    c.fill = PatternFill("solid", fgColor="EEF3F0")
                    c.alignment = Alignment(wrap_text=True, vertical="top")
                cabecalho = False
    for aba in wb.worksheets:
        for col in aba.columns:
            largura = max(len(str(c.value or "")) for c in col)
            aba.column_dimensions[col[0].column_letter].width = min(42, max(12, largura + 2))
    wb.save(dst)


def _num(v):
    try:
        return int(v)
    except ValueError:
        try:
            return float(v.replace(",", "."))
        except ValueError:
            return v


def gerar(src, arquivos):
    name = src.name
    if name.endswith(".pdf.md"):
        dst = arquivos / name.removesuffix(".md")
        build_pdf(src, dst)
    elif name.endswith(".manuscrito.md"):
        dst = arquivos / (name.removesuffix(".manuscrito.md") + ".png")
        build_manuscrito(src, dst)
    elif name.endswith(".xlsx.csv"):
        dst = arquivos / name.removesuffix(".csv")
        build_xlsx(src, dst)
    else:
        dst = arquivos / name
        shutil.copy(src, dst)
    print(f"{src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")


# Na prática 3 o aluno abre a pasta no agente, então o .zip já vem com a pasta de trabalho
# montada: o que o agente lê de referência em base/, o que ele processa em entrada/, e saida/
# vazia. Um arquivo não listado aqui vai para entrada/.
PASTA_AGENTE = {
    "helena-prado": {"base": []},
    "diego-farias": {"base": ["criterios-de-compra.pdf"]},
    "beatriz-lemos": {"base": ["relatorio-outubro-2026.pdf"]},
}


def zipar(persona):
    """Um .zip por persona: os documentos da prática 2 e a pasta de trabalho da prática 3."""
    zips = ROOT / "zips"
    zips.mkdir(exist_ok=True)
    de_base = set(PASTA_AGENTE.get(persona, {}).get("base", []))
    with tempfile.TemporaryDirectory() as tmp:
        raiz = Path(tmp) / persona
        origem2 = ROOT / persona / "pratica-2/arquivos"
        if origem2.exists():
            shutil.copytree(origem2, raiz / "pratica-2-documentos")
        origem3 = ROOT / persona / "pratica-3/arquivos"
        if origem3.exists():
            trabalho = raiz / "pratica-3-pasta-de-trabalho"
            for sub in ("base", "entrada", "saida"):
                (trabalho / sub).mkdir(parents=True)
            (trabalho / "saida/LEIA-ME.txt").write_text(
                "O agente grava aqui o resultado do fluxo.\n", encoding="utf-8")
            for arquivo in sorted(origem3.iterdir()):
                shutil.copy(arquivo, trabalho / ("base" if arquivo.name in de_base else "entrada") / arquivo.name)
        destino = zips / persona
        shutil.make_archive(str(destino), "zip", tmp, persona)
    print(f"zips/{persona}.zip")


def main():
    alvos = [p for p in PERSONAS if not sys.argv[1:] or any(a in p for a in sys.argv[1:])]
    if not alvos:
        sys.exit(f"nenhuma persona casa com {sys.argv[1:]}; use uma de {PERSONAS}")
    for persona in alvos:
        for pratica in PRATICAS:
            fontes = ROOT / persona / pratica / "fontes"
            if not fontes.exists():
                continue
            arquivos = ROOT / persona / pratica / "arquivos"
            arquivos.mkdir(parents=True, exist_ok=True)
            for src in sorted(fontes.iterdir()):
                gerar(src, arquivos)
        zipar(persona)


if __name__ == "__main__":
    main()
