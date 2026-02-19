# 🧠 Model Training

<div align="center">

![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![RandomForest](https://img.shields.io/badge/Algorithm-Random_Forest-green?style=for-the-badge)

**Training logic, hyperparameters, and experiment tracking.**

[⬅️ Back to Root](../README.md)

> [!TIP]
> **For Evaluators**: Training is automated via the DVC pipeline. See [Root README](../README.md) for execution instructions.

</div>

---

## 1. Algorithm Selection

We use a **Random Forest Regressor** for the following reasons:
1.  **Tabular Data Performance**: Excellent baselines for structured medical data.
2.  **Interpretability**: Feature importance is easily extracted.
3.  **Robustness**: Less prone to overfitting than single decision trees.

---

## 2. Training Script (`train.py`)

The script performs the following actions:
1.  Loads processed training data (`X_train.csv`, `y_train.csv`).
2.  Initializes the model using parameters from `params.yaml`.
3.  Fits the model (`model.fit()`).
4.  Serializes the model to `models/model.joblib`.
5.  Logs feature importances to stdout.

### Hyperparameters

| Parameter | Current Value | Source |
| :--- | :--- | :--- |
| `n_estimators` | `200` | `params.yaml` |
| `max_depth` | `15` | `params.yaml` |
| `min_samples_split` | `5` | `params.yaml` |
| `n_jobs` | `1` (Default) | Env Var `N_JOBS` |

---

## 3. Local Development

You can run the training script independently of DVC for debugging:

```bash
# Ensure you are in the virtual environment
source venv/bin/activate

# set necessary environment variables if needed
export N_JOBS=4

# Run script
python training/train.py
```

*Note: DVC is recommended for actual experiments to ensure reproducibility.*
