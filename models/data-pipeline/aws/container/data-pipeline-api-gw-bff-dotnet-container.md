# Data Pipeline - API Gateway BFF Container View [AWS / .NET 8 / ASP.NET Core]

## Domínio
Data Pipeline — Pipeline de Dados e Data Lake

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
Backend-for-Frontend com API Gateway por canal nos containers de pipeline de dados e data lake

## Componentes Principais
- **Data Pipeline Service** — serviço principal rodando em ECS Fargate
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
- **Core Banking Source** — Fonte de dados transacionais
- **Payment Source** — Fonte de dados de pagamentos
- **BI Tools** — Ferramentas de Business Intelligence

## Diagrama
[Data Pipeline - API Gateway BFF Container View (AWS / .NET 8 / ASP.NET Core)](./data-pipeline-api-gw-bff-dotnet-container.mmd)
