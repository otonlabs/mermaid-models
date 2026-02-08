# TEF com CQRS + Event Sourcing [AWS]

## Domínio
TEF — Transferencia Eletronica de Fundos

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de transferencia eletronica de fundos

## Componentes Principais
- **TEF Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF com CQRS + Event Sourcing (AWS)](./tef-cqrs-es-context.mmd)
