#!/usr/bin/env python3
"""Custo mensal e por entrega de uma proposta de transporte, a partir da planilha de volumes.

Exemplos:
  python3 custo.py --por-entrega 62 --minimo 500
  python3 custo.py --por-km 6.50 --km-rota 210 --entregas-rota 18
  python3 custo.py --por-entrega 64                      # o contrato atual, para comparar

Lê base/dados/volumes-entrega-2026.csv (separador ';'), usa só a região --regiao
(padrão: Grande SP) e calcula três cenários: o último mês, a média de 6 meses e o
último mês sem o principal cliente (coluna "Entregas Sabor & Cia").
"""
import argparse
import csv
import math
from pathlib import Path

PLANILHA = Path(__file__).resolve().parents[4] / "base" / "dados" / "volumes-entrega-2026.csv"


def custo(entregas, a):
    if a.por_km is not None:
        rotas = math.ceil(entregas / a.entregas_rota)
        return rotas * a.km_rota * a.por_km, f"{rotas} rotas × {a.km_rota} km × R$ {a.por_km:.2f}"
    faturadas = max(entregas, a.minimo or 0)
    return faturadas * a.por_entrega, f"{faturadas} entregas faturadas × R$ {a.por_entrega:.2f}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--por-entrega", type=float)
    p.add_argument("--minimo", type=int, default=0)
    p.add_argument("--por-km", type=float)
    p.add_argument("--km-rota", type=float, default=0)
    p.add_argument("--entregas-rota", type=int, default=1)
    p.add_argument("--regiao", default="Grande SP")
    p.add_argument("--planilha", default=str(PLANILHA))
    a = p.parse_args()
    if (a.por_entrega is None) == (a.por_km is None):
        p.error("informe --por-entrega ou --por-km")

    linhas = [l for l in csv.DictReader(open(a.planilha, encoding="utf-8"), delimiter=";") if l["Região"] == a.regiao]
    meses = [(l["Mês"], int(l["Entregas"]), int(l["Entregas Sabor & Cia"])) for l in linhas]

    print(f"Região: {a.regiao}\n")
    print("Mês        Entregas   Custo")
    total_c = total_e = 0
    for mes, e, _ in meses:
        c, _ = custo(e, a)
        total_c += c
        total_e += e
        print(f"{mes:<10} {e:>8}   R$ {c:>10,.2f}")
    mes, ult, sabor = meses[-1]
    c_ult, conta = custo(ult, a)
    c_sem, conta_sem = custo(ult - sabor, a)
    print(f"\nÚltimo mês ({mes}): {conta} = R$ {c_ult:,.2f}  ({c_ult / ult:,.2f} por entrega)")
    print(f"Média de {len(meses)} meses: R$ {total_c / len(meses):,.2f} por mês  ({total_c / total_e:,.2f} por entrega)")
    print(f"Sem o principal cliente ({ult - sabor} entregas): {conta_sem} = R$ {c_sem:,.2f}  ({c_sem / (ult - sabor):,.2f} por entrega)")


if __name__ == "__main__":
    main()
