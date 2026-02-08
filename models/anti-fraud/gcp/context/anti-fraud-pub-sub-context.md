# Anti-Fraud com Publish-Subscribe [GCP]

## Domínio
Anti-Fraud — Motor Anti-Fraude e Risco

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Descrição
Broadcast de mensagens para multiplos assinantes aplicado ao contexto de motor anti-fraude e risco

## Componentes Principais
- **Anti-Fraud Platform** — sistema principal (Broadcast de mensagens para multiplos assinantes aplicado ao contexto de motor a)
- **Ory Security Stack** — Identity, OAuth2, Permissions, Zero Trust Proxy
- **OPA Policy Engine** — Policy as Code com Rego para authorization e compliance

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
- **Bureau de Fraude** — Base de dados de fraudadores
- **Device Fingerprint** — Servico de device ID
- **BACEN MED** — Mecanismo Especial de Devolucao

## Diagrama
[Anti-Fraud com Publish-Subscribe (GCP)](./anti-fraud-pub-sub-context.mmd)
