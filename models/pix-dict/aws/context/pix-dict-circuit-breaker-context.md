# Consulta DICT com Circuit Breaker [AWS]

## Domínio
PIX DICT — Diretorio de Identificadores de Contas Transacionais

## Cloud Provider
AWS

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** Design Pattern
- **Padrão:** Circuit Breaker

## Descrição
Protecao contra indisponibilidade da API DICT BACEN com fallback para cache local

## Componentes Principais
- **PIX DICT Platform** — sistema principal (Protecao contra indisponibilidade da API DICT BACEN com fallback para cache loca)

## Integrações Externas
- **BACEN DICT** — API DICT do Banco Central para registro de chaves
- **Participante PSP** — Instituicao participante do arranjo PIX
- **SPI** — Sistema de Pagamentos Instantaneos

## Diagrama
[Consulta DICT com Circuit Breaker (AWS)](./pix-dict-circuit-breaker-context.mmd)
