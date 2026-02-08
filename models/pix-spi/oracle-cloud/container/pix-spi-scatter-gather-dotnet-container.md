# Consulta de Tarifa PIX via Scatter-Gather [Oracle Cloud / .NET 8 / ASP.NET Core]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
Oracle Cloud

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Scatter-Gather

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Consulta paralela a servicos de tarifa, cambio e IOF para PIX internacional

## Componentes Principais
- **PIX SPI Service** — serviço principal rodando em OKE
- **Scatter Gather Processor** — processador do padrão EIP
- **OCI Queue Queue** — canal de mensagens principal
- **Scatter Gather Channel** — canal do padrão EIP via OCI Events
- **Primary Database** — Autonomous Database
- **Cache Layer** — OCI Cache Redis

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
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[Consulta de Tarifa PIX via Scatter-Gather (Oracle Cloud / .NET 8 / ASP.NET Core)](./pix-spi-scatter-gather-dotnet-container.mmd)
