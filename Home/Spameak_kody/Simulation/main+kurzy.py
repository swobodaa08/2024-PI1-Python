import random, time, math

# Funkcia na načítanie štatistík zo súboru
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

def vypocitaj_kurzy(staty1, staty2):
        EA = 1 / (1 + 10 ** ((staty2["elo"] - staty1["elo"]) / 400))
        EB = 1 / (1 + 10 ** ((staty1["elo"] - staty2["elo"]) / 400))
        kurz_1 = round(1 / EA, 2)
        kurz_2 = round(1 / EB, 2)
        if kurz_1 > 150:
            kurz_1 = 150
        if kurz_2 > 150:
            kurz_2 = 150
        kurz_X = round((kurz_1 + kurz_2) / 2, 2)
        return kurz_1, kurz_X, kurz_2

# Generovanie výsledku zápasu
def simuluj_zapas(tim1, tim2, staty1, staty2, delay=0.25):
    
    def vypocitaj_goly(elo1, elo2):
        EA = 1 / (1 + 10 ** ((elo2 - elo1) / 400))
        EB = 1 / (1 + 10 ** ((elo1 - elo2) / 400))
        vysledok = random.choices(
            population=["1", "X", "2"], weights=[EA, 0.1, EB], k=1
        )[0]

        if vysledok == "1":
            goly1 = random.randint(1, 6)
            goly2 = random.randint(0, goly1 - 1)
        elif vysledok == "2":
            goly2 = random.randint(1, 6)
            goly1 = random.randint(0, goly2 - 1)
        else:
            goly1 = goly2 = random.randint(0, 3)
        
        return goly1, goly2

    goly1, goly2 = vypocitaj_goly(staty1["elo"], staty2["elo"])

    zlute1 = random.randint(0, 6)
    zlute2 = random.randint(0, 6)
    cervene1 = 1 if random.random() < staty1["red"] / 100 else 0
    cervene2 = 1 if random.random() < staty2["red"] / 100 else 0

    def rozdel_minuty(pocet):
        return sorted(random.sample(range(1, 91), pocet))

    udalosti = []

    for m in rozdel_minuty(goly1):
        udalosti.append((m, f"⚽ Gól! {tim1} skóroval."))
    for m in rozdel_minuty(goly2):
        udalosti.append((m, f"⚽ Gól! {tim2} skóroval."))
    for m in rozdel_minuty(zlute1):
        udalosti.append((m, f"🟨 Žltá karta pre {tim1}"))
    for m in rozdel_minuty(zlute2):
        udalosti.append((m, f"🟨 Žltá karta pre {tim2}"))
    for m in rozdel_minuty(cervene1):
        udalosti.append((m, f"🟥 Červená karta pre {tim1}"))
    for m in rozdel_minuty(cervene2):
        udalosti.append((m, f"🟥 Červená karta pre {tim2}"))

    udalosti.sort()

    # Pridanie nadstaveného času
    nadstaveny_cas = random.randint(1, 8)


    print("\n🎮 Simulácia zápasu začína...\n")
    for minuta in range(1, 91 + nadstaveny_cas):
        if minuta == 90:
            print(f"🔁 Nadstavený čas: {nadstaveny_cas} minút")
        if minuta > 90:
            print(f"⏱️| 90+{minuta-90}. minúta")
        else:
            print(f"⏱️| {minuta}. minúta")
        for m, udalost in udalosti:
            if m == minuta:
                print("   " + udalost)
        time.sleep(delay)

    if goly1 > goly2:
        staty1["win"] += 1
        staty2["loss"] += 1
    elif goly2 > goly1:
        staty2["win"] += 1
        staty1["loss"] += 1
    else:
        staty1["draw"] += 1
        staty2["draw"] += 1

    staty1["goals_scored"] += goly1
    staty1["goals_conceded"] += goly2
    staty1["yellow"] += zlute1
    staty1["red"] += cervene1

    staty2["goals_scored"] += goly2
    staty2["goals_conceded"] += goly1
    staty2["yellow"] += zlute2
    staty2["red"] += cervene2

    strely1 = random.randint(5, 15) + goly1 - 1
    strely2 = random.randint(5, 15) + goly2 - 1
    na_branu1 = goly1 + random.randint(0, 4)
    na_branu2 = goly2 + random.randint(0, 4)
    drzanie1 = random.randint(51, 80) if staty1["elo"] > staty2["elo"] else random.randint(20, 49)
    drzanie2 = 100 - drzanie1
    rohy1 = random.randint(1, 6) + goly1
    rohy2 = random.randint(1, 6) + goly2
    offsides1 = random.randint(0, 4)
    offsides2 = random.randint(0, 4)
    fauly1 = random.randint(5, 15) + zlute1
    fauly2 = random.randint(5, 15) + zlute2

    print("\n🏁 Zápas skončil!\n")

    return {
        "výsledok": f"{tim1} {goly1} - {goly2} {tim2}",
        "skutocny_tip": "1" if goly1 > goly2 else "2" if goly2 > goly1 else "X",
        "štatistiky": {
            tim1: {
                "strely": strely1,
                "strely na bránu": na_branu1,
                "držanie lopty": drzanie1,
                "rohy": rohy1,
                "offsidy": offsides1,
                "fauly": fauly1,
                "žlté": zlute1, 
                "červené": cervene1
            },
            tim2: {
                "strely": strely2,
                "strely na bránu": na_branu2,
                "držanie lopty": drzanie2,
                "rohy": rohy2,
                "offsidy": offsides2,
                "fauly": fauly2,
                "žlté": zlute2, 
                "červené": cervene2
            }
        }
    }


