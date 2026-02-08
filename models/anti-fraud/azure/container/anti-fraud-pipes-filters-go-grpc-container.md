# Anti-Fraud - Pipes and Filters Container View [Azure / Go / gRPC]

## Domínio
Anti-Fraud — Motor Anti-Fraude e Risco

## Cloud Provider
Azure

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Pipes and Filters

## Stack Tecnológico
Go / gRPC

## Descrição
Processa mensagens atraves de pipeline de filtros sequenciais na camada de containers de motor anti-fraude e risco

## Componentes Principais
- **Anti-Fraud Service** — serviço principal rodando em App Service
- **Pipes Filters Processor** — processador do padrão EIP
- **Service Bus Queue Queue** — canal de mensagens principal
- **Pipes Filters Channel** — canal do padrão EIP via Service Bus Topics
- **Primary Database** — Azure SQL Database
- **Cache Layer** — Azure Cache for Redis

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
- **Bureau de Fraude** — Base de dados de fraudadores
- **Device Fingerprint** — Servico de device ID
- **BACEN MED** — Mecanismo Especial de Devolucao

## Diagrama
[Anti-Fraud - Pipes and Filters Container View (Azure / Go / gRPC)](./anti-fraud-pipes-filters-go-grpc-container.mmd)
