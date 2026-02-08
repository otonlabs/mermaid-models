# DDA - Request-Reply Container View [AWS / Python / FastAPI]

## Domínio
DDA — Debito Direto Autorizado

## Cloud Provider
AWS

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Request-Reply

## Stack Tecnológico
Python / FastAPI

## Descrição
Envia requisicao e aguarda resposta correlacionada na camada de containers de debito direto autorizado

## Componentes Principais
- **DDA Service** — serviço principal rodando em ECS Fargate
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
- **Datadog APM** — Distributed tracing via dd-trace-py com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **CIP DDA** — Central de registro DDA
- **Banco Sacado** — Banco do pagador
- **Registro Boletos** — Sistema de registro de boletos

## Diagrama
[DDA - Request-Reply Container View (AWS / Python / FastAPI)](./dda-request-reply-python-fastapi-container.mmd)
