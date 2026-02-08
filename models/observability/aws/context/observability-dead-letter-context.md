# Observability com Dead Letter Channel [AWS]

## Domínio
Observability — Observabilidade e Monitoramento

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de observabilidade e monitoramento

## Componentes Principais
- **Observability Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Application Services** — Servicos monitorados
- **PagerDuty** — Plataforma de alertas
- **Grafana Cloud** — Plataforma de dashboards

## Diagrama
[Observability com Dead Letter Channel (AWS)](./observability-dead-letter-context.mmd)
