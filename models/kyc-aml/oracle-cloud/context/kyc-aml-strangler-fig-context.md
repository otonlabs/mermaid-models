# KYC AML com Strangler Fig [Oracle Cloud]

## Domínio
KYC AML — Know Your Customer e Anti-Lavagem

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Migra incrementalmente de sistema legado para novo no contexto de know your customer e anti-lavagem

## Componentes Principais
- **KYC AML Platform** — sistema principal (Migra incrementalmente de sistema legado para novo no contexto de know your cust)
- **Ory Security Stack** — Identity, OAuth2, Permissions, Zero Trust Proxy
- **OPA Policy Engine** — Policy as Code com Rego para authorization e compliance

## Camada de Segurança
- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)
- **Ory Kratos** — Identity management (registration, login, MFA, session)
- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)
- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)
- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)

## Camada de Observabilidade
- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)
- **Datadog APM** — Distributed tracing via dd-trace com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **Receita Federal** — Validacao de CPF/CNPJ
- **COAF** — Conselho de Controle de Atividades Financeiras
- **OFAC Sanctions** — Lista de sancoes internacionais

## Diagrama
[KYC AML com Strangler Fig (Oracle Cloud)](./kyc-aml-strangler-fig-context.mmd)
