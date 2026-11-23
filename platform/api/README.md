# Glapagos API, draft specification

**Status: draft design (v0.1). This repo documents no public endpoint.** The routes below describe an intended API. They are not a deployed service, and no OpenAPI file is published here yet. For the platform itself, see [glapagos.com](https://www.glapagos.com).

Proposed base URL: `https://api.glapagos.com/v1`

## Authentication

OAuth 2.0 client credentials with a bearer token:

```
POST https://auth.glapagos.com/oauth/token
grant_type=client_credentials&client_id={id}&client_secret={secret}&scope={scopes}
```

Tokens expire after 3600 seconds.

Scopes: `data:read`, `data:write`, `models:read`, `models:deploy`, `compliance:read`, `admin`

## Conventions

- Request bodies: `Content-Type: application/json`
- Responses: JSON envelope with `status`, `data`, and `meta`
- Pagination: cursor-based
- Versioning: major version in the URL path

## Services

### Data

| Method | Route | Purpose |
|--------|-------|---------|
| GET | `/v1/pipelines` | List pipelines |
| POST | `/v1/pipelines` | Create pipeline |
| GET | `/v1/pipelines/{id}` | Get pipeline |
| POST | `/v1/pipelines/{id}/run` | Trigger run |
| GET | `/v1/catalog` | List data catalog |

### Models

| Method | Route | Purpose |
|--------|-------|---------|
| GET | `/v1/models` | List models |
| POST | `/v1/models` | Register model |
| POST | `/v1/models/{id}/deploy` | Deploy version |
| POST | `/v1/models/{id}/predict` | Run inference |
| POST | `/v1/training-jobs` | Start training job |

### Compliance

| Method | Route | Purpose |
|--------|-------|---------|
| GET | `/v1/compliance/jurisdictions` | List active modules |
| GET | `/v1/compliance/audit-log` | Query audit log |
| DELETE | `/v1/compliance/data-subjects/{id}` | Process deletion request |

### Federation

| Method | Route | Purpose |
|--------|-------|---------|
| GET | `/v1/federation/nodes` | List connected nodes |
| POST | `/v1/federation/jobs` | Start federated training |
| GET | `/v1/federation/jobs/{id}/results` | Get aggregated results |

## Example request (illustrative)

```bash
curl -X POST https://api.glapagos.com/v1/models/<model-id>/predict \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"inputs":[{"text":"El gobierno anunció nuevas medidas.","language":"es-LA"}],"task":"classification"}'
```

SDK interface draft: [tools/glapp](../../tools/glapp/README.md).

Contact: admin@genia.ai
