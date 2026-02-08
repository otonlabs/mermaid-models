# Pipeline de Analise MED com Pipes and Filters [GCP / Java 21 / Spring Boot 3]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

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
Filtros sequenciais: elegibilidade, prazo, saldo disponivel, historico recebedor

## Componentes Principais
- **PIX MED Service** — serviço principal rodando em Cloud Run
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
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Pipeline de Analise MED com Pipes and Filters (GCP / Java 21 / Spring Boot 3)](./pix-med-pipes-filters-java-spring-container.mmd)
