# Decisão — 2026-06-07: reorganização do repo para o Fernando

## Contexto

O repo `passoz/xkull` foi criado por outra pessoa. Os números (idade 45,
sem comorbidades) estavam errados pra mim. Os prompts de check-in pediam
3 refeições por dia e o cardápio era aleatório.

Decidi reescrever o repo todo pra refletir **minha vida real**, conforme
combinei com o Hermes.

## Mudanças

### Bio
- Idade: 45 → **48**
- Comorbidades: vazio → **PA controlada + IAM set/2024 + 3 stents + medicação contínua**
- TMB: 1.871 → **1.850 kcal** (recalculado)
- TDEE: 2.575 → **2.550 kcal**

### Refeições
- 3 refeições → **4 refeições** (café, almoço, **lanche reforçado**, jantar)
- Lanche reforçado porque sinto muita fome no fim da tarde

### Cozinha
- Cardápio genérico → **prato brasileiro tradicional** (esposa cozinha)
- Proteína varia: frango / porco / bovina
- Sódio controlado (cuidado cardíaco)

### Álcool
- Meta rígida "0" na Fase 0 → **"reportar sempre"**
- Não quero regra que eu vou furar escondido. Registro, mas sem pressão.

### Treino
- 3x musculação + 2x caminhada na Fase 0 confirmado
- Começa amanhã (segunda, 8 de junho)
- Cardio progressivo, não HIIT agressivo (cuidado cardíaco)

### Check-in
- 3 check-ins (manhã, tarde, noite) → **1 check-in/dia, 5:35, só dias de semana**
- Conteúdo: peso em jejum + sim/não treino
- Curto. Direto. Sem positividade tóxica.

### Monitoramento
- Novo CSV: `metricas/pa.csv` (PA semanal, cuidado cardíaco)
- Skill nova: `~/.hermes/skills/health_connect/` (OAuth Google Health Connect)
- Após config do OAuth, peso puxa automático às 5:35

## Motivo

Nada do repo original servia pra mim. Regrava a vida de outra pessoa.
Reescrever foi mais honesto do que adaptar.

## Critério de reversão

Cada mudança aqui documentada é decisão **minha**, não do autor original.
Se eu mudar de ideia em qualquer ponto, abro nova `decisao/` referenciando esta.

## Pendências (aberto)

- [ ] Instalar Health Connect no Android
- [ ] Instalar app ponte (ex: "Health Sync") pra Fit → Health Connect
- [ ] Passar Client ID e Client Secret pro Hermes
- [ ] Testar OAuth
- [ ] Configurar cron 5:35
- [ ] Lista exata de medicação (anotar do cardiologista)
- [ ] Medida de cintura atual
- [ ] Teste de esforço recente (data/resultado)
- [ ] Avaliação com nutricionista (sódio, perfil lipídico)
- [ ] Decisão sobre injetável (data alvo: 2026-07-07)
