# PIX MED - Pub Sub - Component View [GCP / .NET 8 / ASP.NET Core]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
GCP

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Notificacao de bloqueio cautelar para todos os canais do recebedor

## Componentes Principais
- **Event Publisher** — responsável por event publisher
- **Subscriber Registry** — responsável por subscriber registry
- **Fan-Out Manager** — responsável por fan-out manager
- **Delivery Tracker** — responsável por delivery tracker

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
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[PIX MED - Pub Sub - Component View (GCP / .NET 8 / ASP.NET Core)](./pix-med-pub-sub-dotnet-component.mmd)
