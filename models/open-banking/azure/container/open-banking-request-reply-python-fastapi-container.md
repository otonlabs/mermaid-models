# Open Banking - Request-Reply Container View [Azure / Python / FastAPI]

## Domínio
Open Banking — Open Finance Brasil

## Cloud Provider
Azure

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Request-Reply

## Stack Tecnológico
Python / FastAPI

## Descrição
Envia requisicao e aguarda resposta correlacionada na camada de containers de open finance brasil

## Componentes Principais
- **Open Banking Service** — serviço principal rodando em App Service
- **Request Reply Processor** — processador do padrão EIP
- **Service Bus Queue Queue** — canal de mensagens principal
- **Request Reply Channel** — canal do padrão EIP via Service Bus Topics
- **Primary Database** — Azure SQL Database
- **Cache Layer** — Azure Cache for Redis

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
- **Open Finance Directory** — Diretorio de participantes
- **Instituicao Receptora** — ITP que recebe dados
- **BACEN** — Regulador Open Finance

## Diagrama
[Open Banking - Request-Reply Container View (Azure / Python / FastAPI)](./open-banking-request-reply-python-fastapi-container.mmd)
