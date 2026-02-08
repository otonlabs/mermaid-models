# Payments com Strangler Fig [GCP]

## Domínio
Payments — Processamento de Pagamentos

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Migra incrementalmente de sistema legado para novo no contexto de processamento de pagamentos

## Componentes Principais
- **Payments Platform** — sistema principal (Migra incrementalmente de sistema legado para novo no contexto de processamento )

## Integrações Externas
- **Rede Adquirente** — Processadora de cartoes
- **PIX SPI** — Sistema PIX do BACEN
- **TED DOC CIP** — Transferencias interbancarias

## Diagrama
[Payments com Strangler Fig (GCP)](./payments-strangler-fig-context.mmd)
