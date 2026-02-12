"""
Stage 4: Model Training
------------------------
Trains a RandomForestRegressor on preprocessed data.
Uses fixed random seed for reproducibility.
Saves model artifact and logs feature importances.
"""

import os
import sys
import yaml
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib


def load_params():
    """Load pipeline parameters from params.yaml."""
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def main():
    params = load_params()
    processed_dir = params["data"]["processed_dir"]
    model_dir = params["data"]["model_dir"]
    random_seed = params["random_seed"]
    model_params = params["model"]

    # --- Load training data ---
    X_train_path = os.path.join(processed_dir, "X_train.csv")
    y_train_path = os.path.join(processed_dir, "y_train.csv")

    if not os.path.exists(X_train_path) or not os.path.exists(y_train_path):
        print("ERROR: Training data not found. Run preprocessing first.")
        sys.exit(1)

    X_train = pd.read_csv(X_train_path)
    y_train = pd.read_csv(y_train_path).values.ravel()

    print(f"Training on {X_train.shape[0]} samples, {X_train.shape[1]} features...")

    # --- Train model ---
    model = RandomForestRegressor(
        n_estimators=model_params["n_estimators"],
        max_depth=model_params["max_depth"],
        min_samples_split=model_params["min_samples_split"],
        min_samples_leaf=model_params["min_samples_leaf"],
        random_state=random_seed,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    # --- Log feature importances ---
    feature_names = list(X_train.columns)
    importances = model.feature_importances_
    sorted_idx = np.argsort(importances)[::-1]

    print("\nTop 10 Feature Importances:")
    for i in range(min(10, len(sorted_idx))):
        idx = sorted_idx[i]
        print(f"  {feature_names[idx]}: {importances[idx]:.4f}")

    # --- Save model ---
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    joblib.dump(model, model_path)

    print(f"\n✓ Training complete:")
    print(f"  Model: RandomForestRegressor")
    print(f"  n_estimators: {model_params['n_estimators']}")
    print(f"  max_depth: {model_params['max_depth']}")
    print(f"  Model saved: {model_path}")


if __name__ == "__main__":
    main()
