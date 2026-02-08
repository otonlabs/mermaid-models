#!/usr/bin/env python3
"""
Mermaid C4 Diagram Generator for Fintech Architecture Scenarios.

Generates ~3000 unique .mmd files with:
- 25 fintech domains × 4 clouds × 3 C4 levels × 10 variations
- Cloud provider icons via $sprite (icepanel.io SVGs)
- UpdateElementStyle with cloud-specific brand colors
- Unique architecture scenarios (simple, medium, complex)
"""

import re
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════
# CLOUD ICONS (sprites via icepanel.io)
# ═══════════════════════════════════════════════════════════════════

CLOUD_ICONS = {
    "aws": {
        "lambda": 'img:https://icon.icepanel.io/AWS/svg/Compute/Lambda.svg',
        "ecs": 'img:https://icon.icepanel.io/AWS/svg/Containers/Elastic-Container-Service.svg',
        "eks": 'img:https://icon.icepanel.io/AWS/svg/Containers/Elastic-Kubernetes-Service.svg',
        "sqs": 'img:https://icon.icepanel.io/AWS/svg/App-Integration/Simple-Queue-Service.svg',
        "sns": 'img:https://icon.icepanel.io/AWS/svg/App-Integration/Simple-Notification-Service.svg',
        "eventbridge": 'img:https://icon.icepanel.io/AWS/svg/App-Integration/EventBridge.svg',
        "step_functions": 'img:https://icon.icepanel.io/AWS/svg/App-Integration/Step-Functions.svg',
        "kinesis": 'img:https://icon.icepanel.io/AWS/svg/Analytics/Kinesis.svg',
        "aurora": 'img:https://icon.icepanel.io/AWS/svg/Database/Aurora.svg',
        "rds": 'img:https://icon.icepanel.io/AWS/svg/Database/RDS.svg',
        "dynamodb": 'img:https://icon.icepanel.io/AWS/svg/Database/DynamoDB.svg',
        "elasticache": 'img:https://icon.icepanel.io/AWS/svg/Database/ElastiCache.svg',
        "s3": 'img:https://icon.icepanel.io/AWS/svg/Storage/Simple-Storage-Service.svg',
        "api_gw": 'img:https://icon.icepanel.io/AWS/svg/Networking-Content-Delivery/API-Gateway.svg',
        "cloudwatch": 'img:https://icon.icepanel.io/AWS/svg/Management-Governance/CloudWatch.svg',
        "secrets": 'img:https://icon.icepanel.io/AWS/svg/Security-Identity-Compliance/Secrets-Manager.svg',
        "cognito": 'img:https://icon.icepanel.io/AWS/svg/Security-Identity-Compliance/Cognito.svg',
        "sagemaker": 'img:https://icon.icepanel.io/AWS/svg/Machine-Learning/SageMaker.svg',
        "ecr": 'img:https://icon.icepanel.io/AWS/svg/Containers/Elastic-Container-Registry.svg',
        "cloudfront": 'img:https://icon.icepanel.io/AWS/svg/Networking-Content-Delivery/CloudFront.svg',
        "route53": 'img:https://icon.icepanel.io/AWS/svg/Networking-Content-Delivery/Route-53.svg',
        "waf": 'img:https://icon.icepanel.io/AWS/svg/Security-Identity-Compliance/WAF.svg',
        "glue": 'img:https://icon.icepanel.io/AWS/svg/Analytics/Glue.svg',
        "athena": 'img:https://icon.icepanel.io/AWS/svg/Analytics/Athena.svg',
        "msk": 'img:https://icon.icepanel.io/AWS/svg/Analytics/Managed-Streaming-for-Apache-Kafka.svg',
    },
    "azure": {
        "functions": 'img:https://icon.icepanel.io/Azure/svg/Compute/Function-Apps.svg',
        "aks": 'img:https://icon.icepanel.io/Azure/svg/Containers/Kubernetes-Services.svg',
        "app_service": 'img:https://icon.icepanel.io/Azure/svg/Compute/App-Services.svg',
        "service_bus": 'img:https://icon.icepanel.io/Azure/svg/Integration/Service-Bus.svg',
        "event_grid": 'img:https://icon.icepanel.io/Azure/svg/Integration/Event-Grid-Domains.svg',
        "event_hubs": 'img:https://icon.icepanel.io/Azure/svg/Analytics/Event-Hubs.svg',
        "sql_db": 'img:https://icon.icepanel.io/Azure/svg/Databases/SQL-Database.svg',
        "cosmos_db": 'img:https://icon.icepanel.io/Azure/svg/Databases/Azure-Cosmos-DB.svg',
        "redis": 'img:https://icon.icepanel.io/Azure/svg/Databases/Cache-Redis.svg',
        "blob": 'img:https://icon.icepanel.io/Azure/svg/Storage/Storage-Accounts.svg',
        "apim": 'img:https://icon.icepanel.io/Azure/svg/Integration/API-Management-Services.svg',
        "key_vault": 'img:https://icon.icepanel.io/Azure/svg/Security/Key-Vaults.svg',
        "monitor": 'img:https://icon.icepanel.io/Azure/svg/Management-Governance/Monitor.svg',
        "entra_id": 'img:https://icon.icepanel.io/Azure/svg/Identity/Entra-ID.svg',
        "acr": 'img:https://icon.icepanel.io/Azure/svg/Containers/Container-Registries.svg',
        "front_door": 'img:https://icon.icepanel.io/Azure/svg/Networking/Front-Doors.svg',
        "synapse": 'img:https://icon.icepanel.io/Azure/svg/Analytics/Azure-Synapse-Analytics.svg',
        "ml_studio": 'img:https://icon.icepanel.io/Azure/svg/AI-Machine-Learning/Machine-Learning.svg',
        "logic_apps": 'img:https://icon.icepanel.io/Azure/svg/Integration/Logic-Apps.svg',
    },
    "gcp": {
        "cloud_run": 'img:https://icon.icepanel.io/GCP/svg/Compute/Cloud-Run.svg',
        "gke": 'img:https://icon.icepanel.io/GCP/svg/Containers/Google-Kubernetes-Engine.svg',
        "cloud_functions": 'img:https://icon.icepanel.io/GCP/svg/Compute/Cloud-Functions.svg',
        "cloud_tasks": 'img:https://icon.icepanel.io/GCP/svg/App-Integration/Cloud-Tasks.svg',
        "pubsub": 'img:https://icon.icepanel.io/GCP/svg/Analytics/Pub-Sub.svg',
        "dataflow": 'img:https://icon.icepanel.io/GCP/svg/Analytics/Dataflow.svg',
        "cloud_sql": 'img:https://icon.icepanel.io/GCP/svg/Databases/Cloud-SQL.svg',
        "spanner": 'img:https://icon.icepanel.io/GCP/svg/Databases/Cloud-Spanner.svg',
        "firestore": 'img:https://icon.icepanel.io/GCP/svg/Databases/Firestore.svg',
        "bigtable": 'img:https://icon.icepanel.io/GCP/svg/Databases/Cloud-Bigtable.svg',
        "memorystore": 'img:https://icon.icepanel.io/GCP/svg/Databases/Memorystore.svg',
        "gcs": 'img:https://icon.icepanel.io/GCP/svg/Storage/Cloud-Storage.svg',
        "apigee": 'img:https://icon.icepanel.io/GCP/svg/API-Management/Apigee-API-Management.svg',
        "secret_mgr": 'img:https://icon.icepanel.io/GCP/svg/Security/Secret-Manager.svg',
        "cloud_monitoring": 'img:https://icon.icepanel.io/GCP/svg/Operations/Cloud-Monitoring.svg',
        "cloud_iam": 'img:https://icon.icepanel.io/GCP/svg/Security/Cloud-IAM.svg',
        "bigquery": 'img:https://icon.icepanel.io/GCP/svg/Analytics/BigQuery.svg',
        "vertex_ai": 'img:https://icon.icepanel.io/GCP/svg/AI-Machine-Learning/Vertex-AI.svg',
        "artifact_reg": 'img:https://icon.icepanel.io/GCP/svg/CI-CD/Artifact-Registry.svg',
    },
    "oracle-cloud": {
        "functions": 'img:https://icon.icepanel.io/OCI/svg/Developer-Services/Functions.svg',
        "oke": 'img:https://icon.icepanel.io/OCI/svg/Developer-Services/Container-Engine-for-Kubernetes.svg',
        "queue": 'img:https://icon.icepanel.io/OCI/svg/Developer-Services/Queue.svg',
        "streaming": 'img:https://icon.icepanel.io/OCI/svg/Developer-Services/Streaming.svg',
        "events": 'img:https://icon.icepanel.io/OCI/svg/Developer-Services/Events.svg',
        "autonomous_db": 'img:https://icon.icepanel.io/OCI/svg/Oracle-Database/Autonomous-Database.svg',
        "nosql": 'img:https://icon.icepanel.io/OCI/svg/Oracle-Database/NoSQL-Database.svg',
        "cache": 'img:https://icon.icepanel.io/OCI/svg/Developer-Services/Cache.svg',
        "object_storage": 'img:https://icon.icepanel.io/OCI/svg/Storage/Object-Storage.svg',
        "api_gw": 'img:https://icon.icepanel.io/OCI/svg/Developer-Services/API-Gateway.svg',
        "vault": 'img:https://icon.icepanel.io/OCI/svg/Security/Vault.svg',
        "monitoring": 'img:https://icon.icepanel.io/OCI/svg/Observability-Management/Monitoring.svg',
        "iam": 'img:https://icon.icepanel.io/OCI/svg/Identity-Security/Identity-and-Access-Management.svg',
        "data_science": 'img:https://icon.icepanel.io/OCI/svg/AI-ML/Data-Science.svg',
        "ocir": 'img:https://icon.icepanel.io/OCI/svg/Developer-Services/Container-Registry.svg',
        "service_mesh": 'img:https://icon.icepanel.io/OCI/svg/Developer-Services/Service-Mesh.svg',
    },
}

# ═══════════════════════════════════════════════════════════════════
# CLOUD STYLES
# ═══════════════════════════════════════════════════════════════════

CLOUD_STYLES = {
    "aws": {"bg": "#FF9900", "font": "#232F3E", "border": "#232F3E"},
    "azure": {"bg": "#0078D4", "font": "#FFFFFF", "border": "#002050"},
    "gcp": {"bg": "#4285F4", "font": "#FFFFFF", "border": "#1A73E8"},
    "oracle-cloud": {"bg": "#F80000", "font": "#FFFFFF", "border": "#C74634"},
}

# ═══════════════════════════════════════════════════════════════════
# CLOUD SERVICE MAPPINGS (name + icon key)
# ═══════════════════════════════════════════════════════════════════

