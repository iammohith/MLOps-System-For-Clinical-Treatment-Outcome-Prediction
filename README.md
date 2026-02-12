# 🏥 MLOps Clinical Treatment Outcome Prediction

An authoritative, truth-backed MLOps system for predicting patient treatment improvement scores. This repository demonstrates a production-honest technical stack focused on reproducibility, observability, and zero-trust validation.

---

## 📖 Purpose & Scope

This system provides an end-to-end pipeline to train, serve, and monitor a machine learning model that predicts an **Improvement_Score** (0–10 scale) for clinical patients based on their medical profile and treatment history.

### 🚫 Non-Goals

* **No Diagnostic Advice**: This is a research/quality analysis tool. It does not provide clinical recommendations.
* **No Live Data Ingestion**: Operates on static CSV batch data (DVC tracked).
* **No Built-in Auth**: Designed for local/VPN deployment; requires external OIDC/OAuth for public exposure.

---

## 🏗️ System Architecture

```text
                                  ┌────────────────────────┐
                                  │      OBSERVABILITY     │
                                  │  Prometheus + Grafana  │
                                  └───────────▲────────────┘
                                              │ /metrics
                                              │
┌────────────────────────┐        ┌───────────┴────────────┐        ┌──────────────────┐
│      DATA PIPELINE     │        │      SERVING LAYER     │        │     FRONTEND     │
│  DVC: Ingest → Train   │───────▶│  FastAPI (Inference)   │◀───────│  Modern Web UI   │
└────────────────────────┘ Model  └────────────────────────┘ Req/Res └──────────────────┘
```

### Tech Stack

* **Pipeline**: [DVC](https://dvc.org/) (Data Version Control)
* **Machine Learning**: [Scikit-learn](https://scikit-learn.org/) (RandomForestRegressor)
* **API**: [FastAPI](https://fastapi.tiangolo.com/) (Pydantic-enforced schemas)
* **Infrastructure**: [Docker Compose](https://docs.docker.com/compose/) & [Kubernetes](https://kubernetes.io/) (Local manifests)
* **Monitoring**: [Prometheus](https://prometheus.io/) & [Grafana](https://grafana.com/)

---

## 🚀 Local Execution (Truth-Backed)

Assume a clean macOS/Linux machine with **Python 3.10+** and **Docker**.

### 1. One-Command Setup

We use a `Makefile` to enforce an idempotent, zero-manual-step environment.

```bash
git clone https://github.com/iammohith/MLOps-System-For-Clinical-Treatment-Outcome-Prediction.git
cd MLOps-System-For-Clinical-Treatment-Outcome-Prediction

# Standardizes venv, dependencies (3.10-3.13), and DVC initialization
make setup
```

### 2. Full Pipeline Execution

Reproduce the entire data science lifecycle from raw data to model artifact.

```bash
make run-pipeline
# Success indicator: models/model.joblib is generated and metrics/scores.json updated.
```

### 3. Zero-Trust Verification (Mandatory before Push)

Runs the authoritative integrity script that builds Docker images, validates K8s manifests, and tests API runtime behavior.

```bash
make validate
```

---

## 🔍 Observability & Interaction

### Standard Execution

```bash
# Start API (Port 8000)
. venv/bin/activate && python -m uvicorn inference.app:app --port 8000

# Start UI (Port 8080)
cd frontend && python -m http.server 8080
```

### Observe in Real-Time

| Component | URL | Expected Metric/Data |
| :--- | :--- | :--- |
| **Web UI** | <http://localhost:8080> | Interactive prediction form + animated gauge |
| **Prometheus** | <http://localhost:9090> | `api_request_total`, `api_prediction_total` |
| **Grafana** | <http://localhost:3000> | Red/Green health status, Latency p95, Model Version |

---

## 📂 Credible Directory Structure

* `pipelines/` & `training/`: Enforced DVC stages for reproducible results.
* `inference/`: Strict Pydantic schemas unified with `params.yaml`.
* `infra/`: Validation-backed Docker and K8s manifests.
* `validation/`: The authoritative `release_check.py` truth engine.

---

## ⚠️ Limitations & Failure Modes

* **Schema Rigidity**: The API hard-fails (422) if inputs deviate from `params.yaml` allowed values.
* **Docker Dependency**: `make validate` requires a running Docker daemon to verify container builds.
* **Local Remote**: DVC uses `/tmp/dvc-remote`. Pipeline history is lost across machine reboots if the temp dir is purged.

---

## 📜 Final Governing Principle

Great documentation does not describe intent — it proves reality. This system is verified end-to-end by the `make validate` protocol.
