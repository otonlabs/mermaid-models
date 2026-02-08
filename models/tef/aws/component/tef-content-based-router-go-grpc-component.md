# TEF - Content Based Router - Component View [AWS / Go / gRPC]

## Domínio
TEF — Transferencia Eletronica de Fundos

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
Roteia mensagens para canais diferentes baseado no conteudo aplicado ao contexto de transferencia eletronica de fundos

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
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF - Content Based Router - Component View (AWS / Go / gRPC)](./tef-content-based-router-go-grpc-component.mmd)
