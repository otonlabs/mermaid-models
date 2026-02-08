# Event Driven - Competing Consumers Container View [Azure / Node.js / NestJS]

## Domínio
Event Driven — Arquitetura Event-Driven

## Cloud Provider
Azure

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Competing Consumers

## Stack Tecnológico
Node.js / NestJS

## Descrição
Multiplos consumidores competem para processar mensagens de fila compartilhada na camada de containers de arquitetura event-driven

## Componentes Principais
- **Event Driven Service** — serviço principal rodando em App Service
- **Competing Consumers Processor** — processador do padrão EIP
- **Service Bus Queue Queue** — canal de mensagens principal
- **Competing Consumers Channel** — canal do padrão EIP via Service Bus Topics
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
- **Datadog APM** — Distributed tracing via dd-trace-js com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **Producer Services** — Servicos produtores de eventos
- **Consumer Services** — Servicos consumidores
- **Monitoring** — Monitoramento de eventos

## Diagrama
[Event Driven - Competing Consumers Container View (Azure / Node.js / NestJS)](./event-driven-competing-consumers-node-nestjs-container.mmd)
