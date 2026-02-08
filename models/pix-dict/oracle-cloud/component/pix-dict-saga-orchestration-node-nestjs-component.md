# PIX DICT - Saga Orchestration - Component View [Oracle Cloud / Node.js / NestJS]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Oracle Cloud

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Stack Tecnológico
Node.js / NestJS

## Descrição
Orquestracao do fluxo de reivindicacao com timeout de 7 dias e compensacao

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
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[PIX DICT - Saga Orchestration - Component View (Oracle Cloud / Node.js / NestJS)](./pix-dict-saga-orchestration-node-nestjs-component.mmd)
