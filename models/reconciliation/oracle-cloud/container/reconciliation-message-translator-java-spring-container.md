# Reconciliation - Message Translator Container View [Oracle Cloud / Java 21 / Spring Boot 3]

## Domínio
Reconciliation — Reconciliacao Financeira

## Cloud Provider
Oracle Cloud

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Message Translator

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Traduz mensagens entre formatos diferentes via modelo canonico na camada de containers de reconciliacao financeira

## Componentes Principais
- **Reconciliation Service** — serviço principal rodando em OKE
- **Message Translator Processor** — processador do padrão EIP
- **OCI Queue Queue** — canal de mensagens principal
- **Message Translator Channel** — canal do padrão EIP via OCI Events
- **Primary Database** — Autonomous Database
- **Cache Layer** — OCI Cache Redis

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
- **Core Banking** — Sistema core de contas
- **Payment Processor** — Processador de pagamentos
- **External Statement** — Extratos de contrapartes

## Diagrama
[Reconciliation - Message Translator Container View (Oracle Cloud / Java 21 / Spring Boot 3)](./reconciliation-message-translator-java-spring-container.mmd)
