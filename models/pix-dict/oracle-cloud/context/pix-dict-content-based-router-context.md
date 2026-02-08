# Registro de Chave PIX via Content-Based Router [Oracle Cloud]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Content-Based Router

## Descrição
Roteamento de registros EVP, CPF, CNPJ, email e telefone para processadores especializados

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Roteamento de registros EVP, CPF, CNPJ, email e telefone para processadores espe)
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
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Registro de Chave PIX via Content-Based Router (Oracle Cloud)](./pix-dict-content-based-router-context.mmd)
