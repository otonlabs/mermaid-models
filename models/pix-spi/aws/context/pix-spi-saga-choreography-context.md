# PIX com Saga Choreography entre Participantes [AWS]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Choreography

## Descrição
Coreografia de eventos entre PSP pagador, SPI e PSP recebedor

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Coreografia de eventos entre PSP pagador, SPI e PSP recebedor)

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[PIX com Saga Choreography entre Participantes (AWS)](./pix-spi-saga-choreography-context.mmd)
