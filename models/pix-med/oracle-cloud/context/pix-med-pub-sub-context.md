# Broadcast de Bloqueio Cautelar via Pub-Sub [Oracle Cloud]

## Domínio
PIX MED — Mecanismo Especial de Devolucao

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Descrição
Notificacao de bloqueio cautelar para todos os canais do recebedor

## Componentes Principais
- **PIX MED Platform** — sistema principal (Notificacao de bloqueio cautelar para todos os canais do recebedor)

## Integrações Externas
- **BACEN MED** — API MED do Banco Central para devolucoes especiais
- **PSP Recebedor** — PSP que recebeu o PIX objeto de devolucao
- **Anti-Fraud System** — Sistema de deteccao de fraude

## Diagrama
[Broadcast de Bloqueio Cautelar via Pub-Sub (Oracle Cloud)](./pix-med-pub-sub-context.mmd)
