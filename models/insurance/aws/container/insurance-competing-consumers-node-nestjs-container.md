# Insurance - Competing Consumers Container View [AWS / Node.js / NestJS]

## Domínio
Insurance — Plataforma de Seguros

## Cloud Provider
AWS

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Competing Consumers

## Stack Tecnológico
Node.js / NestJS

## Descrição
Multiplos consumidores competem para processar mensagens de fila compartilhada na camada de containers de plataforma de seguros

## Componentes Principais
- **Insurance Service** — serviço principal rodando em ECS Fargate
- **Competing Consumers Processor** — processador do padrão EIP
- **SQS Queue** — canal de mensagens principal
- **Competing Consumers Channel** — canal do padrão EIP via SNS
- **Primary Database** — Aurora PostgreSQL
- **Cache Layer** — ElastiCache Redis

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
- **SUSEP** — Superintendencia de Seguros Privados
- **Ressegurador** — Empresa de resseguro
- **Bureau Sinistro** — Base de dados de sinistros

## Diagrama
[Insurance - Competing Consumers Container View (AWS / Node.js / NestJS)](./insurance-competing-consumers-node-nestjs-container.mmd)
