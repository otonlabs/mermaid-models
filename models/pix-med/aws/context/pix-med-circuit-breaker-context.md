# Circuit Breaker na API MED BACEN [AWS]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Circuit Breaker

## Descrição
Protecao contra timeout da API MED com queue local e retry

## Componentes Principais
- **PIX MED Platform** — sistema principal (Protecao contra timeout da API MED com queue local e retry)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Circuit Breaker na API MED BACEN (AWS)](./pix-med-circuit-breaker-context.mmd)
