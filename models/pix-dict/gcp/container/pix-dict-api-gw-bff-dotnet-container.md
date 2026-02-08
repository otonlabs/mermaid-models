# API Gateway BFF para Canais PIX DICT [GCP / .NET 8 / ASP.NET Core]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
GCP

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** API Gateway BFF

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
BFF Mobile com UX otimizada vs BFF Web com gestao completa de chaves

## Componentes Principais
- **PIX DICT Service** — serviço principal rodando em Cloud Run
- **Api Gw Bff Handler** — handler do padrão API Gateway BFF
- **Domain Events** — canal de eventos do domínio via Cloud Tasks
- **Primary Database** — Cloud SQL
- **Cache Layer** — Memorystore Redis
- **Pattern State Store** — Firestore

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
[API Gateway BFF para Canais PIX DICT (GCP / .NET 8 / ASP.NET Core)](./pix-dict-api-gw-bff-dotnet-container.mmd)