CLOUDS = {
    "aws": {
        "label": "AWS",
        "compute": ("ECS Fargate", "ecs"), "compute_fn": ("Lambda", "lambda"), "compute_k8s": ("EKS", "eks"),
        "queue": ("SQS", "sqs"), "pubsub": ("SNS", "sns"), "eventbus": ("EventBridge", "eventbridge"),
        "stream": ("Kinesis", "kinesis"), "orchestrator": ("Step Functions", "step_functions"),
        "db_rel": ("Aurora PostgreSQL", "aurora"), "db_nosql": ("DynamoDB", "dynamodb"),
        "cache": ("ElastiCache Redis", "elasticache"), "storage": ("S3", "s3"),
        "api_gw": ("API Gateway", "api_gw"), "secret": ("Secrets Manager", "secrets"),
        "monitoring": ("CloudWatch", "cloudwatch"), "iam": ("Cognito", "cognito"),
        "registry": ("ECR", "ecr"), "cdn": ("CloudFront", "cloudfront"),
        "ml": ("SageMaker", "sagemaker"), "datalake": ("S3 + Glue + Athena", "glue"),
        "waf": ("WAF", "waf"), "kafka": ("MSK", "msk"),
    },
    "azure": {
        "label": "Azure",
        "compute": ("App Service", "app_service"), "compute_fn": ("Azure Functions", "functions"), "compute_k8s": ("AKS", "aks"),
        "queue": ("Service Bus Queue", "service_bus"), "pubsub": ("Service Bus Topics", "service_bus"), "eventbus": ("Event Grid", "event_grid"),
        "stream": ("Event Hubs", "event_hubs"), "orchestrator": ("Logic Apps", "logic_apps"),
        "db_rel": ("Azure SQL Database", "sql_db"), "db_nosql": ("Cosmos DB", "cosmos_db"),
        "cache": ("Azure Cache for Redis", "redis"), "storage": ("Blob Storage", "blob"),
        "api_gw": ("API Management", "apim"), "secret": ("Key Vault", "key_vault"),
        "monitoring": ("Azure Monitor", "monitor"), "iam": ("Entra ID", "entra_id"),
        "registry": ("ACR", "acr"), "cdn": ("Front Door", "front_door"),
        "ml": ("Azure ML Studio", "ml_studio"), "datalake": ("Synapse Analytics", "synapse"),
        "waf": ("Front Door WAF", "front_door"), "kafka": ("Event Hubs Kafka", "event_hubs"),
    },
    "gcp": {
        "label": "GCP",
        "compute": ("Cloud Run", "cloud_run"), "compute_fn": ("Cloud Functions", "cloud_functions"), "compute_k8s": ("GKE", "gke"),
        "queue": ("Cloud Tasks", "cloud_tasks"), "pubsub": ("Pub/Sub", "pubsub"), "eventbus": ("Pub/Sub", "pubsub"),
        "stream": ("Dataflow", "dataflow"), "orchestrator": ("Cloud Workflows", "cloud_run"),
        "db_rel": ("Cloud SQL", "cloud_sql"), "db_nosql": ("Firestore", "firestore"),
        "cache": ("Memorystore Redis", "memorystore"), "storage": ("Cloud Storage", "gcs"),
        "api_gw": ("Apigee", "apigee"), "secret": ("Secret Manager", "secret_mgr"),
        "monitoring": ("Cloud Monitoring", "cloud_monitoring"), "iam": ("Cloud IAM", "cloud_iam"),
        "registry": ("Artifact Registry", "artifact_reg"), "cdn": ("Cloud CDN", "cloud_run"),
        "ml": ("Vertex AI", "vertex_ai"), "datalake": ("BigQuery", "bigquery"),
        "waf": ("Cloud Armor", "cloud_iam"), "kafka": ("Pub/Sub", "pubsub"),
    },
    "oracle-cloud": {
        "label": "Oracle Cloud",
        "compute": ("OKE", "oke"), "compute_fn": ("OCI Functions", "functions"), "compute_k8s": ("OKE", "oke"),
        "queue": ("OCI Queue", "queue"), "pubsub": ("OCI Events", "events"), "eventbus": ("OCI Events", "events"),
        "stream": ("OCI Streaming", "streaming"), "orchestrator": ("OCI Functions", "functions"),
        "db_rel": ("Autonomous Database", "autonomous_db"), "db_nosql": ("OCI NoSQL", "nosql"),
        "cache": ("OCI Cache Redis", "cache"), "storage": ("Object Storage", "object_storage"),
        "api_gw": ("OCI API Gateway", "api_gw"), "secret": ("OCI Vault", "vault"),
        "monitoring": ("OCI Monitoring", "monitoring"), "iam": ("OCI IAM", "iam"),
        "registry": ("OCIR", "ocir"), "cdn": ("OCI CDN", "oke"),
        "ml": ("OCI Data Science", "data_science"), "datalake": ("OCI Data Lake", "autonomous_db"),
        "waf": ("OCI WAF", "vault"), "kafka": ("OCI Streaming", "streaming"),
    },
}

# ═══════════════════════════════════════════════════════════════════
# TECH STACKS
# ═══════════════════════════════════════════════════════════════════

STACKS = [
    {"id": "java-spring", "label": "Java 21 / Spring Boot 3", "fw": "Spring Boot 3", "api": "Spring WebFlux", "msg": "Spring Cloud Stream", "data": "Spring Data JPA", "grpc": "grpc-spring-boot-starter"},
    {"id": "go-grpc", "label": "Go / gRPC", "fw": "Gin", "api": "gRPC + REST Gateway", "msg": "Watermill", "data": "sqlx + pgx", "grpc": "gRPC-Go"},
    {"id": "dotnet", "label": ".NET 8 / ASP.NET Core", "fw": "ASP.NET Core", "api": "Minimal APIs", "msg": "MassTransit", "data": "EF Core", "grpc": "Grpc.Net"},
    {"id": "python-fastapi", "label": "Python / FastAPI", "fw": "FastAPI", "api": "FastAPI + Uvicorn", "msg": "Celery + Kombu", "data": "SQLAlchemy", "grpc": "grpcio"},
    {"id": "node-nestjs", "label": "Node.js / NestJS", "fw": "NestJS", "api": "NestJS REST", "msg": "Bull + NestJS Microservices", "data": "Prisma", "grpc": "@grpc/grpc-js"},
]

# Datadog tracing library per stack
DD_TRACE_LIBS = {
    "java-spring": "dd-trace-java",
    "go-grpc": "dd-trace-go",
    "dotnet": "dd-trace-dotnet",
    "python-fastapi": "dd-trace-py",
    "node-nestjs": "dd-trace-js",
}

# ═══════════════════════════════════════════════════════════════════
# 25 DOMAIN DEFINITIONS - each with unique scenario templates
# ═══════════════════════════════════════════════════════════════════

