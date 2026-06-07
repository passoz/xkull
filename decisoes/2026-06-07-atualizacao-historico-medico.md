# Decisão — 2026-06-07: atualização de histórico médico

## Contexto

- Fase atual: 0-reset (semana 1).
- A primeira versão do repo assumia idade 45, comorbidades vazias e sem medicação.
- Fernando confirmou durante a sessão com Hermes:
  - **Data de nascimento: 1977-10-23** (48 anos, não 45).
  - **Infarto agudo do miocárdio em setembro de 2024**.
  - **Implante de 3 stents** desde o evento.
  - Em uso contínuo de medicação para a condição.
  - Pressão alta controlada.
  - **Liberado pelo cardiologista** para exercício físico e dieta.

## Mudança

- **De**:
  - `idade: 45`
  - `comorbidades: []`
  - `medicacao_atual: []`
  - TMB 1.871 kcal
- **Para**:
  - `idade: 48`
  - Histórico cardiovascular documentado em `config/biometria.yaml` e
    `registro_emagrecimento.md`.
  - TMB recalculado para ~1.850 kcal.
  - Adicionada seção `cuidados_cardio` no `biometria.yaml`.
  - TDEE recalculado para ~2.550 kcal.

## Motivo

A biometria anterior estava errada e era perigosa. Cardiopatia isquêmica
pós-stent muda protocolos de treino (cardio progressivo, evitar picos
bruscos de FC), dieta (sódio, gordura saturada, fibra) e monitoramento
(PA semanal obrigatória).

## Critério de reversão

Nenhuma. Este é dado clínico, não opinião. Se houver correção dos fatos
(médico errou, memória trocou datas), abre nova decisão imutável em cima
desta.

## Pendências abertas

- Lista exata de medicação em uso.
- Nome do cardiologista e data exata da liberação.
- Data do último teste de esforço.
- Meta de sódio/dia (definir com nutricionista).
- Criar `metricas/pa.csv` (coleta de PA semanal).
