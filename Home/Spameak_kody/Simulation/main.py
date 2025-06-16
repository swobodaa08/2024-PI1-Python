import random, time

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

# Generovanie výsledku zápasu
def simuluj_zapas(tim1, tim2, staty1, staty2, delay=0.19):
    def vypocitaj_goly(utok, obrana):
        zaklad = random.gauss(utok / 10, 1)
        efektivne = max(0, int(zaklad - obrana / 30 + random.uniform(-1, 1)))
        return efektivne

    goly1 = vypocitaj_goly(staty1["goals_scored"], staty2["goals_conceded"])
    goly2 = vypocitaj_goly(staty2["goals_scored"], staty1["goals_conceded"])

    zlute1 = random.randint(0, staty1["yellow"] // 5 + 1)
    zlute2 = random.randint(0, staty2["yellow"] // 5 + 1)
    cervene1 = 1 if random.random() < staty1["red"] / 100 else 0
    cervene2 = 1 if random.random() < staty2["red"] / 100 else 0

    def rozdel_minuty(pocet):
        return sorted(random.sample(range(1, 91), pocet)) if pocet > 0 else []

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

    strely1 = random.randint(5, 15) + goly1
    strely2 = random.randint(5, 15) + goly2
    na_branu1 = int(strely1 * random.uniform(0.3, 0.6))
    na_branu2 = int(strely2 * random.uniform(0.3, 0.6))
    drzanie1 = random.randint(45, 55) + (staty1["elo"] - staty2["elo"]) // 2
    drzanie1 = max(30, min(drzanie1, 70))
    drzanie2 = 100 - drzanie1
    rohy1 = random.randint(1, 6)
    rohy2 = random.randint(1, 6)
    offsides1 = random.randint(0, 4)
    offsides2 = random.randint(0, 4)
    fauly1 = random.randint(5, 15)
    fauly2 = random.randint(5, 15)

    print("\n🏁 Zápas skončil!\n")

    return {
        "výsledok": f"{tim1} {goly1} - {goly2} {tim2}",
        "karty": {
            tim1: {"žlté": zlute1, "červené": cervene1},
            tim2: {"žlté": zlute2, "červené": cervene2},
        },
        "štatistiky": {
            tim1: {
                "strely": strely1,
                "strely na bránu": na_branu1,
                "držanie lopty": drzanie1,
                "rohy": rohy1,
                "offsidy": offsides1,
                "fauly": fauly1
            },
            tim2: {
                "strely": strely2,
                "strely na bránu": na_branu2,
                "držanie lopty": drzanie2,
                "rohy": rohy2,
                "offsidy": offsides2,
                "fauly": fauly2
            }
        }
    }


# ======= HLAVNÝ PROGRAM ========
if __name__ == "__main__":
    timy = nacitaj_timove_statistiky("Home/Spameak_kody/Simulation/teams.txt")

    timy_zoznam = list(timy.keys())
    print("Dostupné tímy:")
    for idx, nazov in enumerate(timy_zoznam):
        print(f"{idx+1}. {nazov}")

    a = int(input("Vyber číslo prvého tímu: ")) - 1
    b = int(input("Vyber číslo druhého tímu: ")) - 1

    tim1, tim2 = timy_zoznam[a], timy_zoznam[b]
    vysledok = simuluj_zapas(tim1, tim2, timy[tim1], timy[tim2])

    print("\n=== Výsledok zápasu ===")
    print(vysledok["výsledok"])
    print("\n=== Karty ===")
    for tim, karty in vysledok["karty"].items():
        print(f"{tim}: Žlté - {karty['žlté']}, Červené - {karty['červené']}")
    print("\n=== Štatistiky ===")
    for tim, stats in vysledok["štatistiky"].items():
        print(f"{tim}:")
        for k, v in stats.items():
            print(f"  {k}: {v}")
    
    zapis_timove_statistiky("Home/Spameak_kody/Simulation/teams.txt", timy)