DOMAINS = {
    "pix-dict": {
        "label": "PIX DICT", "desc": "Diretorio de Identificadores de Contas Transacionais",
        "persons": [("Correntista", "Cliente que registra e gerencia chaves PIX"), ("Operador Backoffice", "Operador que gerencia disputas de chaves")],
        "ext_systems": [("BACEN DICT", "API DICT do Banco Central para registro de chaves"), ("Participante PSP", "Instituicao participante do arranjo PIX"), ("SPI", "Sistema de Pagamentos Instantaneos")],
        "scenarios": {
            "context_eip": [
                {"title": "Registro de Chave PIX via Content-Based Router", "focus": "Roteamento de registros EVP, CPF, CNPJ, email e telefone para processadores especializados", "pattern": "content-based-router", "systems": [("Key Router", "Roteia requisicoes de registro por tipo de chave"), ("EVP Processor", "Processa chaves aleatórias EVP com UUID"), ("CPF CNPJ Processor", "Valida e registra chaves CPF/CNPJ com Receita Federal")]},
                {"title": "Notificacao de Alteracao de Chaves via Pub-Sub", "focus": "Fan-out de eventos de alteracao de chaves para PSPs participantes", "pattern": "pub-sub", "systems": [("Key Change Detector", "Detecta alteracoes em chaves (portabilidade, exclusao)"), ("Notification Broadcaster", "Publica eventos para todos os PSPs afetados"), ("Sync Monitor", "Monitora confirmacao de sincronizacao dos PSPs")]},
                {"title": "Portabilidade de Chave com Splitter-Aggregator", "focus": "Divide processo de portabilidade em validacao no doador e confirmacao no reivindicador", "pattern": "splitter-aggregator", "systems": [("Portability Orchestrator", "Coordena fluxo de portabilidade entre PSPs"), ("Donor Validator", "Valida consentimento do titular no PSP doador"), ("Claimer Confirmer", "Confirma registro no PSP reivindicador")]},
                {"title": "Tratamento de Falhas DICT via Dead Letter", "focus": "Recuperacao de mensagens de sincronizacao DICT que falharam", "pattern": "dead-letter", "systems": [("DICT Sync Service", "Sincroniza base local com DICT BACEN"), ("DLQ Processor", "Reprocessa mensagens que falharam na sincronizacao"), ("Alert Manager", "Notifica operadores sobre falhas persistentes")]},
                {"title": "Auditoria de Operacoes DICT via Wire Tap", "focus": "Interceptacao e registro de todas as operacoes de chave para compliance", "pattern": "wire-tap", "systems": [("Key Operations Gateway", "Gateway para todas as operacoes de chave PIX"), ("Audit Tap", "Intercepta e registra operacoes para trilha de auditoria"), ("Compliance Reporter", "Gera relatorios regulatorios para o BACEN")]},
            ],
            "context_dp": [
                {"title": "DICT com CQRS e Event Sourcing", "focus": "Separacao de comandos de registro/alteracao e consultas de chave com historico completo", "pattern": "cqrs-es", "systems": [("Command Handler", "Processa comandos de registro, alteracao e exclusao"), ("Event Store", "Armazena historico imutavel de todas as operacoes de chave"), ("Query Service", "Consultas otimizadas de chaves por CPF, telefone, email")]},
                {"title": "Reivindicacao de Chave com Saga Orchestration", "focus": "Orquestracao do fluxo de reivindicacao com timeout de 7 dias e compensacao", "pattern": "saga-orchestration", "systems": [("Claim Orchestrator", "Coordena steps: notificar doador, aguardar resposta, transferir"), ("Timeout Controller", "Gerencia janela de 7 dias para resposta do doador"), ("Compensation Handler", "Reverte operacao se doador contestar dentro do prazo")]},
                {"title": "Sincronizacao DICT com Saga Choreography", "focus": "Coreografia de eventos entre PSPs para manter consistencia de chaves", "pattern": "saga-choreography", "systems": [("Key Event Publisher", "Publica eventos de criacao/alteracao de chaves"), ("PSP Sync Consumer", "Consome eventos e atualiza base local do PSP"), ("Consistency Checker", "Verifica consistencia eventual entre PSPs e DICT")]},
                {"title": "Consulta DICT com Circuit Breaker", "focus": "Protecao contra indisponibilidade da API DICT BACEN com fallback para cache local", "pattern": "circuit-breaker", "systems": [("DICT Client", "Cliente da API DICT com circuit breaker integrado"), ("Local Cache", "Cache local de chaves para fallback em caso de falha"), ("Health Monitor", "Monitora disponibilidade da API DICT e ajusta circuit state")]},
                {"title": "Migracao do Legado DICT via Strangler Fig", "focus": "Migracao gradual do sistema legado de chaves para nova plataforma cloud-native", "pattern": "strangler-fig", "systems": [("Traffic Router", "Roteia requests entre sistema legado e novo baseado em feature flags"), ("Legacy DICT Adapter", "Adapter para sistema legado de registro de chaves"), ("New DICT Platform", "Nova plataforma cloud-native com API DICT v2")]},
            ],
            "container_eip": [
                {"title": "Pipeline de Validacao de Chaves com Pipes and Filters", "focus": "Cadeia de filtros: formato, duplicidade, titularidade, OFAC screening", "pattern": "pipes-filters"},
                {"title": "Consulta Multi-PSP com Scatter-Gather", "focus": "Consulta paralela a multiplos PSPs para verificacao de chave", "pattern": "scatter-gather"},
                {"title": "Registro Sincrono via Request-Reply", "focus": "Registro sincrono com BACEN DICT aguardando confirmacao em reply queue", "pattern": "request-reply"},
                {"title": "Processamento Massivo via Competing Consumers", "focus": "Pool de consumers processando bulk de registros de chaves EVP", "pattern": "competing-consumers"},
                {"title": "Transformacao de Mensagens DICT com Message Translator", "focus": "Conversao entre formato interno e XML DICT do BACEN via canonical model", "pattern": "message-translator"},
            ],
            "container_dp": [
                {"title": "API Gateway BFF para Canais PIX DICT", "focus": "BFF Mobile com UX otimizada vs BFF Web com gestao completa de chaves", "pattern": "api-gw-bff"},
                {"title": "Sidecar para mTLS com BACEN DICT", "focus": "Sidecar proxy gerenciando certificados ICP-Brasil e mTLS com RSFN", "pattern": "sidecar"},
                {"title": "Hexagonal Architecture para Domain DICT", "focus": "Portas de entrada (REST, gRPC, messaging) e saida (BACEN, DB, cache) isoladas", "pattern": "hexagonal"},
                {"title": "Outbox Pattern para Consistencia DICT", "focus": "Garantia de publicacao de eventos apos persist de chave via transactional outbox", "pattern": "outbox"},
                {"title": "Bulkhead para Isolamento de Operacoes DICT", "focus": "Thread pools isolados para registro, consulta e portabilidade de chaves", "pattern": "bulkhead"},
            ],
        },
    },
    "pix-spi": {
        "label": "PIX SPI", "desc": "Sistema de Pagamentos Instantaneos",
        "persons": [("Pagador", "Correntista que inicia transferencia PIX"), ("Recebedor", "Beneficiario do pagamento PIX"), ("Operador Tesouraria", "Gerencia liquidez e posicao SPI")],
        "ext_systems": [("BACEN SPI", "Sistema de Pagamentos Instantaneos do Banco Central"), ("Participante Direto", "Instituicao com conta PI no BACEN"), ("STR", "Sistema de Transferencia de Reservas")],
        "scenarios": {
            "context_eip": [
                {"title": "Roteamento de Pagamentos PIX por Tipo", "focus": "Router que direciona PIX instantaneo, agendado, com troco e saque para processadores especificos", "pattern": "content-based-router", "systems": [("PIX Router", "Classifica e roteia pagamentos por tipo e prioridade"), ("Instant Processor", "Processa PIX instantaneo com SLA de 10 segundos"), ("Scheduled Processor", "Processa PIX agendado com validacao de saldo futuro")]},
                {"title": "Broadcast de Liquidacao SPI via Pub-Sub", "focus": "Notificacao em tempo real de liquidacao para tesouraria, contabilidade e reconciliacao", "pattern": "pub-sub", "systems": [("Settlement Publisher", "Publica eventos de liquidacao confirmada pelo SPI"), ("Treasury Consumer", "Atualiza posicao de liquidez em tempo real"), ("Accounting Consumer", "Registra lancamentos contabeis da liquidacao")]},
                {"title": "Pagamento em Lote com Splitter-Aggregator", "focus": "Split de arquivo de pagamentos em lote e agregacao de resultados individuais", "pattern": "splitter-aggregator", "systems": [("Batch Splitter", "Divide arquivo de pagamentos em transacoes individuais"), ("Individual Processor", "Processa cada pagamento com validacao e AML"), ("Result Aggregator", "Agrega status de cada pagamento no resultado do lote")]},
                {"title": "DLQ para Pagamentos Rejeitados pelo SPI", "focus": "Tratamento de rejeicoes do SPI com retry automatico e escalacao", "pattern": "dead-letter", "systems": [("SPI Sender", "Envia mensagens de pagamento para o SPI BACEN"), ("Rejection Handler", "Processa rejeicoes com logica de retry diferenciada"), ("Escalation Service", "Escalona pagamentos que falharam apos retries")]},
                {"title": "Monitoramento de Mensagens SPI via Wire Tap", "focus": "Captura de metricas de latencia e volumetria de mensagens SPI para SLA monitoring", "pattern": "wire-tap", "systems": [("SPI Message Gateway", "Gateway de mensagens ISO 20022 com o SPI"), ("Performance Tap", "Captura tempos de resposta e volumetria em tempo real"), ("SLA Dashboard", "Consolida metricas de SLA do PIX (10s end-to-end)")]},
            ],
            "context_dp": [
                {"title": "PIX com CQRS para Alta Volumetria", "focus": "Write path otimizado para insercao e read path com projecoes para consulta de status", "pattern": "cqrs-es", "systems": [("Payment Command Service", "Recebe e valida comandos de pagamento PIX"), ("Event Store", "Armazena eventos imutaveis de cada transacao PIX"), ("Status Query Service", "Projecoes otimizadas para consulta de status em real-time")]},
                {"title": "Saga de Pagamento PIX com Orquestracao", "focus": "Steps: validar conta, debitar pagador, enviar SPI, creditar recebedor, notificar", "pattern": "saga-orchestration", "systems": [("Payment Saga Orchestrator", "Coordena 5 steps do pagamento com compensacao"), ("Debit Service", "Debita conta do pagador com reserva atomica"), ("Credit Service", "Credita conta do recebedor apos confirmacao SPI")]},
                {"title": "PIX com Saga Choreography entre Participantes", "focus": "Coreografia de eventos entre PSP pagador, SPI e PSP recebedor", "pattern": "saga-choreography", "systems": [("Payer PSP Publisher", "Publica evento de debito confirmado"), ("SPI Relay Consumer", "Consome debito e publica para PSP recebedor"), ("Receiver PSP Consumer", "Consome e credita conta do recebedor")]},
                {"title": "Circuit Breaker para API SPI BACEN", "focus": "Protecao contra instabilidade do SPI com queue de retry e notificacao", "pattern": "circuit-breaker", "systems": [("SPI Client", "Cliente SPI com circuit breaker e retry exponential"), ("Retry Queue Manager", "Gerencia fila de pagamentos pendentes durante instabilidade"), ("Operations Alert", "Alerta operacoes sobre degradacao do SPI")]},
                {"title": "Migracao para Novo Motor PIX via Strangler Fig", "focus": "Migracao gradual de motor de pagamentos monolitico para microservicos", "pattern": "strangler-fig", "systems": [("PIX Traffic Router", "Roteia pagamentos entre motor legado e novo"), ("Legacy Payment Engine", "Motor monolitico de pagamentos PIX v1"), ("New Payment Microservices", "Novo motor baseado em microservicos e event sourcing")]},
            ],
            "container_eip": [
                {"title": "Canonicalizacao de Mensagens ISO 20022", "focus": "Traducao entre formato interno JSON e XML ISO 20022 do SPI via canonical model", "pattern": "message-translator"},
                {"title": "Pipeline de Validacao de Pagamento PIX", "focus": "Filters: schema validation, AML screening, limit check, balance check, fraud check", "pattern": "pipes-filters"},
                {"title": "Consulta de Tarifa PIX via Scatter-Gather", "focus": "Consulta paralela a servicos de tarifa, cambio e IOF para PIX internacional", "pattern": "scatter-gather"},
                {"title": "Confirmacao Sincrona SPI via Request-Reply", "focus": "Envio de MSG PIX e aguardo de confirmacao sincrona do SPI com correlation ID", "pattern": "request-reply"},
                {"title": "Pool de Workers SPI com Competing Consumers", "focus": "Multiplos workers consumindo fila de pagamentos para processamento paralelo", "pattern": "competing-consumers"},
            ],
            "container_dp": [
                {"title": "BFF para Canais PIX (Mobile, Web, API)", "focus": "BFFs especializados: Mobile com UX simplificada, Web com extrato completo, API para parceiros", "pattern": "api-gw-bff"},
                {"title": "Sidecar para Criptografia SPI", "focus": "Sidecar com HSM integration para assinatura digital de mensagens SPI", "pattern": "sidecar"},
                {"title": "Hexagonal Architecture para Payment Domain", "focus": "Domain PIX isolado com ports para SPI, DICT, STR e adapters por cloud", "pattern": "hexagonal"},
                {"title": "Outbox para Eventos de Pagamento PIX", "focus": "Transactional outbox garantindo publicacao de evento apos persist de pagamento", "pattern": "outbox"},
                {"title": "Bulkhead para Isolamento PIX Instant vs Agendado", "focus": "Thread pools separados para nao permitir que PIX agendado impacte instantaneo", "pattern": "bulkhead"},
            ],
        },
    },
    "pix-med": {
        "label": "PIX MED", "desc": "Mecanismo Especial de Devolucao",
        "persons": [("Vitima", "Correntista vitima de fraude ou falha operacional"), ("Analista Fraude", "Analisa casos MED e determina bloqueio"), ("Operador Compliance", "Supervisiona processo MED regulatorio")],
        "ext_systems": [("BACEN MED", "API MED do Banco Central para devolucoes especiais"), ("PSP Recebedor", "PSP que recebeu o PIX objeto de devolucao"), ("Anti-Fraud System", "Sistema de deteccao de fraude")],
        "scenarios": {
            "context_eip": [
                {"title": "Triagem de Notificacoes MED por Tipo", "focus": "Roteamento de MED tipo 1 (fraude) vs tipo 2 (falha operacional) para fluxos distintos", "pattern": "content-based-router", "systems": [("MED Classifier", "Classifica notificacao MED por tipo e urgencia"), ("Fraud MED Processor", "Processa MED tipo 1 com bloqueio cautelar imediato"), ("Operational MED Processor", "Processa MED tipo 2 com analise de falha operacional")]},
                {"title": "Broadcast de Bloqueio Cautelar via Pub-Sub", "focus": "Notificacao de bloqueio cautelar para todos os canais do recebedor", "pattern": "pub-sub", "systems": [("Block Publisher", "Publica evento de bloqueio cautelar de recursos"), ("Channel Blocker", "Bloqueia canais PIX, TED e saque do recebedor"), ("Notification Service", "Notifica recebedor sobre bloqueio e prazo de defesa")]},
                {"title": "Analise de Caso MED com Splitter-Aggregator", "focus": "Split de caso em sub-analises paralelas e agregacao de score final", "pattern": "splitter-aggregator", "systems": [("Case Splitter", "Divide caso em analise de fraude, saldo e historico"), ("Fraud Analyzer", "Analisa padroes de fraude do recebedor"), ("Score Aggregator", "Agrega scores parciais em decisao final de devolucao")]},
                {"title": "Reprocessamento de MEDs Falhos via DLQ", "focus": "Tratamento de falhas na comunicacao com BACEN MED", "pattern": "dead-letter", "systems": [("MED API Client", "Cliente da API MED do BACEN com retry logic"), ("DLQ Reprocessor", "Reprocessa notificacoes que falharam na entrega ao BACEN"), ("Manual Review Queue", "Encaminha para revisao manual apos falhas persistentes")]},
                {"title": "Auditoria Completa do Fluxo MED via Wire Tap", "focus": "Registro detalhado de cada step do MED para conformidade regulatoria", "pattern": "wire-tap", "systems": [("MED Flow Gateway", "Gateway central do fluxo MED"), ("Regulatory Tap", "Captura evidencias de cada decisao para auditoria BACEN"), ("Evidence Store", "Armazena evidencias com imutabilidade e timestamp")]},
            ],
            "context_dp": [
                {"title": "MED com Event Sourcing para Rastreabilidade", "focus": "Historico completo e imutavel de cada caso MED para auditoria BACEN", "pattern": "cqrs-es", "systems": [("MED Command Service", "Processa comandos de abertura, analise e devolucao"), ("MED Event Store", "Historico imutavel de eventos do caso MED"), ("MED Query View", "Consulta de status e historico de casos MED")]},
                {"title": "Orquestracao do Fluxo MED Completo", "focus": "Steps: notificar, bloquear, analisar, decidir, devolver/liberar com compensacao", "pattern": "saga-orchestration", "systems": [("MED Orchestrator", "Coordena fluxo completo com prazos regulatorios"), ("Block Manager", "Gerencia bloqueio e desbloqueio cautelar de recursos"), ("Refund Engine", "Executa devolucao parcial ou total ao pagador")]},
                {"title": "MED Choreography entre PSPs", "focus": "Coreografia de eventos entre PSP pagador, PSP recebedor e BACEN", "pattern": "saga-choreography", "systems": [("Payer PSP Events", "Publica abertura de caso MED pelo PSP pagador"), ("Receiver PSP Events", "Consome notificacao e publica bloqueio cautelar"), ("BACEN MED Relay", "Sincroniza estado do caso com API MED BACEN")]},
                {"title": "Circuit Breaker na API MED BACEN", "focus": "Protecao contra timeout da API MED com queue local e retry", "pattern": "circuit-breaker", "systems": [("MED Client", "Cliente API MED com circuit breaker half-open state"), ("Pending Queue", "Fila local de casos MED aguardando reenvio"), ("Ops Dashboard", "Dashboard de saude da integracao MED")]},
                {"title": "Migracao do Legado MED via Strangler Fig", "focus": "Transicao gradual de sistema batch de devolucao para real-time MED", "pattern": "strangler-fig", "systems": [("MED Router", "Roteia entre sistema batch legado e novo real-time"), ("Legacy Batch Refund", "Sistema batch de devolucao D+1"), ("New Real-Time MED", "Novo sistema MED real-time com event sourcing")]},
            ],
            "container_eip": [
                {"title": "Pipeline de Analise MED com Pipes and Filters", "focus": "Filtros sequenciais: elegibilidade, prazo, saldo disponivel, historico recebedor", "pattern": "pipes-filters"},
                {"title": "Consulta Multi-Fonte para Decisao MED", "focus": "Scatter para anti-fraude, bureau de credito e historico transacional em paralelo", "pattern": "scatter-gather"},
                {"title": "Notificacao Sincrona MED via Request-Reply", "focus": "Envio de notificacao MED ao BACEN aguardando ACK sincrono", "pattern": "request-reply"},
                {"title": "Workers de Analise MED com Competing Consumers", "focus": "Pool de analistas automaticos consumindo fila de casos MED", "pattern": "competing-consumers"},
                {"title": "Traducao de Formato MED via Message Translator", "focus": "Conversao de formato interno de caso para XML MED do BACEN", "pattern": "message-translator"},
            ],
            "container_dp": [
                {"title": "BFF para Canais MED (Vitima, Analista, Compliance)", "focus": "Interface vitima simplificada vs painel analista com evidencias vs dashboard compliance", "pattern": "api-gw-bff"},
                {"title": "Sidecar para Comunicacao MED Segura", "focus": "Sidecar com mTLS, assinatura digital e validacao de certificado ICP-Brasil", "pattern": "sidecar"},
                {"title": "Domain MED com Hexagonal Architecture", "focus": "Domain MED isolado com ports para BACEN, Anti-Fraude e Core Banking", "pattern": "hexagonal"},
                {"title": "Outbox para Garantia de Notificacao MED", "focus": "Outbox transacional garantindo que toda decisao MED seja notificada ao BACEN", "pattern": "outbox"},
                {"title": "Bulkhead Separando MED Fraude vs MED Operacional", "focus": "Isolamento de recursos entre processamento de fraude (prioridade) e falha operacional", "pattern": "bulkhead"},
            ],
        },
    },
}

