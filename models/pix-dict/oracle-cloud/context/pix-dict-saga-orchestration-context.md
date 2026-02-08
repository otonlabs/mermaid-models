# Reivindicacao de Chave com Saga Orchestration [Oracle Cloud]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Orchestration

## Descrição
Orquestracao do fluxo de reivindicacao com timeout de 7 dias e compensacao

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Orquestracao do fluxo de reivindicacao com timeout de 7 dias e compensacao)

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Reivindicacao de Chave com Saga Orchestration (Oracle Cloud)](./pix-dict-saga-orchestration-context.mmd)
