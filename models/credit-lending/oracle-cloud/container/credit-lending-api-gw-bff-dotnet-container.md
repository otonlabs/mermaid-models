# Credit Lending - API Gateway BFF Container View [Oracle Cloud / .NET 8 / ASP.NET Core]

## Domínio
Credit Lending — Credito e Emprestimos

## Cloud Provider
Oracle Cloud

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** API Gateway BFF

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Backend-for-Frontend com API Gateway por canal nos containers de credito e emprestimos

## Componentes Principais
- **Credit Lending Service** — serviço principal rodando em OKE
- **Api Gw Bff Handler** — handler do padrão API Gateway BFF
- **Domain Events** — canal de eventos do domínio via OCI Queue
- **Primary Database** — Autonomous Database
- **Cache Layer** — OCI Cache Redis
- **Pattern State Store** — OCI NoSQL

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
- **Bureau Credito SCR** — Sistema de informacoes de credito BACEN
- **BACEN SCR** — Central de risco do BACEN
- **Seguradora** — Seguro prestamista

## Diagrama
[Credit Lending - API Gateway BFF Container View (Oracle Cloud / .NET 8 / ASP.NET Core)](./credit-lending-api-gw-bff-dotnet-container.mmd)
