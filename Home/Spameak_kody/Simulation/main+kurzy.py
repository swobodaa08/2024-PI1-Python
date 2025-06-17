import random, time, math
import numpy as np

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

# def vypocitaj_kurzy(staty1, staty2):
#         EA = 1 / (1 + 10 ** ((staty2["elo"] - staty1["elo"]) / 400))
#         EB = 1 / (1 + 10 ** ((staty1["elo"] - staty2["elo"]) / 400))
#         kurz_1 = round(1 / EA, 2)
#         kurz_2 = round(1 / EB, 2)
#         if kurz_1 > 150:
#             kurz_1 = 150
#         if kurz_2 > 150:
#             kurz_2 = 150
#         exp_1 = 0.5 if (staty1["elo"] / 150) < 1 else (staty1["elo"] / 250)
#         exp_2 = 0.5 if (staty2["elo"] / 150) < 1 else (staty2["elo"] / 250)
#         exp_both = exp_1 + exp_2
#         kurz_over05 = 1.00 if 1 / (exp_both) < 1 else 1 / (exp_both)
#         kurz_over15 = 1.00 if 2 / (exp_both) < 1 else 2 / (exp_both)
#         kurz_over25 = 1.00 if 3 / (exp_both) < 1 else 3 / (exp_both)
#         kurz_over35 = 1.00 if 4 / (exp_both) < 1 else 4 / (exp_both)
#         kurz_over45 = 1.00 if 5 / (exp_both) < 1 else 5 / (exp_both)
#         kurz_over55 = 1.00 if 6 / (exp_both) < 1 else 6 / (exp_both)
#         kurz_over65 = 1.00 if 7 / (exp_both) < 1 else 7 / (exp_both)
#         kurz_over75 = 1.00 if 8 / (exp_both) < 1 else 8 / (exp_both)
#         kurz_over85 = 1.00 if 9 / (exp_both) < 1 else 9 / (exp_both)
#         kurz_over95 = 1.00 if 10 / (exp_both) < 1 else 10 / (exp_both)
#         kurz_X = round((kurz_1 + kurz_2) / 2, 2)
#         return kurz_1, kurz_X, kurz_2, kurz_over05, kurz_over15, kurz_over25, kurz_over35, kurz_over45, kurz_over55, kurz_over65, kurz_over75, kurz_over85, kurz_over95

# def vypocitaj_kurzy(staty1, staty2):
#     # ELO pravdepodobnosti výhry
#     EA = 1 / (1 + 10 ** ((staty2["elo"] - staty1["elo"]) / 400))
#     EB = 1 / (1 + 10 ** ((staty1["elo"] - staty2["elo"]) / 400))
    
#     kurz_1 = min(round(1 / EA, 2), 150)
#     kurz_2 = min(round(1 / EB, 2), 150)
#     kurz_X = round((kurz_1 + kurz_2) / 2, 2)

#     # --- Očakávané góly podľa ELO a útočnej sily
#     max_elo = 1000  # škálovanie
#     attack1 = staty1["goals_scored"] / max(staty1["win"] + staty1["draw"] + staty1["loss"], 1)
#     attack2 = staty2["goals_scored"] / max(staty2["win"] + staty2["draw"] + staty2["loss"], 1)
#     def_ratio1 = staty1["goals_conceded"] / max(staty1["win"] + staty1["draw"] + staty1["loss"], 1)
#     def_ratio2 = staty2["goals_conceded"] / max(staty2["win"] + staty2["draw"] + staty2["loss"], 1)

#     # ELO faktor medzi 0.1 a 2.0 (čím väčšie ELO, tým silnejší tím)
#     elo_factor1 = 0.1 + 1.9 * (staty1["elo"] / max_elo)
#     elo_factor2 = 0.1 + 1.9 * (staty2["elo"] / max_elo)

