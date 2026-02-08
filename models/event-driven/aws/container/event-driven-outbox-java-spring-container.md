# Event Driven - Outbox Pattern Container View [AWS / Java 21 / Spring Boot 3]

## Domínio
Event Driven — Arquitetura Event-Driven

## Cloud Provider
AWS

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Outbox Pattern

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Garante publicacao confiavel de mensagens via transactional outbox nos containers de arquitetura event-driven

## Componentes Principais
- **Event Driven Service** — serviço principal rodando em ECS Fargate
- **Outbox Handler** — handler do padrão Outbox Pattern
- **Domain Events** — canal de eventos do domínio via SQS
- **Primary Database** — Aurora PostgreSQL
- **Cache Layer** — ElastiCache Redis
- **Pattern State Store** — DynamoDB

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
- **Producer Services** — Servicos produtores de eventos
- **Consumer Services** — Servicos consumidores
- **Monitoring** — Monitoramento de eventos

## Diagrama
[Event Driven - Outbox Pattern Container View (AWS / Java 21 / Spring Boot 3)](./event-driven-outbox-java-spring-container.mmd)
