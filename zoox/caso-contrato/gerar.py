#!/usr/bin/env python3
"""Gera contrato-ipe-roxo-kodama.pdf a partir de fontes/contrato.md.

É o documento que a plateia anexa ao assistente no workshop "Monte o seu assistente" do Zoox
Data Revolution 2026. O caso é fictício: a Ipê Roxo (distribuidora de alimentos) recebeu da
Kodama a minuta de um contrato de transformação digital, e quem está na sala faz o papel de um
executivo da Ipê Roxo que precisa analisá-lo antes de assinar.

O que o contrato NÃO traz é de propósito: não há multa nenhuma para atraso da KODAMA (a única
multa por atraso, a da Cláusula 5, é contra a Ipê Roxo). É essa lacuna que obriga o assistente
a dizer "o contrato não trata disso". O gabarito está em perguntas-e-respostas.md.

    python3 gerar.py
"""
import shutil
import subprocess
import tempfile
from pathlib import Path

import markdown

AQUI = Path(__file__).resolve().parent
SAIDA = AQUI / "contrato-ipe-roxo-kodama.pdf"
CHROMIUM = shutil.which("chromium") or shutil.which("google-chrome")

TIMBRE = """<header class="timbre">
  <div class="marca"><span class="logo">▲</span>
    <div><strong>KODAMA</strong><small>Transformação Digital</small></div>
  </div>
  <div class="end">MINUTA · documento para análise<br>Ref. 2026/118</div>
</header>"""

CSS = """
@page { size: A4; margin: 16mm 18mm 18mm; }
body { font-family: 'Alegreya Sans', 'Adwaita Sans', sans-serif; font-size: 9.6pt; line-height: 1.38; color: #1c1d21; }
.timbre { display: flex; justify-content: space-between; align-items: flex-end; padding-bottom: 8px;
  margin-bottom: 14px; border-bottom: 2px solid #3d5a40; }
.timbre .marca { display: flex; gap: 10px; align-items: center; }
.timbre .logo { color: #3d5a40; font-size: 20pt; }
.timbre strong { display: block; font-size: 13pt; letter-spacing: .18em; }
.timbre small { color: #5b6066; font-size: 8.5pt; }
.timbre .end { font-size: 8pt; color: #7a3b3b; text-align: right; font-weight: 600; }
h1 { font-size: 14pt; margin: 0 0 4px; text-align: center; }
h2 { font-size: 10pt; margin: 11px 0 3px; text-transform: uppercase; letter-spacing: .04em; color: #3d5a40; break-after: avoid; }
p { margin: 3px 0; text-align: justify; }
table { border-collapse: collapse; width: 100%; margin-top: 22px; }
th, td { border: 0; padding: 4px 8px; text-align: center; vertical-align: bottom; font-weight: 400; }
.rodape { margin-top: 26px; padding-top: 6px; border-top: 1px solid #ccd0d8; font-size: 7.5pt; color: #8a8f99; text-align: center; }
"""


def main():
    fonte = AQUI / "fontes/contrato.md"
    corpo = markdown.markdown(fonte.read_text(encoding="utf-8"), extensions=["tables", "sane_lists"])
    rodape = ("Caso fictício, criado para o workshop do Inteli Exec. "
              "Ipê Roxo e Kodama não são empresas reais.")
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
