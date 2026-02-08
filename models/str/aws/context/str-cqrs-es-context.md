# STR com CQRS + Event Sourcing [AWS]

## Domínio
STR — Sistema de Transferencia de Reservas

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de sistema de transferencia de reservas

## Componentes Principais
- **STR Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **BACEN STR** — Sistema de Transferencia de Reservas
- **Banco Participante** — Banco com conta reserva
- **Camara LBTR** — Liquidacao bruta em tempo real

## Diagrama
[STR com CQRS + Event Sourcing (AWS)](./str-cqrs-es-context.mmd)
