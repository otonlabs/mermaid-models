# KYC AML com CQRS + Event Sourcing [AWS]

## Domínio
KYC AML — Know Your Customer e Anti-Lavagem

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separa modelos de leitura e escrita com estado baseado em eventos no contexto de know your customer e anti-lavagem

## Componentes Principais
- **KYC AML Platform** — sistema principal (Separa modelos de leitura e escrita com estado baseado em eventos no contexto de)

## Integrações Externas
- **Receita Federal** — Validacao de CPF/CNPJ
- **COAF** — Conselho de Controle de Atividades Financeiras
- **OFAC Sanctions** — Lista de sancoes internacionais

## Diagrama
[KYC AML com CQRS + Event Sourcing (AWS)](./kyc-aml-cqrs-es-context.mmd)
