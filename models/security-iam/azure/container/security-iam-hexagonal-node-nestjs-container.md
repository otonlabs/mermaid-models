# Security IAM - Hexagonal Architecture Container View [Azure / Node.js / NestJS]

## Domínio
Security IAM — Seguranca e Gestao de Identidade

## Cloud Provider
Azure

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Hexagonal Architecture

## Stack Tecnológico
Node.js / NestJS

## Descrição
Ports and Adapters para isolamento de dominio nos containers de seguranca e gestao de identidade

## Componentes Principais
- **Security IAM Service** — serviço principal rodando em App Service
- **Hexagonal Handler** — handler do padrão Hexagonal Architecture
- **Domain Events** — canal de eventos do domínio via Service Bus Queue
- **Primary Database** — Azure SQL Database
- **Cache Layer** — Azure Cache for Redis
- **Pattern State Store** — Cosmos DB

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
[Security IAM - Hexagonal Architecture Container View (Azure / Node.js / NestJS)](./security-iam-hexagonal-node-nestjs-container.mmd)
