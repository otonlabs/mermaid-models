# Sincronizacao DICT com Saga Choreography [GCP]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Saga Choreography

## Descrição
Coreografia de eventos entre PSPs para manter consistencia de chaves

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Coreografia de eventos entre PSPs para manter consistencia de chaves)

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Sincronizacao DICT com Saga Choreography (GCP)](./pix-dict-saga-choreography-context.mmd)
