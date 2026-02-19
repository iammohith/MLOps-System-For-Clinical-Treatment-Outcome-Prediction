# 📈 Evaluation Metrics

<div align="center">

![JSON](https://img.shields.io/badge/Format-JSON-black?style=for-the-badge&logo=json&logoColor=white)
![DVC](https://img.shields.io/badge/Tracked_by-DVC-945DD6?style=for-the-badge&logo=dvc&logoColor=white)

**Performance KPIs for the Treatment Outcome Model.**

[⬅️ Back to Root](../README.md)

</div>

---

## 1. Overview

We track regression metrics to evaluate model performance to ensure it meets clinical standards before deployment. These metrics are calculated by `training/evaluate.py` on the held-out test set (`data/processed/*_test.csv`).

The results are saved to `metrics/scores.json`, which is tracked by DVC.

---

## 2. Metric Definitions

| Metric | Full Name | Goal | Description |
| :--- | :--- | :--- | :--- |
| **RMSE** | Root Mean Squared Error | **Minimize** | Penalizes large errors heavily. The standard deviation of the residuals. |
| **MAE** | Mean Absolute Error | **Minimize** | Average absolute difference between predicted and actual improvement score. |
| **R²** | Coefficient of Determination | **Maximize** (-> 1.0) | Proportion of variance explained by the model. |

---

## 3. Metrics File Schema (`scores.json`)

```json
{
  "rmse": 6.12,
  "mae": 4.5,
  "r2": 0.05
}
```

> [!NOTE]
> **Synthetic Data Warning**: The current dataset is synthetic/demo data. Do not expect high R² values (e.g., > 0.8) as the signal-to-noise ratio is intentionally challenging. Negative R² values are possible if the model performs worse than a simple mean baseline.

---

## 4. DVC Integration

To see the difference in metrics between the current experiment and the main branch:

```bash
dvc metrics diff --show-json
```

To show current metrics:

```bash
dvc metrics show
```
