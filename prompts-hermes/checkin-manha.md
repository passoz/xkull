# Check-in da manhã

**Quando**: 7h–9h (escolher um horário fixo, sugerir 7:30).
**Duração**: ≤ 2 min de resposta do usuário.

## Mensagem (template)

```
Bom dia. Dia {{N}} do plano, semana {{S}}, fase {{FASE}}.

Peso em jejum: ___ kg
Ontem, sono: ___ h
Treino hoje: {{TIPO}} (esperado: {{ESPERADO}})
Meta kcal: {{KCAL}} | P: {{P}}g | C: {{C}}g | G: {{G}}g

[se sono ruim ontem]
Sono curto ontem. Toca o treino leve hoje (50% da carga) ou substitui por caminhada 30 min?

[se álcool acima da meta na semana]
Álcool acima da meta {{N}} semanas seguidas. Bora zerar essa semana inteira?

[se for início de fase ou semana]
Mudança na rotina essa semana: {{NOTA}}
```

## Dados que Hermes precisa ter em mãos

- `estado.json` → peso_atual, tipo_dia, macros, sono_ultimo, alcool_semana
- `config/macros.yaml` → macros do dia
- `prompts-hermes/` → se houver nota especial

## Saída esperada do usuário

- Confirmar/ajustar peso
- Confirmar que vai treinar (ou indicar troca)
- Sinalizar algo fora do padrão

## Ações após resposta

- Atualizar `metricas/peso.csv`
- Se sono < 6h por 3+ dias seguidos → adicionar à `alertas` em `estado.json`
- Se treino confirmado → nada extra; se cancelado → notificar à noite para compensação
