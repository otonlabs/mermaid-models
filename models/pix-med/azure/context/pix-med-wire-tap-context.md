# Auditoria Completa do Fluxo MED via Wire Tap [Azure]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Registro detalhado de cada step do MED para conformidade regulatoria

## Componentes Principais
- **PIX MED Platform** — sistema principal (Registro detalhado de cada step do MED para conformidade regulatoria)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Auditoria Completa do Fluxo MED via Wire Tap (Azure)](./pix-med-wire-tap-context.mmd)
