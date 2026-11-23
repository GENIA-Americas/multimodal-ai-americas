# GLAPP (Glapagos SDK), draft

**Status: design draft. Nothing here is installable yet.** As of 2026-11-23 there is no `glapagos-sdk` package on PyPI and no `@genia-americas/glapagos` package on npm, and this repo contains no SDK code. The snippets below sketch the interface we intend to build so contributors can critique it before code exists. They will not run.

## Intended interface (illustrative)

Authentication with client credentials:

```python
from glapagos import GlapagosClient

client = GlapagosClient(client_id="...", client_secret="...")
# or read GLAPAGOS_CLIENT_ID and GLAPAGOS_CLIENT_SECRET from the environment
client = GlapagosClient()
```

Models and inference:

```python
models = client.models.list()

result = client.models.predict(
    model_id="<model-id>",
    inputs=[{"text": "Texto en español latinoamericano", "language": "es-LA"}],
    task="classification",
)
```

Data pipelines and compliance:

```python
pipeline = client.pipelines.create(
    name="example-ingestion",
    source={"type": "http", "url": "https://example.org/data.json", "format": "json"},
    schema="<schema-name>",
    jurisdiction="BR",
    schedule="0 6 * * *",
)

status = client.compliance.status(jurisdiction="BR")
```

Federated training:

```python
job = client.federation.train(
    model_config="path/to/config.yaml",
    nodes=["<node-id-1>", "<node-id-2>"],
    rounds=10,
    privacy_budget=1.0,
)
```

Command line:

```bash
glapp models list
glapp predict --model <model-id> --input data.jsonl --output results.jsonl
glapp compliance check --jurisdiction BR
```

The matching HTTP API draft is in [platform/api](../../platform/api/README.md).

## Contributing

Feedback on the interface is the most useful thing right now. Open an issue tagged `sdk`. Workflow: [CONTRIBUTING.md](../../CONTRIBUTING.md).

Contact: admin@genia.ai
