# Credit Lending com Wire Tap [GCP]

## Domínio
Credit Lending — Credito e Emprestimos

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Intercepta e registra mensagens em transito para auditoria aplicado ao contexto de credito e emprestimos

## Componentes Principais
- **Credit Lending Gateway** — Gateway principal para credito e emprestimos
- **Wire Tap Engine** — Motor de wire tap para processamento
- **Credit Lending Monitor** — Monitoramento e alertas de credito e emprestimos
- **Cloud Tasks Queue** — canal de mensagens para wire-tap

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
- **Bureau Credito SCR** — Sistema de informacoes de credito BACEN
- **BACEN SCR** — Central de risco do BACEN
- **Seguradora** — Seguro prestamista

## Diagrama
[Credit Lending com Wire Tap (GCP)](./credit-lending-wire-tap-context.mmd)
