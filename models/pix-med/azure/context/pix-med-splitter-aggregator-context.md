# Analise de Caso MED com Splitter-Aggregator [Azure]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Splitter-Aggregator

## Descrição
Split de caso em sub-analises paralelas e agregacao de score final

## Componentes Principais
- **PIX MED Platform** — sistema principal (Split de caso em sub-analises paralelas e agregacao de score final)
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
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Analise de Caso MED com Splitter-Aggregator (Azure)](./pix-med-splitter-aggregator-context.mmd)
