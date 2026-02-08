# Reconciliation com CQRS + Event Sourcing [Azure]

## Domínio
Reconciliation — Reconciliacao Financeira

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de reconciliacao financeira

## Componentes Principais
- **Reconciliation Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **Core Banking** — Sistema core de contas
- **Payment Processor** — Processador de pagamentos
- **External Statement** — Extratos de contrapartes

## Diagrama
[Reconciliation com CQRS + Event Sourcing (Azure)](./reconciliation-cqrs-es-context.mmd)
