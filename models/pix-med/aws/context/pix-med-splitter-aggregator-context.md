# Analise de Caso MED com Splitter-Aggregator [AWS]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Splitter-Aggregator

## Descrição
Split de caso em sub-analises paralelas e agregacao de score final

## Componentes Principais
- **PIX MED Platform** — sistema principal (Split de caso em sub-analises paralelas e agregacao de score final)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Analise de Caso MED com Splitter-Aggregator (AWS)](./pix-med-splitter-aggregator-context.mmd)
