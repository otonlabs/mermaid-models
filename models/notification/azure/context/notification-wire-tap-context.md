# Notification com Wire Tap [Azure]

## Domínio
Notification — Servicos de Notificacao

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Intercepta e registra mensagens em transito para auditoria aplicado ao contexto de servicos de notificacao

## Componentes Principais
- **Notification Platform** — sistema principal (Intercepta e registra mensagens em transito para auditoria aplicado ao contexto )

## Integrações Externas
- **Email Provider SES** — Servico de email
- **SMS Provider** — Provedor de SMS
- **Push FCM** — Firebase Cloud Messaging

## Diagrama
[Notification com Wire Tap (Azure)](./notification-wire-tap-context.mmd)
