# TEF com Saga Orchestration [Azure]

## Domínio
TEF — Transferencia Eletronica de Fundos

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Coordena transacoes distribuidas via orquestrador central no contexto de transferencia eletronica de fundos

## Componentes Principais
- **TEF Platform** — sistema principal (Coordena transacoes distribuidas via orquestrador central no contexto de transfe)

## Integrações Externas
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF com Saga Orchestration (Azure)](./tef-saga-orchestration-context.mmd)
