# Observability com Circuit Breaker [GCP]

## Domínio
Observability — Observabilidade e Monitoramento

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Circuit Breaker

## Descrição
Previne falhas em cascata com circuit breaker pattern no contexto de observabilidade e monitoramento

## Componentes Principais
- **Observability Platform** — sistema principal (Previne falhas em cascata com circuit breaker pattern no contexto de observabili)
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
- **Application Services** — Servicos monitorados
- **PagerDuty** — Plataforma de alertas
- **Grafana Cloud** — Plataforma de dashboards

## Diagrama
[Observability com Circuit Breaker (GCP)](./observability-circuit-breaker-context.mmd)
