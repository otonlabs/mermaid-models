# Portabilidade de Chave com Splitter-Aggregator [Azure]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Splitter-Aggregator

## Descrição
Divide processo de portabilidade em validacao no doador e confirmacao no reivindicador

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Divide processo de portabilidade em validacao no doador e confirmacao no reivind)
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
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Portabilidade de Chave com Splitter-Aggregator (Azure)](./pix-dict-splitter-aggregator-context.mmd)
