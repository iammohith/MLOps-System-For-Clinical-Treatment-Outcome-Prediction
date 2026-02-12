# Inference Service

FastAPI-based inference API for serving predictions.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Liveness and readiness check |
| POST | `/predict` | Schema-validated prediction |
| GET | `/metrics` | Prometheus format metrics |
| GET | `/dropdown-values` | Valid dropdown values for frontend |
| GET | `/docs` | Swagger UI (auto-generated) |

## Running

```bash
# Direct
python -m uvicorn inference.app:app --host 0.0.0.0 --port 8000

# Or via Docker
docker compose -f infra/docker/docker-compose.yml up inference-api
```

## Schema Enforcement

The API uses Pydantic models (`schemas.py`) that enforce the exact CSV schema. Invalid requests receive HTTP 422 with detailed error messages.
