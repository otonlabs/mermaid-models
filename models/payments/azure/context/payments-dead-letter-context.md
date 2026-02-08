# Payments com Dead Letter Channel [Azure]

## Domínio
Payments — Processamento de Pagamentos

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de processamento de pagamentos

## Componentes Principais
- **Payments Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Rede Adquirente** — Processadora de cartoes
- **PIX SPI** — Sistema PIX do BACEN
- **TED DOC CIP** — Transferencias interbancarias

## Diagrama
[Payments com Dead Letter Channel (Azure)](./payments-dead-letter-context.mmd)
