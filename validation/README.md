# Validation & Quality Gates

The single source of truth for repository integrity. No release is authorized unless the scripts in this directory pass with code `0`.

## 🛡️ Authoritative Check (`release_check.py`)

This is the "Zero-Trust" engine. It assumes nothing and verifies:

1. **Integrity**: Existence of all mandatory ML and Infra files.
2. **Execution**: Completes a full `dvc repro` smoke test.
3. **Containerization**: Builds all 3 custom Docker images.
4. **Orchestration**: Dry-run validates all K8s manifests.
5. **Runtime**: Launches a transient API and verifies `/health`, `/predict`, and `/metrics`.

### Usage

```bash
# Recommended (runs in project venv)
make validate

# Manual
python validation/release_check.py
```

## 📜 Legacy Validation (`validate_repo.py`)

Maintained for air-gapped or restricted environments. It provides "soft" verification (warnings) without enforcing Docker or Pipeline runs.
