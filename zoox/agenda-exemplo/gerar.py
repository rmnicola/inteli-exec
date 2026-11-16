#!/usr/bin/env python3
"""Gera a agenda de exemplo da sessão "Ferramentas em ação" do Zoox Data Revolution 2026.

É para quem não pode ou não quer conectar a própria agenda ao assistente. A persona é a
Helena Prado, diretora de operações da Ipê Roxo (a mesma empresa fictícia do caso do contrato),
na semana de 16 a 20 de novembro de 2026. Uma fonte só (EVENTOS, abaixo), duas saídas:

- agenda-ipe-roxo.pdf: a semana em colunas, para anexar na conversa (funciona em qualquer app);
- agenda-ipe-roxo.ics: os mesmos eventos, para importar numa agenda NOVA (não na sua).

O que a semana traz de propósito:
- terça às 10h há dois compromissos ao mesmo tempo (comitê de compras e a call com a Kodama);
- quarta às 17h há um compromisso "Particular": o assistente não deve marcar nada por cima nem expor;
- janelas livres de 1h30 ou mais, em horário comercial (8h às 18h): quarta 13h30–15h,
  quinta 15h–16h30 (mas ela passa o dia no CD), sexta 13h–15h e sexta 16h–18h. Nenhuma na segunda nem na terça.

    python3 gerar.py
"""
import shutil
import subprocess
import tempfile
from datetime import datetime
from html import escape
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PDF = AQUI / "agenda-ipe-roxo.pdf"
ICS = AQUI / "agenda-ipe-roxo.ics"
CHROMIUM = shutil.which("chromium") or shutil.which("google-chrome")

PESSOA = "Helena Prado"
CARGO = "Diretora de Operações · Ipê Roxo Distribuição de Alimentos"

DIAS = {16: "Segunda, 16/11", 17: "Terça, 17/11", 18: "Quarta, 18/11", 19: "Quinta, 19/11", 20: "Sexta, 20/11"}

# (dia, início, fim, título, local, o que preparar). Início vazio = dia inteiro.
EVENTOS = [
    (16, "08:30", "09:30", "Reunião semanal da diretoria", "Sala do conselho", "Trazer os números de entrega da semana passada."),
    (16, "10:00", "11:00", "1:1 com Rafael Souza (gerente de logística)", "Sala da diretoria", "Rever o atraso das rotas do interior."),
    (16, "12:00", "13:30", "Almoço", "", ""),
    (16, "14:00", "17:00", "Visita ao CD de Jundiaí", "CD Jundiaí (1h de deslocamento incluída)", "Checklist de segurança assinado pelo gerente do CD."),
    (17, "08:00", "09:00", "Café com fornecedor de embalagens (Plastimax)", "Escritório", "Proposta de reajuste de 2027 que eles mandaram."),
    (17, "09:30", "11:00", "Comitê de compras", "Sala do conselho", "Aprovar o pedido de paletes do 1º trimestre."),
    (17, "10:00", "10:30", "Call com a Kodama: dúvidas sobre a minuta", "Online", "Lista de dúvidas do jurídico sobre as cláusulas 3, 10 e 14."),
    (17, "12:00", "13:00", "Almoço", "", ""),
    (17, "14:00", "15:30", "Revisão dos indicadores do trimestre", "Sala da diretoria", "Painel de OTIF e ruptura por região."),
    (17, "16:00", "17:00", "Entrevista: coordenador(a) de TI", "Online", "Currículo e o caso técnico enviados pelo RH."),
    (18, "09:00", "11:00", "Jurídico: análise do contrato Kodama", "Sala do jurídico", "Minuta impressa com os comentários da diretoria."),
    (18, "11:30", "12:00", "Aprovar a escala de fim de ano dos CDs", "Sala da diretoria", "Escala proposta pelo RH."),
    (18, "12:00", "13:30", "Almoço com cliente (Supermercados Serra Azul)", "Restaurante, centro de Campinas", "Histórico de pedidos do cliente em 2026."),
    (18, "15:00", "16:00", "1:1 com o CFO", "Sala do CFO", "Orçamento de operações 2027, versão 2."),
    (18, "17:00", "18:00", "Particular", "", ""),
    (19, "", "", "Inventário anual do CD Campinas (o dia todo no CD)", "CD Campinas", ""),
    (19, "08:00", "12:00", "Inventário: acompanhamento presencial", "CD Campinas", "Botas e colete; a auditoria externa chega às 8h."),
    (19, "13:00", "14:00", "Almoço", "", ""),
    (19, "14:30", "15:00", "Ponto rápido com o RH", "Online", "Duas promoções pendentes da logística."),
    (19, "16:30", "17:30", "Preparação para a assinatura, com o CEO", "Sala do CEO", "Resumo dos riscos do contrato Kodama, uma página."),
    (20, "08:30", "09:30", "Diretoria: decisão sobre o contrato Kodama", "Sala do conselho", "Recomendação final: assinar, renegociar ou não assinar."),
    (20, "10:00", "11:00", "Assinatura do contrato Kodama", "Sala do conselho", "Versão final revisada pelo jurídico."),
    (20, "12:00", "13:00", "Almoço", "", ""),
    (20, "15:00", "16:00", "Fechamento semanal com os gerentes", "Online", "Pendências da semana de cada CD."),
]

