# RSFN Connect com Content-Based Router [AWS]

## Domínio
RSFN Connect — Rede do Sistema Financeiro Nacional

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Content-Based Router

## Descrição
Roteia mensagens para canais diferentes baseado no conteudo aplicado ao contexto de rede do sistema financeiro nacional

## Componentes Principais
- **RSFN Connect Platform** — sistema principal (Roteia mensagens para canais diferentes baseado no conteudo aplicado ao contexto)
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
- **BACEN RSFN** — Rede do SFN do Banco Central
- **Camara de Compensacao** — Camara de liquidacao
- **Participante SFN** — Instituicao participante do SFN

## Diagrama
[RSFN Connect com Content-Based Router (AWS)](./rsfn-connect-content-based-router-context.mmd)
