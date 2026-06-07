# Acompanhamento de Emagrecimento — 101 → 92 → 78

Repo de tracking e plano de recompromisso. O **Hermes** lê e escreve aqui para acompanhar o dia a dia.

## Visão rápida

- **Início**: 2026-06-07 (domingo), 101 kg.
- **Fase atual**: `0-reset` (semanas 1–2, manutenção, foco em reativar).
- **Meta intermediária**: 92 kg em ~4,5 meses.
- **Meta final**: 78 kg em ~10 meses.
- **Sem medicação** por 30 dias a partir do início. Decisão sobre injetável no mês 2.

## Estrutura

```
.
├── README.md                este arquivo
├── plano.md                 plano macro completo
├── estado.json              fonte de verdade (Hermes lê primeiro)
├── registro_emagrecimento.md histórico bruto desde 110 kg
│
├── config/                  biometria, metas, macros, regras
├── diario/                  log diário (YYYY-MM-DD.md)
├── semanas/                 revisão semanal (YYYY-Www.md)
├── metricas/                CSVs (peso, refeições, treino, fome, sono, medidas, álcool)
├── decisoes/                log de ajustes no plano
├── prompts-hermes/          playbooks que o Hermes consulta
└── scripts/                 estado.py, projecao.py, cardapio.py
```

## Contrato com o Hermes

### O que o Hermes lê primeiro
1. `estado.json` — estado atual consolidado.
2. `config/regras.yaml` — thresholds das decisões automáticas.
3. `plan.md` — estratégia macro.

### O que o Hermes lê para contexto
- Último arquivo em `semanas/`.
- CSVs em `metricas/` para tendência e aderência.
- `prompts-hermes/` para decidir o tom e a estrutura das mensagens.

### O que o Hermes escreve
- `diario/AAAA-MM-DD.md` (1 por dia, idempotente — não duplica).
- Linhas novas nos CSVs de `metricas/`.
- Sugestão de conteúdo para `semanas/AAAA-Www.md` (humano confirma).

### O que o Hermes **não** sobrescreve
- `decisoes/` — só cria arquivo novo.
- `config/*.yaml` — pede confirmação antes de mexer.
- `estado.json` — só `scripts/estado.py` (que é determinístico) pode regenerar.

### Tom
Direto, sem positividade tóxica, foco em comportamento do dia, não em resultado. "Você treina hoje?" é melhor que "Você está arrasando!".

## Como rodar os scripts

```bash
# Recalcular estado.json a partir dos CSVs
python3 scripts/estado.py

# Projetar curva de peso até a meta
python3 scripts/projecao.py

# Gerar cardápio dentro dos macros do dia
python3 scripts/cardapio.py --fase 1-recorte-a --tipo treino
```

Não há dependências externas — só a stdlib do Python 3.10+.

## Regras de ouro (não negociáveis)

1. **Proteína primeiro** — 1,6–2,0 g/kg de massa magra estimada (~160–180 g/dia).
2. **Álcool = moeda de troca** — zero nas Fases 0 e 1; máx 2 doses/sem na Fase 3+.
3. **Treino 4x/semana é o piso** (Fases 1+).
4. **Média móvel de 7 dias**, não o peso do dia.
5. **Reverse diet obrigatório** entre fases de corte.
6. **Plato de 2 semanas = ajuste automático** (Hermes aplica).
