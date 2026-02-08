# TEF com Publish-Subscribe [AWS]

## Domínio
TEF — Transferencia Eletronica de Fundos

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Descrição
Broadcast de mensagens para multiplos assinantes aplicado ao contexto de transferencia eletronica de fundos

## Componentes Principais
- **TEF Gateway** — Gateway principal para transferencia eletronica de fundos
- **Publish-Subscribe Engine** — Motor de publish-subscribe para processamento
- **TEF Monitor** — Monitoramento e alertas de transferencia eletronica de fundos
- **SQS Queue** — canal de mensagens para pub-sub

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
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF com Publish-Subscribe (AWS)](./tef-pub-sub-context.mmd)
