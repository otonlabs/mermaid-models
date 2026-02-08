# KYC AML com Dead Letter Channel [Oracle Cloud]

## Domínio
KYC AML — Know Your Customer e Anti-Lavagem

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de know your customer e anti-lavagem

## Componentes Principais
- **KYC AML Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Receita Federal** — Validacao de CPF/CNPJ
- **COAF** — Conselho de Controle de Atividades Financeiras
- **OFAC Sanctions** — Lista de sancoes internacionais

## Diagrama
[KYC AML com Dead Letter Channel (Oracle Cloud)](./kyc-aml-dead-letter-context.mmd)