#     # Výpočet očakávaných gólov
#     exp_1 = attack1 * (def_ratio2 / 2 + 0.5) * elo_factor1 / elo_factor2
#     exp_2 = attack2 * (def_ratio1 / 2 + 0.5) * elo_factor2 / elo_factor1

#     # Minimálne 0.2 gólu na zápas
#     exp_1 = max(exp_1, 0.2)
#     exp_2 = max(exp_2, 0.2)
#     exp_both = exp_1 + exp_2

#     # Výpočet kurzov over podľa očakávaných gólov
#     def over_kurz(threshold):
#         base = threshold / exp_both
#         return round(max(1.01, base), 2)

#     kurz_over05 = over_kurz(0.5)
#     kurz_over15 = over_kurz(1.5)
#     kurz_over25 = over_kurz(2.5)
#     kurz_over35 = over_kurz(3.5)
#     kurz_over45 = over_kurz(4.5)
#     kurz_over55 = over_kurz(5.5)
#     kurz_over65 = over_kurz(6.5)
#     kurz_over75 = over_kurz(7.5)
#     kurz_over85 = over_kurz(8.5)
#     kurz_over95 = over_kurz(9.5)

#     return (
#         kurz_1, kurz_X, kurz_2,
#         kurz_over05, kurz_over15, kurz_over25, kurz_over35,
#         kurz_over45, kurz_over55, kurz_over65, kurz_over75,
#         kurz_over85, kurz_over95
#     )

def vypocitaj_kurzy(staty1, staty2, home_advantage=0.3):
    EA = 1 / (1 + 10 ** ((staty2["elo"] - staty1["elo"]) / 400))
    EB = 1 / (1 + 10 ** ((staty1["elo"] - staty2["elo"]) / 400))

    kurz_1 = min(round(1 / EA, 2), 150)
    kurz_2 = min(round(1 / EB, 2), 150)
    kurz_X = round((kurz_1 + kurz_2) / 2, 2)

    max_elo = 1000
    attack1 = staty1["goals_scored"] / max(staty1["win"] + staty1["draw"] + staty1["loss"], 1)
    attack2 = staty2["goals_scored"] / max(staty2["win"] + staty2["draw"] + staty2["loss"], 1)
    def_ratio1 = staty1["goals_conceded"] / max(staty1["win"] + staty1["draw"] + staty1["loss"], 1)
    def_ratio2 = staty2["goals_conceded"] / max(staty2["win"] + staty2["draw"] + staty2["loss"], 1)

    elo_factor1 = 0.1 + 1.9 * (staty1["elo"] / max_elo)
    elo_factor2 = 0.1 + 1.9 * (staty2["elo"] / max_elo)

    exp_1 = attack1 * (def_ratio2 / 2 + 0.5) * elo_factor1 / elo_factor2 + home_advantage
    exp_2 = attack2 * (def_ratio1 / 2 + 0.5) * elo_factor2 / elo_factor1

    exp_1 = max(exp_1, 0.2)
    exp_2 = max(exp_2, 0.2)
    exp_both = exp_1 + exp_2

    def over_kurz(threshold):
        base = threshold / exp_both
        return round(max(1.01, base), 2)

    kurz_over05 = over_kurz(0.5)
    kurz_over15 = over_kurz(1.5)
    kurz_over25 = over_kurz(2.5)
    kurz_over35 = over_kurz(3.5)
    kurz_over45 = over_kurz(4.5)
    kurz_over55 = over_kurz(5.5)
    kurz_over65 = over_kurz(6.5)
    kurz_over75 = over_kurz(7.5)
    kurz_over85 = over_kurz(8.5)
    kurz_over95 = over_kurz(9.5)

    return (
        kurz_1, kurz_X, kurz_2,
        kurz_over05, kurz_over15, kurz_over25, kurz_over35,
        kurz_over45, kurz_over55, kurz_over65, kurz_over75,
        kurz_over85, kurz_over95
    )

