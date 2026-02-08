# Anti-Fraud com Dead Letter Channel [AWS]

## Domínio
Anti-Fraud — Motor Anti-Fraude e Risco

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de motor anti-fraude e risco

## Componentes Principais
- **Anti-Fraud Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Bureau de Fraude** — Base de dados de fraudadores
- **Device Fingerprint** — Servico de device ID
- **BACEN MED** — Mecanismo Especial de Devolucao

## Diagrama
[Anti-Fraud com Dead Letter Channel (AWS)](./anti-fraud-dead-letter-context.mmd)
