# Revisão semanal

**Quando**: domingo, 19h–20h.
**Quem executa**: `scripts/estado.py` + intervenção manual.

## Fluxo

1. **Calcular** (automatizado):
   - Média móvel 7d do peso
   - Delta semanal vs semana anterior
   - Aderência de kcal, treino, álcool, sono
   - Cintura (se mediu)
   - Fome média

2. **Aplicar regras** (automatizado, via `config/regras.yaml`):
   - Plato → propor corte 150 kcal ou +1 cardio
   - Fome alta sustentada → propor +200 kcal carbo no treino
   - Sono ruim → propor pausa do déficit
   - Álcool excessivo → propor semana de zerar

3. **Gerar arquivo** `semanas/AAAA-Www.md` a partir de `template-semana.md`.

4. **Mensagem do Hermes** (domingo 20h):

```
Semana {{S}} fechou.

Peso: {{DELTA}} kg ({{DIRECAO}} vs semana passada)
Média móvel 7d: {{MEDIA}} kg
Treinos: {{FEITOS}}/{{META}}
Álcool: {{TOTAL}} doses (meta: {{META}})
Sono médio: {{HORAS}} h
Fome média: {{NIVEL}}/10

[se alerta]
{{TEXTO_DO_ALERTA}}

Próxima semana: {{ACAO}}
```

5. **Confirmação humana**: usuário lê `semanas/AAAA-Www.md`, edita se quiser, commita.

## Arquivos a consultar

- `metricas/peso.csv` (últimos 7 dias)
- `metricas/refeicoes.csv` (agregado diário)
- `metricas/treino.csv`
- `metricas/alcool.csv`
- `metricas/sono.csv`
- `metricas/medidas.csv`
- `metricas/fome.csv`
- `config/regras.yaml`
- `config/metas.yaml` (critérios de saída da fase)
- `estado.json` (semana anterior para delta)

## Saída do `scripts/estado.py`

- Atualiza `estado.json` com:
  - `peso.media_7d_kg`
  - `peso.delta_semanal_kg`
  - `aderencia.media_7d_kcal`
  - `fome.media_7d`
  - `sono.media_7d_horas`
  - `alertas: []` (limpa antigos, recalcula)
  - `ultima_revisao_semanal: AAAA-MM-DD`
- Cria `semanas/AAAA-Www.md` (se não existir) com template preenchido.
- Imprime resumo no terminal.
