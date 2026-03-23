import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path

# Get project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent


def load_data():
    df = pd.read_csv(BASE_DIR / "data" / "vendor_invoice_sample.csv")
    return df


def prepare_features(df):
    # Basic features (simple and stable)
    X = df[['Dollars', 'Quantity']]
    y = df['Freight']
    return X, y


def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)