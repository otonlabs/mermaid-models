# Circuit Breaker para API SPI BACEN [Oracle Cloud]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Circuit Breaker

## Descrição
Protecao contra instabilidade do SPI com queue de retry e notificacao

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Protecao contra instabilidade do SPI com queue de retry e notificacao)

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[Circuit Breaker para API SPI BACEN (Oracle Cloud)](./pix-spi-circuit-breaker-context.mmd)
