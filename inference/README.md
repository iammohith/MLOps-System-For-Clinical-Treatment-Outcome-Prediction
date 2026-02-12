# Inference Service (FastAPI)

Production-ready prediction engine providing low-latency clinical outcome scores.

## 🔌 API Contract

| Method | Path | Enforced Behavior |
| :--- | :--- | :--- |
| `GET` | `/health` | Returns model status and version info. |
| `POST` | `/predict` | Strict Pydantic validation; returns 0–10 score. |
| `GET` | `/metrics` | Prometheus counters and latency histograms. |
| `GET` | `/dropdown-values` | **Dynamic**: Fetched directly from `params.yaml`. |

## 🏗️ Architecture Role

The API acts as the bridge between model artifacts (`models/model.joblib`) and the frontend. It is the single source of truth for "allowed" categorical inputs.

### Dynamic Sync

Validation logic in `schemas.py` is dynamically loaded from `params.yaml`. If you update a valid drug name in the config, the API immediately reflects this in its validation and frontend dropdown endpoints.

## 🏃 Running locally

```bash
. venv/bin/activate
export MODEL_PATH=models/model.joblib
python -m uvicorn inference.app:app --host 127.0.0.1 --port 8000
```

## 🩺 Health Check Indicator

The API is "ready" only when `model_loaded` is `true`.

```json
{
  "status": "healthy",
  "model_loaded": true,
  "model_version": "b190856..."
}
```
