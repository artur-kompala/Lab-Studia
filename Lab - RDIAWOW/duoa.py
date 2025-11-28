import pandas as pd
import itertools

# 1. Wczytanie Twojego zbioru (taki sam csv jak do RSES – po dyskretyzacji)
df = pd.read_csv("WATER_POTABILITY.csv",sep=';')

# Dostosuj nazwy kolumn do tego, co naprawdę masz w pliku:
cond_attrs = ['ph', 'Hardness', 'Solids', 'Chloramines',
              'Sulfate', 'Conductivity', 'Organic_carbon',
              'Trihalomethanes', 'Turbidity']
dec_attr = 'Potability'

# 2. Funkcja: sprawdza, czy dany podzbiór atrybutów jest reduktem
def is_reduct(attrs):
    # dla każdej kombinacji wartości attrs sprawdzamy,
    # czy decyzja jest jednoznaczna (max 1 unikalna wartość)
    grp = df.groupby(list(attrs))[dec_attr].nunique()
    # brak konfliktów decyzji
    if (grp > 1).any():
        return False
    # minimalność: żaden właściwy podzbiór nie ma tej własności
    for r in range(1, len(attrs)):
        for sub in itertools.combinations(attrs, r):
            gsub = df.groupby(list(sub))[dec_attr].nunique()
            if not (gsub > 1).any():  # podzbiór też bez konfliktów
                return False
    return True

# 3. Szukanie reduktów – UWAGA: kombinatoryka; przy 9 atrybutach może być wolne
reducts = []
for k in range(1, len(cond_attrs)+1):
    for comb in itertools.combinations(cond_attrs, k):
        if is_reduct(comb):
            reducts.append(comb)
    if reducts:
        break  # znalazłeś minimalne – dalsze (większe) już nie są potrzebne

print("Znalezione (przybliżone) redukty:")
for r in reducts:
    print(r)
