# Migracao para Novo Motor PIX via Strangler Fig [GCP]

## Domínio
PIX SPI — Sistema de Pagamentos Instantaneos

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Migracao gradual de motor de pagamentos monolitico para microservicos

## Componentes Principais
- **PIX SPI Platform** — sistema principal (Migracao gradual de motor de pagamentos monolitico para microservicos)

## Integrações Externas
- **BACEN SPI** — Sistema de Pagamentos Instantaneos do Banco Central
- **Participante Direto** — Instituicao com conta PI no BACEN
- **STR** — Sistema de Transferencia de Reservas

## Diagrama
[Migracao para Novo Motor PIX via Strangler Fig (GCP)](./pix-spi-strangler-fig-context.mmd)
