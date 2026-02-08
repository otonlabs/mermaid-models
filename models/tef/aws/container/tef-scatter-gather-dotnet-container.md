# TEF - Scatter-Gather Container View [AWS / .NET 8 / ASP.NET Core]

## Domínio
TEF — Transferencia Eletronica de Fundos

## Cloud Provider
AWS

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Scatter-Gather

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Distribui requisicao para multiplos destinatarios e agrega respostas na camada de containers de transferencia eletronica de fundos

## Componentes Principais
- **TEF Service** — serviço principal rodando em ECS Fargate
- **Scatter Gather Processor** — processador do padrão EIP
- **SQS Queue** — canal de mensagens principal
- **Scatter Gather Channel** — canal do padrão EIP via SNS
- **Primary Database** — Aurora PostgreSQL
- **Cache Layer** — ElastiCache Redis

## Camada de Segurança
- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)
- **Ory Kratos** — Identity management (registration, login, MFA, session)
- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)
- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)
- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)

## Camada de Observabilidade
- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)
- **Datadog APM** — Distributed tracing via dd-trace-dotnet com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF - Scatter-Gather Container View (AWS / .NET 8 / ASP.NET Core)](./tef-scatter-gather-dotnet-container.mmd)
