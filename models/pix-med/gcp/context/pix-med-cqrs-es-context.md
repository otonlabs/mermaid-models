# MED com Event Sourcing para Rastreabilidade [GCP]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Historico completo e imutavel de cada caso MED para auditoria BACEN

## Componentes Principais
- **PIX MED Platform** — sistema principal (Historico completo e imutavel de cada caso MED para auditoria BACEN)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[MED com Event Sourcing para Rastreabilidade (GCP)](./pix-med-cqrs-es-context.mmd)
