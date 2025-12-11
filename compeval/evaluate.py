import pandas as pd
import numpy as np
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error, root_mean_squared_error
)
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
import io

pred_path = "predictions_helt_på_jordet.csv"
fasit_enc_path = "test_fasit.enc"


def load_encrypted_fasit(enc_path):
    load_dotenv()
    key = os.getenv("FASIT_KEY")
    if key is None:
        raise RuntimeError("FASIT_KEY manglar i .env")

    fernet = Fernet(key.encode())

    with open(enc_path, "rb") as f:
        encrypted = f.read()

    decrypted = fernet.decrypt(encrypted)
    return pd.read_csv(io.BytesIO(decrypted))

def load_and_validate(pred_path, truth_path):
    # Load CSVs
    pred = pd.read_csv(pred_path)
    truth = load_encrypted_fasit(fasit_enc_path)

    # Required columns
    required_cols = {"id", "lonn"}

    if not required_cols.issubset(pred.columns):
        raise ValueError(f"{pred_path} må innehalde kolonnene {required_cols}")

    if not required_cols.issubset(truth.columns):
        raise ValueError(f"{truth_path} må innehalde kolonnene {required_cols}")

    # Check same number of rows
    if len(pred) != len(truth):
        raise ValueError(
            f"Ulikt tal rader: "
            f"{pred_path}={len(pred)}, {truth_path}={len(truth)}"
        )

    # Sort by id to be safe
    pred = pred.sort_values("id").reset_index(drop=True)
    truth = truth.sort_values("id").reset_index(drop=True)

    # Check IDs match exactly
    if not pred["id"].equals(truth["id"]):
        raise ValueError("ID-ar samsvarar ikkje mellom filene")

    # Check for missing values
    if pred.isna().any().any():
        raise ValueError("Manglande verdiar funne i predictions.csv")

    if truth.isna().any().any():
        raise ValueError("Manglande verdiar funne i test_fasit.csv")

    return pred["lonn"], truth["lonn"]


def regression_metrics(y_true, y_pred):
    return {
        "R2": r2_score(y_true, y_pred),
        "MAE": mean_absolute_error(y_true, y_pred),
        "MSE": mean_squared_error(y_true, y_pred),
        "RMSE": root_mean_squared_error(y_true, y_pred),
        "MAPE (%)": np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    }

y_pred, y_true = load_and_validate(pred_path, fasit_enc_path)
metrics = regression_metrics(y_true, y_pred)

print("\n✅ Datavalidering OK")
print("📊 Evaluering av prediksjonar")
print("-" * 40)

for k, v in metrics.items():
    if k == "R2":
        print(f"{k:10s}: {v:.4f}")
    else:
        print(f"{k:10s}: {v:,.0f}")

print(f"\nTal observasjonar: {len(y_true)}")


