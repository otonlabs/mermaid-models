# Notificacao de Alteracao de Chaves via Pub-Sub [AWS]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Publish-Subscribe

## Descrição
Fan-out de eventos de alteracao de chaves para PSPs participantes

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Fan-out de eventos de alteracao de chaves para PSPs participantes)

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Notificacao de Alteracao de Chaves via Pub-Sub (AWS)](./pix-dict-pub-sub-context.mmd)
