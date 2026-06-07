# Onboarding de injetável (tirzepatida / semaglutida)

**Quando usar**: depois de 30 dias de plano sem medicação e a fome continuar inviável (≥ 7/10 por 14+ dias).

## Antes da consulta

Levar para o médico:
- Este repo (print ou acesso) com peso, kcal, treino, sono
- Histórico de Rybelsus (dose, tempo, resposta, motivo da parada)
- Comorbidades e medicação atual
- Última cintura abdominal medida
- Plano de saída caso aprovado

## Perguntas para fazer ao médico

1. Tirzepatida ou semaglutida injetável? Qual dose inicial?
2. Como fazer a transição do Rybelsus (que estava suspenso) para o injetável?
3. Efeitos colaterais esperados no primeiro mês?
4. Periodicidade de exames (glicemia, lipidograma, função renal, tireoide)?
5. Combina com álcool eventual? Combina com treino pesado?
6. Quando reavaliar se a dose está adequada?
7. **Plano de saída**: como faço tapering quando atingir a meta? O injetável foi o que faltou no ciclo anterior.

## Janela de uso sugerida

- **Início**: depois da Fase 1 (92 kg) ou no meio da Fase 1 se a fome inviabilizar.
- **Fim previsto**: ao atingir 78 kg + 8 semanas de estabilização na Fase 2.
- **Saída**: tapering de dose + reverse diet simultâneo.

## Adaptando o plano com injetável

Se aprovado:
- Calorias podem subir 200–300 kcal/dia (a medicação controla fome, então menos privação).
- Manter proteína 160–180 g (proteína + treino = massa magra preservada).
- Manter treino 4x (medicação sem treino = perda de massa, não de gordura).
- Álcool: continuar zero nas Fases 0 e 1. Introduzir com moderação na Fase 3.
- Tracking diário continua igual — não relaxar.

## Risco #1 a evitar

Sair do injetável abruptamente quando chegar em 78 kg, sem plano de reverse diet + tracking contínuo. **Foi o que aconteceu com o Rybelsus**: tirou a ferramenta, voltou a fome, vieram 7 kg de volta. Não repete.

## Ações após decisão

- Atualizar `config/metas.yaml::medicacao.injetavel.status` para "aprovado" ou "rejeitado".
- Se aprovado, criar `decisoes/AAAA-MM-DD-inicio-injetavel.md` com dose, data, médico.
- Ajustar `macros_hoje` em `estado.json` se houver mudança de kcal.
