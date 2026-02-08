# Payments - Message Translator Container View [Azure / Java 21 / Spring Boot 3]

## Domínio
Payments — Processamento de Pagamentos

## Cloud Provider
Azure

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Message Translator

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Traduz mensagens entre formatos diferentes via modelo canonico na camada de containers de processamento de pagamentos

## Componentes Principais
- **Payments Service** — serviço principal rodando em App Service
- **Message Translator Processor** — processador do padrão EIP
- **Service Bus Queue Queue** — canal de mensagens principal
- **Message Translator Channel** — canal do padrão EIP via Service Bus Topics
- **Primary Database** — Azure SQL Database
- **Cache Layer** — Azure Cache for Redis

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
- **Rede Adquirente** — Processadora de cartoes
- **PIX SPI** — Sistema PIX do BACEN
- **TED DOC CIP** — Transferencias interbancarias

## Diagrama
[Payments - Message Translator Container View (Azure / Java 21 / Spring Boot 3)](./payments-message-translator-java-spring-container.mmd)
