# PIX MED - Circuit Breaker - Component View [GCP / Go / gRPC]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
GCP

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Circuit Breaker

## Stack Tecnológico
Go / gRPC

## Descrição
Protecao contra timeout da API MED com queue local e retry

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
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[PIX MED - Circuit Breaker - Component View (GCP / Go / gRPC)](./pix-med-circuit-breaker-go-grpc-component.mmd)
