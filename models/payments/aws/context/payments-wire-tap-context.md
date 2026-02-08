# Payments com Wire Tap [AWS]

## Domínio
Payments — Processamento de Pagamentos

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Intercepta e registra mensagens em transito para auditoria aplicado ao contexto de processamento de pagamentos

## Componentes Principais
- **Payments Platform** — sistema principal (Intercepta e registra mensagens em transito para auditoria aplicado ao contexto )

## Integrações Externas
- **Rede Adquirente** — Processadora de cartoes
- **PIX SPI** — Sistema PIX do BACEN
- **TED DOC CIP** — Transferencias interbancarias

## Diagrama
[Payments com Wire Tap (AWS)](./payments-wire-tap-context.mmd)
