# Auditoria Completa do Fluxo MED via Wire Tap [Oracle Cloud]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Registro detalhado de cada step do MED para conformidade regulatoria

## Componentes Principais
- **MED Flow Gateway** — Gateway central do fluxo MED
- **Regulatory Tap** — Captura evidencias de cada decisao para auditoria BACEN
- **Evidence Store** — Armazena evidencias com imutabilidade e timestamp
- **OCI Queue Queue** — canal de mensagens para wire-tap

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
[Auditoria Completa do Fluxo MED via Wire Tap (Oracle Cloud)](./pix-med-wire-tap-context.mmd)
