# 🚦 Release Validation & CI/CD

<div align="center">

![CI/CD](https://img.shields.io/badge/Pipeline-Validation-blue?style=for-the-badge)
![Quality](https://img.shields.io/badge/Gate-Strict-red?style=for-the-badge)

**Automated quality gates restricting infrastructure deployments ensuring system health integrity.**

[⬅️ Back to Root](../README.md)

</div>

---

## 1. Executive Overview

### Purpose
The `validation/` module serves as the final arbiter preventing regressions from entering production. It executes rigorous boundary checks across the application footprint bridging Data, Code, and Operations.

### Business & Technical Problems Solved
- **Business**: Protects users from operational downtime.
- **Technical**: Integrates disparate ecosystem failures—such as a DVC hash mismatch, a malformed Docker manifest, or a JSON Pydantic crash—into a singular unifying Failure Exit Code natively parsed by GitHub Actions / CI runners.

### Role Within the System
The CI/CD Gatekeeper context. Executed fundamentally as a precondition before branch merging or container tagging.

---

## 2. System Context & Architecture

### Continuous Integration Context

```mermaid
graph TD
    PR[New Pull Request] -->|Triggers| Make(make validate)
    
    Make --> Repo[validate_repo.py]
    Repo -->|Checks YAML Config| Y(params.yaml)
    Repo -->|Checks DVC Stage| D(dvc.lock)
    
    Make --> Runtime[release_check.py]
    Runtime -->|Compiles| Images[docker compose build]
    Runtime -->|Deploys| Containers[Runtime Sandbox]
    Runtime -->|Curls API| Endpoint(POST /predict)
    
    Containers --> |If SUCCESS| Merge(Merge Permitted)
```

### Architectural Principles
- **End-To-End Ephemeral Checking**: Tests execute actively against temporary runtime sandboxes, assuring zero "mock bias" across integration checkpoints.
- **Fail Fast Execution**: Halts execution cleanly at the earliest detection event, ensuring developer loop feedback returns instantly.

---

## 3. Component-Level Design

### Core Modules

1. **`validation/validate_repo.py`**
   - **Responsibility**: Static Analysis. Scans local registry structure, confirms dependencies exist, checks `.yaml` configuration limits logically.
2. **`validation/release_check.py`**
   - **Responsibility**: Operational Analytics. Generates full Docker containers implicitly, boots them, intercepts them via raw `cURL` commands testing HTTP 200 outputs, and tears them down.

---

## 4. Data Design
*(Not applicable)*

---

## 5. API Design
*(Not applicable)*

---

## 6. Execution Flow

### Comprehensive Sequence ( `make validate` )
1. Initializes `validate_repo`.
2. Asserts standard directory tree logic.
3. Tests DVC structural status bounds.
4. Invokes `release_check`.
5. Automates a `docker build` targeting `infra/Dockerfile.inference`.
6. Executes `docker run` detached.
7. Iteratively queries the Liveness Probe Endpoint `GET /health` with linear backoff.
8. Posts a mock JSON clinical record mathematically asserting standard success routing.
9. Executes cleanup bounds triggering SIGKILL against targeted validation containers.

---

## 7. Infrastructure & Deployment
Runs locally natively via standard bash binaries (`python`, `docker`, `curl`).

---

## 8. Security Architecture
The release validation inherently catches massive misconfigurations. If Docker files contain faulty `EXPOSE` logic or missing Security Header arrays natively expected during startup sequences, the health checks will trap an operational failure.

---

## 9. Performance & Scalability
Validation cycles efficiently run under 60-seconds locally leveraging pervasive layer caching via the Docker daemon engine avoiding total scratch builds.

---

## 10. Reliability & Fault Tolerance
Linear sleep loops protect against race conditions where the Kestrel/Uvicorn HTTP bindings map slowly compared to instantaneous curl logic firing mechanisms.

---

## 11. Observability
Detailed console logs generated.
```text
[INFO] Starting release validation...
[INFO] Step 1: Checking code integrity... OK
[INFO] Step 2: DVC Pipeline check... OK
[INFO] Step 3: Docker build check... OK
[SUCCESS] Release validation passed!
```

---

## 12. Testing Strategy
The validation module **is** the core integration testing boundary executing End-To-End routines. 

---

## 13. Configuration & Environment Variables
*(Not applicable directly)*

---

## 14. Development Guide

### Initiating Validations locally
To execute standard checks:
```bash
make validate
```
If errors trap, read the standard `stderr` to identify if the boundary breach occurred in the Code Syntax, the Offline Network, or the Runtime Execution mapping.

---

## 15. Future Improvements / Technical Debt

- **Comprehensive Security Scanning**: Integrate tools like `trivy` natively inside `release_check` boundaries to scan built Docker geometries recursively checking against upstream CVE registry lists.
- **Expanded Application Testing**: Shift towards PyTest frameworking standardizing reporting outputs to standardized `.xml` arrays consumable by Jenkins tracking GUIs automatically.
