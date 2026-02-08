# Tratamento de Falhas DICT via Dead Letter [Azure]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Dead Letter Channel

## Descrição
Recuperacao de mensagens de sincronizacao DICT que falharam

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Recuperacao de mensagens de sincronizacao DICT que falharam)

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Tratamento de Falhas DICT via Dead Letter (Azure)](./pix-dict-dead-letter-context.mmd)