# Generovanie výsledku zápasu
# def simuluj_zapas(tim1, tim2, staty1, staty2, delay=0.25):
    
#     def vypocitaj_goly(elo1, elo2):
#         EA = 1 / (1 + 10 ** ((elo2 - elo1) / 400))
#         EB = 1 / (1 + 10 ** ((elo1 - elo2) / 400))
#         vysledok = random.choices(
#             population=["1", "X", "2"], weights=[EA, 0.1, EB], k=1
#         )[0]

#         if vysledok == "1":
#             exp_1 = 1 if (staty1["elo"] / 100) < 1 else math.ceil(staty1["elo"] / 100)
#             goly1 = random.randint(1, exp_1+2)
#             exp_2 = 1 if (staty2["elo"] / 100) < 1 else math.ceil(staty2["elo"] / 200)
#             if exp_2 == 1:
#                 goly2 = random.randint(0, goly1 - 2)
#             else:
#                 goly2 = random.randint(0, goly1 - 1)
#         elif vysledok == "2":
#             exp_2 = 1 if (staty2["elo"] / 100) < 1 else math.ceil(staty2["elo"] / 100)
#             goly2 = random.randint(1, exp_2+2)
#             exp_1 = 1 if (staty1["elo"] / 100) < 1 else math.ceil(staty1["elo"] / 200)
#             if exp_1 == 1:
#                 goly1 = random.randint(0, goly2 - 2)
#             else:
#                 goly1 = random.randint(0, goly2 - 1)
#         else:
#             goly1 = goly2 = random.randint(0, 3)
        
#         return goly1, goly2

#     goly1, goly2 = vypocitaj_goly(staty1["elo"], staty2["elo"])

#     zlute1 = random.randint(0, 6)
#     zlute2 = random.randint(0, 6)
#     cervene1 = 1 if random.random() < staty1["red"] / 100 else 0
#     cervene2 = 1 if random.random() < staty2["red"] / 100 else 0

#     def rozdel_minuty(pocet):
#         return sorted(random.sample(range(1, 91), pocet))

#     udalosti = []

#     for m in rozdel_minuty(goly1):
#         udalosti.append((m, f"⚽ Gól! {tim1} skóroval."))
#     for m in rozdel_minuty(goly2):
#         udalosti.append((m, f"⚽ Gól! {tim2} skóroval."))
#     for m in rozdel_minuty(zlute1):
#         udalosti.append((m, f"🟨 Žltá karta pre {tim1}"))
#     for m in rozdel_minuty(zlute2):
#         udalosti.append((m, f"🟨 Žltá karta pre {tim2}"))
#     for m in rozdel_minuty(cervene1):
#         udalosti.append((m, f"🟥 Červená karta pre {tim1}"))
#     for m in rozdel_minuty(cervene2):
#         udalosti.append((m, f"🟥 Červená karta pre {tim2}"))

#     udalosti.sort()

#     # Pridanie nadstaveného času
#     nadstaveny_cas = random.randint(1, 8)


#     print("\n🎮 Simulácia zápasu začína...\n")
#     for minuta in range(1, 91 + nadstaveny_cas):
#         if minuta == 90:
#             print(f"🔁 Nadstavený čas: {nadstaveny_cas} minút")
#         if minuta > 90:
#             print(f"⏱️| 90+{minuta-90}. minúta")
#         else:
#             print(f"⏱️| {minuta}. minúta")
#         for m, udalost in udalosti:
#             if m == minuta:
#                 print("   " + udalost)
#         time.sleep(delay)

#     if goly1 > goly2:
#         staty1["win"] += 1
#         staty2["loss"] += 1
#     elif goly2 > goly1:
#         staty2["win"] += 1
#         staty1["loss"] += 1
#     else:
#         staty1["draw"] += 1
#         staty2["draw"] += 1

