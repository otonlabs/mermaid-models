# Credit Lending com CQRS + Event Sourcing [Azure]

## Domínio
Credit Lending — Credito e Emprestimos

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de credito e emprestimos

## Componentes Principais
- **Credit Lending Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **Bureau Credito SCR** — Sistema de informacoes de credito BACEN
- **BACEN SCR** — Central de risco do BACEN
- **Seguradora** — Seguro prestamista

## Diagrama
[Credit Lending com CQRS + Event Sourcing (Azure)](./credit-lending-cqrs-es-context.mmd)
