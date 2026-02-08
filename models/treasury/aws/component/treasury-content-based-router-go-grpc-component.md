# Treasury - Content Based Router - Component View [AWS / Go / gRPC]

## Domínio
Treasury — Gestao de Tesouraria

## Cloud Provider
AWS

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Content-Based Router

## Stack Tecnológico
Go / gRPC

## Descrição
Roteia mensagens para canais diferentes baseado no conteudo aplicado ao contexto de gestao de tesouraria

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
- **BACEN STR** — Sistema de Transferencia de Reservas
- **Bloomberg Terminal** — Terminal de dados de mercado
- **CETIP** — Central de custodia de titulos

## Diagrama
[Treasury - Content Based Router - Component View (AWS / Go / gRPC)](./treasury-content-based-router-go-grpc-component.mmd)
