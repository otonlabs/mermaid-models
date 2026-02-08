# Data Pipeline com Circuit Breaker [GCP]

## Domínio
Data Pipeline — Pipeline de Dados e Data Lake

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Circuit Breaker

## Descrição
Previne falhas em cascata com circuit breaker pattern no contexto de pipeline de dados e data lake

## Componentes Principais
- **Data Pipeline Platform** — sistema principal (Previne falhas em cascata com circuit breaker pattern no contexto de pipeline de)
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
- **Core Banking Source** — Fonte de dados transacionais
- **Payment Source** — Fonte de dados de pagamentos
- **BI Tools** — Ferramentas de Business Intelligence

## Diagrama
[Data Pipeline com Circuit Breaker (GCP)](./data-pipeline-circuit-breaker-context.mmd)
