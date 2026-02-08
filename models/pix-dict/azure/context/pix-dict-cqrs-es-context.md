# DICT com CQRS e Event Sourcing [Azure]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** CQRS + Event Sourcing

## Descrição
Separacao de comandos de registro/alteracao e consultas de chave com historico completo

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Separacao de comandos de registro/alteracao e consultas de chave com historico c)

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[DICT com CQRS e Event Sourcing (Azure)](./pix-dict-cqrs-es-context.mmd)
