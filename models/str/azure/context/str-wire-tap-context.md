# STR com Wire Tap [Azure]

## Domínio
STR — Sistema de Transferencia de Reservas

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Intercepta e registra mensagens em transito para auditoria aplicado ao contexto de sistema de transferencia de reservas

## Componentes Principais
- **STR Platform** — sistema principal (Intercepta e registra mensagens em transito para auditoria aplicado ao contexto )

## Integrações Externas
- **BACEN STR** — Sistema de Transferencia de Reservas
- **Banco Participante** — Banco com conta reserva
- **Camara LBTR** — Liquidacao bruta em tempo real

## Diagrama
[STR com Wire Tap (Azure)](./str-wire-tap-context.mmd)
