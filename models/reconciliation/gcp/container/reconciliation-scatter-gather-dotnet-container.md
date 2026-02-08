# Reconciliation - Scatter-Gather Container View [GCP / .NET 8 / ASP.NET Core]

## Domínio
Reconciliation — Reconciliacao Financeira

## Cloud Provider
GCP

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Scatter-Gather

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Distribui requisicao para multiplos destinatarios e agrega respostas na camada de containers de reconciliacao financeira

## Componentes Principais
- **Reconciliation Service** — serviço principal rodando em Cloud Run
- **Scatter Gather Processor** — processador do padrão EIP
- **Cloud Tasks Queue** — canal de mensagens principal
- **Scatter Gather Channel** — canal do padrão EIP via Pub/Sub
- **Primary Database** — Cloud SQL
- **Cache Layer** — Memorystore Redis

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
- **Core Banking** — Sistema core de contas
- **Payment Processor** — Processador de pagamentos
- **External Statement** — Extratos de contrapartes

## Diagrama
[Reconciliation - Scatter-Gather Container View (GCP / .NET 8 / ASP.NET Core)](./reconciliation-scatter-gather-dotnet-container.mmd)
