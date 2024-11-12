# SpameakBet v1.2 - [Copyright by SpameakBetting a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024]


import random

# Funkcia na načítanie tímov zo súboru
def nacitaj_timy(subor):
    timy = []
    with open(subor, "r") as f:
        for riadok in f:
            nazov, hodnotenie = riadok.strip().split(',')
            timy.append((nazov, int(hodnotenie)))
    return timy

# Funkcia na výpočet kurzov na základe hodnotenia
def vypocitaj_kurzy(hodnotenie1, hodnotenie2):
    # Pravdepodobnosť výhry pre tím 1 (E_A) a tím 2 (E_B) podľa vzorcov
    EA = 1 / (1 + 10 ** ((hodnotenie2 - hodnotenie1) / 400))
    EB = 1 / (1 + 10 ** ((hodnotenie1 - hodnotenie2) / 400))
    
    # Kurzy sú prevrátenou hodnotou pravdepodobností
    kurz_1 = round(1 / EA, 2)
    kurz_2 = round(1 / EB, 2)
    
    # Stanovenie kurzu na remízu
    kurz_X = round((kurz_1 + kurz_2) / 2, 2)
    
    return kurz_1, kurz_X, kurz_2


# Funkcia na uloženie výsledku zápasu do súboru
def uloz_vysledok(nazov1, goly_tim1, nazov2, goly_tim2):
    vysledok = f"{nazov1} {goly_tim1}:{goly_tim2} {nazov2}\n"
    with open("c:/2024-PI1-Python-1/Spameak_Casino/Betting/vysledky.txt", "a") as f:
        f.write(vysledok)
    print("Výsledok zápasu bol uložený do súboru vysledky.txt")

# Funkcia na výpočet kurzu pre "Obaja dajú gól"
def vypocitaj_kurz_goly(hodnotenie1, hodnotenie2):
    priemer = (hodnotenie1 + hodnotenie2) / 2
    rozdiel = abs(hodnotenie1 - hodnotenie2)
    kurz_ano = max(1.5, 2.5 - priemer * 0.01)
    kurz_nie = min(4.0, 3.0 + rozdiel * 0.05)
    return round(kurz_ano, 2), round(kurz_nie, 2)

# Funkcia na náhodné vyhodnotenie zápasu
def vyhodnot_zapas(hodnotenie1, hodnotenie2):
    # Náhodne rozhodne o výsledku, pričom vyššie hodnotenie zvyšuje šancu na výhru
    goly_tim1 = random.randint(0, 5) if hodnotenie1 > hodnotenie2 else random.randint(0, 3)
    goly_tim2 = random.randint(0, 5) if hodnotenie2 > hodnotenie1 else random.randint(0, 3)
    return goly_tim1, goly_tim2

# Hlavný program
def hlavny_program():
    timy = nacitaj_timy("c:/2024-PI1-Python-1/Spameak_Casino/Betting/timy.txt")
    tim1, tim2 = random.sample(timy, 2)
    nazov1, hodnotenie1 = tim1
    nazov2, hodnotenie2 = tim2
    
    kurz_1, kurz_X, kurz_2 = vypocitaj_kurzy(hodnotenie1, hodnotenie2)
    kurz_ano, kurz_nie = vypocitaj_kurz_goly(hodnotenie1, hodnotenie2)
    
    # Výstup pre užívateľa
    print("                                                   ")
    print("---------------------------------------------------")
    print(f"{nazov1} : {nazov2}")
    print("                                                   ")
    print(f"1 (Vyhrá {nazov1}) = {kurz_1}")
    print(f"X (Remíza) = {kurz_X}")
    print(f"2 (Vyhrá {nazov2}) = {kurz_2}")
    print("                                                   ")
    print(f"Obaja dajú gól - A = {kurz_ano}, N = {kurz_nie}")
    print("---------------------------------------------------")
    
    # Používateľ zadá svoje tipy
    tip_vysledok = input("Tipnite si víťaza (1, X alebo 2): ")
    tip_goly = input("Tipnite si, či obaja dajú gól (A/N): ")
    
    # Vyhodnotenie zápasu
    goly_tim1, goly_tim2 = vyhodnot_zapas(hodnotenie1, hodnotenie2)
    vysledok = "1" if goly_tim1 > goly_tim2 else "2" if goly_tim2 > goly_tim1 else "X"
    obaja_daju_gol = "A" if goly_tim1 > 0 and goly_tim2 > 0 else "N"
    
    # Výsledok zápasu a stávky
    print(f"\nKonečný výsledok: {nazov1} ({goly_tim1}) : {nazov2} ({goly_tim2})")
    print(f"Výsledok zápasu: {vysledok}")
    print(f"Obaja dali gól: {obaja_daju_gol}")

    # Uloženie výsledku do súboru
    uloz_vysledok(nazov1, goly_tim1, nazov2, goly_tim2)
    
    # Vyhodnotenie stávky používateľa
    if tip_vysledok == vysledok and tip_goly == obaja_daju_gol:
        print("Gratulujem! Vyhrali ste stávku!")
    else:
        print("Bohužiaľ, vaša stávka nebola úspešná.")

# Spustenie programu
hlavny_program()
