# DDA com Strangler Fig [Azure]

## Domínio
DDA — Debito Direto Autorizado

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Migra incrementalmente de sistema legado para novo no contexto de debito direto autorizado

## Componentes Principais
- **DDA Platform** — sistema principal (Migra incrementalmente de sistema legado para novo no contexto de debito direto )

## Integrações Externas
- **CIP DDA** — Central de registro DDA
- **Banco Sacado** — Banco do pagador
- **Registro Boletos** — Sistema de registro de boletos

## Diagrama
[DDA com Strangler Fig (Azure)](./dda-strangler-fig-context.mmd)
