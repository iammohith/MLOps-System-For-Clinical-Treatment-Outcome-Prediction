"""
Hyperparameter Tuning
---------------------
Grid search over RandomForest hyperparameters.
Reports best parameters and cross-validation scores.
This is run manually, not as part of the DVC pipeline.

Usage:
    python training/tune.py
"""

import os
import sys
import yaml
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, mean_squared_error


def load_params():
    """Load pipeline parameters from params.yaml."""
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def rmse_scorer(y_true, y_pred):
    """Custom RMSE scorer for GridSearchCV."""
    return -np.sqrt(mean_squared_error(y_true, y_pred))


def main():
    params = load_params()
    processed_dir = params["data"]["processed_dir"]
    random_seed = params["random_seed"]

    # --- Load training data ---
    X_train = pd.read_csv(os.path.join(processed_dir, "X_train.csv"))
    y_train = pd.read_csv(os.path.join(processed_dir, "y_train.csv")).values.ravel()

    print(f"Tuning on {X_train.shape[0]} samples, {X_train.shape[1]} features...")

    # --- Define parameter grids ---
    rf_param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [10, 15, 20, None],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
    }

    gb_param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [3, 5, 7],
        "learning_rate": [0.01, 0.05, 0.1],
        "min_samples_split": [2, 5],
    }

    scorer = make_scorer(rmse_scorer, greater_is_better=True)

    # --- RandomForest Grid Search ---
    print("\n--- RandomForest Grid Search ---")
    rf = RandomForestRegressor(random_state=random_seed, n_jobs=-1)
    rf_search = GridSearchCV(
        rf, rf_param_grid, cv=5, scoring=scorer, n_jobs=-1, verbose=1
    )
    rf_search.fit(X_train, y_train)

    print(f"Best RF RMSE: {-rf_search.best_score_:.4f}")
    print(f"Best RF params: {rf_search.best_params_}")

    # --- GradientBoosting Grid Search ---
    print("\n--- GradientBoosting Grid Search ---")
    gb = GradientBoostingRegressor(random_state=random_seed)
    gb_search = GridSearchCV(
        gb, gb_param_grid, cv=5, scoring=scorer, n_jobs=-1, verbose=1
    )
    gb_search.fit(X_train, y_train)

    print(f"Best GB RMSE: {-gb_search.best_score_:.4f}")
    print(f"Best GB params: {gb_search.best_params_}")

    # --- Compare ---
    print("\n--- Summary ---")
    print(f"RandomForest best RMSE:      {-rf_search.best_score_:.4f}")
    print(f"GradientBoosting best RMSE:  {-gb_search.best_score_:.4f}")

    if -rf_search.best_score_ < -gb_search.best_score_:
        print("→ RandomForest wins! Update params.yaml with:")
        print(f"  {rf_search.best_params_}")
    else:
        print("→ GradientBoosting wins! Consider switching model in params.yaml.")
        print(f"  {gb_search.best_params_}")


if __name__ == "__main__":
    main()
