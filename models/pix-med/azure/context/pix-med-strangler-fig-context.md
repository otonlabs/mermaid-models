# Migracao do Legado MED via Strangler Fig [Azure]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Transicao gradual de sistema batch de devolucao para real-time MED

## Componentes Principais
- **PIX MED Platform** — sistema principal (Transicao gradual de sistema batch de devolucao para real-time MED)
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
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Migracao do Legado MED via Strangler Fig (Azure)](./pix-med-strangler-fig-context.mmd)
