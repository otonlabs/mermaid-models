# Notification com Saga Orchestration [Oracle Cloud]

## Domínio
Notification — Servicos de Notificacao

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Coordena transacoes distribuidas via orquestrador central no contexto de servicos de notificacao

## Componentes Principais
- **Notification Platform** — sistema principal (Coordena transacoes distribuidas via orquestrador central no contexto de servico)
- **Ory Security Stack** — Identity, OAuth2, Permissions, Zero Trust Proxy
- **OPA Policy Engine** — Policy as Code com Rego para authorization e compliance

## Camada de Segurança
- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)
- **Ory Kratos** — Identity management (registration, login, MFA, session)
- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)
- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)
- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)

## Camada de Observabilidade
- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)
- **Datadog APM** — Distributed tracing via dd-trace com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **Email Provider SES** — Servico de email
- **SMS Provider** — Provedor de SMS
- **Push FCM** — Firebase Cloud Messaging

## Diagrama
[Notification com Saga Orchestration (Oracle Cloud)](./notification-saga-orchestration-context.mmd)