# ======= HLAVNÝ PROGRAM ========
if __name__ == "__main__":
    konto = 10000
    timy = nacitaj_timove_statistiky("Home/Spameak_kody/Simulation/teams.txt")

    timy_zoznam = list(timy.keys())
    print("Dostupné tímy:")
    for idx, nazov in enumerate(timy_zoznam):
        print(f"{idx+1}. {nazov}")
    print(f"\nTvoj zostatok na účte: {konto}€\n--------------------------------\n")

    a = int(input("Vyber číslo prvého tímu: ")) - 1
    b = int(input("Vyber číslo druhého tímu: ")) - 1

    tim1, tim2 = timy_zoznam[a], timy_zoznam[b]

    kurz_1, kurz_X, kurz_2 = vypocitaj_kurzy(timy[tim1], timy[tim2])

    print("\n\n\n\n--------------------------------------------------- \n")
    print(f"Stav tvojho účtu je : {konto}€")
    print("                                                     ")
    print("\n---------------------------------------------------")
    print(f"{tim1} : {tim2}")
    print("                                                     ")
    print(f"1 (Vyhrá {tim1}) = {kurz_1}")
    print(f"X (Remíza) = {kurz_X}")
    print(f"2 (Vyhrá {tim2}) = {kurz_2}")
    print("---------------------------------------------------")
        
    # Používateľ zadá svoje tipy
    while True:
        tip_vysledok = input("Tipnite si víťaza (1, X alebo 2): ")
        if tip_vysledok in ["1", "X", "x", "2"]:
            break
        else:
            print("Zadaj prosím 1, X alebo 2.")

    while True:
            try:
                suma = float(input("Zadaj koľko € chceš vsadiť: "))
                if konto >= suma and 0.50 <= suma <= 10000:
                    break
                else:  
                    print("---------------------------------------------------")
                    print("Nieje možné vytvoriť stávku.. Uisti sa či je suma aspoň 50 centov, či nepresahuje 10000€ a či máš na stávku peniaze!")
                    print("---------------------------------------------------")
            except ValueError:
                print("Prosím, zadaj platnú sumu (číslo).")

    vysledok = simuluj_zapas(tim1, tim2, timy[tim1], timy[tim2])


    print("\n=== Výsledok zápasu ===")
    print(vysledok["výsledok"])
    print("\n=== Štatistiky ===")
    for tim, stats in vysledok["štatistiky"].items():
        print(f"{tim}:")
        for k, v in stats.items():
            print(f"  {k}: {v}")


    if tip_vysledok.upper() == vysledok["skutocny_tip"]:
        vyhra = round(suma * (kurz_1 if vysledok["skutocny_tip"] == "1" else kurz_X if vysledok["skutocny_tip"] == "X" else kurz_2), 2)
        konto += vyhra
        konto = round(konto, 2)
        print("----------------------------------------------------")
        print(f"Gratulujem! Vyhral/-a si {vyhra}€")
        print(f"Aktuálny zostatok na konte: {konto}€")
    else:   
        konto -= suma
        konto = round(konto, 2)
        print("----------------------------------------------------")
        print("Bohužiaľ, tvoja stávka nebola úspešná")
        print("----------------------------------------------------")
        print(f"Aktuálny zostatok na konte: {konto}€")

    
    zapis_timove_statistiky("Home/Spameak_kody/Simulation/teams.txt", timy)