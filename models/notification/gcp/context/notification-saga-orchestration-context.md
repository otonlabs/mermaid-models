# Notification com Saga Orchestration [GCP]

## Domínio
Notification — Servicos de Notificacao

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Coordena transacoes distribuidas via orquestrador central no contexto de servicos de notificacao

## Componentes Principais
- **Notification Platform** — sistema principal (Coordena transacoes distribuidas via orquestrador central no contexto de servico)

## Integrações Externas
- **Email Provider SES** — Servico de email
- **SMS Provider** — Provedor de SMS
- **Push FCM** — Firebase Cloud Messaging

## Diagrama
[Notification com Saga Orchestration (GCP)](./notification-saga-orchestration-context.mmd)
