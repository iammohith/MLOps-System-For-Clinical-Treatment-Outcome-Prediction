# Data Management

This directory manages the lifecycle of clinical treatment records. All data transitions are enforced by the DVC pipeline defined in `dvc.yaml`.

## 📂 Structure & Enforcement

| Path | Enforcement | Purpose |
| :--- | :--- | :--- |
| `raw/real_drug_dataset.csv` | **DVC Tracked** | Immutable source (1,000 patient records). |
| `processed/preprocessor.joblib` | **Pipeline Generated** | Scikit-learn transformer for inference encoding. |
| `processed/X_train.csv` | **Pipeline Generated** | Encoded features for Stage 4 training. |
| `processed/y_train.csv` | **Pipeline Generated** | Target labels for Stage 4 training. |

## 📜 Data Contract (params.yaml)

The system operates on an exact schema contract. Any deviation during `make run-pipeline` or `/predict` runtime will result in a hard failure.

| Feature | Range/Values | Role |
| :--- | :--- | :--- |
| **Age** | 18–79 | Numeric Feature |
| **Gender** | Female, Male | Categorical Feature |
| **Dosage_mg** | 50, 100, 250, 500, 850 | Numeric Feature |
| **Side_Effects** | 30 unique reports | Categorical Feature |
| **Improvement_Score** | 0.0–10.0 | **Target Variable** |

## 🔧 Recovery

If processed files are corrupted, run:

```bash
rm -rf data/processed/* && dvc repro
```
