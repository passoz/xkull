# Plano Macro — Recompromisso 101 → 92 → 78 kg

## Premissas

- Janela de **1 mês sem medicação** (Rybelsus suspenso). Plano desenhado para funcionar autônomo. Decisão sobre injetável no mês 2.
- Sem restrições alimentares.
- Biometria: homem, 173 cm, 45 anos, trabalho sedentário, sono 6–7 h.
- Álcool: 3–5 doses/sem no histórico → precisa zerar nas Fases 0 e 1.

## Estratégia em 4 fases

| Fase | Semanas | Peso alvo | Déficit (média) | kcal/dia | Álcool | Treino |
|---|---|---|---|---|---|---|
| **0. Reset** | 2 | 101 → 99 | 0 (manutenção) | ~2.250 | 0 | 3x musculação + 2x caminhada |
| **1. Recorte A** | 14–16 | 99 → 92 | –750 kcal | ~1.740 | 0 | 4x musculação + 2x cardio |
| **2. Consolidação** | 3–4 | 92 (estável) | +100 kcal/sem até TDEE | 1.900 → 2.300 | 0 | 4x musculação |
| **3. Recorte B** | 20–24 | 92 → 78 | –500 kcal | ~1.890 | 1–2 doses/sem | 4x musculação + 2x cardio |
| **4. Manutenção** | contínuo | 78 ± 2 | TDEE | ~2.400 | livre c/ moderação | 4x/sem |

**Cronograma**: ~10–11 meses até 78 kg. 92 kg em ~4,5 meses.

## Princípios inegociáveis

1. **Proteína primeiro** — 1,6–2,0 g/kg de massa magra estimada (~160–180 g/dia).
2. **Álcool = moeda de troca** — zero na Fase 0 e 1; máximo 2 doses/sem na Fase 3+.
3. **Treino 4x/semana é o piso** (Fases 1+) — musculação não é negociável.
4. **Média móvel de 7 dias**, não o peso do dia.
5. **Reverse diet obrigatório** entre fases de corte.
6. **Plato de 2 semanas = ajuste automático**.

## Regras de decisão (Hermes aplica automaticamente)

```yaml
queda_peso_semanal_minima: 0.5     # kg/sem na média 7d
plate_2_semanas: 0.3               # abaixo disso por 2 semanas → ajusta
corte_kcal_ajuste: 150             # kcal a cortar se plato
cardio_extra_se_plato: 1           # sessão de cardio a mais
fome_alta_threshold: 7             # em escala 0-10
fome_alta_duracao: 3               # dias seguidos → ajusta macros
sono_minimo_horas: 6
sono_ruim_duracao: 5               # dias → pausa déficit 1 semana
alcool_meta_padrao: 0              # Fases 0 e 1
refeicao_livre_fase3_quinzena: 1   # almoço de domingo quinzenal
kcal_piso_homens: 1500             # nunca abaixo disso na média semanal
```

## Estrutura de refeições (modelo — ajustar por preferência)

**Café (≈ 400 kcal, 35 g P)** — 3 ovos mexidos (ou 2 + 30 g whey) + 1 fatia pão integral + 1 fruta.

**Almoço (≈ 550 kcal, 45 g P)** — prato brasileiro recalibrado:
- 1 concha média de feijão
- 3–4 colheres de arroz OU batata-doce/aipim
- 150 g de proteína magra
- Salada à vontade com 1 fio de azeite
- 1 fruta pequena de sobremesa

**Lanche (≈ 250 kcal, 30 g P)** — whey + banana, OU iogurte grego + castanhas, OU pão integral + peito de peru.

**Jantar (≈ 500 kcal, 50 g P)** — 200 g proteína + vegetais + 1 colher de azeite. Omelete, salmão, frango desfiado.

**Total**: ~1.700 kcal, ~160–180 g proteína.

> **Regra de ouro**: proteína primeiro, vegetal abundante, carbo em torno do treino, gordura como tempero.

## Estratégias anti-fome (substitutas do Rybelsus)

1. Volume de vegetais low-cal (brócolis, espinafre, abobrinha, pepino).
2. Fibra — meta 30 g/dia (aveia, feijão, chia, linhaça).
3. Termogênicos naturais — café preto pré-treino, gengibre, pimenta.
4. Saciogênicos — whey isolado, ovo, batata-doce, aveia, frango desfiado.
5. Janela 12 h (opcional) — 12:00–20:00 ou 13:00–19:00.
6. Regra dos 20 min — sede, fome ou tédio, espera 20 min bebendo água/chá.
7. Substitutos de doce — fruta congelada, cacau 70%, iogurte natural com canela.

## Treino — Fase 1 (4x/semana)

| Dia | Sessão | Tempo |
|---|---|---|
| Segunda | Full Body A | 50 min |
| Terça | Cardio LISS (caminhada/bike) | 30–40 min |
| Quarta | Full Body B | 50 min |
| Quinta | Descanso ativo (caminhada leve) | 20 min |
| Sexta | Full Body A | 50 min |
| Sábado | Cardio LISS + mobilidade | 40 min |
| Domingo | Descanso total | — |

**Full Body A**: agachamento, supino, remada curvada, desenvolvimento, abdominal.
**Full Body B**: terra romeno, puxada frontal, leg press, elevação lateral, prancha.

Progressão: +2,5 kg por semana em cada composto se completar todas as séries com 2 reps na reserva.

## Sinais de alerta e ajustes

| Sinal | Ação |
|---|---|
| Peso parado por 2 semanas | –150 kcal OU +1 cardio |
| Fome > 7/10 por 3+ dias | +200 kcal de carbo no treino, manter proteína |
| Sono < 6 h por 5+ dias | Pausa déficit, manutenção 1 semana |
| Humor/ansiedade piorando | +gordura (35%), –cardio 1 semana |
| Refeição livre não programada | Anotar, não compensar no dia seguinte |
| 2 semanas de regain | Day-reset: jejum 24h + 2 dias manutenção |

## Marcos e celebração

- **5 kg perdidos** (~semana 6): roupa do guarda-roupa que não servia.
- **92 kg**: foto, registro, **iniciar consolidação** (não acelerar).
- **85 kg**: segunda "roupa de meta".
- **78 kg**: foto profissional, **manutenção vitalícia** com pesagem semanal indefinida.

## Sobre o Rybelsus / injetável

| Opção | Quando | Cuidado |
|---|---|---|
| Não retomar | Se em 2–3 semanas da Fase 0 a fome estiver sob controle | Mais disciplina inicial |
| Retomar (injetável) | Se fome continuar sabotando após 30 dias | Sair dele só com plano de tapering de calorias |

Recomendação: começar **só com o comportamental**. Se em 30 dias a fome estiver inviável, retomar com o médico e seguir.

## Critério para avançar de fase

- **Fase 0 → Fase 1**: completou 2 semanas, treino 6/6 sessões, álcool 0, sono ≥ 6,5 h média.
- **Fase 1 → Fase 2**: atingiu 92 kg E está há pelo menos 2 semanas estáveis na média móvel.
- **Fase 2 → Fase 3**: reverse diet completo, peso estabilizado 7 dias seguidos.
- **Fase 3 → Fase 4**: atingiu 78 kg, reverse diet feito, força mantida ou aumentada.
