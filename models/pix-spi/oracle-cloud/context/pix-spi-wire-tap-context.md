# Monitoramento de Mensagens SPI via Wire Tap [Oracle Cloud]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Captura de metricas de latencia e volumetria de mensagens SPI para SLA monitoring

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Captura de metricas de latencia e volumetria de mensagens SPI para SLA monitorin)
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
[Monitoramento de Mensagens SPI via Wire Tap (Oracle Cloud)](./pix-spi-wire-tap-context.mmd)
