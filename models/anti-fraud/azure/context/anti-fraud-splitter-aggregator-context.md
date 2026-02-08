# Anti-Fraud com Splitter-Aggregator [Azure]

## Domínio
Anti-Fraud — Motor Anti-Fraude e Risco

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Splitter-Aggregator

## Descrição
Divide mensagens compostas e agrega respostas aplicado ao contexto de motor anti-fraude e risco

## Componentes Principais
- **Anti-Fraud Platform** — sistema principal (Divide mensagens compostas e agrega respostas aplicado ao contexto de motor anti)
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
[Anti-Fraud com Splitter-Aggregator (Azure)](./anti-fraud-splitter-aggregator-context.mmd)
