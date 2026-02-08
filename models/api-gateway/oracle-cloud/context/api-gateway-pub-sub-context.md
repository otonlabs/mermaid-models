# API Gateway com Publish-Subscribe [Oracle Cloud]

## Domínio
API Gateway — API Gateway e Hub de Integracao

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Descrição
Broadcast de mensagens para multiplos assinantes aplicado ao contexto de api gateway e hub de integracao

## Componentes Principais
- **API Gateway Gateway** — Gateway principal para api gateway e hub de integracao
- **Publish-Subscribe Engine** — Motor de publish-subscribe para processamento
- **API Gateway Monitor** — Monitoramento e alertas de api gateway e hub de integracao
- **OCI Queue Queue** — canal de mensagens para pub-sub

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
- **External Partner** — Parceiro externo consumidor
- **Internal Microservice** — Microservico interno
- **Identity Provider** — Provedor de identidade

## Diagrama
[API Gateway com Publish-Subscribe (Oracle Cloud)](./api-gateway-pub-sub-context.mmd)
