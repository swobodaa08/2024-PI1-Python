import random, math
import numpy as np

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

def vypocitaj_kurzy(staty1, staty2):
    EA = 1 / (1 + 10 ** ((staty2["elo"] - staty1["elo"]) / 400))
    EB = 1 / (1 + 10 ** ((staty1["elo"] - staty2["elo"]) / 400))
    kurz_1 = min(round(1 / EA, 2), 150)
    kurz_2 = min(round(1 / EB, 2), 150)
    kurz_X = round((kurz_1 + kurz_2) / 2, 2)
    return (kurz_1, kurz_X, kurz_2)

def simuluj_zapas(tim1, tim2, staty1, staty2):
    def expected_goals(elo1, elo2):
        max_goly, min_goly = 20, 0.2
        ratio = (elo1 + 1) / (elo2 + 1)
        g1 = min(max_goly, max(min_goly, math.log(ratio, 1.25)))
        g2 = min(max_goly, max(min_goly, math.log(1 / ratio, 1.25)))
        return g1, g2

    exp_g1, exp_g2 = expected_goals(staty1["elo"], staty2["elo"])
    goly1, goly2 = np.random.poisson(exp_g1), np.random.poisson(exp_g2)

    staty1["goals_scored"] += goly1
    staty1["goals_conceded"] += goly2
    staty2["goals_scored"] += goly2
    staty2["goals_conceded"] += goly1

    staty1["matches"] += 1
    staty2["matches"] += 1

    if goly1 > goly2:
        staty1["win"] += 1
        staty2["loss"] += 1
    elif goly2 > goly1:
        staty2["win"] += 1
        staty1["loss"] += 1
    else:
        staty1["draw"] += 1
        staty2["draw"] += 1

def vypis_tabulku(timy):
    tabulka = []
    for nazov, data in timy.items():
        body = data["win"] * 3 + data["draw"]
        skore = f"{data['goals_scored']}:{data['goals_conceded']}"
        tabulka.append({
            "tim": nazov,
            "z": data["matches"],
            "win": data["win"],
            "draw": data["draw"],
            "loss": data["loss"],
            "body": body,
            "skore": skore,
            "goly_plus": data["goals_scored"],
            "goly_minus": data["goals_conceded"]
        })

    tabulka.sort(key=lambda x: (x["body"], x["goly_plus"] - x["goly_minus"], x["goly_plus"]), reverse=True)

    print("\n=== Konečná tabuľka ===")
    print(f"{'Por.':<4} {'Tím':<20} {'Z':<2} {'V':<2} {'R':<2} {'P':<2} {'Body':<5} {'Skóre'}")
    for i, t in enumerate(tabulka, 1):
        print(f"{i:<4} {t['tim']:<20} {t['z']:<2} {t['win']:<2} {t['draw']:<2} {t['loss']:<2} {t['body']:<5} {t['skore']}")

# ======= HLAVNÝ BLOK =======
if __name__ == "__main__":
    subor = "Home/Spameak_kody/Simulation-Slovakia/timy-slovakia.txt"
    timy = nacitaj_timove_statistiky(subor)
    timy_zoznam = list(timy.keys())

    for data in timy.values():
        data["win"] = data["draw"] = data["loss"] = 0
        data["goals_scored"] = data["goals_conceded"] = 0
        data["matches"] = 0

    # každý s každým – 2x (domáci a vonkajší zápas)
    for i in range(len(timy_zoznam)):
        for j in range(len(timy_zoznam)):
            if i != j:
                t1, t2 = timy_zoznam[i], timy_zoznam[j]
                simuluj_zapas(t1, t2, timy[t1], timy[t2])

    vypis_tabulku(timy)
