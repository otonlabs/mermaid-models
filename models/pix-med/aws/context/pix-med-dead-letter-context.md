# Reprocessamento de MEDs Falhos via DLQ [AWS]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Tratamento de falhas na comunicacao com BACEN MED

## Componentes Principais
- **PIX MED Platform** — sistema principal (Tratamento de falhas na comunicacao com BACEN MED)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Reprocessamento de MEDs Falhos via DLQ (AWS)](./pix-med-dead-letter-context.mmd)