CSS = """
@page { size: A4 landscape; margin: 12mm 12mm 14mm; }
body { font-family: 'Alegreya Sans', 'Adwaita Sans', sans-serif; font-size: 8.6pt; line-height: 1.3; color: #1c1d21; }
header { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2px solid #5b3a7a; padding-bottom: 6px; margin-bottom: 10px; }
header h1 { font-size: 15pt; margin: 0; }
header p { margin: 0; color: #5b6066; }
header .sem { text-align: right; font-weight: 700; color: #5b3a7a; }
.semana { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
.dia h2 { font-size: 10pt; margin: 0 0 6px; padding: 4px 6px; background: #efe9f5; color: #5b3a7a; }
.ev { border-left: 3px solid #5b3a7a; background: #fafafc; padding: 4px 6px; margin-bottom: 6px; break-inside: avoid; }
.ev.inteiro { border-left-color: #c98a2b; background: #fdf6ea; }
.ev.particular { border-left-color: #9aa0ab; color: #5b6066; }
.ev b { display: block; }
.ev .h { font-variant-numeric: tabular-nums; font-weight: 700; }
.ev .l { color: #5b6066; }
.ev .p { margin-top: 2px; }
.rodape { margin-top: 10px; font-size: 7.5pt; color: #8a8f99; text-align: center; }
"""


def html():
    colunas = []
    for d, nome in DIAS.items():
        itens = []
        evs = sorted((e for e in EVENTOS if e[0] == d), key=lambda e: e[1] or "00:00")
        for _, ini, fim, tit, local, prep in evs:
            cls = "ev inteiro" if not ini else ("ev particular" if tit == "Particular" else "ev")
            h = "Dia inteiro" if not ini else f"{ini}–{fim}"
            partes = [f'<span class="h">{h}</span>', f"<b>{escape(tit)}</b>"]
            if local:
                partes.append(f'<span class="l">{escape(local)}</span>')
            if prep:
                partes.append(f'<div class="p">Preparar: {escape(prep)}</div>')
            itens.append(f'<div class="{cls}">{"".join(partes)}</div>')
        colunas.append(f'<div class="dia"><h2>{nome}</h2>{"".join(itens)}</div>')
    return (f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head><body>"
            f"<header><div><h1>Agenda de {PESSOA}</h1><p>{CARGO}</p></div>"
            f"<p class='sem'>Semana de 16 a 20 de novembro de 2026<br>Horário comercial: 8h às 18h</p></header>"
            f"<div class='semana'>{''.join(colunas)}</div>"
            f"<p class='rodape'>Agenda fictícia, criada para o workshop do Inteli Exec. Helena Prado, Ipê Roxo e Kodama não existem.</p>"
            f"</body></html>")


def ics():
    def dt(d, hm):
        return f"202611{d:02d}T{hm.replace(':', '')}00"
    linhas = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Inteli Exec//Agenda de exemplo//PT-BR",
              "CALSCALE:GREGORIAN", "X-WR-CALNAME:Agenda de exemplo (Helena Prado)", "X-WR-TIMEZONE:America/Sao_Paulo"]
    carimbo = datetime(2026, 11, 16, 12, 0).strftime("%Y%m%dT%H%M%SZ")
    for i, (d, ini, fim, tit, local, prep) in enumerate(EVENTOS):
        linhas += ["BEGIN:VEVENT", f"UID:ipe-roxo-{i}@inteli-exec", f"DTSTAMP:{carimbo}"]
        if ini:
            linhas += [f"DTSTART;TZID=America/Sao_Paulo:{dt(d, ini)}", f"DTEND;TZID=America/Sao_Paulo:{dt(d, fim)}"]
        else:
            linhas += [f"DTSTART;VALUE=DATE:202611{d:02d}", f"DTEND;VALUE=DATE:202611{d + 1:02d}"]
        linhas.append(f"SUMMARY:{tit}")
        if local:
            linhas.append(f"LOCATION:{local}")
        if prep:
            linhas.append(f"DESCRIPTION:Preparar: {prep}")
        if tit == "Particular":
            linhas.append("CLASS:PRIVATE")
        linhas.append("END:VEVENT")
    linhas.append("END:VCALENDAR")
    ICS.write_text("\r\n".join(linhas) + "\r\n", encoding="utf-8")


def main():
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html())
    subprocess.run([CHROMIUM, "--headless=new", "--disable-gpu", "--no-sandbox",
                    "--no-pdf-header-footer", f"--print-to-pdf={PDF}", f"file://{f.name}"],
                   check=True, capture_output=True)
    ics()
    print(PDF)
    print(ICS)


if __name__ == "__main__":
    main()
