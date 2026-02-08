# Event Driven - Pipes and Filters Container View [GCP / Go / gRPC]

## Domínio
Event Driven — Arquitetura Event-Driven

## Cloud Provider
GCP

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Pipes and Filters

## Stack Tecnológico
Go / gRPC

## Descrição
Processa mensagens atraves de pipeline de filtros sequenciais na camada de containers de arquitetura event-driven

## Componentes Principais
- **Event Driven Service** — serviço principal rodando em Cloud Run
- **Pipes Filters Processor** — processador do padrão EIP
- **Cloud Tasks Queue** — canal de mensagens principal
- **Pipes Filters Channel** — canal do padrão EIP via Pub/Sub
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
- **Datadog APM** — Distributed tracing via dd-trace-go com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **Producer Services** — Servicos produtores de eventos
- **Consumer Services** — Servicos consumidores
- **Monitoring** — Monitoramento de eventos

## Diagrama
[Event Driven - Pipes and Filters Container View (GCP / Go / gRPC)](./event-driven-pipes-filters-go-grpc-container.mmd)
