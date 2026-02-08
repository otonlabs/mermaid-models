# DevOps CICD - Message Translator Container View [AWS / Java 21 / Spring Boot 3]

## Domínio
DevOps CICD — DevOps e Pipelines CI/CD

## Cloud Provider
AWS

## Nível C4
Container

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Message Translator

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Traduz mensagens entre formatos diferentes via modelo canonico na camada de containers de devops e pipelines ci/cd

## Componentes Principais
- **DevOps CICD Service** — serviço principal rodando em ECS Fargate
- **Message Translator Processor** — processador do padrão EIP
- **SQS Queue** — canal de mensagens principal
- **Message Translator Channel** — canal do padrão EIP via SNS
- **Primary Database** — Aurora PostgreSQL
- **Cache Layer** — ElastiCache Redis

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
- **Git Repository** — Repositorio de codigo fonte
- **Container Registry** — Registro de imagens Docker
- **Security Scanner** — Scanner SAST/DAST

## Diagrama
[DevOps CICD - Message Translator Container View (AWS / Java 21 / Spring Boot 3)](./devops-cicd-message-translator-java-spring-container.mmd)
