# Pipeline de Validacao de Chaves com Pipes and Filters [GCP / Java 21 / Spring Boot 3]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
GCP

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Pipes and Filters

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Cadeia de filtros: formato, duplicidade, titularidade, OFAC screening

## Componentes Principais
- **PIX DICT Service** — serviço principal rodando em Cloud Run
- **Pipes Filters Processor** — processador do padrão EIP
- **Cloud Tasks Queue** — canal de mensagens principal
- **Pipes Filters Channel** — canal do padrão EIP via Pub/Sub
- **Primary Database** — Cloud SQL
- **Cache Layer** — Memorystore Redis

## Camada de Segurança
- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)
- **Ory Kratos** — Identity management (registration, login, MFA, session)
- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)
- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)
- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)

## Camada de Observabilidade
- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)
- **Datadog APM** — Distributed tracing via dd-trace-java com auto-instrumentacao
- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id
- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Pipeline de Validacao de Chaves com Pipes and Filters (GCP / Java 21 / Spring Boot 3)](./pix-dict-pipes-filters-java-spring-container.mmd)
