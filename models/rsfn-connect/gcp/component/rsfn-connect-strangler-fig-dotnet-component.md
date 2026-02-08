# RSFN Connect - Strangler Fig - Component View [GCP / .NET 8 / ASP.NET Core]

## Domínio
RSFN Connect — Rede do Sistema Financeiro Nacional

## Cloud Provider
GCP

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Migra incrementalmente de sistema legado para novo no contexto de rede do sistema financeiro nacional

## Componentes Principais
- **Traffic Router** — responsável por traffic router
- **Legacy Adapter** — responsável por legacy adapter
- **Feature Toggle** — responsável por feature toggle
- **Migration Tracker** — responsável por migration tracker

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
- **BACEN RSFN** — Rede do SFN do Banco Central
- **Camara de Compensacao** — Camara de liquidacao
- **Participante SFN** — Instituicao participante do SFN

## Diagrama
[RSFN Connect - Strangler Fig - Component View (GCP / .NET 8 / ASP.NET Core)](./rsfn-connect-strangler-fig-dotnet-component.mmd)
