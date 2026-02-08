# RSFN Connect com Wire Tap [GCP]

## Domínio
RSFN Connect — Rede do Sistema Financeiro Nacional

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Intercepta e registra mensagens em transito para auditoria aplicado ao contexto de rede do sistema financeiro nacional

## Componentes Principais
- **RSFN Connect Gateway** — Gateway principal para rede do sistema financeiro nacional
- **Wire Tap Engine** — Motor de wire tap para processamento
- **RSFN Connect Monitor** — Monitoramento e alertas de rede do sistema financeiro nacional
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
- **BACEN RSFN** — Rede do SFN do Banco Central
- **Camara de Compensacao** — Camara de liquidacao
- **Participante SFN** — Instituicao participante do SFN

## Diagrama
[RSFN Connect com Wire Tap (GCP)](./rsfn-connect-wire-tap-context.mmd)
