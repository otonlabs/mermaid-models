# Portabilidade de Chave com Splitter-Aggregator [Oracle Cloud]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
Oracle Cloud

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Splitter-Aggregator

## Descrição
Divide processo de portabilidade em validacao no doador e confirmacao no reivindicador

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Divide processo de portabilidade em validacao no doador e confirmacao no reivind)

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Portabilidade de Chave com Splitter-Aggregator (Oracle Cloud)](./pix-dict-splitter-aggregator-context.mmd)