# Remaining 22 domains - generate programmatically with unique scenarios
_REMAINING_DOMAINS = {
    "rsfn-connect": ("RSFN Connect", "Rede do Sistema Financeiro Nacional", [("Operador RSFN", "Opera gateway RSFN"), ("Admin Certificados", "Gerencia certificados ICP-Brasil")], [("BACEN RSFN", "Rede do SFN do Banco Central"), ("Camara de Compensacao", "Camara de liquidacao"), ("Participante SFN", "Instituicao participante do SFN")]),
    "str": ("STR", "Sistema de Transferencia de Reservas", [("Operador Tesouraria", "Opera mesa de tesouraria"), ("Gerente Liquidez", "Gerencia posicao de liquidez")], [("BACEN STR", "Sistema de Transferencia de Reservas"), ("Banco Participante", "Banco com conta reserva"), ("Camara LBTR", "Liquidacao bruta em tempo real")]),
    "tef": ("TEF", "Transferencia Eletronica de Fundos", [("Lojista", "Estabelecimento comercial com POS"), ("Portador Cartao", "Cliente que paga com cartao")], [("Rede Adquirente", "Processadora de transacoes"), ("Bandeira", "Visa, Mastercard, Elo"), ("Banco Emissor", "Banco emissor do cartao")]),
    "dda": ("DDA", "Debito Direto Autorizado", [("Sacado", "Pagador do boleto"), ("Cedente", "Emitente do boleto")], [("CIP DDA", "Central de registro DDA"), ("Banco Sacado", "Banco do pagador"), ("Registro Boletos", "Sistema de registro de boletos")]),
    "open-banking": ("Open Banking", "Open Finance Brasil", [("Cliente", "Titular dos dados financeiros"), ("TPP Developer", "Desenvolvedor de aplicacao terceira")], [("Open Finance Directory", "Diretorio de participantes"), ("Instituicao Receptora", "ITP que recebe dados"), ("BACEN", "Regulador Open Finance")]),
    "core-banking": ("Core Banking", "Plataforma Core Banking", [("Correntista", "Cliente com conta corrente"), ("Gerente Conta", "Gerente de relacionamento")], [("CIP", "Camara Interbancaria de Pagamentos"), ("BACEN", "Banco Central do Brasil"), ("Bureau Credito", "Serasa, SPC, Boa Vista")]),
    "payments": ("Payments", "Processamento de Pagamentos", [("Pagador", "Pessoa que efetua pagamento"), ("Recebedor", "Beneficiario do pagamento")], [("Rede Adquirente", "Processadora de cartoes"), ("PIX SPI", "Sistema PIX do BACEN"), ("TED DOC CIP", "Transferencias interbancarias")]),
    "credit-lending": ("Credit Lending", "Credito e Emprestimos", [("Solicitante", "Pessoa solicitando credito"), ("Analista Credito", "Analista de risco de credito")], [("Bureau Credito SCR", "Sistema de informacoes de credito BACEN"), ("BACEN SCR", "Central de risco do BACEN"), ("Seguradora", "Seguro prestamista")]),
    "cards": ("Cards", "Processamento de Cartoes", [("Portador", "Titular do cartao"), ("Operador Cartoes", "Operador de gestao de cartoes")], [("Bandeira Visa Master", "Redes de cartao"), ("TSP Token Requestor", "Provedor de tokenizacao"), ("Rede Adquirente", "Processadora de transacoes")]),
    "anti-fraud": ("Anti-Fraud", "Motor Anti-Fraude e Risco", [("Analista Fraude", "Investiga alertas de fraude"), ("Data Scientist", "Treina modelos de deteccao")], [("Bureau de Fraude", "Base de dados de fraudadores"), ("Device Fingerprint", "Servico de device ID"), ("BACEN MED", "Mecanismo Especial de Devolucao")]),
    "kyc-aml": ("KYC AML", "Know Your Customer e Anti-Lavagem", [("Cliente", "Pessoa em processo de onboarding"), ("Analista Compliance", "Analista de PLD/FT")], [("Receita Federal", "Validacao de CPF/CNPJ"), ("COAF", "Conselho de Controle de Atividades Financeiras"), ("OFAC Sanctions", "Lista de sancoes internacionais")]),
    "data-pipeline": ("Data Pipeline", "Pipeline de Dados e Data Lake", [("Data Engineer", "Engenheiro de dados"), ("Data Analyst", "Analista de dados")], [("Core Banking Source", "Fonte de dados transacionais"), ("Payment Source", "Fonte de dados de pagamentos"), ("BI Tools", "Ferramentas de Business Intelligence")]),
    "api-gateway": ("API Gateway", "API Gateway e Hub de Integracao", [("API Consumer", "Consumidor de APIs"), ("API Developer", "Desenvolvedor de APIs")], [("External Partner", "Parceiro externo consumidor"), ("Internal Microservice", "Microservico interno"), ("Identity Provider", "Provedor de identidade")]),
    "security-iam": ("Security IAM", "Seguranca e Gestao de Identidade", [("End User", "Usuario final da plataforma"), ("Security Admin", "Administrador de seguranca")], [("External IdP", "Provedor de identidade externo"), ("HSM Provider", "Hardware Security Module"), ("SIEM", "Security Information and Event Management")]),
    "observability": ("Observability", "Observabilidade e Monitoramento", [("SRE Engineer", "Engenheiro de confiabilidade"), ("Developer", "Desenvolvedor que monitora servicos")], [("Application Services", "Servicos monitorados"), ("PagerDuty", "Plataforma de alertas"), ("Grafana Cloud", "Plataforma de dashboards")]),
    "devops-cicd": ("DevOps CICD", "DevOps e Pipelines CI/CD", [("Developer", "Desenvolvedor de software"), ("DevOps Engineer", "Engenheiro DevOps")], [("Git Repository", "Repositorio de codigo fonte"), ("Container Registry", "Registro de imagens Docker"), ("Security Scanner", "Scanner SAST/DAST")]),
    "event-driven": ("Event Driven", "Arquitetura Event-Driven", [("Developer", "Desenvolvedor de microservicos"), ("Architect", "Arquiteto de solucoes")], [("Producer Services", "Servicos produtores de eventos"), ("Consumer Services", "Servicos consumidores"), ("Monitoring", "Monitoramento de eventos")]),
    "insurance": ("Insurance", "Plataforma de Seguros", [("Segurado", "Cliente segurado"), ("Corretor", "Corretor de seguros")], [("SUSEP", "Superintendencia de Seguros Privados"), ("Ressegurador", "Empresa de resseguro"), ("Bureau Sinistro", "Base de dados de sinistros")]),
    "investments": ("Investments", "Investimentos e Patrimonio", [("Investidor", "Cliente investidor"), ("Assessor", "Assessor de investimentos")], [("B3 Bolsa", "Bolsa de Valores do Brasil"), ("CVM", "Comissao de Valores Mobiliarios"), ("Custodiante", "Custodia de ativos")]),
    "treasury": ("Treasury", "Gestao de Tesouraria", [("Tesoureiro", "Tesoureiro da instituicao"), ("Operador Mesa", "Operador de mesa de cambio")], [("BACEN STR", "Sistema de Transferencia de Reservas"), ("Bloomberg Terminal", "Terminal de dados de mercado"), ("CETIP", "Central de custodia de titulos")]),
    "reconciliation": ("Reconciliation", "Reconciliacao Financeira", [("Analista Conciliacao", "Analista de reconciliacao"), ("Auditor", "Auditor financeiro")], [("Core Banking", "Sistema core de contas"), ("Payment Processor", "Processador de pagamentos"), ("External Statement", "Extratos de contrapartes")]),
    "notification": ("Notification", "Servicos de Notificacao", [("End User", "Usuario que recebe notificacoes"), ("Marketing Manager", "Gestor de campanhas")], [("Email Provider SES", "Servico de email"), ("SMS Provider", "Provedor de SMS"), ("Push FCM", "Firebase Cloud Messaging")]),
}

