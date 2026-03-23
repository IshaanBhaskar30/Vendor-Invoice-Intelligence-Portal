import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def load_data():
    df = pd.read_csv(BASE_DIR / "data" / "vendor_invoice_sample.csv")
    return df


def create_label(df):
    df = df.copy()

    def flag(row):
        score = 0

        # softer conditions (not strict rules)
        if abs(row['Dollars'] - row['total_item_dollars']) / row['total_item_dollars'] > 0.08:
            score += 1

        if row['avg_receiving_delay'] > 12:
            score += 1

        if row['Freight'] / row['Dollars'] > 0.12:
            score += 1

        # probabilistic labeling (IMPORTANT)
        if score >= 2:
            return 1 if np.random.rand() > 0.2 else 0   # 80% chance
        else:
            return 1 if np.random.rand() < 0.1 else 0   # 10% noise

    df['flag_invoice'] = df.apply(flag, axis=1)

    return df


def split_data(df, features, target):
    X = df[features]
    y = df[target]

    return train_test_split(X, y, test_size=0.2, random_state=42)