"""
Stage 1: Data Ingestion
-----------------------
Copies the raw dataset from data/raw/ to data/processed/ingested.csv
Validates file existence and basic integrity (non-empty, has rows).
"""

import os
import sys
import shutil
import yaml
import pandas as pd


def load_params():
    """Load pipeline parameters from params.yaml."""
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def main():
    params = load_params()
    raw_path = params["data"]["raw_path"]
    processed_dir = params["data"]["processed_dir"]
    output_path = os.path.join(processed_dir, "ingested.csv")

    # --- Validate source file exists ---
    if not os.path.exists(raw_path):
        print(f"ERROR: Raw data file not found: {raw_path}")
        sys.exit(1)

    # --- Validate file is non-empty ---
    file_size = os.path.getsize(raw_path)
    if file_size == 0:
        print(f"ERROR: Raw data file is empty: {raw_path}")
        sys.exit(1)

    # --- Load and validate row count ---
    df = pd.read_csv(raw_path)
    if len(df) == 0:
        print(f"ERROR: Raw data file has no data rows: {raw_path}")
        sys.exit(1)

    # --- Ensure output directory exists ---
    os.makedirs(processed_dir, exist_ok=True)

    # --- Copy to processed ---
    shutil.copy2(raw_path, output_path)

    print(f"✓ Ingestion complete: {len(df)} rows ingested from {raw_path}")
    print(f"  Output: {output_path}")
    print(f"  File size: {file_size:,} bytes")
    print(f"  Columns: {list(df.columns)}")


if __name__ == "__main__":
    main()