# EIP and DP pattern definitions for scenario generation
_EIP_IDS = ["content-based-router", "pub-sub", "splitter-aggregator", "dead-letter", "wire-tap",
            "message-translator", "pipes-filters", "scatter-gather", "request-reply", "competing-consumers"]
_EIP_LABELS = ["Content-Based Router", "Publish-Subscribe", "Splitter-Aggregator", "Dead Letter Channel", "Wire Tap",
               "Message Translator", "Pipes and Filters", "Scatter-Gather", "Request-Reply", "Competing Consumers"]
_EIP_DESCS = [
    "Roteia mensagens para canais diferentes baseado no conteudo",
    "Broadcast de mensagens para multiplos assinantes",
    "Divide mensagens compostas e agrega respostas",
    "Encaminha mensagens nao processaveis para canal de dead letter",
    "Intercepta e registra mensagens em transito para auditoria",
    "Traduz mensagens entre formatos diferentes via modelo canonico",
    "Processa mensagens atraves de pipeline de filtros sequenciais",
    "Distribui requisicao para multiplos destinatarios e agrega respostas",
    "Envia requisicao e aguarda resposta correlacionada",
    "Multiplos consumidores competem para processar mensagens de fila compartilhada",
]

_DP_IDS = ["cqrs-es", "saga-orchestration", "saga-choreography", "circuit-breaker", "strangler-fig",
           "api-gw-bff", "sidecar", "hexagonal", "outbox", "bulkhead"]
_DP_LABELS = ["CQRS + Event Sourcing", "Saga Orchestration", "Saga Choreography", "Circuit Breaker", "Strangler Fig",
              "API Gateway BFF", "Sidecar Pattern", "Hexagonal Architecture", "Outbox Pattern", "Bulkhead Pattern"]
_DP_DESCS = [
    "Separa modelos de leitura e escrita com estado baseado em eventos",
    "Coordena transacoes distribuidas via orquestrador central",
    "Coordena transacoes distribuidas via coreografia de eventos",
    "Previne falhas em cascata com circuit breaker pattern",
    "Migra incrementalmente de sistema legado para novo",
    "Backend-for-Frontend com API Gateway por canal",
    "Deploy de componentes auxiliares ao lado do servico principal",
    "Ports and Adapters para isolamento de dominio",
    "Garante publicacao confiavel de mensagens via transactional outbox",
    "Isola recursos criticos para prevenir falhas em cascata",
]

# Generate remaining domains with formulaic but unique scenarios
for dk, (lbl, desc, persons, ext_sys) in _REMAINING_DOMAINS.items():
    ctx_eip = []
    for i in range(5):
        ctx_eip.append({
            "title": f"{lbl} com {_EIP_LABELS[i]}",
            "focus": f"{_EIP_DESCS[i]} aplicado ao contexto de {desc.lower()}",
            "pattern": _EIP_IDS[i],
            "systems": [
                (f"{lbl} Gateway", f"Gateway principal para {desc.lower()}"),
                (f"{_EIP_LABELS[i]} Engine", f"Motor de {_EIP_LABELS[i].lower()} para processamento"),
                (f"{lbl} Monitor", f"Monitoramento e alertas de {desc.lower()}"),
            ],
        })
    ctx_dp = []
    for i in range(5):
        ctx_dp.append({
            "title": f"{lbl} com {_DP_LABELS[i]}",
            "focus": f"{_DP_DESCS[i]} no contexto de {desc.lower()}",
            "pattern": _DP_IDS[i],
            "systems": [
                (f"{lbl} Command Service", f"Servico de comandos para {desc.lower()}"),
                (f"{_DP_LABELS[i]} Handler", f"Handler do padrao {_DP_LABELS[i]}"),
                (f"{lbl} Query Service", f"Servico de consultas otimizadas"),
            ],
        })
    cnt_eip = []
    for i in range(5, 10):
        cnt_eip.append({
            "title": f"{lbl} - {_EIP_LABELS[i]} Container View",
            "focus": f"{_EIP_DESCS[i]} na camada de containers de {desc.lower()}",
            "pattern": _EIP_IDS[i],
        })
    cnt_dp = []
    for i in range(5, 10):
        cnt_dp.append({
            "title": f"{lbl} - {_DP_LABELS[i]} Container View",
            "focus": f"{_DP_DESCS[i]} nos containers de {desc.lower()}",
            "pattern": _DP_IDS[i],
        })
    DOMAINS[dk] = {
        "label": lbl, "desc": desc, "persons": persons, "ext_systems": ext_sys,
        "scenarios": {
            "context_eip": ctx_eip, "context_dp": ctx_dp,
            "container_eip": cnt_eip, "container_dp": cnt_dp,
        },
    }


# ═══════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════

# ELK Manhattan layout frontmatter (orthogonal edge routing)
ELK_FRONTMATTER = """---
config:
  layout: elk
  elk:
    mergeEdges: true
    nodePlacementStrategy: NETWORK_SIMPLEX
    cycleBreakingStrategy: GREEDY
  c4:
    diagramMarginX: 25
    diagramMarginY: 25
---"""


def sid(text):
    """Safe Mermaid identifier."""
    return re.sub(r'[^a-zA-Z0-9]', '_', text).strip('_')

def sprite(cloud, icon_key):
    """Get sprite string for a cloud service icon."""
    icons = CLOUD_ICONS.get(cloud, {})
    url = icons.get(icon_key, "")
    if url:
        return f', $sprite="{url}"'
    return ""

def cloud_svc(cloud, svc_type):
    """Get (name, icon_key) for a cloud service type."""
    return CLOUDS[cloud].get(svc_type, ("Unknown", ""))

def style_lines(cloud, element_ids):
    """Generate UpdateElementStyle lines for cloud-branded elements."""
    s = CLOUD_STYLES[cloud]
    lines = []
    for eid in element_ids:
        lines.append(f'    UpdateElementStyle({eid}, $fontColor="{s["font"]}", $bgColor="{s["bg"]}", $borderColor="{s["border"]}")')
    return lines

def pick_stack(idx):
    return STACKS[idx % len(STACKS)]


# Pattern ID → (type, label) mapping for documentation
_PATTERN_INFO = {pid: ("EIP", lbl) for pid, lbl in zip(_EIP_IDS, _EIP_LABELS)}
_PATTERN_INFO.update({pid: ("Design Pattern", lbl) for pid, lbl in zip(_DP_IDS, _DP_LABELS)})


