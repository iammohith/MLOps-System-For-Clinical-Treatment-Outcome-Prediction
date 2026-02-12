# Pipelines

Data processing pipeline stages for the DVC pipeline.

## Stages

| Stage | Script | Input | Output |
|-------|--------|-------|--------|
| **Ingest** | `ingest.py` | `data/raw/real_drug_dataset.csv` | `data/processed/ingested.csv` |
| **Validate** | `validate.py` | `ingested.csv` | `validated.csv` |
| **Preprocess** | `preprocess.py` | `validated.csv` | `X_train.csv`, `X_test.csv`, `y_train.csv`, `y_test.csv`, `preprocessor.joblib` |

## Running

```bash
# Via DVC (recommended)
dvc repro

# Individual stages
python pipelines/ingest.py
python pipelines/validate.py
python pipelines/preprocess.py
```
