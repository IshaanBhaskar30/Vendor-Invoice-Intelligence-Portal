import joblib
from pathlib import Path

from data_preprocessing import load_data, prepare_features, split_data
from model_evaluation import train_models, evaluate_models


def main():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    model_dir = BASE_DIR / "models"
    model_dir.mkdir(exist_ok=True)

    print("Loading data...")
    df = load_data()

    print("Preparing features...")
    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    print("Training models...")
    models = train_models(X_train, y_train)

    print("Evaluating models...")
    results = evaluate_models(models, X_test, y_test)

    # Select best model (lowest MAE)
    best_model_name = min(results, key=lambda x: x['mae'])['model']
    best_model = models[best_model_name]

    # Save model
    model_path = model_dir / "freight_model.pkl"
    joblib.dump(best_model, model_path)

    print("\nBest Model:", best_model_name)
    print("Saved at:", model_path)


if __name__ == "__main__":
    main()