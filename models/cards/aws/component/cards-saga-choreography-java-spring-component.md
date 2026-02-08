# Cards - Saga Choreography - Component View [AWS / Java 21 / Spring Boot 3]

## Domínio
Cards — Processamento de Cartoes

## Cloud Provider
AWS

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Choreography

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Coordena transacoes distribuidas via coreografia de eventos no contexto de processamento de cartoes

## Componentes Principais
- **Event Publisher** — responsável por event publisher
- **Event Consumer** — responsável por event consumer
- **Compensation Listener** — responsável por compensation listener
- **State Tracker** — responsável por state tracker

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
- **Bandeira Visa Master** — Redes de cartao
- **TSP Token Requestor** — Provedor de tokenizacao
- **Rede Adquirente** — Processadora de transacoes

## Diagrama
[Cards - Saga Choreography - Component View (AWS / Java 21 / Spring Boot 3)](./cards-saga-choreography-java-spring-component.mmd)
