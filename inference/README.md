# 🚀 Inference Service

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-Production-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Container-AppUser-2496ED?style=for-the-badge&logo=docker&logoColor=white)

**High-performance, schema-validated REST API for clinical outcome prediction.**

[⬅️ Back to Root](../README.md)

> [!TIP]
> **For Non-Technical Users**: This is a backend service. You do not need to run this manually. Please use the [Quick Start Guide](../README.md) to launch the full system via Docker.

</div>

---

## 1. Executive Overview

### Purpose

The Inference Service is the core runtime component of the MLOps system. It wraps the trained Scikit-Learn model in a robust FastAPI shell, handling request validation, prediction execution, and metric telemetry.

### Key Capabilities

*   **Singleton Model Loading**: Efficiently loads the heavy model artifact once at startup (`ModelLoader`).
*   **Strict Validation**: Uses Pydantic models to reject invalid medical data (e.g., negative Age) before it hits the model.
*   **Observability**: Native Prometheus instrumentation for request rates, latencies, and prediction distributions.
*   **Security**: Runs as non-root `appuser`, enforcing trusted host and CORS policies.

---

## 2. API Reference

The API runs on port **8000** by default. Full interactive documentation triggers at `/docs`.

### Endpoints

| Method | Path | Description | Access |
| :--- | :--- | :--- | :--- |
| `GET` | `/health` | Liveness/Readiness probe. Returns `503` if model not loaded. | Public |
| `POST` | `/predict` | Main inference endpoint. Accepts JSON payload. | Public |
| `GET` | `/metrics` | Prometheus scrape target (Text format). | Prometheus |
| `GET` | `/dropdown-values` | Returns valid enum values for Frontend forms. | Frontend |

### Prediction Payload Schema

```json
{
  "Patient_ID": "P12345",
  "Age": 45,
  "Gender": "Male",
  "Condition": "Diabetes",
  "Drug_Name": "Metformin",
  "Dosage_mg": 500.0,
  "Treatment_Duration_days": 30,
  "Side_Effects": "None"
}
```

---

## 3. Observability Code (Prometheus)

We do not use a sidecar for metrics; the application instrument itself using `prometheus_client`.

| Metric Name | Type | Labels | Description |
| :--- | :--- | :--- | :--- |
| `api_request_total` | Counter | `method`, `endpoint`, `status` | Total incoming HTTP requests. |
| `api_prediction_total` | Counter | None | Total successful predictions. |
| `api_prediction_errors_total` | Counter | None | Total failed predictions (5xx/4xx). |
| `api_request_duration_seconds`| Histogram| `endpoint` | Request latency buckets. |
| `model_info` | Gauge | `version` | Currently loaded model SHA-256 hash. |

---

## 4. Security Architecture

The application (`app.py`) implements a defense-in-depth middleware chain:

1.  **TrustedHostMiddleware**: Rejects requests with invalid `Host` headers.
2.  **CORSMiddleware**: strictly controls cross-origin access (Configured via `ALLOWED_ORIGINS` env var).
3.  **Security Headers**: Injects `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `CSP`, etc.
4.  **Request Logging**: Audits all access with timing data.

---

## 5. Development Guide

### Running Locally

```bash
# Install dependencies
pip install -r requirements-inference.txt

# Run Uvicorn
uvicorn inference.app:app --reload --host 0.0.0.0 --port 8000
```

### Configuration ( Environment Variables)

*   `MODEL_PATH`: Path to `.joblib` model (Default: `models/model.joblib`).
*   `PREPROCESSOR_PATH`: Path to preprocessor (Default: `data/processed/preprocessor.joblib`).
*   `ALLOWED_ORIGINS`: Comma-separated list of CORS origins (Default: `http://localhost:8080`).
