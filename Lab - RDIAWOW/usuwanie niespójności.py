import pandas as pd
from fontTools.misc.psCharStrings import read_byte
from pandas import read_csv


def remove_inconsistencies(df, decision_col='decision'):
    # Grupowanie wierszy na podstawie atrybutów (bez decyzji)
    attributes = df.columns.difference([decision_col])
    grouped = df.groupby(list(attributes))

    # Znajdowanie niezgodnych grup
    inconsistent_indices = []
    for _, group in grouped:
        # Sprawdź, czy w grupie występują różne wartości decyzji
        if group[decision_col].nunique() > 1:
            # display(group)

            # Znajdź wsparcie dla każdej decyzji w grupie
            decision_counts = group[decision_col].value_counts()
            # display(decision_counts)

            # Znajdź decyzję o największym wsparciu
            max_support_decision = decision_counts.idxmax()
            # Dodaj do listy indeksy wierszy z mniejszym wsparciem (do usunięcia)
            inconsistent_indices.extend(group[group[decision_col] != max_support_decision].index)

    # Usuń wiersze z niezgodnymi decyzjami o mniejszym wsparciu
    df_cleaned = df.drop(inconsistent_indices)

    # Usuń duplikaty
    df_cleaned = df_cleaned.drop_duplicates()

    return df_cleaned



data = read_csv("WATER_POTABILITY.csv",sep=';')
cleaned_data = remove_inconsistencies(data, decision_col='Potability')
cleaned_data.to_csv("WATER_POTABILITY_CLEANED.csv", index=False, sep=';')
print("Tablica po usunięciu niespójności i duplikatów:")
print(cleaned_data)