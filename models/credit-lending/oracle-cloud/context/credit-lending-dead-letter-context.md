# Credit Lending com Dead Letter Channel [Oracle Cloud]

## Domínio
Credit Lending — Credito e Emprestimos

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Encaminha mensagens nao processaveis para canal de dead letter aplicado ao contexto de credito e emprestimos

## Componentes Principais
- **Credit Lending Platform** — sistema principal (Encaminha mensagens nao processaveis para canal de dead letter aplicado ao conte)

## Integrações Externas
- **Bureau Credito SCR** — Sistema de informacoes de credito BACEN
- **BACEN SCR** — Central de risco do BACEN
- **Seguradora** — Seguro prestamista

## Diagrama
[Credit Lending com Dead Letter Channel (Oracle Cloud)](./credit-lending-dead-letter-context.mmd)
