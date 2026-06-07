#!/usr/bin/env python3
"""
Cardápio para a realidade do Fernando.

- Prato brasileiro tradicional (esposa cozinha)
- 4 refeições (café, almoço, LANCHE reforçado, jantar)
- Proteína varia: frango, porco, bovina
- Não sugere comida aleatória: lista opções por refeição pra esposa escolher
"""
from __future__ import annotations
import argparse
import json
import random
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML necessário: apt install python3-yaml", file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).resolve().parent.parent
ESTADO = REPO / "estado.json"
CONFIG = REPO / "config"


# Banco de opções REAIS (prato brasileiro caseiro)
OPCOES = {
    "cafe": {
        "descricao": "Café da manhã — ~500 kcal | P 35g | C 50g | G 15g",
        "opcoes": [
            "2 ovos mexidos + 1 pão integral + 1 fruta (banana/mamão) + café com leite",
            "Tapioca com queijo minas + 1 ovo cozido + 1 fruta",
            "Pão francês (1) + 1 ovo + queijo branco + café com leite",
            "Iogurte natural + aveia + banana + 1 colher de pasta de amendoim",
            "Omelete (2 ovos + queijo) + 1 fatia pão integral + fruta",
        ],
    },
    "almoco": {
        "descricao": "Almoço — ~720 kcal | P 45g | C 110g | G 10g",
        "opcoes": [
            "Frango grelhado + arroz (3 col) + feijão (1 concha) + salada à vontade",
            "Carne bovina (bife/patinho) + arroz + feijão + brócolis refogado + azeite",
            "Porco (lombo/pernil) + arroz + feijão + abobrinha + salada",
            "Frango desfiado + batata-doce + feijão + salada verde",
            "Carne moída + arroz + feijão + chuchu refogado",
            "Tilápia ou salmão + arroz integral + feijão + espinafre + azeite",
        ],
    },
    "lanche": {
        "descricao": "Lanche — ~370 kcal | P 30g | C 25g | G 15g (reforçado pra segurar até o jantar)",
        "opcoes": [
            "1 ovo cozido + 1 banana + 5 castanhas",
            "Pão integral (1) + queijo minas + 1 fruta",
            "Iogurte grego + 1 colher de granola + 1 fruta",
            "Whey (1 scoop) + banana + 1 colher de aveia",
            "Pão integral + peito de peru + queijo branco",
            "2 ovos cozidos + 1 fruta + 5 castanhas do Brasil",
        ],
    },
    "jantar": {
        "descricao": "Jantar — ~680 kcal | P 50g | C 55g | G 25g",
        "opcoes": [
            "Omelete (3 ovos + frango desfiado) + salada verde com azeite",
            "Salmão + brócolis refogado + azeite",
            "Frango grelhado + salada grande + 1 fatia pão integral",
            "Carne magra + abobrinha refogada + azeite",
            "Sopa de legumes com frango desfiado (concha grande)",
            "Tilápia assada + espinafre + 1 fio de azeite + 1 fruta",
        ],
    },
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", default=None, help="ID da fase (ex.: 0-reset). Padrão: fase atual do estado.json")
    ap.add_argument("--tipo", default=None, choices=["treino", "descanso"], help="Tipo de dia")
    ap.add_argument("--random", action="store_true", help="sortear uma opção por refeição (em vez de listar)")
    args = ap.parse_args()

    macros_y = yaml.safe_load((CONFIG / "macros.yaml").read_text(encoding="utf-8"))
    estado = json.loads(ESTADO.read_text(encoding="utf-8"))
    fase = args.fase or estado.get("fase_atual", "0-reset")
    tipo = args.tipo or "treino"

    fase_cfg = macros_y.get("fases", {}).get(fase, {})
    if "treino" in fase_cfg and isinstance(fase_cfg["treino"], dict):
        meta = fase_cfg[tipo]
    else:
        meta = fase_cfg.get("semana_1", {}).get(tipo) or fase_cfg.get("treino")
    if not meta:
        print(f"Não encontrei macros para fase={fase} tipo={tipo}")
        sys.exit(1)

    print(f"# Cardápio — Fase {fase} ({tipo})")
    print(f"# Meta: {meta['kcal']} kcal | P {meta['proteina_g']}g | C {meta['carbo_g']}g | G {meta['gordura_g']}g\n")

    totais = {"cafe": 0, "almoco": 0, "lanche": 0, "jantar": 0}
    for refeicao, cfg in OPCOES.items():
        print(f"## {refeicao.capitalize()}")
        print(f"_{cfg['descricao']}_\n")
        if args.random:
            print(f"- {random.choice(cfg['opcoes'])}")
        else:
            for i, op in enumerate(cfg["opcoes"], 1):
                print(f"{i}. {op}")
        print()

    print("---")
    print("## Lembrete pra esposa")
    print("Escolhe 1 de cada. Proteína do almoço pode ser frango/porco/bovina — varia no dia.")
    print("Sódio: controlar (cuidado cardíaco). Usar sal com moderação, ervas no lugar.")
    print("Azeite: 1 fio por refeição. Gordura boa, protetora.")


if __name__ == "__main__":
    main()
