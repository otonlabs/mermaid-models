# API Gateway - Bulkhead Pattern Container View [GCP / Go / gRPC]

## Domínio
API Gateway — API Gateway e Hub de Integracao

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
Isola recursos criticos para prevenir falhas em cascata nos containers de api gateway e hub de integracao

## Componentes Principais
- **API Gateway Service** — serviço principal rodando em Cloud Run
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
- **External Partner** — Parceiro externo consumidor
- **Internal Microservice** — Microservico interno
- **Identity Provider** — Provedor de identidade

## Diagrama
[API Gateway - Bulkhead Pattern Container View (GCP / Go / gRPC)](./api-gateway-bulkhead-go-grpc-container.mmd)
