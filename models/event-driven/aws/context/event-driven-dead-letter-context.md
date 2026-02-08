# Event Driven com Dead Letter Channel [AWS]

## Domínio
Event Driven — Arquitetura Event-Driven

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de arquitetura event-driven

## Componentes Principais
- **Event Driven Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Producer Services** — Servicos produtores de eventos
- **Consumer Services** — Servicos consumidores
- **Monitoring** — Monitoramento de eventos

## Diagrama
[Event Driven com Dead Letter Channel (AWS)](./event-driven-dead-letter-context.mmd)
