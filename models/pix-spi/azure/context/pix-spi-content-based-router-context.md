# Roteamento de Pagamentos PIX por Tipo [Azure]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Content-Based Router

## Descrição
Router que direciona PIX instantaneo, agendado, com troco e saque para processadores especificos

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Router que direciona PIX instantaneo, agendado, com troco e saque para processad)

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[Roteamento de Pagamentos PIX por Tipo (Azure)](./pix-spi-content-based-router-context.mmd)
