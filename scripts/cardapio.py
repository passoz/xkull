#!/usr/bin/env python3
"""
Gera um cardápio dentro dos macros do dia para a fase atual.

Uso:
    python3 scripts/cardapio.py
    python3 scripts/cardapio.py --fase 1-recorte-a --tipo treino
    python3 scripts/cardapio.py --vegetariano
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
    print("Erro: PyYAML não instalado.", file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).resolve().parent.parent
CONFIG = REPO / "config"
ESTADO = REPO / "estado.json"

# Base de alimentos: kcal, P, C, G por 100 g (ou por unidade)
ALIMENTOS = {
    # Proteínas
    "peito_frango_grelhado": {"kcal": 165, "p": 31, "c": 0, "g": 3.6, "porcao_g": 150},
    "carne_magra_grelhada": {"kcal": 200, "p": 26, "c": 0, "g": 10, "porcao_g": 150},
    "tilapia_assada": {"kcal": 128, "p": 26, "c": 0, "g": 2.7, "porcao_g": 150},
    "salmao_assado": {"kcal": 208, "p": 22, "c": 0, "g": 13, "porcao_g": 150},
    "ovo_cozido": {"kcal": 78, "p": 6, "c": 0.6, "g": 5, "porcao_g": 50},
    "ovo_mexido_2": {"kcal": 188, "p": 13, "c": 2, "g": 14, "porcao_g": 100},
    "whey_scoop": {"kcal": 120, "p": 24, "c": 3, "g": 1.5, "porcao_g": 30},
    "iogurte_grego_natural": {"kcal": 100, "p": 17, "c": 6, "g": 0, "porcao_g": 170},
    "queijo_minas": {"kcal": 240, "p": 17, "c": 3, "g": 17, "porcao_g": 30},
    "peito_peru": {"kcal": 104, "p": 18, "c": 4, "g": 1.5, "porcao_g": 50},
    "atum_lata_agua": {"kcal": 116, "p": 26, "c": 0, "g": 1, "porcao_g": 120},
    # Carboidratos
    "arroz_branco_cozido": {"kcal": 130, "p": 2.7, "c": 28, "g": 0.3, "porcao_g": 100},
    "arroz_integral_cozido": {"kcal": 124, "p": 2.6, "c": 26, "g": 1, "porcao_g": 100},
    "batata_doce_cozida": {"kcal": 86, "p": 1.6, "c": 20, "g": 0.1, "porcao_g": 100},
    "aipim_cozido": {"kcal": 125, "p": 0.6, "c": 30, "g": 0.3, "porcao_g": 100},
    "pao_integral_fatia": {"kcal": 70, "p": 4, "c": 12, "g": 1, "porcao_g": 30},
    "pao_frances": {"kcal": 150, "p": 5, "c": 28, "g": 1.5, "porcao_g": 50},
    "aveia_em_flocos": {"kcal": 389, "p": 17, "c": 66, "g": 7, "porcao_g": 30},
    "tapioca_goma": {"kcal": 240, "p": 0.5, "c": 60, "g": 0.1, "porcao_g": 30},
    "feijao_carioca_cozido": {"kcal": 76, "p": 4.8, "c": 13, "g": 0.5, "porcao_g": 100},
    "lentilha_cozida": {"kcal": 93, "p": 6, "c": 16, "g": 0.5, "porcao_g": 100},
    # Vegetais (low-cal, alto volume)
    "brocolis_cozido": {"kcal": 35, "p": 2.4, "c": 7, "g": 0.4, "porcao_g": 100},
    "espinafre": {"kcal": 23, "p": 2.9, "c": 3.6, "g": 0.4, "porcao_g": 100},
    "abobrinha": {"kcal": 17, "p": 1.2, "c": 3.1, "g": 0.2, "porcao_g": 100},
    "salada_verde": {"kcal": 15, "p": 1, "c": 3, "g": 0.2, "porcao_g": 100},
    "tomate": {"kcal": 18, "p": 1, "c": 4, "g": 0.2, "porcao_g": 100},
    "cenoura": {"kcal": 41, "p": 0.9, "c": 10, "g": 0.2, "porcao_g": 100},
    "almeirao_refogado": {"kcal": 30, "p": 2, "c": 5, "g": 0.5, "porcao_g": 100},
    # Frutas
    "banana": {"kcal": 89, "p": 1.1, "c": 23, "g": 0.3, "porcao_g": 100},
    "maca": {"kcal": 52, "p": 0.3, "c": 14, "g": 0.2, "porcao_g": 150},
    "morango": {"kcal": 32, "p": 0.7, "c": 8, "g": 0.3, "porcao_g": 150},
    "abacate_1_4": {"kcal": 80, "p": 1, "c": 4, "g": 7, "porcao_g": 50},
    # Gorduras
    "azeite_fio": {"kcal": 40, "p": 0, "c": 0, "g": 4.5, "porcao_g": 5},
    "castanha_para": {"kcal": 200, "p": 5, "c": 4, "g": 18, "porcao_g": 15},
    "pasta_amendoim": {"kcal": 188, "p": 8, "c": 7, "g": 16, "porcao_g": 15},
    "manteiga_fina": {"kcal": 36, "p": 0, "c": 0, "g": 4, "porcao_g": 5},
}


def macros_refeicao(meta_total: dict, distribuicao: dict, macros_por_refeicao: dict) -> dict:
    """Calcula macros alvo por refeição."""
    out = {}
    for refeicao, pct in distribuicao.items():
        m_ref = macros_por_refeicao.get(refeicao, {})
        out[refeicao] = {
            "kcal": int(meta_total.get("kcal", 0) * pct),
            "p_pct": m_ref.get("proteina_pct", 0.25),
            "c_pct": m_ref.get("carbo_pct", 0.30),
            "g_pct": m_ref.get("gordura_pct", 0.25),
        }
    return out


def pick(grupo: list[str]) -> str:
    return random.choice(grupo)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", default=None, help="ID da fase (ex.: 1-recorte-a)")
    ap.add_argument("--tipo", default=None, choices=["treino", "descanso"])
    ap.add_argument("--vegetariano", action="store_true")
    args = ap.parse_args()

    macros_y = yaml.safe_load((CONFIG / "macros.yaml").read_text(encoding="utf-8"))
    estado = json.loads(ESTADO.read_text(encoding="utf-8"))
    fase = args.fase or estado.get("fase_atual", "0-reset")
    tipo = args.tipo or "treino"

    fase_cfg = macros_y.get("fases", {}).get(fase, {})
    if tipo not in fase_cfg:
        # fase 2 usa semana_X
        if "semana_1" in fase_cfg:
            meta = fase_cfg["semana_1"].get(tipo)
        else:
            meta = None
    else:
        meta = fase_cfg.get(tipo)
    if not meta:
        print(f"Não encontrei macros para fase={fase} tipo={tipo}")
        sys.exit(1)

    print(f"# Cardápio sugerido — Fase {fase} ({tipo})")
    print(f"Meta: {meta['kcal']} kcal | P {meta['proteina_g']}g | C {meta['carbo_g']}g | G {meta['gordura_g']}g")
    print()

    distribuicao = macros_y.get("distribuicao_refeicoes", {})
    macros_por_refeicao = macros_y.get("distribuicao_macros", {})
    metas_ref = macros_refeicao(meta, distribuicao, macros_por_refeicao)

    # Templates simples
    cardapios = {
        "cafe": {
            "treino": [
                ("3 ovos mexidos com espinafre", "ovo_mexido_2", 1.5, "abacate_1_4", 1),
                ("2 ovos + 30 g whey + 1 banana", "ovo_cozido", 2, "whey_scoop", 1, "banana", 1),
                ("Tapioca com queijo minas + ovo", "tapioca_goma", 2, "queijo_minas", 1, "ovo_cozido", 2),
            ],
            "descanso": [
                ("Aveia com iogurte grego e morangos", "aveia_em_flocos", 0.5, "iogurte_grego_natural", 1, "morango", 0.5),
                ("Omelete com queijo + maçã", "ovo_mexido_2", 1, "queijo_minas", 0.5, "maca", 1),
            ],
        },
        "almoco": {
            "treino": [
                ("Frango grelhado + arroz + feijão + brócolis", "peito_frango_grelhado", 1, "arroz_branco_cozido", 1, "feijao_carioca_cozido", 1, "brocolis_cozido", 1.5),
                ("Carne magra + batata-doce + salada verde", "carne_magra_grelhada", 1, "batata_doce_cozida", 1.5, "salada_verde", 2, "azeite_fio", 1),
                ("Tilápia + arroz integral + abobrinha", "tilapia_assada", 1, "arroz_integral_cozido", 1, "abobrinha", 1.5, "azeite_fio", 1),
            ],
            "descanso": [
                ("Salmão + aipim + espinafre", "salmao_assado", 1, "aipim_cozido", 1, "espinafre", 1.5, "azeite_fio", 1),
                ("Frango + lentilha + brócolis", "peito_frango_grelhado", 1, "lentilha_cozida", 1, "brocolis_cozido", 1.5),
            ],
        },
        "lanche": {
            "treino": [
                ("Whey + banana", "whey_scoop", 1, "banana", 1),
                ("Pão integral + peito de peru + queijo minas", "pao_integral_fatia", 2, "peito_peru", 2, "queijo_minas", 0.5),
                ("Iogurte grego + castanhas", "iogurte_grego_natural", 1, "castanha_para", 0.5),
            ],
            "descanso": [
                ("Ovo cozido + maçã", "ovo_cozido", 2, "maca", 1),
                ("Atum + pão integral", "atum_lata_agua", 0.5, "pao_integral_fatia", 2),
            ],
        },
        "jantar": {
            "treino": [
                ("Omelete com frango desfiado + salada", "ovo_mexido_2", 2, "peito_frango_grelhado", 0.7, "salada_verde", 1.5),
                ("Tilápia + brócolis + azeite", "tilapia_assada", 1, "brocolis_cozido", 2, "azeite_fio", 1),
            ],
            "descanso": [
                ("Salmão + espinafre refogado", "salmao_assado", 1, "espinafre", 1.5, "azeite_fio", 1),
                ("Ovos + almeirão", "ovo_mexido_2", 1.5, "almeirao_refogado", 1.5, "azeite_fio", 1),
            ],
        },
    }

    totais = {"kcal": 0, "p": 0, "c": 0, "g": 0}
    for refeicao in ("cafe", "almoco", "lanche", "jantar"):
        if refeicao not in metas_ref:
            continue
        m = metas_ref[refeicao]
        opcoes = cardapios[refeicao].get(tipo, cardapios[refeicao]["treino"])
        # Filtra vegetariano se necessário
        if args.vegetariano:
            opcoes = [o for o in opcoes if not any("frango" in str(x) or "carne" in str(x) or "tilapia" in str(x) or "salmao" in str(x) or "atum" in str(x) or "peru" in str(x) for x in o)]
        if not opcoes:
            opcoes = cardapios[refeicao]["treino"]

        escolhido = random.choice(opcoes)
        nome = escolhido[0]
        kcal_ref = p_ref = c_ref = g_ref = 0
        # Calcula totais da opção (nome, chave1, qtd1, chave2, qtd2, ...)
        i = 1
        while i < len(escolhido):
            chave = escolhido[i]
            qtd = escolhido[i + 1]
            if chave in ALIMENTOS:
                al = ALIMENTOS[chave]
                kcal_ref += al["kcal"] * qtd
                p_ref += al["p"] * qtd
                c_ref += al["c"] * qtd
                g_ref += al["g"] * qtd
            i += 2
        totais["kcal"] += kcal_ref
        totais["p"] += p_ref
        totais["c"] += c_ref
        totais["g"] += g_ref
        print(f"## {refeicao.capitalize()} (~{int(kcal_ref)} kcal | P {p_ref:.0f} | C {c_ref:.0f} | G {g_ref:.0f})")
        print(f"  → {nome}")
        print()

    print("---")
    print(f"Total estimado: {int(totais['kcal'])} kcal | P {totais['p']:.0f}g | C {totais['c']:.0f}g | G {totais['g']:.0f}g")
    print(f"Meta:           {meta['kcal']} kcal | P {meta['proteina_g']}g | C {meta['carbo_g']}g | G {meta['gordura_g']}g")
    delta_kcal = totais["kcal"] - meta["kcal"]
    if abs(delta_kcal) < 50:
        print("Status: ✅ dentro da meta")
    else:
        print(f"Status: ⚠️ delta de {delta_kcal:+.0f} kcal — ajuste porções no cardápio escolhido")
    print()
    print("Lista de compras (sugestão):")
    print("(Cardápio é uma BASE — ajuste as porções ±30% para fechar a meta calórica.)")
    compras = [
        "ovos (1 dúzia)", "peito de frango (1 kg)", "carne magra (500 g)",
        "tilápia ou salmão (500 g)", "iogurte grego natural (4 un)",
        "whey (1 pote)", "queijo minas (1 un)", "peito de peru (1 pacote)",
        "arroz branco (1 kg)", "arroz integral (500 g)", "batata-doce (500 g)",
        "aipim (500 g)", "aveia em flocos (500 g)", "feijão carioca (1 kg)",
        "lentilha (500 g)", "tapioca (1 pacote)",
        "brócolis, espinafre, abobrinha, alface, tomate",
        "banana, maçã, morango, abacate", "castanhas (200 g)",
        "azeite, manteiga, pasta de amendoim",
    ]
    for c in compras:
        print(f"  - {c}")


if __name__ == "__main__":
    main()
