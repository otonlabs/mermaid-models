# Data Pipeline com Dead Letter Channel [GCP]

## Domínio
Data Pipeline — Pipeline de Dados e Data Lake

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de pipeline de dados e data lake

## Componentes Principais
- **Data Pipeline Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Core Banking Source** — Fonte de dados transacionais
- **Payment Source** — Fonte de dados de pagamentos
- **BI Tools** — Ferramentas de Business Intelligence

## Diagrama
[Data Pipeline com Dead Letter Channel (GCP)](./data-pipeline-dead-letter-context.mmd)
