# GLAPP — Glapagos SDK

GENIA Americas Corporation
https://www.glapagos.com

## Installation

pip install glapagos-sdk
npm install @genia-americas/glapagos

## Authentication

from glapagos import GlapagosClient
client = GlapagosClient(client_id="...", client_secret="...")

Or via environment variables:
export GLAPAGOS_CLIENT_ID=...
export GLAPAGOS_CLIENT_SECRET=...
client = GlapagosClient()

## Core Operations

# List models
models = client.models.list()

# Run inference
result = client.models.predict(
    model_id="ameri-xlm-v1",
    inputs=[{"text": "Texto en español latinoamericano", "language": "es-LA"}],
    task="classification"
)

# Create a pipeline
pipeline = client.pipelines.create(
    name="conab-ingestion",
    source={"type": "http", "url": "https://www.conab.gov.br/api/crops", "format": "json"},
    schema="agriculture-production",
    jurisdiction="BR",
    schedule="0 6 * * *"
)

# Check compliance
status = client.compliance.status(jurisdiction="BR")

# Start federated training
job = client.federation.train(
    model_config="regional-nlp/ameri-xlm/config.yaml",
    nodes=["node_br_01", "node_co_01", "node_mx_01"],
    rounds=10,
    privacy_budget=1.0
)

## CLI

glapp models list
glapp predict --model ameri-xlm-v1 --input data.jsonl --output results.jsonl
glapp compliance check --jurisdiction BR

## Contributing

Issues tagged sdk in the issue tracker. Contributions follow CONTRIBUTING.md.

Contact: admin@genia.ai
https://docs.glapagos.com