def gen_doc(mmd_path, title, domain, cloud, c4_level, scenario, is_eip, stack=None):
    """Generate markdown documentation file (.md) alongside an .mmd diagram."""
    c = CLOUDS[cloud]
    pattern = scenario["pattern"]
    p_type, p_label = _PATTERN_INFO.get(pattern, ("Unknown", pattern.replace("-", " ").title()))
    full_title = f"{title} [{c['label']}]" if not stack else f"{title} [{c['label']} / {stack['label']}]"

    L = [f"# {full_title}", ""]
    L += ["## Domínio", f"{domain['label']} — {domain['desc']}", ""]
    L += ["## Cloud Provider", c["label"], ""]
    L += ["## Nível C4", c4_level, ""]
    L += ["## Padrão Utilizado", f"- **Tipo:** {p_type}", f"- **Padrão:** {p_label}", ""]

    if stack:
        L += ["## Stack Tecnológico", stack["label"], ""]

    focus = scenario.get("focus", f"Implementação de {p_label} para {domain['desc'].lower()}")
    L += ["## Descrição", focus, ""]

    L.append("## Componentes Principais")
    if c4_level == "Context":
        L.append(f"- **{domain['label']} Platform** — sistema principal ({scenario.get('focus', 'plataforma do dominio')[:80]})")
        L.append(f"- **Ory Security Stack** — Identity, OAuth2, Permissions, Zero Trust Proxy")
        L.append(f"- **OPA Policy Engine** — Policy as Code com Rego para authorization e compliance")
    elif c4_level == "Container":
        L.append(f"- **{domain['label']} Service** — serviço principal rodando em {cloud_svc(cloud, 'compute')[0]}")
        if is_eip:
            L.append(f"- **{pattern.replace('-', ' ').title()} Processor** — processador do padrão EIP")
            L.append(f"- **{cloud_svc(cloud, 'queue')[0]} Queue** — canal de mensagens principal")
            L.append(f"- **{pattern.replace('-', ' ').title()} Channel** — canal do padrão EIP via {cloud_svc(cloud, 'pubsub')[0]}")
        else:
            L.append(f"- **{pattern.replace('-', ' ').title()} Handler** — handler do padrão {p_label}")
            L.append(f"- **Domain Events** — canal de eventos do domínio via {cloud_svc(cloud, 'queue')[0]}")
        L.append(f"- **Primary Database** — {cloud_svc(cloud, 'db_rel')[0]}")
        L.append(f"- **Cache Layer** — {cloud_svc(cloud, 'cache')[0]}")
        if not is_eip:
            L.append(f"- **Pattern State Store** — {cloud_svc(cloud, 'db_nosql')[0]}")
    elif c4_level == "Component":
        comp_template = _COMP_TEMPLATES.get(pattern, [("Controller", "api"), ("Service", "fw"), ("Repository", "data"), ("Client", "grpc")])
        for comp_name, _ in comp_template:
            L.append(f"- **{comp_name}** — responsável por {comp_name.lower()}")
    L.append("")

    L.append("## Camada de Segurança")
    L.append("- **Ory Oathkeeper** — Zero Trust Identity & Access Proxy (authenticators, authorizers, mutators)")
    L.append("- **Ory Kratos** — Identity management (registration, login, MFA, session)")
    L.append("- **Ory Keto** — Permission system Google Zanzibar (relation tuples, check/expand API)")
    L.append("- **Ory Hydra** — OAuth 2.0 & OpenID Connect Server (FAPI, consent, JWT)")
    L.append("- **OPA Policy Engine** — Policy as Code com Rego (authorization, compliance, business rules)")
    L.append("")

    dd_lib = DD_TRACE_LIBS.get(stack["id"], "dd-trace") if stack else "dd-trace"
    L.append("## Camada de Observabilidade")
    L.append(f"- **Datadog Agent** — DaemonSet/Sidecar coletando metricas, traces e logs (portas 8125/8126)")
    L.append(f"- **Datadog APM** — Distributed tracing via {dd_lib} com auto-instrumentacao")
    L.append(f"- **Datadog Log Management** — Coleta e correlacao de logs com trace_id/span_id")
    L.append(f"- **Datadog Dashboards** — Dashboards e alertas customizados com SLOs")
    L.append("")

    L.append("## Integrações Externas")
    for e_name, e_desc in domain["ext_systems"][:3]:
        L.append(f"- **{e_name}** — {e_desc}")
    L.append("")

    # Use link syntax (not image) and avoid brackets in link text
    link_text = full_title.replace("[", "(").replace("]", ")")
    L += ["## Diagrama", f"[{link_text}](./{mmd_path.name})", ""]

    md_path = mmd_path.with_suffix(".md")
    md_path.write_text("\n".join(L), encoding="utf-8")


# ═══════════════════════════════════════════════════════════════════
# C4 CONTEXT GENERATORS
# ═══════════════════════════════════════════════════════════════════

def gen_context(domain_key, domain, cloud, scenario, is_eip):
    """Generate C4 Context diagram — high-level conceptual view.

    Shows only: Persons, ONE main System, cross-cutting Systems (Ory Stack,
    OPA), System_Ext (Datadog, domain externals). No queues, databases,
    boundaries, or individual Ory components.
    """
    c = CLOUDS[cloud]
    L = [ELK_FRONTMATTER, "C4Context"]
    L.append(f'    title {scenario["title"]} [{c["label"]}]')
    L.append("")

    # Persons
    for p_name, p_desc in domain["persons"][:2]:
        L.append(f'    Person({sid(p_name)}, "{p_name}", "{p_desc}")')
    L.append("")

    # Main system — ONE box representing the entire platform
    compute_name, compute_icon = cloud_svc(cloud, "compute")
    L.append(f'    System(main_system, "{domain["label"]} Platform", "{scenario["focus"]}"{sprite(cloud, compute_icon)})')
    L.append("")

    # Cross-cutting systems — ONE box each (not expanded)
    L.append(f'    System(ory_stack, "Ory Security Stack", "Identity (Kratos), OAuth2 (Hydra), Permissions (Keto), Zero Trust (Oathkeeper)"{sprite(cloud, cloud_svc(cloud, "iam")[1])})')
    L.append(f'    System(opa_engine, "OPA Policy Engine", "Policy as Code com Rego para authorization e compliance"{sprite(cloud, cloud_svc(cloud, "waf")[1])})')
    L.append(f'    System_Ext(datadog_platform, "Datadog", "Observabilidade: APM, Logs, Metrics, SIEM"{sprite(cloud, cloud_svc(cloud, "monitoring")[1])})')
    L.append("")

    # External systems (domain-specific)
    for e_name, e_desc in domain["ext_systems"][:3]:
        L.append(f'    System_Ext({sid(e_name)}, "{e_name}", "{e_desc}")')
    L.append("")

    styled = ["main_system", "ory_stack", "opa_engine"]

    # Relationships — high-level, conceptual
    if domain["persons"]:
        L.append(f'    Rel({sid(domain["persons"][0][0])}, main_system, "Usa", "HTTPS")')
    if len(domain["persons"]) >= 2:
        L.append(f'    Rel({sid(domain["persons"][1][0])}, main_system, "Gerencia", "HTTPS")')

    L.append(f'    Rel(main_system, ory_stack, "Autentica e autoriza via", "HTTPS/gRPC")')
    L.append(f'    Rel(main_system, opa_engine, "Avalia policies de negocio", "REST")')
    L.append(f'    Rel(main_system, datadog_platform, "Envia telemetria", "HTTPS/Agent")')

    if domain["ext_systems"]:
        L.append(f'    Rel(main_system, {sid(domain["ext_systems"][0][0])}, "Integra com", "HTTPS/mTLS")')
    if len(domain["ext_systems"]) >= 2:
        L.append(f'    Rel(main_system, {sid(domain["ext_systems"][1][0])}, "Reporta para", "HTTPS")')

    L.append("")
    L.extend(style_lines(cloud, styled))
    L.append('    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")')
    return "\n".join(L)


# ═══════════════════════════════════════════════════════════════════
# C4 CONTAINER GENERATORS
# ═══════════════════════════════════════════════════════════════════

