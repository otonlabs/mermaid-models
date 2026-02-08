# Core Banking com Content-Based Router [AWS]

## Domínio
Core Banking — Plataforma Core Banking

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Content-Based Router

## Descrição
Roteia mensagens para canais diferentes baseado no conteudo aplicado ao contexto de plataforma core banking

## Componentes Principais
- **Core Banking Gateway** — Gateway principal para plataforma core banking
- **Content-Based Router Engine** — Motor de content-based router para processamento
- **Core Banking Monitor** — Monitoramento e alertas de plataforma core banking
- **SQS Queue** — canal de mensagens para content-based-router

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
- **CIP** — Camara Interbancaria de Pagamentos
- **BACEN** — Banco Central do Brasil
- **Bureau Credito** — Serasa, SPC, Boa Vista

## Diagrama
[Core Banking com Content-Based Router (AWS)](./core-banking-content-based-router-context.mmd)
