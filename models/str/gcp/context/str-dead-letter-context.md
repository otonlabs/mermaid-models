# STR com Dead Letter Channel [GCP]

## Domínio
STR — Sistema de Transferencia de Reservas

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de sistema de transferencia de reservas

## Componentes Principais
- **STR Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **BACEN STR** — Sistema de Transferencia de Reservas
- **Banco Participante** — Banco com conta reserva
- **Camara LBTR** — Liquidacao bruta em tempo real

## Diagrama
[STR com Dead Letter Channel (GCP)](./str-dead-letter-context.mmd)
