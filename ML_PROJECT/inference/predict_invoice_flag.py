import joblib
import pandas as pd
from pathlib import Path
from src.invoice.feature_engineering import add_features

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "invoice_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"


def predict_invoice_flag(data):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    df = pd.DataFrame(data)


    FEATURES = [
    'Quantity',
    'Dollars',
    'total_item_quantity'
]

    df = df[FEATURES]

    # ✅ SAME scaling as training
    df_scaled = scaler.transform(df)

    df['Predicted_Flag'] = model.predict(df_scaled)

    return df