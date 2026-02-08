# Notification com CQRS + Event Sourcing [Oracle Cloud]

## Domínio
Notification — Servicos de Notificacao

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de servicos de notificacao

## Componentes Principais
- **Notification Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **Email Provider SES** — Servico de email
- **SMS Provider** — Provedor de SMS
- **Push FCM** — Firebase Cloud Messaging

## Diagrama
[Notification com CQRS + Event Sourcing (Oracle Cloud)](./notification-cqrs-es-context.mmd)
