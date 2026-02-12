# Training

Model training and evaluation scripts.

## Scripts

| Script | Description |
|--------|-------------|
| `train.py` | Train RandomForestRegressor, save model artifact |
| `evaluate.py` | Evaluate on test set, generate metrics (RMSE, MAE, R²) |
| `tune.py` | Grid search hyperparameter tuning (RF + GradientBoosting) |

## Running

```bash
# Via DVC pipeline
dvc repro

# Manual
python training/train.py
python training/evaluate.py

# Tuning (manual, not in DVC pipeline)
python training/tune.py
```

## Model Details

- **Algorithm**: RandomForestRegressor
- **Random Seed**: 42 (fixed for reproducibility)
- **Hyperparameters**: Defined in `params.yaml`
