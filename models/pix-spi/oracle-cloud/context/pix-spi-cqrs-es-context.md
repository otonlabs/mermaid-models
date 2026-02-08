# PIX com CQRS para Alta Volumetria [Oracle Cloud]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Write path otimizado para insercao e read path com projecoes para consulta de status

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Write path otimizado para insercao e read path com projecoes para consulta de st)

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[PIX com CQRS para Alta Volumetria (Oracle Cloud)](./pix-spi-cqrs-es-context.mmd)
