# Reconciliation com Dead Letter Channel [AWS]

## Domínio
Reconciliation — Reconciliacao Financeira

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de reconciliacao financeira

## Componentes Principais
- **Reconciliation Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Core Banking** — Sistema core de contas
- **Payment Processor** — Processador de pagamentos
- **External Statement** — Extratos de contrapartes

## Diagrama
[Reconciliation com Dead Letter Channel (AWS)](./reconciliation-dead-letter-context.mmd)
