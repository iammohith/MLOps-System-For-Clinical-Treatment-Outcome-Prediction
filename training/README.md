# Model Training & Evaluation

This directory contains the core logic for generating clinical outcome predictions.

## 🧬 Algorithm & Determinism

* **Algorithm**: `RandomForestRegressor` (Scikit-learn)
* **Determinism**: Enforced via `random_seed: 42` in `params.yaml`.
* **Target**: `Improvement_Score` (Continuous 0–10).

## 📄 Components

| File | Role | Verification Indicator |
| :--- | :--- | :--- |
| `train.py` | Training Stage | Generates `models/model.joblib` |
| `evaluate.py` | Evaluation Stage | Updates `metrics/scores.json` |
| `tune.py` | Manual Tuning | Console output of best hyperparams |

## 🏃 Instructions

```bash
# Run full training lifecycle
dvc repro train

# Verify metrics
cat metrics/scores.json
```

## ⚠️ Failure Modes

* **Data Skew**: If the input features in `data/processed/` change without re-running preprocessing, `train.py` will fail with a shape mismatch.
* **Memory Errors**: Small VM instances may struggle with 200 estimators. Adjust `n_estimators` in `params.yaml` if needed.
