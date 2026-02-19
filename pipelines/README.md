# ⚙️ Data Pipelines (DVC)

<div align="center">

![DVC](https://img.shields.io/badge/Orchestrator-DVC-945DD6?style=for-the-badge&logo=dvc&logoColor=white)
![DAG](https://img.shields.io/badge/Architecture-DAG-blue?style=for-the-badge)

**The production pipeline for reproducible model training.**

[⬅️ Back to Root](../README.md)

> [!TIP]
> **For Managers**: You can reproduce the entire pipeline by running `make run-pipeline` from the root directory.

</div>

---

## 1. The Pipeline DAG

The Directed Acyclic Graph (DAG) is defined in `dvc.yaml`. It ensures that every step is cached and only re-run if its dependencies (code or data) change.

```mermaid
graph LR
    Raw[Raw CSV] --> Ingest
    Ingest[ingest.py] --> Ingested[ingested.csv]
    Ingested --> Validate
    Validate[validate.py] --> Validated[validated.csv]
    Validated --> Preprocess
    Preprocess[preprocess.py] --> Train
    Preprocess --> Test[Test Set]
    Train[train.py] --> Model[model.joblib]
    Test --> Evaluate
    Model --> Evaluate
    Evaluate[evaluate.py] --> Metrics[scores.json]

    style Raw fill:#f9f,stroke:#333
    style Model fill:#f96,stroke:#333
    style Metrics fill:#ff9,stroke:#333
```

---

## 2. Stages & Artifacts

| Stage | Script | Input | Output | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Ingest** | `pipelines/ingest.py` | `raw/real_drug_dataset.csv` | `processed/ingested.csv` | Immutable copy of raw data. |
| **Validate** | `pipelines/validate.py` | `processed/ingested.csv` | `processed/validated.csv` | Schema enforcement. Fails pipeline on invalid data. |
| **Preprocess** | `pipelines/preprocess.py` | `processed/validated.csv` | `X_train`, `y_test`, etc. | Splitting (80/20) and Feature Engineering. |
| **Train** | `training/train.py` | `X_train.csv`, `y_train.csv` | `models/model.joblib` | Training RandomForestRegressor. |
| **Evaluate** | `training/evaluate.py` | `model.joblib`, `X_test.csv` | `metrics/scores.json` | Calculating RMSE/R². |

---

## 3. Configuration (`params.yaml`)

The pipeline execution is controlled by `params.yaml`. Key tuning parameters:

```yaml
model:
  n_estimators: 200     # Number of trees
  max_depth: 15         # Tree depth
  min_samples_split: 5  # Node split threshold
```

---

## 4. Usage

### Reproduce the Pipeline

To run the entire end-to-end flow:

```bash
dvc repro
```

### Run a Specific Stage

To run only the validation step (and its dependencies):

```bash
dvc repro validate
```

### Visualize the DAG

```bash
dvc dag
```
