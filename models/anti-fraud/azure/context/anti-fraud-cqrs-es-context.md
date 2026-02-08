# Anti-Fraud com CQRS + Event Sourcing [Azure]

## Domínio
Anti-Fraud — Motor Anti-Fraude e Risco

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de motor anti-fraude e risco

## Componentes Principais
- **Anti-Fraud Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **Bureau de Fraude** — Base de dados de fraudadores
- **Device Fingerprint** — Servico de device ID
- **BACEN MED** — Mecanismo Especial de Devolucao

## Diagrama
[Anti-Fraud com CQRS + Event Sourcing (Azure)](./anti-fraud-cqrs-es-context.mmd)
