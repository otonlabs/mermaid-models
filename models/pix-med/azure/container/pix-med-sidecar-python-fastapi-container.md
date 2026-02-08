# Sidecar para Comunicacao MED Segura [Azure / Python / FastAPI]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
Azure

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
- **PIX MED Service** — serviço principal rodando em App Service
- **Sidecar Handler** — handler do padrão Sidecar Pattern
- **Domain Events** — canal de eventos do domínio via Service Bus Queue
- **Primary Database** — Azure SQL Database
- **Cache Layer** — Azure Cache for Redis
- **Pattern State Store** — Cosmos DB

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
[Sidecar para Comunicacao MED Segura (Azure / Python / FastAPI)](./pix-med-sidecar-python-fastapi-container.mmd)
