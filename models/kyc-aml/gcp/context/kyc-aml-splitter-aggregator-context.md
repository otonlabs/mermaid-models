# KYC AML com Splitter-Aggregator [GCP]

## Domínio
KYC AML — Know Your Customer e Anti-Lavagem

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Splitter-Aggregator

## Descrição
Divide mensagens compostas e agrega respostas aplicado ao contexto de know your customer e anti-lavagem

## Componentes Principais
- **KYC AML Gateway** — Gateway principal para know your customer e anti-lavagem
- **Splitter-Aggregator Engine** — Motor de splitter-aggregator para processamento
- **KYC AML Monitor** — Monitoramento e alertas de know your customer e anti-lavagem
- **Cloud Tasks Queue** — canal de mensagens para splitter-aggregator

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
[KYC AML com Splitter-Aggregator (GCP)](./kyc-aml-splitter-aggregator-context.mmd)
