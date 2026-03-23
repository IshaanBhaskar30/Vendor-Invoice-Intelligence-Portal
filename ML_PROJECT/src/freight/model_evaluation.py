from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def train_models(X_train, y_train):
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(random_state=42)
    }

    trained_models = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model

    return trained_models


def evaluate_models(models, X_test, y_test):
    results = []

    for name, model in models.items():
        preds = model.predict(X_test)

        results.append({
            "model": name,
            "mae": mean_absolute_error(y_test, preds),
            "rmse": mean_squared_error(y_test, preds, squared=False),
            "r2": r2_score(y_test, preds)
        })

        print(f"\n{name} Performance")
        print("MAE:", results[-1]['mae'])
        print("RMSE:", results[-1]['rmse'])
        print("R2:", results[-1]['r2'])

    return results