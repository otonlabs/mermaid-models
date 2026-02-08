# Sidecar para Comunicacao MED Segura [AWS / Python / FastAPI]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
AWS

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Sidecar Pattern

## Stack Tecnológico
Python / FastAPI

## Descrição
Sidecar com mTLS, assinatura digital e validacao de certificado ICP-Brasil

## Componentes Principais
- **PIX MED Service** — serviço principal rodando em ECS Fargate
- **Sidecar Handler** — handler do padrão Sidecar Pattern
- **Domain Events** — canal de eventos do domínio via SQS
- **Primary Database** — Aurora PostgreSQL
- **Cache Layer** — ElastiCache Redis
- **Pattern State Store** — DynamoDB

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
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Sidecar para Comunicacao MED Segura (AWS / Python / FastAPI)](./pix-med-sidecar-python-fastapi-container.mmd)
