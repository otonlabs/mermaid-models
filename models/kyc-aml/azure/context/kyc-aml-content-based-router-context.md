# KYC AML com Content-Based Router [Azure]

## Domínio
KYC AML — Know Your Customer e Anti-Lavagem

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Content-Based Router

## Descrição
Roteia mensagens para canais diferentes baseado no conteudo aplicado ao contexto de know your customer e anti-lavagem

## Componentes Principais
- **KYC AML Platform** — sistema principal (Roteia mensagens para canais diferentes baseado no conteudo aplicado ao contexto)

## Integrações Externas
- **Receita Federal** — Validacao de CPF/CNPJ
- **COAF** — Conselho de Controle de Atividades Financeiras
- **OFAC Sanctions** — Lista de sancoes internacionais

## Diagrama
[KYC AML com Content-Based Router (Azure)](./kyc-aml-content-based-router-context.mmd)
