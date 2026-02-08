# Data Pipeline - Outbox Pattern Container View [Oracle Cloud / Java 21 / Spring Boot 3]

## Domínio
Data Pipeline — Pipeline de Dados e Data Lake

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
Garante publicacao confiavel de mensagens via transactional outbox nos containers de pipeline de dados e data lake

## Componentes Principais
- **Data Pipeline Service** — serviço principal rodando em OKE
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
- **Core Banking Source** — Fonte de dados transacionais
- **Payment Source** — Fonte de dados de pagamentos
- **BI Tools** — Ferramentas de Business Intelligence

## Diagrama
[Data Pipeline - Outbox Pattern Container View (Oracle Cloud / Java 21 / Spring Boot 3)](./data-pipeline-outbox-java-spring-container.mmd)
