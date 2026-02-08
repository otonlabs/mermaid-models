# PIX SPI - Dead Letter - Component View [GCP / Node.js / NestJS]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
GCP

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Stack Tecnológico
Node.js / NestJS

## Descrição
Tratamento de rejeicoes do SPI com retry automatico e escalacao

## Componentes Principais
- **DLQ Consumer** — responsável por dlq consumer
- **Retry Scheduler** — responsável por retry scheduler
- **Poison Detector** — responsável por poison detector
- **Alert Notifier** — responsável por alert notifier

## Camada de Segurança
- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)
- **Ory Kratos** — Identity management (registration, login, MFA, session)
- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)
- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)
- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)

## Camada de Observabilidade
- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)
- **Datadog APM** — Distributed tracing via dd-trace-js com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[PIX SPI - Dead Letter - Component View (GCP / Node.js / NestJS)](./pix-spi-dead-letter-node-nestjs-component.mmd)
