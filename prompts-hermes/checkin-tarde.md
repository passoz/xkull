# Check-in da tarde

**Quando**: 14h–16h.
**Duração**: ≤ 1 min.

## Mensagem (template)

```
Check-in rápido.

Almoço: o que comeu? (uma linha)
Fome agora (0-10): ___
Plano pro lanche: {{LANCHE_SUGERIDO}}

Lembrete: treino {{TREINO_HOJE}} às {{HORA_TREINO}}.
```

## Sinais para Hermes ativar estratégia extra

- Se fome ≥ 7 → consultar `quando-fome-alta.md` e adicionar dica.
- Se usuário relatar "como besteira no almoço" → não julgar, perguntar o que aconteceu antes (privação de sono, estresse, álcool de ontem?).
- Se for dia de treino e lanche ainda não planejado → sugerir a proteína de pós-treino (whey + fruta).

## Ações após resposta

- Atualizar `metricas/refeicoes.csv` (linha do almoço)
- Atualizar `metricas/fome.csv`
- Se treino marcado para essa tarde → nada extra
- Se treino já foi feito → parabenizar seco ("fez. segue o dia."), atualizar `metricas/treino.csv`
