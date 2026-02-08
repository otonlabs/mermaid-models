# TEF com Dead Letter Channel [GCP]

## Domínio
TEF — Transferencia Eletronica de Fundos

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de transferencia eletronica de fundos

## Componentes Principais
- **TEF Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF com Dead Letter Channel (GCP)](./tef-dead-letter-context.mmd)
