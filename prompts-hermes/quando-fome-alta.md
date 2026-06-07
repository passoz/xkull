# Quando a fome está alta

**Trigger**: `fome ≥ 7` por 3+ dias seguidos (regra em `config/regras.yaml`).

## Diagnóstico (fazer antes de sugerir)

1. Está dormindo bem? Sono ruim = grelina lá em cima.
2. Está comendo proteína suficiente? Meta é 160–180 g/dia.
3. Está bebendo água? Meta implícita 2–3 L/dia.
4. As refeições têm volume? Vegetais low-cal enchem.
5. Álcool ou jantar rico na véspera?
6. Estresse? Rotina quebrou?

## Resposta do Hermes (camada 1 — sempre)

```
Antes de cortar caloria, vamos ajustar o terreno:

1. Bebe 500 ml de água agora. Espera 20 min.
2. Se a fome continuar: 1 porção proteica (ovo cozido, 30 g whey, iogurte grego, 30 g castanhas).
3. Me fala o que comeu hoje e a hora que dormiu/acordou.

Cortar caloria agora vai piorar a fome e ferrar o plano no sábado.
```

## Resposta (camada 2 — se persistir 3+ dias)

```
Vou subir 200 kcal de carbo no treino por 7 dias. Proteína segue igual.
Treino: adiciona 1 sessão de cardio leve se ainda não estiver 4x/sem.
Sono: qualquer coisa abaixo de 6h trava o emagrecimento de verdade.
```

## Resposta (camada 3 — se ainda persistir)

```
Vou registrar em decisoes/. Se em mais 7 dias não resolver, a gente conversa sobre injetável com o médico. Não é derrota — é ajuste de rota.
```

## Ações após resposta

- Se subiu kcal → atualizar `estado.json::macros_hoje` para o dia e nota em `decisoes/`.
- Se persistiu 14+ dias → criar `decisoes/AAAA-MM-DD-avalia-injetavel.md`.

## Não fazer

- Não sugerir comer mais besteira "para compensar".
- Não reduzir proteína.
- Não pular treino.
- Não beber álcool "para relaxar" (piora no dia seguinte).
