# Event Driven - API Gateway BFF Container View [AWS / .NET 8 / ASP.NET Core]

## Domínio
Event Driven — Arquitetura Event-Driven

## Cloud Provider
AWS

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** API Gateway BFF

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Backend-for-Frontend com API Gateway por canal nos containers de arquitetura event-driven

## Componentes Principais
- **Event Driven Service** — serviço principal rodando em ECS Fargate
- **Api Gw Bff Handler** — handler do padrão API Gateway BFF
- **Domain Events** — canal de eventos do domínio via SQS
- **Primary Database** — Aurora PostgreSQL
- **Cache Layer** — ElastiCache Redis
- **Pattern State Store** — DynamoDB

## Camada de Segurança
- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)
- **Ory Kratos** — Identity management (registration, login, MFA, session)
- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)
- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)
- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)

## Camada de Observabilidade
- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)
- **Datadog APM** — Distributed tracing via dd-trace-dotnet com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **Producer Services** — Servicos produtores de eventos
- **Consumer Services** — Servicos consumidores
- **Monitoring** — Monitoramento de eventos

## Diagrama
[Event Driven - API Gateway BFF Container View (AWS / .NET 8 / ASP.NET Core)](./event-driven-api-gw-bff-dotnet-container.mmd)
