# Orquestracao do Fluxo MED Completo [GCP]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Steps: notificar, bloquear, analisar, decidir, devolver/liberar com compensacao

## Componentes Principais
- **PIX MED Platform** — sistema principal (Steps: notificar, bloquear, analisar, decidir, devolver/liberar com compensacao)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Orquestracao do Fluxo MED Completo (GCP)](./pix-med-saga-orchestration-context.mmd)
