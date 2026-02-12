"""
Stage 3: Data Preprocessing
----------------------------
- Drops Patient_ID (not a predictive feature)
- One-hot encodes categorical features (Gender, Condition, Drug_Name, Side_Effects)
- Scales numeric features (Age, Dosage_mg, Treatment_Duration_days)
- Splits into train/test sets
- Saves preprocessor pipeline as .joblib for inference reuse
"""

import os
import sys
import yaml
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib


def load_params():
    """Load pipeline parameters from params.yaml."""
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def main():
    params = load_params()
    processed_dir = params["data"]["processed_dir"]
    random_seed = params["random_seed"]
    test_split = params["test_split"]
    features = params["features"]

    input_path = os.path.join(processed_dir, "validated.csv")

    # --- Load data ---
    if not os.path.exists(input_path):
        print(f"ERROR: Input file not found: {input_path}")
        sys.exit(1)

    df = pd.read_csv(input_path)
    print(f"Preprocessing {len(df)} rows...")

    # --- Separate target and features ---
    target_col = features["target"]
    id_col = features["id_column"]
    numeric_cols = features["numeric"]
    categorical_cols = features["categorical"]

    y = df[target_col].values
    X = df.drop(columns=[target_col, id_col])

    # --- Build preprocessor pipeline ---
    numeric_transformer = Pipeline(
        steps=[("scaler", StandardScaler())]
    )

    categorical_transformer = Pipeline(
        steps=[("onehot", OneHotEncoder(handle_unknown="error", sparse_output=False))]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_cols),
            ("cat", categorical_transformer, categorical_cols),
        ],
        remainder="drop",
    )

    # --- Split data ---
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_split, random_state=random_seed
    )

    # --- Fit preprocessor on training data only ---
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    # --- Get feature names after transformation ---
    feature_names = (
        numeric_cols
        + list(preprocessor.named_transformers_["cat"]
               .named_steps["onehot"]
               .get_feature_names_out(categorical_cols))
    )

    # --- Save processed data ---
    pd.DataFrame(X_train_processed, columns=feature_names).to_csv(
        os.path.join(processed_dir, "X_train.csv"), index=False
    )
    pd.DataFrame(X_test_processed, columns=feature_names).to_csv(
        os.path.join(processed_dir, "X_test.csv"), index=False
    )
    pd.DataFrame(y_train, columns=[target_col]).to_csv(
        os.path.join(processed_dir, "y_train.csv"), index=False
    )
    pd.DataFrame(y_test, columns=[target_col]).to_csv(
        os.path.join(processed_dir, "y_test.csv"), index=False
    )

    # --- Save preprocessor ---
    preprocessor_path = os.path.join(processed_dir, "preprocessor.joblib")
    joblib.dump(preprocessor, preprocessor_path)

    print(f"✓ Preprocessing complete:")
    print(f"  Train set: {X_train_processed.shape[0]} rows, {X_train_processed.shape[1]} features")
    print(f"  Test set: {X_test_processed.shape[0]} rows, {X_test_processed.shape[1]} features")
    print(f"  Feature names: {feature_names}")
    print(f"  Preprocessor saved: {preprocessor_path}")


if __name__ == "__main__":
    main()