def gen_container(domain_key, domain, cloud, scenario, is_eip, stack):
    c = CLOUDS[cloud]
    L = [ELK_FRONTMATTER, "C4Container"]
    L.append(f'    title {scenario["title"]} [{c["label"]} / {stack["label"]}]')
    L.append("")

    if domain["persons"]:
        p = domain["persons"][0]
        L.append(f'    Person({sid(p[0])}, "{p[0]}", "{p[1]}")')
    L.append("")

    styled = []
    L.append(f'    Container_Boundary(cb0, "{domain["label"]} Platform") {{')

    # Main service
    compute_name, compute_icon = cloud_svc(cloud, "compute")
    svc_id = f'{sid(domain["label"])}_svc'
    L.append(f'        Container({svc_id}, "{domain["label"]} Service", "{stack["fw"]}", "Servico principal rodando em {compute_name}"{sprite(cloud, compute_icon)})')
    styled.append(svc_id)

    if is_eip:
        # EIP-specific containers
        fn_name, fn_icon = cloud_svc(cloud, "compute_fn")
        proc_id = f'{sid(scenario["pattern"])}_proc'
        L.append(f'        Container({proc_id}, "{scenario["pattern"].replace("-", " ").title()} Processor", "{stack["msg"]}", "{scenario["focus"]}"{sprite(cloud, fn_icon)})')
        styled.append(proc_id)

        q_name, q_icon = cloud_svc(cloud, "queue")
        L.append(f'        ContainerQueue(main_q, "{q_name} Queue", "{q_name}", "Canal de mensagens principal"{sprite(cloud, q_icon)})')
        styled.append("main_q")

        q2_name, q2_icon = cloud_svc(cloud, "pubsub")
        L.append(f'        ContainerQueue(pattern_q, "{scenario["pattern"].replace("-", " ").title()} Channel", "{q2_name}", "Canal do padrao EIP"{sprite(cloud, q2_icon)})')
        styled.append("pattern_q")
    else:
        # DP-specific containers
        k8s_name, k8s_icon = cloud_svc(cloud, "compute_k8s")
        dp_id = f'{sid(scenario["pattern"])}_handler'
        L.append(f'        Container({dp_id}, "{scenario["pattern"].replace("-", " ").title()} Handler", "{stack["api"]}", "{scenario["focus"]}"{sprite(cloud, k8s_icon)})')
        styled.append(dp_id)

        event_q_name, event_q_icon = cloud_svc(cloud, "queue")
        L.append(f'        ContainerQueue(event_q, "Domain Events", "{event_q_name}", "Canal de eventos do dominio"{sprite(cloud, event_q_icon)})')
        styled.append("event_q")

    # Database
    db_name, db_icon = cloud_svc(cloud, "db_rel")
    L.append(f'        ContainerDb(main_db, "Primary Database", "{db_name}", "Armazenamento principal do dominio"{sprite(cloud, db_icon)})')
    styled.append("main_db")

    # Cache
    cache_name, cache_icon = cloud_svc(cloud, "cache")
    L.append(f'        ContainerDb(cache, "Cache Layer", "{cache_name}", "Cache de consultas frequentes"{sprite(cloud, cache_icon)})')
    styled.append("cache")

    # NoSQL for patterns that need it
    if not is_eip:
        nosql_name, nosql_icon = cloud_svc(cloud, "db_nosql")
        L.append(f'        ContainerDb(pattern_db, "Pattern State Store", "{nosql_name}", "Estado do padrao {scenario["pattern"]}"{sprite(cloud, nosql_icon)})')
        styled.append("pattern_db")

    L.append("    }")
    L.append("")

    # Security layer - Ory Stack + OPA
    L.append(f'    Container_Boundary(sec0, "Security Layer") {{')
    L.append(f'        Container(ory_oathkeeper, "Ory Oathkeeper", "Go", "Zero Trust proxy: authenticators, authorizers, mutators"{sprite(cloud, cloud_svc(cloud, "api_gw")[1])})')
    L.append(f'        Container(ory_kratos, "Ory Kratos", "Go", "Identity management: registration, login, MFA, sessions"{sprite(cloud, cloud_svc(cloud, "iam")[1])})')
    L.append(f'        Container(ory_keto, "Ory Keto", "Go", "Permissions (Zanzibar): relation tuples, check/expand API"{sprite(cloud, cloud_svc(cloud, "secret")[1])})')
    L.append(f'        Container(opa_sidecar, "OPA Policy Engine", "OPA + Rego", "Policy as Code para authorization e compliance"{sprite(cloud, cloud_svc(cloud, "waf")[1])})')
    L.append(f'        ContainerDb(identity_db, "Identity Store", "{db_name}", "Identidades, sessions, credentials"{sprite(cloud, db_icon)})')
    L.append(f'        ContainerDb(keto_db, "Keto Store", "{db_name}", "Relation tuples e namespaces"{sprite(cloud, db_icon)})')
    L.append("    }")
    styled.extend(["ory_oathkeeper", "ory_kratos", "ory_keto", "opa_sidecar", "identity_db", "keto_db"])
    L.append("")

    # Observability layer - Datadog
    dd_lib = DD_TRACE_LIBS.get(stack["id"], "dd-trace")
    L.append(f'    Container_Boundary(obs0, "Observability Layer") {{')
    L.append(f'        Container(dd_agent, "Datadog Agent", "DaemonSet", "Coleta metricas, traces e logs de todos os containers"{sprite(cloud, cloud_svc(cloud, "monitoring")[1])})')
    mon_name_obs, mon_icon_obs = cloud_svc(cloud, "monitoring")
    L.append(f'        Container(dd_apm, "APM Tracer", "{dd_lib}", "Distributed tracing com auto-instrumentacao"{sprite(cloud, mon_icon_obs)})')
    L.append(f'        Container(dd_logs, "Log Forwarder", "Datadog Agent", "Coleta e envia logs para Datadog Log Management"{sprite(cloud, mon_icon_obs)})')
    L.append("    }")
    styled.extend(["dd_agent", "dd_apm", "dd_logs"])
    L.append("")

    for e_name, e_desc in domain["ext_systems"][:2]:
        L.append(f'    System_Ext({sid(e_name)}, "{e_name}", "{e_desc}")')
    L.append(f'    System_Ext(ory_hydra, "Ory Hydra", "OAuth 2.0 & OpenID Connect Server (FAPI)"{sprite(cloud, cloud_svc(cloud, "api_gw")[1])})')
    L.append(f'    System_Ext(datadog_platform, "Datadog Platform", "SaaS: APM, Logs, Metrics, Dashboards, Alerts"{sprite(cloud, mon_icon_obs)})')
    L.append("")

    # Relationships
    if domain["persons"]:
        L.append(f'    Rel({sid(domain["persons"][0][0])}, ory_oathkeeper, "Acessa via proxy", "HTTPS")')
        L.append(f'    Rel(ory_oathkeeper, ory_kratos, "Valida session", "HTTPS")')
        L.append(f'    Rel(ory_oathkeeper, {svc_id}, "Roteia autenticado", "HTTPS")')

    L.append(f'    Rel({svc_id}, ory_keto, "Verifica permissao", "gRPC")')
    L.append(f'    Rel({svc_id}, opa_sidecar, "Avalia policy", "localhost:8181")')
    L.append(f'    Rel(ory_kratos, ory_hydra, "Emite tokens OAuth2", "HTTPS")')
    L.append(f'    Rel(ory_kratos, identity_db, "Persiste identidades", "{db_name}")')
    L.append(f'    Rel(ory_keto, keto_db, "Persiste relation tuples", "{db_name}")')
    L.append(f'    Rel({svc_id}, dd_apm, "Envia traces", "localhost:8126")')
    L.append(f'    Rel({svc_id}, dd_agent, "Envia metricas", "localhost:8125/DogStatsD")')
    L.append(f'    Rel(dd_agent, datadog_platform, "Forwarda telemetria", "HTTPS")')
    L.append(f'    Rel(dd_logs, datadog_platform, "Forwarda logs", "HTTPS")')

    if is_eip:
        L.append(f'    Rel({svc_id}, main_q, "Publica mensagens", "{cloud_svc(cloud, "queue")[0]}")')
        L.append(f'    Rel(main_q, {proc_id}, "Consome e processa", "Async")')
        L.append(f'    Rel({proc_id}, pattern_q, "Roteia para canal", "{cloud_svc(cloud, "pubsub")[0]}")')
        L.append(f'    Rel({proc_id}, main_db, "Persiste resultado", "{db_name}")')
    else:
        L.append(f'    Rel({svc_id}, {dp_id}, "Delega para padrao", "{stack["api"]}")')
        L.append(f'    Rel({dp_id}, event_q, "Emite eventos", "{cloud_svc(cloud, "queue")[0]}")')
        L.append(f'    Rel({svc_id}, main_db, "Persiste dados", "{db_name}")')
        L.append(f'    Rel({dp_id}, pattern_db, "Armazena estado", "{cloud_svc(cloud, "db_nosql")[0]}")')

    L.append(f'    Rel({svc_id}, cache, "Consulta cache", "{cache_name}")')

    if domain["ext_systems"]:
        L.append(f'    Rel({svc_id}, {sid(domain["ext_systems"][0][0])}, "Integra com", "HTTPS/mTLS")')

    L.append("")
    L.extend(style_lines(cloud, styled))
    L.append('    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")')
    return "\n".join(L)


# ═══════════════════════════════════════════════════════════════════
# C4 COMPONENT GENERATORS
# ═══════════════════════════════════════════════════════════════════

# Component templates per pattern type
_COMP_TEMPLATES = {
    "content-based-router": [("Route Controller", "api"), ("Content Inspector", "fw"), ("Route Table", "data"), ("Channel Dispatcher", "msg")],
    "pub-sub": [("Event Publisher", "msg"), ("Subscriber Registry", "data"), ("Fan-Out Manager", "fw"), ("Delivery Tracker", "data")],
    "splitter-aggregator": [("Message Splitter", "fw"), ("Correlation Manager", "data"), ("Parallel Processor", "msg"), ("Result Aggregator", "fw")],
    "dead-letter": [("DLQ Consumer", "msg"), ("Retry Scheduler", "fw"), ("Poison Detector", "fw"), ("Alert Notifier", "msg")],
    "wire-tap": [("Tap Interceptor", "fw"), ("Message Logger", "data"), ("Audit Writer", "data"), ("Compliance Reporter", "fw")],
    "message-translator": [("Schema Validator", "fw"), ("Canonical Mapper", "fw"), ("Format Converter", "fw"), ("Validation Reporter", "data")],
    "pipes-filters": [("Pipeline Controller", "api"), ("Validation Filter", "fw"), ("Enrichment Filter", "fw"), ("Transform Filter", "fw")],
    "scatter-gather": [("Scatter Controller", "api"), ("Request Dispatcher", "msg"), ("Response Collector", "fw"), ("Timeout Handler", "fw")],
    "request-reply": [("Request Builder", "fw"), ("Correlation Service", "data"), ("Reply Handler", "fw"), ("Timeout Monitor", "fw")],
    "competing-consumers": [("Consumer Manager", "fw"), ("Partition Assigner", "fw"), ("Work Distributor", "msg"), ("Progress Tracker", "data")],
    "cqrs-es": [("Command Handler", "api"), ("Event Writer", "data"), ("Projection Builder", "fw"), ("Snapshot Manager", "data")],
    "saga-orchestration": [("Saga Controller", "api"), ("Step Executor", "fw"), ("State Machine", "fw"), ("Compensation Handler", "fw")],
    "saga-choreography": [("Event Publisher", "msg"), ("Event Consumer", "msg"), ("Compensation Listener", "fw"), ("State Tracker", "data")],
    "circuit-breaker": [("Circuit Manager", "fw"), ("Fallback Handler", "fw"), ("Health Checker", "fw"), ("Metrics Recorder", "data")],
    "strangler-fig": [("Traffic Router", "api"), ("Legacy Adapter", "fw"), ("Feature Toggle", "data"), ("Migration Tracker", "data")],
    "api-gw-bff": [("Mobile BFF", "api"), ("Web BFF", "api"), ("Partner BFF", "api"), ("Response Aggregator", "fw")],
    "sidecar": [("Sidecar Proxy", "fw"), ("mTLS Handler", "fw"), ("Service Discovery", "fw"), ("Config Loader", "data")],
    "hexagonal": [("Inbound Adapter", "api"), ("Domain Service", "fw"), ("Outbound Port", "fw"), ("Repository Adapter", "data")],
    "outbox": [("Outbox Writer", "data"), ("Outbox Poller", "fw"), ("Message Relay", "msg"), ("Dedup Service", "fw")],
    "bulkhead": [("Bulkhead Manager", "fw"), ("Pool Isolator", "fw"), ("Semaphore Guard", "fw"), ("Resource Monitor", "data")],
}

_TECH_MAP = {"api": "api", "fw": "fw", "msg": "msg", "data": "data", "grpc": "grpc"}


