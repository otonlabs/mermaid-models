# DLQ para Pagamentos Rejeitados pelo SPI [GCP]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Tratamento de rejeicoes do SPI com retry automatico e escalacao

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Tratamento de rejeicoes do SPI com retry automatico e escalacao)

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[DLQ para Pagamentos Rejeitados pelo SPI (GCP)](./pix-spi-dead-letter-context.mmd)
