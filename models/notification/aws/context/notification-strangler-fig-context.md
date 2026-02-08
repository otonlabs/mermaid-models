# Notification com Strangler Fig [AWS]

## Domínio
Notification — Servicos de Notificacao

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Migra incrementalmente de sistema legado para novo no contexto de servicos de notificacao

## Componentes Principais
- **Notification Platform** — sistema principal (Migra incrementalmente de sistema legado para novo no contexto de servicos de no)
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
[Notification com Strangler Fig (AWS)](./notification-strangler-fig-context.mmd)
