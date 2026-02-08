# PIX MED - Content Based Router - Component View [Oracle Cloud / Go / gRPC]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
Oracle Cloud

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Content-Based Router

## Stack Tecnológico
Go / gRPC

## Descrição
Roteamento de MED tipo 1 (fraude) vs tipo 2 (falha operacional) para fluxos distintos

## Componentes Principais
- **Route Controller** — responsável por route controller
- **Content Inspector** — responsável por content inspector
- **Route Table** — responsável por route table
- **Channel Dispatcher** — responsável por channel dispatcher

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
[PIX MED - Content Based Router - Component View (Oracle Cloud / Go / gRPC)](./pix-med-content-based-router-go-grpc-component.mmd)