#     staty1["goals_scored"] += goly1
#     staty1["goals_conceded"] += goly2
#     staty1["yellow"] += zlute1
#     staty1["red"] += cervene1

#     staty2["goals_scored"] += goly2
#     staty2["goals_conceded"] += goly1
#     staty2["yellow"] += zlute2
#     staty2["red"] += cervene2

#     strely1 = random.randint(5, 15) + goly1 - 1
#     strely2 = random.randint(5, 15) + goly2 - 1
#     na_branu1 = goly1 + random.randint(0, 4)
#     na_branu2 = goly2 + random.randint(0, 4)
#     drzanie1 = random.randint(51, 80) if staty1["elo"] > staty2["elo"] else random.randint(20, 49)
#     drzanie2 = 100 - drzanie1
#     rohy1 = random.randint(1, 6) + goly1
#     rohy2 = random.randint(1, 6) + goly2
#     offsides1 = random.randint(0, 4)
#     offsides2 = random.randint(0, 4)
#     fauly1 = random.randint(5, 15) + zlute1
#     fauly2 = random.randint(5, 15) + zlute2

#     print("\n🏁 Zápas skončil!\n")

#     return {
#         "výsledok": f"{tim1} {goly1} - {goly2} {tim2}",
#         "skutocny_tip": "1" if goly1 > goly2 else "2" if goly2 > goly1 else "X",
#         "štatistiky": {
#             tim1: {
#                 "goly": goly1,
#                 "strely": strely1,
#                 "strely na bránu": na_branu1,
#                 "držanie lopty": drzanie1,
#                 "rohy": rohy1,
#                 "offsidy": offsides1,
#                 "fauly": fauly1,
#                 "žlté": zlute1, 
#                 "červené": cervene1
#             },
#             tim2: {
#                 "goly": goly2,
#                 "strely": strely2,
#                 "strely na bránu": na_branu2,
#                 "držanie lopty": drzanie2,
#                 "rohy": rohy2,
#                 "offsidy": offsides2,
#                 "fauly": fauly2,
#                 "žlté": zlute2, 
#                 "červené": cervene2
#             }
#         }
#     }


