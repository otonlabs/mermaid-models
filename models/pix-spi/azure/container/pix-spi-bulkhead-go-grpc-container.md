# Bulkhead para Isolamento PIX Instant vs Agendado [Azure / Go / gRPC]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
Azure

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Bulkhead Pattern

## Stack Tecnológico
Go / gRPC

## Descrição
Thread pools separados para nao permitir que PIX agendado impacte instantaneo

## Componentes Principais
- **PIX SPI Service** — serviço principal rodando em App Service
- **Bulkhead Handler** — handler do padrão Bulkhead Pattern
- **Domain Events** — canal de eventos do domínio via Service Bus Queue
- **Primary Database** — Azure SQL Database
- **Cache Layer** — Azure Cache for Redis
- **Pattern State Store** — Cosmos DB

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
[Bulkhead para Isolamento PIX Instant vs Agendado (Azure / Go / gRPC)](./pix-spi-bulkhead-go-grpc-container.mmd)
