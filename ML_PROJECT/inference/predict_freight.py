import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "freight_model.pkl"


def predict_freight(data):
    model = joblib.load(MODEL_PATH)

    df = pd.DataFrame(data)
    df['Predicted_Freight'] = model.predict(df)

    return df