# Cards com Strangler Fig [GCP]

## Domínio
Cards — Processamento de Cartoes

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Migra incrementalmente de sistema legado para novo no contexto de processamento de cartoes

## Componentes Principais
- **Cards Platform** — sistema principal (Migra incrementalmente de sistema legado para novo no contexto de processamento )

## Integrações Externas
- **Bandeira Visa Master** — Redes de cartao
- **TSP Token Requestor** — Provedor de tokenizacao
- **Rede Adquirente** — Processadora de transacoes

## Diagrama
[Cards com Strangler Fig (GCP)](./cards-strangler-fig-context.mmd)
