# TEF com Circuit Breaker [Azure]

## Domínio
TEF — Transferencia Eletronica de Fundos

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Circuit Breaker

## Descrição
Previne falhas em cascata com circuit breaker pattern no contexto de transferencia eletronica de fundos

## Componentes Principais
- **TEF Platform** — sistema principal (Previne falhas em cascata com circuit breaker pattern no contexto de transferenc)

## Integrações Externas
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF com Circuit Breaker (Azure)](./tef-circuit-breaker-context.mmd)
