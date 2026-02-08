# Broadcast de Liquidacao SPI via Pub-Sub [GCP]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Descrição
Notificacao em tempo real de liquidacao para tesouraria, contabilidade e reconciliacao

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Notificacao em tempo real de liquidacao para tesouraria, contabilidade e reconci)

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[Broadcast de Liquidacao SPI via Pub-Sub (GCP)](./pix-spi-pub-sub-context.mmd)
