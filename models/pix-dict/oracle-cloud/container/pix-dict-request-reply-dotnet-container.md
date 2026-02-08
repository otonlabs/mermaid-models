# Registro Sincrono via Request-Reply [Oracle Cloud / .NET 8 / ASP.NET Core]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Oracle Cloud

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Request-Reply

## Stack Tecnológico
.NET 8 / ASP.NET Core

## Descrição
Registro sincrono com BACEN DICT aguardando confirmacao em reply queue

## Componentes Principais
- **PIX DICT Service** — serviço principal rodando em OKE
- **Request Reply Processor** — processador do padrão EIP
- **OCI Queue Queue** — canal de mensagens principal
- **Request Reply Channel** — canal do padrão EIP via OCI Events
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
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Registro Sincrono via Request-Reply (Oracle Cloud / .NET 8 / ASP.NET Core)](./pix-dict-request-reply-dotnet-container.mmd)
