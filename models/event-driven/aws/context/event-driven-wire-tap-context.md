# Event Driven com Wire Tap [AWS]

## Domínio
Event Driven — Arquitetura Event-Driven

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Intercepta e registra mensagens em transito para auditoria aplicado ao contexto de arquitetura event-driven

## Componentes Principais
- **Event Driven Platform** — sistema principal (Intercepta e registra mensagens em transito para auditoria aplicado ao contexto )
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
- **Producer Services** — Servicos produtores de eventos
- **Consumer Services** — Servicos consumidores
- **Monitoring** — Monitoramento de eventos

## Diagrama
[Event Driven com Wire Tap (AWS)](./event-driven-wire-tap-context.mmd)
