# Auditoria de Operacoes DICT via Wire Tap [Azure]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Azure

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Interceptacao e registro de todas as operacoes de chave para compliance

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Interceptacao e registro de todas as operacoes de chave para compliance)

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Auditoria de Operacoes DICT via Wire Tap (Azure)](./pix-dict-wire-tap-context.mmd)