def gen_component(domain_key, domain, cloud, scenario, is_eip, stack, variation_idx):
    c = CLOUDS[cloud]
    pattern = scenario["pattern"]
    comp_template = _COMP_TEMPLATES.get(pattern, [("Controller", "api"), ("Service", "fw"), ("Repository", "data"), ("Client", "grpc")])

    L = [ELK_FRONTMATTER, "C4Component"]
    L.append(f'    title {domain["label"]} - {pattern.replace("-", " ").title()} - Component View [{c["label"]} / {stack["label"]}]')
    L.append("")

    # External containers
    api_gw_name, api_gw_icon = cloud_svc(cloud, "api_gw")
    L.append(f'    Container(api_layer, "{domain["label"]} API", "{stack["api"]}", "Camada de API do dominio"{sprite(cloud, api_gw_icon)})')

    db_name, db_icon = cloud_svc(cloud, "db_rel")
    L.append(f'    ContainerDb(main_db, "Database", "{db_name}", "Banco de dados principal"{sprite(cloud, db_icon)})')

    q_name, q_icon = cloud_svc(cloud, "queue")
    L.append(f'    ContainerQueue(msg_queue, "Message Queue", "{q_name}", "Fila de mensagens"{sprite(cloud, q_icon)})')

    if not is_eip:
        nosql_name, nosql_icon = cloud_svc(cloud, "db_nosql")
        L.append(f'    ContainerDb(pattern_store, "Pattern Store", "{nosql_name}", "Estado do padrao"{sprite(cloud, nosql_icon)})')
    L.append("")

    # Component boundary
    styled = []
    L.append(f'    Container_Boundary(comp0, "{domain["label"]} {pattern.replace("-", " ").title()}") {{')
    for comp_name, comp_type in comp_template:
        tech = stack.get(_TECH_MAP.get(comp_type, "fw"), stack["fw"])
        comp_id = sid(comp_name)
        compute_name, compute_icon = cloud_svc(cloud, "compute_fn" if comp_type == "msg" else "compute")
        L.append(f'        Component({comp_id}, "{comp_name}", "{tech}", "Responsavel por {comp_name.lower()}"{sprite(cloud, compute_icon)})')
        styled.append(comp_id)

    # Security components - Ory + OPA
    L.append(f'        Component(ory_identity_handler, "Identity Handler", "Ory Kratos Client", "Gerencia authentication, session e MFA"{sprite(cloud, cloud_svc(cloud, "iam")[1])})')
    L.append(f'        Component(ory_permission_checker, "Permission Checker", "Ory Keto Client", "Check/Expand API para RBAC/ABAC via Zanzibar"{sprite(cloud, cloud_svc(cloud, "secret")[1])})')
    L.append(f'        Component(opa_policy_evaluator, "OPA Policy Evaluator", "OPA REST Client", "Avalia Rego policies para authorization e compliance"{sprite(cloud, cloud_svc(cloud, "waf")[1])})')
    styled.extend(["ory_identity_handler", "ory_permission_checker", "opa_policy_evaluator"])

    # Observability components - Datadog
    dd_lib = DD_TRACE_LIBS.get(stack["id"], "dd-trace")
    mon_name_c, mon_icon_c = cloud_svc(cloud, "monitoring")
    L.append(f'        Component(dd_tracer, "DD Tracer", "{dd_lib}", "Instrumentacao automatica de spans para HTTP, gRPC, DB, Queue"{sprite(cloud, mon_icon_c)})')
    L.append(f'        Component(dd_metrics_client, "Metrics Client", "DogStatsD Client", "Emite custom metrics: counters, gauges, histograms, distributions"{sprite(cloud, mon_icon_c)})')
    L.append(f'        Component(dd_log_enricher, "Log Enricher", "Datadog Log Correlation", "Injeta trace_id e span_id nos logs para correlacao APM-Logs"{sprite(cloud, mon_icon_c)})')
    styled.extend(["dd_tracer", "dd_metrics_client", "dd_log_enricher"])
    L.append("    }")
    L.append("")

    # Relationships
    L.append(f'    Rel(api_layer, ory_identity_handler, "Valida identity/session", "Internal")')
    L.append(f'    Rel(ory_identity_handler, {sid(comp_template[0][0])}, "Autoriza e delega", "Internal")')
    L.append(f'    Rel({sid(comp_template[0][0])}, ory_permission_checker, "Verifica permissao", "Internal")')
    L.append(f'    Rel({sid(comp_template[0][0])}, opa_policy_evaluator, "Avalia policy de negocio", "Internal")')
    for i in range(len(comp_template) - 1):
        L.append(f'    Rel({sid(comp_template[i][0])}, {sid(comp_template[i+1][0])}, "Delega para", "Internal")')

    last_comp = sid(comp_template[-1][0])
    L.append(f'    Rel({last_comp}, main_db, "Lê/Escreve", "{db_name}")')

    if is_eip:
        L.append(f'    Rel({sid(comp_template[0][0])}, msg_queue, "Publica em", "{q_name}")')
    else:
        L.append(f'    Rel({sid(comp_template[0][0])}, pattern_store, "Persiste estado", "{cloud_svc(cloud, "db_nosql")[0]}")')
        L.append(f'    Rel({sid(comp_template[-1][0])}, msg_queue, "Emite eventos", "{q_name}")')

    # Datadog observability relationships
    L.append(f'    Rel({sid(comp_template[0][0])}, dd_tracer, "Cria spans", "Internal")')
    L.append(f'    Rel({sid(comp_template[-1][0])}, dd_metrics_client, "Emite metricas", "DogStatsD")')
    L.append(f'    Rel({sid(comp_template[0][0])}, dd_log_enricher, "Enriquece logs com trace context", "Internal")')

    L.append("")
    L.extend(style_lines(cloud, styled))
    L.append('    UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")')
    return "\n".join(L)


# ═══════════════════════════════════════════════════════════════════
# MAIN GENERATION
# ═══════════════════════════════════════════════════════════════════

def generate_all(base_dir="models"):
    base = Path(base_dir)
    count = 0
    md_count = 0
    stats = {"context": 0, "container": 0, "component": 0}
    cloud_stats = {c: 0 for c in CLOUDS}
    domain_stats = {d: 0 for d in DOMAINS}

    for dk, domain in DOMAINS.items():
        for ck in CLOUDS:
            scenarios = domain["scenarios"]

            # CONTEXT: 5 EIP + 5 DP = 10 files
            for i, sc in enumerate(scenarios.get("context_eip", [])[:5]):
                content = gen_context(dk, domain, ck, sc, is_eip=True)
                fp = base / dk / ck / "context" / f"{dk}-{sc['pattern']}-context.mmd"
                fp.parent.mkdir(parents=True, exist_ok=True)
                fp.write_text(content, encoding="utf-8")
                gen_doc(fp, sc["title"], domain, ck, "Context", sc, is_eip=True)
                count += 1; md_count += 1; stats["context"] += 1; cloud_stats[ck] += 1; domain_stats[dk] += 1

            for i, sc in enumerate(scenarios.get("context_dp", [])[:5]):
                content = gen_context(dk, domain, ck, sc, is_eip=False)
                fp = base / dk / ck / "context" / f"{dk}-{sc['pattern']}-context.mmd"
                fp.parent.mkdir(parents=True, exist_ok=True)
                fp.write_text(content, encoding="utf-8")
                gen_doc(fp, sc["title"], domain, ck, "Context", sc, is_eip=False)
                count += 1; md_count += 1; stats["context"] += 1; cloud_stats[ck] += 1; domain_stats[dk] += 1

            # CONTAINER: 5 EIP + 5 DP = 10 files (rotating stacks)
            for i, sc in enumerate(scenarios.get("container_eip", [])[:5]):
                stack = pick_stack(i)
                content = gen_container(dk, domain, ck, sc, is_eip=True, stack=stack)
                fp = base / dk / ck / "container" / f"{dk}-{sc['pattern']}-{stack['id']}-container.mmd"
                fp.parent.mkdir(parents=True, exist_ok=True)
                fp.write_text(content, encoding="utf-8")
                gen_doc(fp, sc["title"], domain, ck, "Container", sc, is_eip=True, stack=stack)
                count += 1; md_count += 1; stats["container"] += 1; cloud_stats[ck] += 1; domain_stats[dk] += 1

            for i, sc in enumerate(scenarios.get("container_dp", [])[:5]):
                stack = pick_stack(i + 2)
                content = gen_container(dk, domain, ck, sc, is_eip=False, stack=stack)
                fp = base / dk / ck / "container" / f"{dk}-{sc['pattern']}-{stack['id']}-container.mmd"
                fp.parent.mkdir(parents=True, exist_ok=True)
                fp.write_text(content, encoding="utf-8")
                gen_doc(fp, sc["title"], domain, ck, "Container", sc, is_eip=False, stack=stack)
                count += 1; md_count += 1; stats["container"] += 1; cloud_stats[ck] += 1; domain_stats[dk] += 1

            # COMPONENT: 5 EIP + 5 DP = 10 files (rotating stacks)
            eip_patterns = scenarios.get("context_eip", scenarios.get("container_eip", []))
            dp_patterns = scenarios.get("context_dp", scenarios.get("container_dp", []))

            for i in range(5):
                sc = eip_patterns[i % len(eip_patterns)] if eip_patterns else {"pattern": _EIP_IDS[i], "title": f"{domain['label']} {_EIP_LABELS[i]}", "focus": _EIP_DESCS[i]}
                stack = pick_stack(i + 1)
                content = gen_component(dk, domain, ck, sc, is_eip=True, stack=stack, variation_idx=i)
                fp = base / dk / ck / "component" / f"{dk}-{sc['pattern']}-{stack['id']}-component.mmd"
                fp.parent.mkdir(parents=True, exist_ok=True)
                fp.write_text(content, encoding="utf-8")
                comp_title = f"{domain['label']} - {sc['pattern'].replace('-', ' ').title()} - Component View"
                gen_doc(fp, comp_title, domain, ck, "Component", sc, is_eip=True, stack=stack)
                count += 1; md_count += 1; stats["component"] += 1; cloud_stats[ck] += 1; domain_stats[dk] += 1

            for i in range(5):
                sc = dp_patterns[i % len(dp_patterns)] if dp_patterns else {"pattern": _DP_IDS[i+5], "title": f"{domain['label']} {_DP_LABELS[i+5]}", "focus": _DP_DESCS[i+5]}
                stack = pick_stack(i + 3)
                content = gen_component(dk, domain, ck, sc, is_eip=False, stack=stack, variation_idx=i)
                fp = base / dk / ck / "component" / f"{dk}-{sc['pattern']}-{stack['id']}-component.mmd"
                fp.parent.mkdir(parents=True, exist_ok=True)
                fp.write_text(content, encoding="utf-8")
                comp_title = f"{domain['label']} - {sc['pattern'].replace('-', ' ').title()} - Component View"
                gen_doc(fp, comp_title, domain, ck, "Component", sc, is_eip=False, stack=stack)
                count += 1; md_count += 1; stats["component"] += 1; cloud_stats[ck] += 1; domain_stats[dk] += 1

    print(f"\n{'='*60}")
    print(f"Generation complete!")
    print(f"{'='*60}")
    print(f"Total .mmd files: {count}")
    print(f"Total .md  files: {md_count}")
    print(f"Total files:      {count + md_count}")
    print(f"\nBy C4 level:")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print(f"\nBy cloud:")
    for k, v in cloud_stats.items():
        print(f"  {k}: {v}")
    print(f"\nBy domain:")
    for k, v in sorted(domain_stats.items()):
        print(f"  {k}: {v}")
    return count


if __name__ == "__main__":
    total = generate_all()
    if 2000 <= total <= 5000:
        print(f"\nSUCCESS: {total} .mmd + {total} .md = {total * 2} total files generated.")
    else:
        print(f"\nWARNING: {total} files generated (target: 2000-5000).")
