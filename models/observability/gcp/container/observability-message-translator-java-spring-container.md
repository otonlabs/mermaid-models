# Observability - Message Translator Container View [GCP / Java 21 / Spring Boot 3]

## Domínio
Observability — Observabilidade e Monitoramento

## Cloud Provider
GCP

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Message Translator

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Traduz mensagens entre formatos diferentes via modelo canonico na camada de containers de observabilidade e monitoramento

## Componentes Principais
- **Observability Service** — serviço principal rodando em Cloud Run
- **Message Translator Processor** — processador do padrão EIP
- **Cloud Tasks Queue** — canal de mensagens principal
- **Message Translator Channel** — canal do padrão EIP via Pub/Sub
- **Primary Database** — Cloud SQL
- **Cache Layer** — Memorystore Redis

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
- **Application Services** — Servicos monitorados
- **PagerDuty** — Plataforma de alertas
- **Grafana Cloud** — Plataforma de dashboards

## Diagrama
[Observability - Message Translator Container View (GCP / Java 21 / Spring Boot 3)](./observability-message-translator-java-spring-container.mmd)
