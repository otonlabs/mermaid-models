# Migracao do Legado DICT via Strangler Fig [GCP]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Strangler Fig

## Descrição
Migracao gradual do sistema legado de chaves para nova plataforma cloud-native

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Migracao gradual do sistema legado de chaves para nova plataforma cloud-native)

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Migracao do Legado DICT via Strangler Fig (GCP)](./pix-dict-strangler-fig-context.mmd)
