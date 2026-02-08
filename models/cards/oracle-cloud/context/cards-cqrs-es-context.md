# Cards com CQRS + Event Sourcing [Oracle Cloud]

## Domínio
Cards — Processamento de Cartoes

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de processamento de cartoes

## Componentes Principais
- **Cards Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **Bandeira Visa Master** — Redes de cartao
- **TSP Token Requestor** — Provedor de tokenizacao
- **Rede Adquirente** — Processadora de transacoes

## Diagrama
[Cards com CQRS + Event Sourcing (Oracle Cloud)](./cards-cqrs-es-context.mmd)
