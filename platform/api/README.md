# API Reference

Glapagos Platform — GENIA Americas Corporation
Version: 1.0
Base URL: https://api.glapagos.com/v1

## Authentication

Bearer token via OAuth 2.0 client credentials:

POST https://auth.glapagos.com/oauth/token
grant_type=client_credentials&client_id={id}&client_secret={secret}&scope={scopes}

Tokens expire after 3600 seconds.

Scopes: data:read, data:write, models:read, models:deploy, compliance:read, admin

## Conventions

All request bodies: Content-Type: application/json
All responses: JSON envelope with status, data, and meta fields.
Pagination: cursor-based. Versioning: major version in URL path.

## Services

### Data Service
GET  /v1/pipelines          List pipelines
POST /v1/pipelines          Create pipeline
GET  /v1/pipelines/{id}     Get pipeline
POST /v1/pipelines/{id}/run Trigger run
GET  /v1/catalog            List data catalog

### Model Service
GET  /v1/models             List models
POST /v1/models             Register model
POST /v1/models/{id}/deploy Deploy version
POST /v1/models/{id}/predict Run inference
POST /v1/training-jobs      Start training job

### Compliance Service
GET    /v1/compliance/jurisdictions  List active modules
GET    /v1/compliance/audit-log      Query audit log
DELETE /v1/compliance/data-subjects/{id}  Process deletion request

### Federation Service
GET  /v1/federation/nodes        List connected nodes
POST /v1/federation/jobs         Start federated training
GET  /v1/federation/jobs/{id}/results  Get aggregated results

## Example

curl -X POST https://api.glapagos.com/v1/models/ameri-xlm-v1/predict \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{"inputs":[{"text":"El gobierno anunció nuevas medidas.","language":"es-LA"}],"task":"classification"}'

## SDKs

Python: pip install glapagos-sdk
Node.js: npm install @genia-americas/glapagos
Full SDK documentation: tools/glapp/

Contact: admin@genia.ai
https://docs.glapagos.com