def simuluj_zapas(tim1, tim2, staty1, staty2, delay=0.25):
    def expected_goals(elo1, elo2):
        # Nelineárne rozdelenie očakávaných gólov na základe rozdielu ELO
        max_goly = 20  # maximálny počet gólov pre silný tím
        min_goly = 0.2 # minimálny pre slabý tím

        # Pridáme malú konštantu aby sme sa vyhli deleniu nulou
        ratio = (elo1 + 1) / (elo2 + 1)

        # Logaritmická funkcia na transformáciu pomeru
        g1 = min(max_goly, max(min_goly, math.log(ratio, 1.25)))  # logaritmus so základom 1.25
        g2 = min(max_goly, max(min_goly, math.log(1 / ratio, 1.25)))  # druhý tím
        
        return g1, g2

    # --- Výpočet očakávaných gólov a simulácia pomocou Poissonovho rozdelenia
    exp_g1, exp_g2 = expected_goals(staty1["elo"], staty2["elo"])
    goly1 = np.random.poisson(exp_g1)
    goly2 = np.random.poisson(exp_g2)

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

    # Výsledok zápasu ovplyvňuje štatistiky
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

    # --- Realistické odvodenie štatistík
    strely1 = random.randint(4, 8) + goly1 * random.randint(2, 4)
    strely2 = random.randint(4, 8) + goly2 * random.randint(2, 4)

    na_branu1 = max(goly1 + random.randint(1, 4), goly1)
    na_branu2 = max(goly2 + random.randint(1, 4), goly2)

    drzanie1 = random.randint(51, 75) if staty1["elo"] > staty2["elo"] else random.randint(25, 49)
    drzanie2 = 100 - drzanie1

    rohy1 = random.randint(1, 5) + goly1
    rohy2 = random.randint(1, 5) + goly2

    offsides1 = random.randint(0, 3)
    offsides2 = random.randint(0, 3)
    fauly1 = random.randint(7, 14) + zlute1
    fauly2 = random.randint(7, 14) + zlute2

    print("\n🏁 Zápas skončil!\n")

    return {
        "výsledok": f"{tim1} {goly1} - {goly2} {tim2}",
        "skutocny_tip": "1" if goly1 > goly2 else "2" if goly2 > goly1 else "X",
        "štatistiky": {
            tim1: {
                "goly": goly1,
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
                "goly": goly2,
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
    
    while True:
        a = int(input("Vyber číslo domáceho tímu: ")) - 1
        if a > 131:
            print("\nZadaj číslo tímu zo zoznamu...\n")
            continue
        b = int(input("Vyber číslo hosťovského tímu: ")) - 1
        if b > 131:
            print("\nZadaj číslo tímu zo zoznamu... Znovu od začiatku...\n")
            continue
        if a and b <= 131:
            break

    tim1, tim2 = timy_zoznam[a], timy_zoznam[b]

    kurz_1, kurz_X, kurz_2, kurz_over05, kurz_over15, kurz_over25, kurz_over35, kurz_over45, kurz_over55, kurz_over65, kurz_over75, kurz_over85, kurz_over95 = vypocitaj_kurzy(timy[tim1], timy[tim2])

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
        print(f"[1] Kto vyhrá\n[2] Počet gólov v zápase(viac ako)\n[3] Počet gólov {tim1}\n[4] Počet gólov {tim2}\n[5] Počet žltých kariet v zápase\n[6] Počet žltých kariet {tim1}\n[7] Počet žltých kariet {tim2}\n---------------------------------")
        choice = int(input("Vyber podla čísla, na čo si chceš podať: "))

        if choice == 1:
            tip_vysledok = input("\nTipnite si víťaza (1, X alebo 2): ")
            if tip_vysledok in ["1", "X", "x", "2"]:
                break
            else:
                print("Zadaj prosím 1, X alebo 2.")
        
        elif choice == 2:
            print(f"Viac ako 0.5 góla: {kurz_over05}\n"
                f"Viac ako 1.5 góla: {kurz_over15}\n"
                f"Viac ako 2.5 góla: {kurz_over25}\n"
                f"Viac ako 3.5 góla: {kurz_over35}\n"
                f"Viac ako 4.5 góla: {kurz_over45}\n"
                f"Viac ako 5.5 góla: {kurz_over55}\n"
                f"Viac ako 6.5 góla: {kurz_over65}\n"
                f"Viac ako 7.5 góla: {kurz_over75}\n"
                f"Viac ako 8.5 góla: {kurz_over85}\n"
                f"Viac ako 9.5 góla: {kurz_over95}\n")
            tip_goly = int(input("Koľko gólov bude v zápase? 2 = viac ako 1.5 góla: "))
            if tip_goly > 0:
                break
            else:
                print("Tvoj tip na počet gólov musí byť aspon 1 gól...")

    while True:
            try:
                suma = float(input("\nZadaj koľko € chceš vsadiť: "))
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

    if choice == 1:
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
    elif choice == 2:
        skutocne_goly = vysledok["štatistiky"][tim1]["goly"] + vysledok["štatistiky"][tim2]["goly"]
        if skutocne_goly >= tip_goly:
            kurz = (
            kurz_over05 if tip_goly == 1 else
            kurz_over15 if tip_goly == 2 else
            kurz_over25 if tip_goly == 3 else
            kurz_over35 if tip_goly == 4 else
            kurz_over45 if tip_goly == 5 else
            kurz_over55 if tip_goly == 6 else
            kurz_over65 if tip_goly == 7 else
            kurz_over75 if tip_goly == 8 else
            kurz_over85 if tip_goly == 9 else
            kurz_over95
            )
            vyhra = round(suma * kurz, 2)
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