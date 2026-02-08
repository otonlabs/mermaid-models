# PIX SPI - Circuit Breaker - Component View [AWS / Go / gRPC]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
AWS

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Circuit Breaker

## Stack Tecnológico
Go / gRPC

## Descrição
Protecao contra instabilidade do SPI com queue de retry e notificacao

## Componentes Principais
- **Circuit Manager** — responsável por circuit manager
- **Fallback Handler** — responsável por fallback handler
- **Health Checker** — responsável por health checker
- **Metrics Recorder** — responsável por metrics recorder

## Camada de Segurança
- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)
- **Ory Kratos** — Identity management (registration, login, MFA, session)
- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)
- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)
- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)

## Camada de Observabilidade
- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)
- **Datadog APM** — Distributed tracing via dd-trace-go com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[PIX SPI - Circuit Breaker - Component View (AWS / Go / gRPC)](./pix-spi-circuit-breaker-go-grpc-component.mmd)
