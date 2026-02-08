# Treasury - Scatter-Gather Container View [Azure / .NET 8 / ASP.NET Core]

## Domínio
Treasury — Gestao de Tesouraria

## Cloud Provider
Azure

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Scatter-Gather

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Distribui requisicao para multiplos destinatarios e agrega respostas na camada de containers de gestao de tesouraria

## Componentes Principais
- **Treasury Service** — serviço principal rodando em App Service
- **Scatter Gather Processor** — processador do padrão EIP
- **Service Bus Queue Queue** — canal de mensagens principal
- **Scatter Gather Channel** — canal do padrão EIP via Service Bus Topics
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
- **Datadog APM** — Distributed tracing via dd-trace-dotnet com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **BACEN STR** — Sistema de Transferencia de Reservas
- **Bloomberg Terminal** — Terminal de dados de mercado
- **CETIP** — Central de custodia de titulos

## Diagrama
[Treasury - Scatter-Gather Container View (Azure / .NET 8 / ASP.NET Core)](./treasury-scatter-gather-dotnet-container.mmd)
