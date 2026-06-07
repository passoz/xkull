# Diário — {{DATA}} ({{DIA_SEMANA}})

## 1. Peso em jejum

```
Peso:    ___ kg
```

> Pesagem logo ao acordar, após ir ao banheiro, antes de comer/beber.

## 2. Refeições

### Café (~{{MACROS_CAFE}} kcal | P: __ g | C: __ g | G: __ g)

```
[ ]
```

### Almoço (~{{MACROS_ALMOCO}} kcal | P: __ g | C: __ g | G: __ g)

```
[ ]
```

### Lanche (~{{MACROS_LANCHE}} kcal | P: __ g | C: __ g | G: __ g)

```
[ ]
```

### Jantar (~{{MACROS_JANTAR}} kcal | P: __ g | C: __ g | G: __ g)

```
[ ]
```

### Extras / bebidas calóricas

```
[ ]
```

### Totais do dia

| | Meta | Real |
|---|---|---|
| kcal | {{META_KCAL}} | ___ |
| Proteína (g) | {{META_PROT}} | ___ |
| Carbo (g) | {{META_CARB}} | ___ |
| Gordura (g) | {{META_GORD}} | ___ |

## 3. Treino

```
Tipo:          [ ] Full Body A  [ ] Full Body B  [ ] Cardio  [ ] Descanso ativo  [ ] Descanso total
Horário:       __:__
Duração:       ___ min
Completou:     [ ] sim  [ ] parcial  [ ] não
Carga (kg) por exercício:
  - ___: ___
  - ___: ___
  - ___: ___
Notas:         
```

## 4. Fome (escala 0–10)

| Momento | Nível | Contexto |
|---|---|---|
| Meio da manhã | __ / 10 | |
| Final da tarde | __ / 10 | |

> 0 = sem fome. 5 = fome normal. 7+ = fome alta. 10 = incontrolável.

## 5. Sono

```
Dormiu:        __:__
Acordou:       __:__
Total:         ___ h
Qualidade:     [ ] ótima  [ ] ok  [ ] ruim
Acordou durante a noite: [ ] não  [ ] sim — quantas vezes: ___
```

## 6. Álcool

```
Bebeu:         [ ] não
Se sim:
  Tipo:        [ ] cerveja  [ ] vinho  [ ] destilado  [ ] outro
  Doses:       ___
  Horário:     __:__
  Contexto:    [ ] social  [ ] estresse  [ ] hábito  [ ] outro
```

## 7. Notas e humor

```
Humor (0-10):        ___
Energia (0-10):      ___
Disposição p/treino: ___
Algo fora do plano:  [ ] não  [ ] sim — descrever:
```

---

> **Checkin do Hermes**: este arquivo é gerado a partir de `template-diario.md` e preenchido com os macros do dia em `config/macros.yaml`. Os CSVs em `metricas/` recebem uma linha por refeição, treino, fome, sono, álcool e peso.
