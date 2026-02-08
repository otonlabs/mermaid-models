# Cards com Wire Tap [AWS]

## Domínio
Cards — Processamento de Cartoes

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Intercepta e registra mensagens em transito para auditoria aplicado ao contexto de processamento de cartoes

## Componentes Principais
- **Cards Platform** — sistema principal (Intercepta e registra mensagens em transito para auditoria aplicado ao contexto )

## Integrações Externas
- **Bandeira Visa Master** — Redes de cartao
- **TSP Token Requestor** — Provedor de tokenizacao
- **Rede Adquirente** — Processadora de transacoes

## Diagrama
[Cards com Wire Tap (AWS)](./cards-wire-tap-context.mmd)
