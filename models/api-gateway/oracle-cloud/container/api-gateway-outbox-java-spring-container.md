# API Gateway - Outbox Pattern Container View [Oracle Cloud / Java 21 / Spring Boot 3]

## Domínio
API Gateway — API Gateway e Hub de Integracao

## Cloud Provider
Oracle Cloud

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Outbox Pattern

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Garante publicacao confiavel de mensagens via transactional outbox nos containers de api gateway e hub de integracao

## Componentes Principais
- **API Gateway Service** — serviço principal rodando em OKE
- **Outbox Handler** — handler do padrão Outbox Pattern
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
- **Datadog APM** — Distributed tracing via dd-trace-java com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **External Partner** — Parceiro externo consumidor
- **Internal Microservice** — Microservico interno
- **Identity Provider** — Provedor de identidade

## Diagrama
[API Gateway - Outbox Pattern Container View (Oracle Cloud / Java 21 / Spring Boot 3)](./api-gateway-outbox-java-spring-container.mmd)
