# Notification - Request-Reply Container View [Oracle Cloud / Python / FastAPI]

## Domínio
Notification — Servicos de Notificacao

## Cloud Provider
Oracle Cloud

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Request-Reply

## Stack Tecnológico
Python / FastAPI

## Descrição
Envia requisicao e aguarda resposta correlacionada na camada de containers de servicos de notificacao

## Componentes Principais
- **Notification Service** — serviço principal rodando em OKE
- **Request Reply Processor** — processador do padrão EIP
- **OCI Queue Queue** — canal de mensagens principal
- **Request Reply Channel** — canal do padrão EIP via OCI Events
- **Primary Database** — Autonomous Database
- **Cache Layer** — OCI Cache Redis

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
- **Email Provider SES** — Servico de email
- **SMS Provider** — Provedor de SMS
- **Push FCM** — Firebase Cloud Messaging

## Diagrama
[Notification - Request-Reply Container View (Oracle Cloud / Python / FastAPI)](./notification-request-reply-python-fastapi-container.mmd)
