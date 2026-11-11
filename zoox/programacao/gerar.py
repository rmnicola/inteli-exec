#!/usr/bin/env python3
"""Gera programacao.pdf a partir de fontes/programacao.pdf.md.

É o documento que a plateia anexa ao assistente no workshop de 45 minutos do Zoox Data
Revolution 2026. O conteúdo vem da agenda pública em datarevolution.zooxsmart.com, lida em
11/11/2026; a página avisa que a programação pode mudar sem aviso prévio, então vale reler
na véspera e rodar este script de novo.

O que o documento NÃO traz é de propósito: wifi, estacionamento e a sala de cada atividade
não estão publicados. São eles que fazem o assistente ter de dizer "não sei".

    python3 gerar.py
"""
import re
import shutil
import subprocess
import tempfile
from datetime import date
from pathlib import Path

import markdown

AQUI = Path(__file__).resolve().parent
SAIDA = AQUI / "programacao.pdf"
CHROMIUM = shutil.which("chromium") or shutil.which("google-chrome")

TIMBRE = """<header class="timbre">
  <div class="marca"><span class="logo">◆</span>
    <div><strong>Zoox Data Revolution 2026</strong><small>Dados e inteligência artificial · São Paulo</small></div>
  </div>
  <div class="end">17 de novembro de 2026 · Hotel Unique</div>
</header>"""

CSS = """
@page { size: A4; margin: 16mm 16mm 18mm; }
body { font-family: 'Alegreya Sans', 'Adwaita Sans', sans-serif; font-size: 10pt; line-height: 1.4; color: #1a1c22; }
.timbre { display: flex; justify-content: space-between; align-items: flex-end; padding-bottom: 8px;
  margin-bottom: 18px; border-bottom: 3px solid #1b1f6b; }
.timbre .marca { display: flex; gap: 10px; align-items: center; }
.timbre .logo { color: #1b1f6b; font-size: 22pt; }
.timbre strong { display: block; font-size: 13pt; letter-spacing: .02em; }
.timbre small { color: #5b6066; font-size: 8.5pt; }
.timbre .end { font-size: 8.5pt; color: #5b6066; text-align: right; }
h1 { font-size: 17pt; margin: 0 0 2px; }
h2 { font-size: 12pt; margin: 18px 0 6px; color: #1b1f6b; }
p { margin: 2px 0; }
table { border-collapse: collapse; width: 100%; margin: 6px 0 10px; font-size: 9pt; }
th, td { border: 1px solid #ccd0d8; padding: 4px 7px; text-align: left; vertical-align: top; }
th { background: #eef0f6; }
td:first-child { white-space: nowrap; width: 88px; font-variant-numeric: tabular-nums; }
blockquote { margin: 10px 0 0; padding: 6px 12px; border-left: 3px solid #9aa0b5; background: #f5f6fa;
  font-size: 9pt; color: #4a4f5c; }
.rodape { position: fixed; bottom: -11mm; left: 0; right: 0; font-size: 7.5pt; color: #8a8f99; text-align: center; }
"""


def main():
    fonte = AQUI / "fontes/programacao.pdf.md"
    corpo = markdown.markdown(fonte.read_text(encoding="utf-8"), extensions=["tables", "sane_lists"])
    corpo = re.sub(r"<h1>(.*?)</h1>", r"<h1>\1</h1>", corpo, count=1)
    rodape = f"Programação publicada em datarevolution.zooxsmart.com · versão de {date.today():%d/%m/%Y}"
    html = (f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head>"
            f"<body>{TIMBRE}{corpo}<div class='rodape'>{rodape}</div></body></html>")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
    subprocess.run([CHROMIUM, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={SAIDA}", f"file://{f.name}"],
                   check=True, capture_output=True)
    print(SAIDA)


if __name__ == "__main__":
    main()
