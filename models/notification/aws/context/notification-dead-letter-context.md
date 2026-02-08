# Notification com Dead Letter Channel [AWS]

## Domínio
Notification — Servicos de Notificacao

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de servicos de notificacao

## Componentes Principais
- **Notification Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Email Provider SES** — Servico de email
- **SMS Provider** — Provedor de SMS
- **Push FCM** — Firebase Cloud Messaging

## Diagrama
[Notification com Dead Letter Channel (AWS)](./notification-dead-letter-context.mmd)
