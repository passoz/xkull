# 2026-06-08 — Revisão crítica do plano e meta 78 kg até 31/12

## Contexto

Fernando questionou a meta anterior de 2.250 kcal/dia por considerar alta demais. Informou que na última dieta não passava de 1.800 kcal/dia. Depois pediu uma análise crítica do plano e avaliação da possibilidade de chegar a 78 kg até 31/12/2026.

## Cálculo da meta 78 kg

- Data-base: 2026-06-08
- Peso atual: 99,95 kg
- Meta: 78 kg em 2026-12-31
- Tempo: 206 dias / 29,4 semanas
- Perda necessária: 21,95 kg
- Ritmo necessário: ~0,75 kg/semana
- Déficit médio estimado: ~820 kcal/dia

## Decisão

A meta de 78 kg até 31/12 foi classificada como **possível no papel, mas agressiva**. Será tratada como meta ambiciosa condicional, não promessa. A ordem de prioridade passa a ser:

1. Segurança clínica.
2. Aderência semanal.
3. Preservar força/massa magra.
4. Chegar a 92 kg.
5. Perseguir 78 kg até 31/12 se os dados mostrarem que o ritmo é sustentável.

## Mudanças aplicadas

- `plano.md` reescrito para remover dados antigos/contraditórios.
- Fase 0 deixou de ser descrita como manutenção e virou corte inicial controlado.
- Meta calórica operacional: 1.800 kcal em dia de treino, 1.700 kcal em descanso.
- Proteína passou a operar por faixas: mínimo 130 g, alvo 145–150 g, excelente 160 g.
- `macros.yaml` corrigido para fechar matematicamente.
- `day_reset` deixou de conter jejum 24h automático.
- Criado `metricas/cintura.csv` para medição semanal.

## Observações

Jejum 24h automático foi removido por ser agressivo demais no contexto de IAM/stents/medicação contínua. Qualquer intervenção desse tipo deve ser decisão consciente e, preferencialmente, discutida com médico/nutricionista.
