#!/usr/bin/env python3
"""
Recalcula estado.json a partir dos CSVs de metricas/.
Aplica as regras de config/regras.yaml e gera semanas/AAAA-Www.md.

Uso:
    python3 scripts/estado.py                # recalcula e atualiza
    python3 scripts/estado.py --dry-run      # só mostra, não grava
    python3 scripts/estado.py --print        # imprime resumo sem alterar nada
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Erro: PyYAML não instalado. Rode: apt install python3-yaml", file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).resolve().parent.parent
ESTADO = REPO / "estado.json"
CONFIG = REPO / "config"
METRICAS = REPO / "metricas"
SEMANAS = REPO / "semanas"
TEMPLATE_SEMANA = SEMANAS / "template-semana.md"


def iso_week(d: date) -> str:
    y, w, _ = d.isocalendar()
    return f"{y}-W{w:02d}"


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_date(s: str) -> date | None:
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def ultimos_n_dias(rows: list[dict], n: int) -> list[dict]:
    """Filtra últimos N dias a partir de hoje."""
    if not rows:
        return []
    datas = [parse_date(r["data"]) for r in rows if parse_date(r.get("data"))]
    datas = [d for d in datas if d is not None]
    if not datas:
        return []
    hoje = max(datas)  # usar a data mais recente dos dados, não hoje do sistema
    limite = hoje - timedelta(days=n - 1)
    return [r for r in rows if (d := parse_date(r.get("data"))) and d >= limite]


def media(valores: list[float]) -> float | None:
    vals = [v for v in valores if v is not None]
    return sum(vals) / len(vals) if vals else None


def soma_refeicoes_por_dia(rows: list[dict]) -> dict[date, dict]:
    """Agrega kcal/proteina/carbo/gordura por dia."""
    agg: dict[date, dict] = defaultdict(
        lambda: {"kcal": 0.0, "proteina_g": 0.0, "carbo_g": 0.0, "gordura_g": 0.0}
    )
    for r in rows:
        d = parse_date(r.get("data"))
        if not d:
            continue
        for k in ("kcal", "proteina_g", "carbo_g", "gordura_g"):
            try:
                agg[d][k] += float(r.get(k) or 0)
            except ValueError:
                pass
    return agg


def calcular_peso(rows: list[dict], hoje: date) -> dict:
    rows7 = ultimos_n_dias(rows, 7)
    if not rows7:
        return {"media_7d_kg": None, "delta_semanal_kg": None, "ultimo_kg": None}

    pesos = []
    for r in rows7:
        try:
            pesos.append((parse_date(r["data"]), float(r["peso_kg"])))
        except (KeyError, ValueError, TypeError):
            continue
    pesos.sort()

    if not pesos:
        return {"media_7d_kg": None, "delta_semanal_kg": None, "ultimo_kg": None}

    media_7d = media([p[1] for p in pesos])
    ultimo = pesos[-1][1]

    # Delta: comparar com a semana anterior (dias 8-14 atrás)
    rows14 = ultimos_n_dias(rows, 14)
    pesos_ant = []
    for r in rows14:
        d = parse_date(r["data"])
        try:
            p = float(r["peso_kg"])
        except (KeyError, ValueError, TypeError):
            continue
        if d and (hoje - d).days >= 7:
            pesos_ant.append(p)
    media_ant = media(pesos_ant)
    delta = (media_7d - media_ant) if (media_7d and media_ant) else None

    return {
        "media_7d_kg": round(media_7d, 2) if media_7d else None,
        "delta_semanal_kg": round(delta, 3) if delta is not None else None,
        "ultimo_kg": round(ultimo, 2),
    }


def calcular_aderencia_kcal(
    refeicoes: list[dict], regras: dict, macros: dict
) -> dict:
    """Calcula aderência de kcal vs meta da fase atual."""
    agg = soma_refeicoes_por_dia(refeicoes)
    if not agg:
        return {"media_7d_kcal": None, "dias_aderentes": 0, "janela_pct": 10}

    janela_pct = regras.get("aderencia", {}).get("janela_kcal_aceitavel_pct", 10)
    ult7 = sorted(agg.keys())[-7:]
    kcals = [agg[d]["kcal"] for d in ult7]
    media_kcal = media(kcals)
    return {
        "media_7d_kcal": round(media_kcal, 0) if media_kcal else None,
        "dias_aderentes": 0,
        "janela_pct": janela_pct,
    }


def calcular_treino(rows: list[dict]) -> int:
    rows7 = ultimos_n_dias(rows, 7)
    return sum(
        1
        for r in rows7
        if r.get("completou", "").strip().lower() in ("sim", "s", "true", "1")
    )


def calcular_alcool(rows: list[dict]) -> int:
    rows7 = ultimos_n_dias(rows, 7)
    total = 0
    for r in rows7:
        try:
            total += int(r.get("doses") or 0)
        except ValueError:
            pass
    return total


def calcular_sono(rows: list[dict]) -> float | None:
    rows7 = ultimos_n_dias(rows, 7)
    vals = []
    for r in rows7:
        try:
            vals.append(float(r.get("horas") or 0))
        except ValueError:
            pass
    return round(media(vals), 2) if vals else None


def calcular_fome(rows: list[dict]) -> float | None:
    rows7 = ultimos_n_dias(rows, 7)
    vals = []
    for r in rows7:
        try:
            vals.append(float(r.get("nivel_0_10") or 0))
        except ValueError:
            pass
    return round(media(vals), 2) if vals else None


def calcular_cintura(rows: list[dict]) -> float | None:
    """Última medida de cintura (não necessariamente da semana)."""
    if not rows:
        return None
    ultima = max(
        (r for r in rows if parse_date(r.get("data"))),
        key=lambda r: parse_date(r["data"]),
        default=None,
    )
    if not ultima:
        return None
    try:
        return float(ultima.get("cintura_cm") or 0)
    except ValueError:
        return None


def aplicar_regras(estado: dict, regras: dict, peso_info: dict) -> list[str]:
    alertas = []
    cfg_peso = regras.get("peso", {})
    queda_min = cfg_peso.get("queda_minima_aceitavel_kg_sem", 0.3)
    plato_sem = cfg_peso.get("plato_semanas_para_ajustar", 2)
    regain_kg = cfg_peso.get("regain_2_semanas_kg", 1.0)

    delta = peso_info.get("delta_semanal_kg")
    if delta is not None:
        if delta < -queda_min:
            pass  # OK
        elif delta < 0:
            alertas.append(
                f"PLATO: queda de {delta:.2f} kg/sem abaixo de {queda_min:.2f} por 1+ semana. "
                f"Se repetir semana que vem, ajustar."
            )
        elif delta > 0.1:
            alertas.append(
                f"REGAIN: peso subiu {delta:.2f} kg/sem. Acompanhar; se ≥ {regain_kg} kg em 2 semanas, day-reset."
            )

    sono_meta = regras.get("sono", {}).get("minimo_horas", 6)
    sono_atual = estado.get("sono", {}).get("media_7d_horas")
    if sono_atual is not None and sono_atual < sono_meta:
        alertas.append(
            f"SONO: média {sono_atual:.1f} h (meta {sono_meta} h). Sono ruim sabota o plano."
        )

    cfg_fome = regras.get("fome", {})
    if cfg_fome:
        fome_atual = estado.get("fome", {}).get("media_7d")
        if fome_atual is not None and fome_atual >= cfg_fome.get("threshold_alto", 7):
            alertas.append(
                f"FOME ALTA: média {fome_atual:.1f}/10. Se persistir 3+ dias, ajustar macros."
            )

    cfg_alcool = regras.get("alcool", {})
    meta_alcool = cfg_alcool.get(f"meta_{estado.get('fase_atual', '0-reset')}", 0)
    alcool = estado.get("alcool", {}).get("consumido_semana", 0)
    if alcool > meta_alcool:
        alertas.append(
            f"ÁLCOOL: {alcool} doses na semana (meta {meta_alcool}). Revisar gatilho."
        )

    return alertas


def gerar_arquivo_semana(estado: dict, regras: dict, hoje: date) -> Path:
    iso = iso_week(hoje)
    path = SEMANAS / f"{iso}.md"
    if not TEMPLATE_SEMANA.exists():
        return path
    tpl = TEMPLATE_SEMANA.read_text(encoding="utf-8")
    meta_treinos = estado.get("treino", {}).get("meta_semanal", 4)
    fase = estado.get("fase_atual", "")
    macros_fase = {}
    try:
        macros_y = load_yaml(CONFIG / "macros.yaml")
        macros_fase = macros_y.get("fases", {}).get(fase, {}).get("treino", {})
    except Exception:
        pass

    conteudo = (
        tpl.replace("{{ISO_WEEK}}", iso)
        .replace("{{DATA_INICIO}}", (hoje - timedelta(days=6)).isoformat())
        .replace("{{DATA_FIM}}", hoje.isoformat())
        .replace("{{META_TREINOS}}", str(meta_treinos))
        .replace("{{NOME_FASE}}", estado.get("fase_nome", ""))
        .replace("{{META_KCAL}}", str(macros_fase.get("kcal", "")))
        .replace("{{META_PROT}}", str(macros_fase.get("proteina_g", "")))
        .replace("{{META_CARB}}", str(macros_fase.get("carbo_g", "")))
        .replace("{{META_GORD}}", str(macros_fase.get("gordura_g", "")))
    )
    if not path.exists():
        path.write_text(conteudo, encoding="utf-8")
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--print", action="store_true")
    args = ap.parse_args()

    estado = load_json(ESTADO)
    regras = load_yaml(CONFIG / "regras.yaml")
    metas = load_yaml(CONFIG / "metas.yaml")
    macros = load_yaml(CONFIG / "macros.yaml")

    peso_rows = read_csv(METRICAS / "peso.csv")
    ref_rows = read_csv(METRICAS / "refeicoes.csv")
    treino_rows = read_csv(METRICAS / "treino.csv")
    fome_rows = read_csv(METRICAS / "fome.csv")
    sono_rows = read_csv(METRICAS / "sono.csv")
    medidas_rows = read_csv(METRICAS / "medidas.csv")
    alcool_rows = read_csv(METRICAS / "alcool.csv")

    datas_existentes = [
        parse_date(r["data"]) for r in peso_rows if parse_date(r.get("data"))
    ]
    hoje = max(datas_existentes) if datas_existentes else date.today()

    peso_info = calcular_peso(peso_rows, hoje)
    ader = calcular_aderencia_kcal(ref_rows, regras, macros)
    treinos_feitos = calcular_treino(treino_rows)
    alcool = calcular_alcool(alcool_rows)
    sono = calcular_sono(sono_rows)
    fome = calcular_fome(fome_rows)
    cintura = calcular_cintura(medidas_rows)

    # Atualiza estado em memória
    estado["data_atualizacao"] = hoje.isoformat()
    estado["peso"]["media_7d_kg"] = peso_info["media_7d_kg"]
    estado["peso"]["delta_semanal_kg"] = peso_info["delta_semanal_kg"]
    if peso_info["ultimo_kg"] is not None:
        estado["peso"]["atual_kg"] = peso_info["ultimo_kg"]
    estado["aderencia"]["media_7d_kcal"] = ader["media_7d_kcal"]
    estado["treino"]["feitas_semana"] = treinos_feitos
    estado["alcool"]["consumido_semana"] = alcool
    estado["sono"]["media_7d_horas"] = sono
    estado["fome"]["media_7d"] = fome
    if cintura is not None:
        estado["peso"]["cintura_cm"] = cintura

    alertas = aplicar_regras(estado, regras, peso_info)
    # Mantém só alertas não resolvidos
    antigos = estado.get("alertas", []) or []
    resolvidos = {"inicio_plano"}
    estado["alertas"] = [a for a in antigos if a in resolvidos] + alertas
    estado["ultima_revisao_semanal"] = hoje.isoformat()

    resumo = {
        "data": hoje.isoformat(),
        "peso_ultimo_kg": peso_info["ultimo_kg"],
        "peso_media_7d_kg": peso_info["media_7d_kg"],
        "delta_semanal_kg": peso_info["delta_semanal_kg"],
        "kcal_media_7d": ader["media_7d_kcal"],
        "treinos_feitos": treinos_feitos,
        "treino_meta": estado["treino"].get("meta_semanal"),
        "alcool_total": alcool,
        "alcool_meta": 0,
        "sono_media_h": sono,
        "fome_media": fome,
        "cintura_cm": cintura,
        "alertas": alertas,
    }

    if args.print or args.dry_run:
        print(json.dumps(resumo, indent=2, ensure_ascii=False))
        return

    gerar_arquivo_semana(estado, regras, hoje)
    save_json(ESTADO, estado)
    print(json.dumps(resumo, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
