# MED Choreography entre PSPs [AWS]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Choreography

## Descrição
Coreografia de eventos entre PSP pagador, PSP recebedor e BACEN

## Componentes Principais
- **PIX MED Platform** — sistema principal (Coreografia de eventos entre PSP pagador, PSP recebedor e BACEN)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[MED Choreography entre PSPs (AWS)](./pix-med-saga-choreography-context.mmd)
