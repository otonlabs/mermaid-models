# Treasury com Saga Orchestration [GCP]

## Domínio
Treasury — Gestao de Tesouraria

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Coordena transacoes distribuidas via orquestrador central no contexto de gestao de tesouraria

## Componentes Principais
- **Treasury Command Service** — Servico de comandos para gestao de tesouraria
- **Saga Orchestration Handler** — Handler do padrao Saga Orchestration
- **Treasury Query Service** — Servico de consultas otimizadas
- **Cloud SQL** — persistência principal do domínio

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
- **BACEN STR** — Sistema de Transferencia de Reservas
- **Bloomberg Terminal** — Terminal de dados de mercado
- **CETIP** — Central de custodia de titulos

## Diagrama
[Treasury com Saga Orchestration (GCP)](./treasury-saga-orchestration-context.mmd)
