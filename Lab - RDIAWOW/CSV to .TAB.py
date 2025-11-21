import re

def csv_to_rses_tab(filepath):
    with open(filepath, "r") as f1:
        # Odczytaj nagłówki
        header = f1.readline().strip().split(';')
        header = [x.replace(' ', '_').replace('"', '') for x in header]

        tab_filepath = filepath[:-4] + '.tab'

        with open(tab_filepath, "w") as f2:
            f2.write(f"TABLE {filepath[:-4]}\n")
            f2.write(f"ATTRIBUTES {len(header)}\n")

            # Atrybuty (ostatni = klasa)
            for i, column in enumerate(header):
                if i == len(header) - 1:
                    f2.write(f"{column} symbolic\n")  # klasa
                else:
                    f2.write(f"{column} symbolic\n")  # albo numeric

            # Odczytaj wszystkie wiersze
            lines = f1.readlines()
            f2.write(f"OBJECTS {len(lines)}\n")

            for line in lines:
                line = line.strip()

                # usuń cudzysłowy
                line = line.replace('"', '')

                # zamień średniki na spacje
                line = line.replace(';', ' ')

                # zamiana True/False na 1/0
                line = re.sub(r'\bTrue\b', '1', line)
                line = re.sub(r'\bFalse\b', '0', line)

                f2.write(line + '\n')

    print(f'Plik {tab_filepath} został utworzony.')

csv_to_rses_tab('WATER_POTABILITY.csv')