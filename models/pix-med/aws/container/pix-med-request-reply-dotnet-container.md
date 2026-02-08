# Notificacao Sincrona MED via Request-Reply [AWS / .NET 8 / ASP.NET Core]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
AWS

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Request-Reply

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Envio de notificacao MED ao BACEN aguardando ACK sincrono

## Componentes Principais
- **PIX MED Service** — serviço principal rodando em ECS Fargate
- **Request Reply Processor** — processador do padrão EIP
- **SQS Queue** — canal de mensagens principal
- **Request Reply Channel** — canal do padrão EIP via SNS
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
- **Datadog APM** — Distributed tracing via dd-trace-dotnet com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Notificacao Sincrona MED via Request-Reply (AWS / .NET 8 / ASP.NET Core)](./pix-med-request-reply-dotnet-container.mmd)
