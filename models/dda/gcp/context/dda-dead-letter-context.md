# DDA com Dead Letter Channel [GCP]

## Domínio
DDA — Debito Direto Autorizado

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de debito direto autorizado

## Componentes Principais
- **DDA Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **CIP DDA** — Central de registro DDA
- **Banco Sacado** — Banco do pagador
- **Registro Boletos** — Sistema de registro de boletos

## Diagrama
[DDA com Dead Letter Channel (GCP)](./dda-dead-letter-context.mmd)
