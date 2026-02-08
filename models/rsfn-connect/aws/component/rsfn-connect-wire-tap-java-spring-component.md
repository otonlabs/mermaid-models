# RSFN Connect - Wire Tap - Component View [AWS / Java 21 / Spring Boot 3]

## Domínio
RSFN Connect — Rede do Sistema Financeiro Nacional

## Cloud Provider
AWS

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Intercepta e registra mensagens em transito para auditoria aplicado ao contexto de rede do sistema financeiro nacional

## Componentes Principais
- **Tap Interceptor** — responsável por tap interceptor
- **Message Logger** — responsável por message logger
- **Audit Writer** — responsável por audit writer
- **Compliance Reporter** — responsável por compliance reporter

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
- **BACEN RSFN** — Rede do SFN do Banco Central
- **Camara de Compensacao** — Camara de liquidacao
- **Participante SFN** — Instituicao participante do SFN

## Diagrama
[RSFN Connect - Wire Tap - Component View (AWS / Java 21 / Spring Boot 3)](./rsfn-connect-wire-tap-java-spring-component.mmd)
