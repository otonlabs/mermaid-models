# DevOps CICD - Sidecar Pattern Container View [Azure / Python / FastAPI]

## Domínio
DevOps CICD — DevOps e Pipelines CI/CD

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
Deploy de componentes auxiliares ao lado do servico principal nos containers de devops e pipelines ci/cd

## Componentes Principais
- **DevOps CICD Service** — serviço principal rodando em App Service
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
- **Git Repository** — Repositorio de codigo fonte
- **Container Registry** — Registro de imagens Docker
- **Security Scanner** — Scanner SAST/DAST

## Diagrama
[DevOps CICD - Sidecar Pattern Container View (Azure / Python / FastAPI)](./devops-cicd-sidecar-python-fastapi-container.mmd)
