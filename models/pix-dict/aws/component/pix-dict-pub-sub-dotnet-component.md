# PIX DICT - Pub Sub - Component View [AWS / .NET 8 / ASP.NET Core]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
AWS

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Fan-out de eventos de alteracao de chaves para PSPs participantes

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
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[PIX DICT - Pub Sub - Component View (AWS / .NET 8 / ASP.NET Core)](./pix-dict-pub-sub-dotnet-component.mmd)
