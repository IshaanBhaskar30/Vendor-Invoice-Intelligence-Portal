from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report


def train_model(X_train, y_train):
    rf = RandomForestClassifier(random_state=42, class_weight='balanced')

    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 5]
    }

    grid = GridSearchCV(
        rf,
        param_grid,
        cv=3,
        scoring='f1',
        n_jobs=-1
    )

    grid.fit(X_train, y_train)

    return grid


def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)

    print("\nClassification Report:\n")
    print(classification_report(y_test, preds))