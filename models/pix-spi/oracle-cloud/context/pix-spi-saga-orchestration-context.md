# Saga de Pagamento PIX com Orquestracao [Oracle Cloud]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Steps: validar conta, debitar pagador, enviar SPI, creditar recebedor, notificar

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Steps: validar conta, debitar pagador, enviar SPI, creditar recebedor, notificar)

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[Saga de Pagamento PIX com Orquestracao (Oracle Cloud)](./pix-spi-saga-orchestration-context.mmd)
