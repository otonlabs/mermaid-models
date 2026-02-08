# DevOps CICD com Content-Based Router [Oracle Cloud]

## Domínio
DevOps CICD — DevOps e Pipelines CI/CD

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Content-Based Router

## Descrição
Roteia mensagens para canais diferentes baseado no conteudo aplicado ao contexto de devops e pipelines ci/cd

## Componentes Principais
- **DevOps CICD Gateway** — Gateway principal para devops e pipelines ci/cd
- **Content-Based Router Engine** — Motor de content-based router para processamento
- **DevOps CICD Monitor** — Monitoramento e alertas de devops e pipelines ci/cd
- **OCI Queue Queue** — canal de mensagens para content-based-router

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
- **Git Repository** — Repositorio de codigo fonte
- **Container Registry** — Registro de imagens Docker
- **Security Scanner** — Scanner SAST/DAST

## Diagrama
[DevOps CICD com Content-Based Router (Oracle Cloud)](./devops-cicd-content-based-router-context.mmd)
