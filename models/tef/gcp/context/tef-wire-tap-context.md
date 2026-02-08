# TEF com Wire Tap [GCP]

## Domínio
TEF — Transferencia Eletronica de Fundos

## Cloud Provider
GCP

## Nível C4
Context

## Padrão Utilizado
- **Tipo:** EIP
- **Padrão:** Wire Tap

## Descrição
Intercepta e registra mensagens em transito para auditoria aplicado ao contexto de transferencia eletronica de fundos

## Componentes Principais
- **TEF Platform** — sistema principal (Intercepta e registra mensagens em transito para auditoria aplicado ao contexto )

## Integrações Externas
- **Rede Adquirente** — Processadora de transacoes
- **Bandeira** — Visa, Mastercard, Elo
- **Banco Emissor** — Banco emissor do cartao

## Diagrama
[TEF com Wire Tap (GCP)](./tef-wire-tap-context.mmd)
