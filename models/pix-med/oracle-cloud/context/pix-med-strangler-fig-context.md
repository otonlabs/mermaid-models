# Migracao do Legado MED via Strangler Fig [Oracle Cloud]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Transicao gradual de sistema batch de devolucao para real-time MED

## Componentes Principais
- **PIX MED Platform** — sistema principal (Transicao gradual de sistema batch de devolucao para real-time MED)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Migracao do Legado MED via Strangler Fig (Oracle Cloud)](./pix-med-strangler-fig-context.mmd)
