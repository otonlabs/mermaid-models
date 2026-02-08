# Event Driven - Splitter Aggregator - Component View [GCP / Python / FastAPI]

## Domínio
Event Driven — Arquitetura Event-Driven

## Cloud Provider
GCP

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Splitter-Aggregator

## Stack Tecnológico
Python / FastAPI

## Descrição
Divide mensagens compostas e agrega respostas aplicado ao contexto de arquitetura event-driven

## Componentes Principais
- **Message Splitter** — responsável por message splitter
- **Correlation Manager** — responsável por correlation manager
- **Parallel Processor** — responsável por parallel processor
- **Result Aggregator** — responsável por result aggregator

## Camada de Segurança
- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)
- **Ory Kratos** — Identity management (registration, login, MFA, session)
- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)
- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)
- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)

## Camada de Observabilidade
- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)
- **Datadog APM** — Distributed tracing via dd-trace-py com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **Producer Services** — Servicos produtores de eventos
- **Consumer Services** — Servicos consumidores
- **Monitoring** — Monitoramento de eventos

## Diagrama
[Event Driven - Splitter Aggregator - Component View (GCP / Python / FastAPI)](./event-driven-splitter-aggregator-python-fastapi-component.mmd)
