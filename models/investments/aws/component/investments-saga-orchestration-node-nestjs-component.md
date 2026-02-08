# Investments - Saga Orchestration - Component View [AWS / Node.js / NestJS]

## Domínio
Investments — Investimentos e Patrimonio

## Cloud Provider
AWS

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Stack Tecnológico
Node.js / NestJS

## Descrição
Coordena transacoes distribuidas via orquestrador central no contexto de investimentos e patrimonio

## Componentes Principais
- **Saga Controller** — responsável por saga controller
- **Step Executor** — responsável por step executor
- **State Machine** — responsável por state machine
- **Compensation Handler** — responsável por compensation handler

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
- **B3 Bolsa** — Bolsa de Valores do Brasil
- **CVM** — Comissao de Valores Mobiliarios
- **Custodiante** — Custodia de ativos

## Diagrama
[Investments - Saga Orchestration - Component View (AWS / Node.js / NestJS)](./investments-saga-orchestration-node-nestjs-component.mmd)
