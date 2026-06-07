# Quando o peso para (plato)

**Trigger**: média móvel 7d abaixo de 0,3 kg/semana por 2 semanas consecutivas (regra em `config/regras.yaml`).

## Diagnóstico (ordem importa)

1. **Tracking está certo?** Soma de kcal das refeições bate com a meta? Erro comum: subestimar óleo, molhos, "petiscos".
2. **Álcool?** Volta escondida. 3 cervejas = ~450 kcal.
3. **Sono?** < 6h derruba leptina e aumenta grelina.
4. **Treino?** Está fazendo as 4 sessões ou regrediu?
5. **NEAT?** Passos diários caíram? Trabalho mais sedentário?
6. **Estresse?** Cortisol elevado retém água e derruba perda.
7. **Retenção hídrica?** Mulher não é — mas homem também retém (carbo, sal, treino pesado).

## Resposta do Hermes (camada 1)

```
Plato confirmado. Antes de cortar caloria, auditar:

1. Tracking de ontem e anteontem — me joga a lista de refeições crua.
2. Álcool na última semana: ___ doses.
3. Sono médio: ___ h.
4. Treinos feitos: ___/4.
5. Passos médios/dia: ___.

Vou esperar sua resposta para decidir o ajuste.
```

## Resposta (camada 2 — depois da auditoria)

Possíveis ajustes, do menos invasivo ao mais:

| Causa provável | Ajuste |
|---|---|
| Tracking subestimado | Refazer contagem crua, sem "achismo" |
| Álcool | Zerar 2 semanas e reavaliar |
| Sono | Manutenção 1 semana, foco em sono |
| Treino irregular | Cumprir as 4 sessões por 2 semanas |
| NEAT baixo | +2.000 passos/dia (20 min de caminhada) |
| Nenhuma causa clara | –150 kcal OU +1 sessão cardio, manter 14 dias |

## Não fazer

- Não cortar mais de 200 kcal de uma vez.
- Não somar cardio + corte de kcal (pula um de cada vez).
- Não descer abaixo de 1.500 kcal/dia (média semanal).
- Não aumentar treino de musculação — musculação em plato é aliada, não inimiga.

## Ações após resposta

- Registrar em `decisoes/AAAA-MM-DD-ajuste-plato.md` (imutável).
- Atualizar `estado.json::macros_hoje` se houver mudança.
- Marcar `alertas` para reavaliar em 14 dias.
