# Data Pipeline - Dead Letter - Component View [GCP / Node.js / NestJS]

## Domínio
Data Pipeline — Pipeline de Dados e Data Lake

## Cloud Provider
GCP

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Stack Tecnológico
Node.js / NestJS

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de pipeline de dados e data lake

## Componentes Principais
- **DLQ Consumer** — responsável por dlq consumer
- **Retry Scheduler** — responsável por retry scheduler
- **Poison Detector** — responsável por poison detector
- **Alert Notifier** — responsável por alert notifier

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
- **Core Banking Source** — Fonte de dados transacionais
- **Payment Source** — Fonte de dados de pagamentos
- **BI Tools** — Ferramentas de Business Intelligence

## Diagrama
[Data Pipeline - Dead Letter - Component View (GCP / Node.js / NestJS)](./data-pipeline-dead-letter-node-nestjs-component.mmd)
