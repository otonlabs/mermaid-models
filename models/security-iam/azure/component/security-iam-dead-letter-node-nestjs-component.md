# Security IAM - Dead Letter - Component View [Azure / Node.js / NestJS]

## Domínio
Security IAM — Seguranca e Gestao de Identidade

## Cloud Provider
Azure

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Stack Tecnológico
Node.js / NestJS

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de seguranca e gestao de identidade

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
- **External IdP** — Provedor de identidade externo
- **HSM Provider** — Hardware Security Module
- **SIEM** — Security Information and Event Management

## Diagrama
[Security IAM - Dead Letter - Component View (Azure / Node.js / NestJS)](./security-iam-dead-letter-node-nestjs-component.mmd)
