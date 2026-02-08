# PIX SPI - Cqrs Es - Component View [AWS / Python / FastAPI]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
AWS

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Stack Tecnológico
Python / FastAPI

## Descrição
Write path otimizado para insercao e read path com projecoes para consulta de status

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
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[PIX SPI - Cqrs Es - Component View (AWS / Python / FastAPI)](./pix-spi-cqrs-es-python-fastapi-component.mmd)
