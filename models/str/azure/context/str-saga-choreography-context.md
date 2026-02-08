# STR com Saga Choreography [Azure]

## Domínio
STR — Sistema de Transferencia de Reservas

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Choreography

## Descrição
Coordena transacoes distribuidas via coreografia de eventos no contexto de sistema de transferencia de reservas

## Componentes Principais
- **STR Platform** — sistema principal (Coordena transacoes distribuidas via coreografia de eventos no contexto de siste)

## Integrações Externas
- **BACEN STR** — Sistema de Transferencia de Reservas
- **Banco Participante** — Banco com conta reserva
- **Camara LBTR** — Liquidacao bruta em tempo real

## Diagrama
[STR com Saga Choreography (Azure)](./str-saga-choreography-context.mmd)
