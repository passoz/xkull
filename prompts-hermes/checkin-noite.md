# Check-in da noite

**Quando**: 21h–22h.
**Duração**: ≤ 3 min.

## Mensagem (template)

```
Fechando o dia.

Treinou? [ ] sim  [ ] não
Jantar: ___
Álcool? [ ] não  [ ] sim — {{TIPO}} {{DOSES}} doses
Vai dormir que horas? __:__
Humor/energia (0-10): ___

[se sono for dormir < 22h]
Boa. Lembrete: tela off 1h antes.

[se treino não foi feito]
Aconteceu o quê? Vamos ajustar amanhã?
```

## Validações automáticas

- Se treinou → registrar em `metricas/treino.csv`.
- Se álcool sim → registrar em `metricas/alcool.csv` com horário e contexto.
- Se kcal do dia estimada (via soma das refeições) → calcular desvio da meta:
  - < 80% → flag "subnutrição" (pedir para revisar).
  - > 110% → flag "excedeu" (não compensar no dia seguinte).
- Atualizar `metricas/sono.csv` (horário que vai dormir é proxy, confirma no dia seguinte).

## Ações após resposta

- Calcular kcal total do dia somando `metricas/refeicoes.csv` (filtro por data).
- Adicionar a `aderencia.media_7d_kcal` em `estado.json`.
- Se sono previsto < 6h E isso repete 3+ dias → consultar `quando-plato.md` (porque sono ruim derruba desempenho).
- Se álcool > meta E 2ª semana seguida → consultar `quando-recaida.md` (versão leve).
