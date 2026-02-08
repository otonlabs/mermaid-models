# Payments com CQRS + Event Sourcing [Azure]

## Domínio
Payments — Processamento de Pagamentos

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de processamento de pagamentos

## Componentes Principais
- **Payments Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **Rede Adquirente** — Processadora de cartoes
- **PIX SPI** — Sistema PIX do BACEN
- **TED DOC CIP** — Transferencias interbancarias

## Diagrama
[Payments com CQRS + Event Sourcing (Azure)](./payments-cqrs-es-context.mmd)
