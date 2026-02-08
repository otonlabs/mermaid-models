# STR com Saga Orchestration [Azure]

## Domínio
STR — Sistema de Transferencia de Reservas

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Coordena transacoes distribuidas via orquestrador central no contexto de sistema de transferencia de reservas

## Componentes Principais
- **STR Platform** — sistema principal (Coordena transacoes distribuidas via orquestrador central no contexto de sistema)

## Integrações Externas
- **BACEN STR** — Sistema de Transferencia de Reservas
- **Banco Participante** — Banco com conta reserva
- **Camara LBTR** — Liquidacao bruta em tempo real

## Diagrama
[STR com Saga Orchestration (Azure)](./str-saga-orchestration-context.mmd)
