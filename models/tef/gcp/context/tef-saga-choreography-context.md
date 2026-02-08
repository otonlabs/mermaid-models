# TEF com Saga Choreography [GCP]

## Domínio
TEF — Transferencia Eletronica de Fundos

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Choreography

## Descrição
Coordena transacoes distribuidas via coreografia de eventos no contexto de transferencia eletronica de fundos

## Componentes Principais
- **TEF Platform** — sistema principal (Coordena transacoes distribuidas via coreografia de eventos no contexto de trans)

## Integrações Externas
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF com Saga Choreography (GCP)](./tef-saga-choreography-context.mmd)
