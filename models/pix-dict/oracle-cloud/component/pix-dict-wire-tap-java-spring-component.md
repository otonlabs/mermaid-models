# PIX DICT - Wire Tap - Component View [Oracle Cloud / Java 21 / Spring Boot 3]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Oracle Cloud

## Nível C4
Component

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Stack Tecnológico
Java 21 / Spring Boot 3

## Descrição
Interceptacao e registro de todas as operacoes de chave para compliance

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
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[PIX DICT - Wire Tap - Component View (Oracle Cloud / Java 21 / Spring Boot 3)](./pix-dict-wire-tap-java-spring-component.mmd)
