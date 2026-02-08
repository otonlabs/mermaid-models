# DDA - Competing Consumers Container View [GCP / Node.js / NestJS]

## Domínio
DDA — Debito Direto Autorizado

## Cloud Provider
GCP

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Competing Consumers

## Stack Tecnológico
Node.js / NestJS

## Descrição
Multiplos consumidores competem para processar mensagens de fila compartilhada na camada de containers de debito direto autorizado

## Componentes Principais
- **DDA Service** — serviço principal rodando em Cloud Run
- **Competing Consumers Processor** — processador do padrão EIP
- **Cloud Tasks Queue** — canal de mensagens principal
- **Competing Consumers Channel** — canal do padrão EIP via Pub/Sub
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
- **Datadog APM** — Distributed tracing via dd-trace-js com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **CIP DDA** — Central de registro DDA
- **Banco Sacado** — Banco do pagador
- **Registro Boletos** — Sistema de registro de boletos

## Diagrama
[DDA - Competing Consumers Container View (GCP / Node.js / NestJS)](./dda-competing-consumers-node-nestjs-container.mmd)
