# SpameakBet v2.0 - [Copyright by SpameakBetting a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024]


import random
suma = 0

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

# Funkcia na náhodné vyhodnotenie zápasu podľa pravdepodobností
def vyhodnot_zapas(hodnotenie1, hodnotenie2):
    # Vypočítame pravdepodobnosti výhry pre oba tímy na základe ELO ratingov
    EA = 1 / (1 + 10 ** ((hodnotenie2 - hodnotenie1) / 400))
    EB = 1 / (1 + 10 ** ((hodnotenie1 - hodnotenie2) / 400))
    
    # Náhodne rozhodneme o výsledku zápasu podľa vypočítaných pravdepodobností
    vysledok = random.choices(
        population=["1", "X", "2"],            # Výhra tímu 1, Remíza, Výhra tímu 2
        weights=[EA, 0.1, EB],                 # Pravdepodobnosť výhry pre každý výsledok
        k=1                                    # Vyberieme jeden výsledok
    )[0]

    # Generovanie náhodného skóre podľa výsledku
    if vysledok == "1":  # Tím 1 vyhral
        goly_tim1 = random.randint(1, 5)
        goly_tim2 = random.randint(0, goly_tim1 - 1)
    elif vysledok == "2":  # Tím 2 vyhral
        goly_tim2 = random.randint(1, 5)
        goly_tim1 = random.randint(0, goly_tim2 - 1)
    else:  # Remíza
        goly_tim1 = goly_tim2 = random.randint(0, 3)
    
    return goly_tim1, goly_tim2

# Hlavný program
def hlavny_program():
    timy = nacitaj_timy("c:/2024-PI1-Python-1/Spameak_Casino/Betting/timy.txt")
    tim1, tim2 = random.sample(timy, 2)
    nazov1, hodnotenie1 = tim1
    nazov2, hodnotenie2 = tim2
    
    kurz_1, kurz_X, kurz_2 = vypocitaj_kurzy(hodnotenie1, hodnotenie2)
    
    # Výstup pre užívateľa
    print("                                                   ")
    print("---------------------------------------------------")
    print(f"{nazov1} : {nazov2}")
    print("                                                   ")
    print(f"1 (Vyhrá {nazov1}) = {kurz_1}")
    print(f"X (Remíza) = {kurz_X}")
    print(f"2 (Vyhrá {nazov2}) = {kurz_2}")
    print("                                                   ")
    print("---------------------------------------------------")
    
    # Kontrola vstupu pre sumu
    while True:
        try:
            suma = float(input("Zadaj koľko € chceš vsadiť: "))
            if 10000 >= suma >= 0.50:
                break
            else:
                print("--------------------------------------")
                print("Vklad musí byť aspoň 0.50€ a nemôže byť vyšší ako 10000€ na jednu hru...")
                print("--------------------------------------")
                print("                                                       ")
        except ValueError:
            print("-------------------------------------------")
            print("ČISLOOOO! Zadaj prosím platnú sumu (číslo).")
            print("-------------------------------------------")
            print("                                                       ")
    
    # Používateľ zadá svoje tipy
    while True:
        try:
            tip_vysledok = input("Tipnite si víťaza (1, X alebo 2): ")
            if tip_vysledok == "1":
                break
            if tip_vysledok == "2":
                break
            if tip_vysledok == "X":
                break
            if tip_vysledok == "X":
                break
            else:
                print("-------------------------------------------------------------------------------------------------------------")
                print("Zadaj prosím 1, X alebo 2, aby si neprišiel o svoj vklad bez šance vyhrať...")
                print("-------------------------------------------------------------------------------------------------------------")
                print("                                                       ")
        except ValueError:
            print("-------------------------------------------")
            print("TIPNI SPRAVNE! Zadaj prosím 1, X alebo 2.")
            print("-------------------------------------------")
            print("                                                       ")
    
    # Vyhodnotenie zápasu
    goly_tim1, goly_tim2 = vyhodnot_zapas(hodnotenie1, hodnotenie2)
    vysledok = "1" if goly_tim1 > goly_tim2 else "2" if goly_tim2 > goly_tim1 else "X"
    
    # Výsledok zápasu a stávky
    print(f"\nKonečný výsledok: {nazov1} {goly_tim1}:{goly_tim2} {nazov2}")
    print(f"Výsledok zápasu: {vysledok}")

    # Uloženie výsledku do súboru
    uloz_vysledok(nazov1, goly_tim1, nazov2, goly_tim2)
    
    # Vyhodnotenie stávky používateľa
    if tip_vysledok == vysledok:
        print("Gratulujem! Vyhrali ste stávku!")
    else:
        print("Bohužiaľ, vaša stávka nebola úspešná.")

# Spustenie programu
hlavny_program()