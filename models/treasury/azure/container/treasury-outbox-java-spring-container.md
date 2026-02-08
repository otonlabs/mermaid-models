# Treasury - Outbox Pattern Container View [Azure / Java 21 / Spring Boot 3]

## Domínio
Treasury — Gestao de Tesouraria

## Cloud Provider
Azure

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Outbox Pattern

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Garante publicacao confiavel de mensagens via transactional outbox nos containers de gestao de tesouraria

## Componentes Principais
- **Treasury Service** — serviço principal rodando em App Service
- **Outbox Handler** — handler do padrão Outbox Pattern
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
- **Datadog APM** — Distributed tracing via dd-trace-java com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **BACEN STR** — Sistema de Transferencia de Reservas
- **Bloomberg Terminal** — Terminal de dados de mercado
- **CETIP** — Central de custodia de titulos

## Diagrama
[Treasury - Outbox Pattern Container View (Azure / Java 21 / Spring Boot 3)](./treasury-outbox-java-spring-container.mmd)
