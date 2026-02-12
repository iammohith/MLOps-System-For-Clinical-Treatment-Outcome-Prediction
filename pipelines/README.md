# Data Pipeline Stages

Modular Python scripts that define the first three stages of the DVC lifecycle.

## 🛠️ Pipeline Roles

1. **Ingest** (`ingest.py`): Extracts raw CSV and performs a basic record count audit.
2. **Validate** (`validate.py`): Performs a strict schema check against `params.yaml`. Drops malformed rows.
3. **Preprocess** (`preprocess.py`): Engages feature engineering (encoding, scaling) and generates the `preprocessor.joblib` artifact required by the inference service.

## 🏃 Execution

These stages are designed to be run via DVC:

```bash
dvc repro ingest
dvc repro validate
dvc repro preprocess
```

## 🚫 Critical Constraints

* **Schema Sync**: These scripts depend on `params.yaml`. Changing a column name in the CSV without updating `params.yaml` will break the **Validate** stage.
* **Stateful Output**: All outputs are written to `data/processed/`. Ensure this directory is writable.
