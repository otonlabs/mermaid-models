# Notificacao de Alteracao de Chaves via Pub-Sub [GCP]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Descrição
Fan-out de eventos de alteracao de chaves para PSPs participantes

## Componentes Principais
- **Key Change Detector** — Detecta alteracoes em chaves (portabilidade, exclusao)
- **Notification Broadcaster** — Publica eventos para todos os PSPs afetados
- **Sync Monitor** — Monitora confirmacao de sincronizacao dos PSPs
- **Cloud Tasks Queue** — canal de mensagens para pub-sub

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
[Notificacao de Alteracao de Chaves via Pub-Sub (GCP)](./pix-dict-pub-sub-context.mmd)
