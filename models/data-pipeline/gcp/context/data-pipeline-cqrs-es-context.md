# Data Pipeline com CQRS + Event Sourcing [GCP]

## Domínio
Data Pipeline — Pipeline de Dados e Data Lake

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de pipeline de dados e data lake

## Componentes Principais
- **Data Pipeline Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **Core Banking Source** — Fonte de dados transacionais
- **Payment Source** — Fonte de dados de pagamentos
- **BI Tools** — Ferramentas de Business Intelligence

## Diagrama
[Data Pipeline com CQRS + Event Sourcing (GCP)](./data-pipeline-cqrs-es-context.mmd)
