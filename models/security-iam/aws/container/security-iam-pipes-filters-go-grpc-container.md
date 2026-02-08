# Security IAM - Pipes and Filters Container View [AWS / Go / gRPC]

## Domínio
Security IAM — Seguranca e Gestao de Identidade

## Cloud Provider
AWS

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Pipes and Filters

## Stack Tecnológico
Go / gRPC

## Descrição
Processa mensagens atraves de pipeline de filtros sequenciais na camada de containers de seguranca e gestao de identidade

## Componentes Principais
- **Security IAM Service** — serviço principal rodando em ECS Fargate
- **Pipes Filters Processor** — processador do padrão EIP
- **SQS Queue** — canal de mensagens principal
- **Pipes Filters Channel** — canal do padrão EIP via SNS
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
- **Datadog APM** — Distributed tracing via dd-trace-go com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **External IdP** — Provedor de identidade externo
- **HSM Provider** — Hardware Security Module
- **SIEM** — Security Information and Event Management

## Diagrama
[Security IAM - Pipes and Filters Container View (AWS / Go / gRPC)](./security-iam-pipes-filters-go-grpc-container.mmd)
