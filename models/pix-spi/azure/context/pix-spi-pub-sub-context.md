# Broadcast de Liquidacao SPI via Pub-Sub [Azure]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Descrição
Notificacao em tempo real de liquidacao para tesouraria, contabilidade e reconciliacao

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Notificacao em tempo real de liquidacao para tesouraria, contabilidade e reconci)
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
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[Broadcast de Liquidacao SPI via Pub-Sub (Azure)](./pix-spi-pub-sub-context.mmd)
