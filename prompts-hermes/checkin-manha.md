# Check-in da manhã

**Quando**: 5:35, segunda a sexta.
**Duração**: ≤ 30 segundos de resposta.
**Quem responde**: Fernando.

## Mensagem (template)

```
Bom dia. {{DIA_SEMANA}} {{DATA}}.

1) Peso em jejum (kg): ___
2) Treino hoje? [ ] sim  [ ] não
```

Responde com: `100,8 sim` ou `100,8 não`. Só isso.

## O que o Hermes faz com a resposta

- Grava em `metricas/peso.csv` (linha nova)
- Grava em `metricas/treino.csv` se "sim"
- Recalcula `estado.json` (média 7d, delta semanal, alertas)
- Se for domingo (ou 7 dias desde o último check-in com treino), sugere `decisao/` de revisão semanal
- **NÃO** pergunta mais nada

## Quando o Health Connect estiver configurado

- Peso puxa automático às 5:35 via skill `health_connect` ✅ **ATIVO desde 2026-06-08**
- Check-in vira só: "Treino hoje? [sim/não]" ✅
- Fernando não reporta mais peso manualmente — fonte única é o Health Connect

## Tom

Direto. Sem positividade tóxica. Sem "você está arrasando". Sem "força!".

## Pendências

- [ ] Após Health Connect configurado, automatizar peso
- [ ] Adaptar pra fds (Fernando respondeu que quer check-in só em dia de semana)
