# RSFN Connect - Cqrs Es - Component View [GCP / Python / FastAPI]

## Domínio
RSFN Connect — Rede do Sistema Financeiro Nacional

## Cloud Provider
GCP

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Stack Tecnológico
Python / FastAPI

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de rede do sistema financeiro nacional

## Componentes Principais
- **Command Handler** — responsável por command handler
- **Event Writer** — responsável por event writer
- **Projection Builder** — responsável por projection builder
- **Snapshot Manager** — responsável por snapshot manager

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
- **BACEN RSFN** — Rede do SFN do Banco Central
- **Camara de Compensacao** — Camara de liquidacao
- **Participante SFN** — Instituicao participante do SFN

## Diagrama
[RSFN Connect - Cqrs Es - Component View (GCP / Python / FastAPI)](./rsfn-connect-cqrs-es-python-fastapi-component.mmd)
