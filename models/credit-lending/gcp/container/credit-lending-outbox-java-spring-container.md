# Credit Lending - Outbox Pattern Container View [GCP / Java 21 / Spring Boot 3]

## Domínio
Credit Lending — Credito e Emprestimos

## Cloud Provider
GCP

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Outbox Pattern

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Garante publicacao confiavel de mensagens via transactional outbox nos containers de credito e emprestimos

## Componentes Principais
- **Credit Lending Service** — serviço principal rodando em Cloud Run
- **Outbox Handler** — handler do padrão Outbox Pattern
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
- **Datadog APM** — Distributed tracing via dd-trace-java com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **Bureau Credito SCR** — Sistema de informacoes de credito BACEN
- **BACEN SCR** — Central de risco do BACEN
- **Seguradora** — Seguro prestamista

## Diagrama
[Credit Lending - Outbox Pattern Container View (GCP / Java 21 / Spring Boot 3)](./credit-lending-outbox-java-spring-container.mmd)
