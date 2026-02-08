# Triagem de Notificacoes MED por Tipo [Azure]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Content-Based Router

## Descrição
Roteamento de MED tipo 1 (fraude) vs tipo 2 (falha operacional) para fluxos distintos

## Componentes Principais
- **PIX MED Platform** — sistema principal (Roteamento de MED tipo 1 (fraude) vs tipo 2 (falha operacional) para fluxos dist)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Triagem de Notificacoes MED por Tipo (Azure)](./pix-med-content-based-router-context.mmd)
