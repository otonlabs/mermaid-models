# Data Pipeline - Bulkhead Pattern Container View [GCP / Go / gRPC]

## Domínio
Data Pipeline — Pipeline de Dados e Data Lake

## Cloud Provider
GCP

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Bulkhead Pattern

## Stack Tecnológico
Go / gRPC

## Descrição
Isola recursos criticos para prevenir falhas em cascata nos containers de pipeline de dados e data lake

## Componentes Principais
- **Data Pipeline Service** — serviço principal rodando em Cloud Run
- **Bulkhead Handler** — handler do padrão Bulkhead Pattern
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
- **Datadog APM** — Distributed tracing via dd-trace-go com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **Core Banking Source** — Fonte de dados transacionais
- **Payment Source** — Fonte de dados de pagamentos
- **BI Tools** — Ferramentas de Business Intelligence

## Diagrama
[Data Pipeline - Bulkhead Pattern Container View (GCP / Go / gRPC)](./data-pipeline-bulkhead-go-grpc-container.mmd)
