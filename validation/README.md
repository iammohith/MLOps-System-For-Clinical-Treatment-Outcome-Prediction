# 🚦 Release Validation & CI/CD

<div align="center">

![CI/CD](https://img.shields.io/badge/Pipeline-Validation-blue?style=for-the-badge)
![Quality](https://img.shields.io/badge/Gate-Strict-red?style=for-the-badge)

**Automated quality gates for ensuring release integrity.**

[⬅️ Back to Root](../README.md)

</div>

---

## 1. Strategy

Release validation acts as the final gatekeeper before deployment. It runs a suite of checks covering:
1.  **Code Integrity**: Syntax checks.
2.  **Data Integrity**: Schema validation.
3.  **Reproducibility**: DVC pipeline status.
4.  **Container Health**: Docker build and run checks.
5.  **Runtime Logic**: API endpoint verification.

---

## 2. Validation Scripts

The validation logic is split into two specialized scripts:

### A. Repository Validator (`validate_repo.py`)
*   **Focus**: Static Analysis & Configuration.
*   **Checks**:
    *   `verify_structure`: Ensures all required files exist.
    *   `verify_schema`: Validates `params.yaml` structure.
    *   `verify_dvc`: Checks DVC pipeline consistency.
    *   `verify_requirements`: Checks dependency files.
    *   `verify_docker`: dry-run build checks.

### B. Release Check (`release_check.py`)
*   **Focus**: End-to-End Execution.
*   **Checks**:
    1.  **DVC Integration**: Ensures `dvc repro` runs without error.
    2.  **Containerization**: Builds the actual Docker image.
    3.  **Runtime**: Starts the container and curls `/health` and `/predict`.
    4.  **Cleanup**: Tears down test resources.

---

## 3. Usage

To run the full validation suite (recommended before opening a PR):

```bash
make validate
```

This command wraps `python validation/release_check.py` inside the virtual environment.

### Expected Output

```text
[INFO] Starting release validation...
[INFO] Step 1: Checking code integrity... OK
[INFO] Step 2: DVC Pipeline check... OK
[INFO] Step 3: Docker build check... OK
[INFO] Step 4: Kubernetes manifest check... OK
[INFO] Step 5: Runtime API check... OK
[SUCCESS] Release validation passed!
```
