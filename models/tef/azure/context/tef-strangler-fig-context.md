# TEF com Strangler Fig [Azure]

## Domínio
TEF — Transferencia Eletronica de Fundos

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Migra incrementalmente de sistema legado para novo no contexto de transferencia eletronica de fundos

## Componentes Principais
- **TEF Platform** — sistema principal (Migra incrementalmente de sistema legado para novo no contexto de transferencia )

## Integrações Externas
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF com Strangler Fig (Azure)](./tef-strangler-fig-context.mmd)
