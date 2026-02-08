# Core Banking - Hexagonal Architecture Container View [GCP / Node.js / NestJS]

## Domínio
Core Banking — Plataforma Core Banking

## Cloud Provider
GCP

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Hexagonal Architecture

## Stack Tecnológico
Node.js / NestJS

## Descrição
Ports and Adapters para isolamento de dominio nos containers de plataforma core banking

## Componentes Principais
- **Core Banking Service** — serviço principal rodando em Cloud Run
- **Hexagonal Handler** — handler do padrão Hexagonal Architecture
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
- **Datadog APM** — Distributed tracing via dd-trace-js com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **CIP** — Camara Interbancaria de Pagamentos
- **BACEN** — Banco Central do Brasil
- **Bureau Credito** — Serasa, SPC, Boa Vista

## Diagrama
[Core Banking - Hexagonal Architecture Container View (GCP / Node.js / NestJS)](./core-banking-hexagonal-node-nestjs-container.mmd)
