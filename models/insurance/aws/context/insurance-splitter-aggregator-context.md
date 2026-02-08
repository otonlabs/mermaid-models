# Insurance com Splitter-Aggregator [AWS]

## Domínio
Insurance — Plataforma de Seguros

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Splitter-Aggregator

## Descrição
Divide mensagens compostas e agrega respostas aplicado ao contexto de plataforma de seguros

## Componentes Principais
- **Insurance Gateway** — Gateway principal para plataforma de seguros
- **Splitter-Aggregator Engine** — Motor de splitter-aggregator para processamento
- **Insurance Monitor** — Monitoramento e alertas de plataforma de seguros
- **SQS Queue** — canal de mensagens para splitter-aggregator

## Camada de Segurança
- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)
- **Ory Kratos** — Identity management (registration, login, MFA, session)
- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)
- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)
- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)

## Camada de Observabilidade
- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)
- **Datadog APM** — Distributed tracing via dd-trace com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **SUSEP** — Superintendencia de Seguros Privados
- **Ressegurador** — Empresa de resseguro
- **Bureau Sinistro** — Base de dados de sinistros

## Diagrama
[Insurance com Splitter-Aggregator (AWS)](./insurance-splitter-aggregator-context.mmd)
