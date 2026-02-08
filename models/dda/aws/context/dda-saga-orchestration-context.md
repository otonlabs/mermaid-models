# DDA com Saga Orchestration [AWS]

## Domínio
DDA — Debito Direto Autorizado

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Coordena transacoes distribuidas via orquestrador central no contexto de debito direto autorizado

## Componentes Principais
- **DDA Platform** — sistema principal (Coordena transacoes distribuidas via orquestrador central no contexto de debito )

## Integrações Externas
- **CIP DDA** — Central de registro DDA
- **Banco Sacado** — Banco do pagador
- **Registro Boletos** — Sistema de registro de boletos

## Diagrama
[DDA com Saga Orchestration (AWS)](./dda-saga-orchestration-context.mmd)
