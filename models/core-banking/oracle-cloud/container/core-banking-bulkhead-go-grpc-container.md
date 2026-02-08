# Core Banking - Bulkhead Pattern Container View [Oracle Cloud / Go / gRPC]

## Domínio
Core Banking — Plataforma Core Banking

## Cloud Provider
Oracle Cloud

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Bulkhead Pattern

## Stack Tecnológico
Go / gRPC

## Descrição
Isola recursos criticos para prevenir falhas em cascata nos containers de plataforma core banking

## Componentes Principais
- **Core Banking Service** — serviço principal rodando em OKE
- **Bulkhead Handler** — handler do padrão Bulkhead Pattern
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
- **Datadog APM** — Distributed tracing via dd-trace-go com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **CIP** — Camara Interbancaria de Pagamentos
- **BACEN** — Banco Central do Brasil
- **Bureau Credito** — Serasa, SPC, Boa Vista

## Diagrama
[Core Banking - Bulkhead Pattern Container View (Oracle Cloud / Go / gRPC)](./core-banking-bulkhead-go-grpc-container.mmd)
