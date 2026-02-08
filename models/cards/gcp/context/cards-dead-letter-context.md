# Cards com Dead Letter Channel [GCP]

## Domínio
Cards — Processamento de Cartoes

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de processamento de cartoes

## Componentes Principais
- **Cards Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Bandeira Visa Master** — Redes de cartao
- **TSP Token Requestor** — Provedor de tokenizacao
- **Rede Adquirente** — Processadora de transacoes

## Diagrama
[Cards com Dead Letter Channel (GCP)](./cards-dead-letter-context.mmd)
