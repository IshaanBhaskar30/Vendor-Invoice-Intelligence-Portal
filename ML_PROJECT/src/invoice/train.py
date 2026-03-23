import joblib
from pathlib import Path
from sklearn.preprocessing import StandardScaler

from data_preprocessing import load_data, create_label, split_data
from feature_engineering import add_features
from model_evaluation import train_model, evaluate_model


def main():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    model_dir = BASE_DIR / "models"
    model_dir.mkdir(exist_ok=True)

    print("Loading data...")
    df = load_data()

    print("Creating labels...")
    df = create_label(df)

    print("Adding features...")
    df = add_features(df)

    FEATURES = [
    'Quantity',
    'Dollars',
    'total_item_quantity'
]

    TARGET = 'flag_invoice'

    X_train, X_test, y_train, y_test = split_data(df, FEATURES, TARGET)

    print("Scaling features...")
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Training model...")
    model = train_model(X_train, y_train)

    print("Evaluating model...")
    evaluate_model(model.best_estimator_, X_test, y_test)

    # Save model + scaler
    joblib.dump(model.best_estimator_, model_dir / "invoice_model.pkl")
    joblib.dump(scaler, model_dir / "scaler.pkl")

    print("\nModel and scaler saved.")


if __name__ == "__main__":
    main()