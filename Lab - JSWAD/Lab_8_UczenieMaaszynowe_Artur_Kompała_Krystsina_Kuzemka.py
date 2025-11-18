import numpy as np
import pandas as pd
from catboost import CatBoostClassifier

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score


def main():
    # Wczytanie danych treningowych
    train = pd.read_csv("train.csv")

    # Podział na X (cechy) i y (target)
    y = train["loan_paid_back"].astype(int)
    X = train.drop(columns=["loan_paid_back", "id"])

    # Rozpoznanie typów kolumn
    numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_cols = X.select_dtypes(include=["object"]).columns.tolist()

    # Preprocessing:
    #  liczby: bez zmian
    #  kategorie: OrdinalEncoder (u nas każda kategoria dostaje numer)
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", numeric_cols),
            (
                "cat",
                OrdinalEncoder(
                    handle_unknown="use_encoded_value",
                    unknown_value=-1
                ),
                cat_cols,
            ),
        ]
    )

    # Model: CatBoostClassifier
    model = CatBoostClassifier(
        verbose=False
    )

    # Pipeline: preprocessing + model
    clf = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", model),
        ]
    )

    # Walidacja krzyżowa na zbiorze treningowym (AUC)
    skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
    oof_pred = np.zeros(len(X), dtype=float)

    print("Walidacja krzyżowa (3-fold, metryka: ROC AUC)")
    fold_idx = 1
    for train_idx, valid_idx in skf.split(X, y):
        X_train_fold = X.iloc[train_idx]
        y_train_fold = y.iloc[train_idx]
        X_valid_fold = X.iloc[valid_idx]
        y_valid_fold = y.iloc[valid_idx]

        clf.fit(X_train_fold, y_train_fold)
        proba_valid = clf.predict_proba(X_valid_fold)[:, 1]

        oof_pred[valid_idx] = proba_valid

        fold_auc = roc_auc_score(y_valid_fold, proba_valid)
        print(f"Fold {fold_idx} AUC: {fold_auc:.4f}")
        fold_idx += 1

    full_auc = roc_auc_score(y, oof_pred)
    print(f"Średni AUC (OOF): {full_auc:.4f}")

    # Trenowanie finalnego modelu na całym zbiorze treningowym
    clf.fit(X, y)

    # Próba obsługi zbioru testowego (to jest odrazu dla Pana, kiedy już będzie zbiór testowy)
    try:
        test = pd.read_csv("test.csv")
        X_test = test.drop(columns=["id"])

        proba_test = clf.predict_proba(X_test)[:, 1]

        # Zaokrąglenie prawdopodobieństwa do 1 miejsca po przecinku
        proba_test_rounded = np.round(proba_test, 1)

        submission = pd.DataFrame({
            "id": test["id"],
            "loan_paid_back": proba_test_rounded
        })

        submission.to_csv("przewidywania.csv", index=False)
        print("Zapisano plik z przewidywanymi prawdopodobieństwami")
    except FileNotFoundError:
        # To dla nas - bo odpalamy kod tylko z train.csv
        print("Brak pliku test.csv, pomijam generowanie przewidywania.csv.")


main()