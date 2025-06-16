import random, time

# ===================== ŠTATISTIKY A ZÁKLADNÁ SIMULÁCIA =====================

def nacitaj_timove_statistiky(subor):
    with open(subor, 'r', encoding='utf-8') as f:
        data = f.read().strip().split("\n\n")
    timy = {}
    for blok in data:
        riadky = blok.strip().split("\n")
        tim = {}
        for riadok in riadky:
            kluc, hodnota = riadok.split(":")
            tim[kluc.strip()] = hodnota.strip()
        nazov = tim.pop("Team")
        tim = {k: int(v) for k, v in tim.items()}
        timy[nazov] = tim
    return timy

def zapis_timove_statistiky(subor, timy):
    with open(subor, 'w', encoding='utf-8') as f:
        for nazov, data in timy.items():
            f.write(f"Team: {nazov}\n")
            for k, v in data.items():
                f.write(f"{k}: {v}\n")
            f.write("\n")

def simuluj_zapas(tim1, tim2, staty1, staty2):
    def vypocitaj_goly(utok, obrana):
        zaklad = random.gauss(utok / 10, 1)
        efektivne = max(0, int(zaklad - obrana / 30 + random.uniform(-1, 1)))
        return efektivne

    goly1 = vypocitaj_goly(staty1["goals_scored"], staty2["goals_conceded"])
    goly2 = vypocitaj_goly(staty2["goals_scored"], staty1["goals_conceded"])

    if goly1 > goly2:
        vysledok = "1"
    elif goly1 < goly2:
        vysledok = "2"
    else:
        vysledok = "X"

    return vysledok, goly1, goly2

# ===================== TIPOVANIE =====================

def vypocitaj_kurzy(elo1, elo2):
    EA = 1 / (1 + 10 ** ((elo2 - elo1) / 400))
    EB = 1 / (1 + 10 ** ((elo1 - elo2) / 400))
    kurz_1 = round(1 / EA, 2)
    kurz_2 = round(1 / EB, 2)
    kurz_X = round((kurz_1 + kurz_2) / 2, 2)
    return kurz_1, kurz_X, kurz_2

# ===================== HLAVNÝ PROGRAM =====================

def hlavny_program():
    timy = nacitaj_timove_statistiky("Home/Spameak_kody/Simulation/teams.txt")
    timy_zoznam = list(timy.keys())

    konto = 100.0
    casino = 10000.0

    for i in range(3):  # 3 kolá
        print(f"\nKolo {i + 1} z 3")
        tim1, tim2 = random.sample(timy_zoznam, 2)
        staty1, staty2 = timy[tim1], timy[tim2]

        kurz_1, kurz_X, kurz_2 = vypocitaj_kurzy(staty1['elo'], staty2['elo'])

        print("---------------------------------------------------")
        print(f"Zápas: {tim1} vs {tim2}")
        print(f"1 (Výhra {tim1}) = {kurz_1}")
        print(f"X (Remíza) = {kurz_X}")
        print(f"2 (Výhra {tim2}) = {kurz_2}")
        print(f"Zostatok: {konto}€")
        print("---------------------------------------------------")

        while True:
            tip = input("Zadaj svoj tip (1, X, 2): ").upper()
            if tip in ["1", "X", "2"]:
                break

        while True:
            try:
                suma = float(input("Koľko chceš vsadiť? "))
                if 0.5 <= suma <= konto:
                    break
            except ValueError:
                continue

        vysledok, goly1, goly2 = simuluj_zapas(tim1, tim2, staty1, staty2)
        print(f"Výsledok: {tim1} {goly1}:{goly2} {tim2} => {vysledok}")

        if tip == vysledok:
            vyhra = suma * (kurz_1 if tip == "1" else kurz_2 if tip == "2" else kurz_X)
            konto += round(vyhra - suma, 2)
            casino -= vyhra
            print(f"✔️ Vyhral si {round(vyhra, 2)}€!")
        else:
            konto -= suma
            casino += suma
            print("❌ Tip nevyšiel. Smola!")

    print(f"\n💰 Finálny stav účtu: {konto}€")

if __name__ == "__main__":
    hlavny_program()
