# DevOps CICD com Saga Orchestration [Azure]

## Domínio
DevOps CICD — DevOps e Pipelines CI/CD

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Coordena transacoes distribuidas via orquestrador central no contexto de devops e pipelines ci/cd

## Componentes Principais
- **DevOps CICD Command Service** — Servico de comandos para devops e pipelines ci/cd
- **Saga Orchestration Handler** — Handler do padrao Saga Orchestration
- **DevOps CICD Query Service** — Servico de consultas otimizadas
- **Azure SQL Database** — persistência principal do domínio

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
[DevOps CICD com Saga Orchestration (Azure)](./devops-cicd-saga-orchestration-context.mmd)
