#!/usr/bin/env python3
"""
Projeta curva de peso até a meta com base na taxa atual.

Uso:
    python3 scripts/projecao.py
    python3 scripts/projecao.py --janela 21   # usa últimos N dias
    python3 scripts/projecao.py --meta 78
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ESTADO = REPO / "estado.json"
METRICAS = REPO / "metricas"
CONFIG = REPO / "config"


def parse_date(s: str) -> date | None:
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def linear_regression(points: list[tuple[float, float]]) -> tuple[float, float]:
    """Retorna (inclinacao_kg_por_dia, intercepto_kg)."""
    n = len(points)
    if n < 2:
        return (0.0, points[0][1] if points else 0.0)
    sx = sum(p[0] for p in points)
    sy = sum(p[1] for p in points)
    sxx = sum(p[0] ** 2 for p in points)
    sxy = sum(p[0] * p[1] for p in points)
    denom = n * sxx - sx * sx
    if denom == 0:
        return (0.0, sy / n)
    m = (n * sxy - sx * sy) / denom
    b = (sy - m * sx) / n
    return (m, b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--janela", type=int, default=14, help="Dias para calcular a taxa")
    ap.add_argument("--meta", type=float, default=None, help="Override da meta em kg")
    args = ap.parse_args()

    estado = json.loads(ESTADO.read_text(encoding="utf-8"))
    meta = args.meta or estado["peso"].get("meta_final_kg", 78.0)
    peso_atual = estado["peso"].get("atual_kg", 0.0)

    peso_path = METRICAS / "peso.csv"
    rows = []
    if peso_path.exists():
        with peso_path.open(encoding="utf-8") as f:
            for r in csv.DictReader(f):
                d = parse_date(r.get("data"))
                try:
                    p = float(r["peso_kg"])
                except (KeyError, ValueError, TypeError):
                    continue
                if d:
                    rows.append((d, p))
    rows.sort()

    if len(rows) < 3:
        print("Histórico insuficiente. Precisa de pelo menos 3 pesagens.")
        return

    hoje = rows[-1][0]
    janela_inicio = hoje - timedelta(days=args.janela - 1)
    pts = [(d.toordinal(), p) for d, p in rows if d >= janela_inicio]
    m, b = linear_regression(pts)
    kg_por_dia = m
    kg_por_semana = kg_por_dia * 7

    if kg_por_dia >= 0:
        print(f"ATENÇÃO: tendência é de ganho ({kg_por_semana:+.3f} kg/sem).")
        print("Plano atual não está gerando déficit. Revisar.")
        return

    dias_ate_meta = (peso_atual - meta) / -kg_por_dia
    data_proj = hoje + timedelta(days=int(dias_ate_meta))

    print("=" * 60)
    print("PROJEÇÃO DE PESO")
    print("=" * 60)
    print(f"Data base:           {hoje.isoformat()}")
    print(f"Peso atual:          {peso_atual:.2f} kg")
    print(f"Meta:                {meta:.2f} kg")
    print(f"Janela de cálculo:   {args.janela} dias ({len(pts)} pesagens)")
    print(f"Tendência:           {kg_por_semana:+.3f} kg/semana")
    print(f"                     {kg_por_dia * 1000:+.2f} g/dia")
    print()
    print(f"Dias até a meta:     {int(dias_ate_meta)}")
    print(f"Data projetada:      {data_proj.isoformat()}")
    print()

    # Projeção semanal visual
    print("Projeção semanal:")
    print("-" * 40)
    for sem in range(0, int(dias_ate_meta / 7) + 1, 2):
        d = sem * 7
        p = peso_atual + kg_por_dia * d
        if p < meta:
            break
        barra = "#" * max(0, int((p - meta) * 2))
        print(f"  +{sem:2d} sem ({hoje + timedelta(days=d)}): {p:6.2f} kg {barra}")
    print("-" * 40)
    print(f"  Meta:               {meta:6.2f} kg")

    # Comparação com cronograma de metas.yaml
    metas_path = CONFIG / "metas.yaml"
    if metas_path.exists():
        import yaml
        metas = yaml.safe_load(metas_path.read_text(encoding="utf-8")) or {}
        for f in metas.get("fases", []):
            if f.get("peso_fim_kg") and f.get("data_fim_prevista"):
                f_meta = f["peso_fim_kg"]
                f_data = datetime.strptime(f["data_fim_prevista"], "%Y-%m-%d").date()
                # peso projetado nessa data
                dias = (f_data - hoje).days
                p_proj = peso_atual + kg_por_dia * dias
                delta = p_proj - f_meta
                sinal = "OK" if delta <= 0.5 else "ATRASADO" if delta > 1.5 else "NO LIMITE"
                print(f"  {f.get('nome', f['id']):20s} meta {f_meta:.1f} em {f['data_fim_prevista']}: proj {p_proj:.1f} [{sinal}]")


if __name__ == "__main__":
    main()
