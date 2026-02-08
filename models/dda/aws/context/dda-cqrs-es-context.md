# DDA com CQRS + Event Sourcing [AWS]

## Domínio
DDA — Debito Direto Autorizado

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de debito direto autorizado

## Componentes Principais
- **DDA Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **CIP DDA** — Central de registro DDA
- **Banco Sacado** — Banco do pagador
- **Registro Boletos** — Sistema de registro de boletos

## Diagrama
[DDA com CQRS + Event Sourcing (AWS)](./dda-cqrs-es-context.mmd)
