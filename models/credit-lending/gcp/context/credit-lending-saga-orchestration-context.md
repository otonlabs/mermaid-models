# Credit Lending com Saga Orchestration [GCP]

## Domínio
Credit Lending — Credito e Emprestimos

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Coordena transacoes distribuidas via orquestrador central no contexto de credito e emprestimos

## Componentes Principais
- **Credit Lending Platform** — sistema principal (Coordena transacoes distribuidas via orquestrador central no contexto de credito)

## Integrações Externas
- **Bureau Credito SCR** — Sistema de informacoes de credito BACEN
- **BACEN SCR** — Central de risco do BACEN
- **Seguradora** — Seguro prestamista

## Diagrama
[Credit Lending com Saga Orchestration (GCP)](./credit-lending-saga-orchestration-context.mmd)
