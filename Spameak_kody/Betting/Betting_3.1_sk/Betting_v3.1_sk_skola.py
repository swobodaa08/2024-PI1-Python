# SpameakBet v3.1 - [Copyright by SpameakBetting a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024]


import random


print("                                                       ")
print("                                                       ")
print("                                                       ")
print("-------------------------------------------------------")
print("                                                       ")
print("Vitaj v hre SpameakBetting")
print("Hra je veľmi jednoduchá, stačí tipnúť tím ktorý vyhrá")
print("Táto hra je stále v Beta verzii, ak si narazil na chybu, kontaktuj môj instagram : @swobodaa08")
print("Ak trafíš správne tím, ktorý vyhrá, tvoj vklad sa vynásobí kurzom vypísaným pred stávkou")
print("Uži si Gamble <33333333")
print("                                                       ")
print("-------------------------------------------------------")
print("                                                       ")
print("                                                       ")
print("                                                       ")

# Kapital
while True:
    try:
        vklad = float(input("Koľko eur chceš vložiť na svoj účet: "))
        if 0.50 <= vklad <= 100000:
            break
        else:
            print("-----------------------------------------------------------------------------------------------------")
            print("Tvoj herný vklad nemôže byť vyšší ako 100000€, taktiež nie menší ako 0.50€!")
            print("-----------------------------------------------------------------------------------------------------")
            print("                                                       ")
    except ValueError:
        print("-------------------------------------------------------")
        print("Neplatný vstup! Zadaj prosím číslo.")
        print("-------------------------------------------------------")
        print("                                                       ")

# Kontrola vstupu pre počet kôl
while True:
    try:
        počet_kôl = int(input("Zadaj počet kôl koľko chceš hrať? (Maximálne 20): "))
        if 0 < počet_kôl <= 20:
            break
        else:
            print("-----------------------------------------------------------------------------------------------------")
            print("Počet hraných hier nemôže byť vyšší ako 20, taktiež nie menší ako 1! Zadaj prosím číslo medzi 1 a 20.")
            print("-----------------------------------------------------------------------------------------------------")
            print("                                                       ")
    except ValueError:
        print("-------------------------------------------------------")
        print("Neplatný vstup! Zadaj prosím číslo.")
        print("-------------------------------------------------------")
        print("                                                       ")

konto = vklad
round(konto, 2)

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
    EA = 1 / (1 + 10 ** ((hodnotenie2 - hodnotenie1) / 400))
    EB = 1 / (1 + 10 ** ((hodnotenie1 - hodnotenie2) / 400))
    kurz_1 = round(1 / EA, 2)
    kurz_2 = round(1 / EB, 2)
    kurz_X = round((kurz_1 + kurz_2) / 2, 2)
    return kurz_1, kurz_X, kurz_2

# Funkcia na uloženie výsledku zápasu do súboru
def uloz_vysledok(nazov1, goly_tim1, nazov2, goly_tim2):
    vysledok = f"{nazov1} {goly_tim1}:{goly_tim2} {nazov2}\n"
    with open("Z:/2024-PI1-Python/Spameak_Casino/Betting/vysledky_sk.txt", "a") as f:
        f.write(vysledok)

# Funkcia na náhodné vyhodnotenie zápasu podľa pravdepodobností
def vyhodnot_zapas(hodnotenie1, hodnotenie2):
    EA = 1 / (1 + 10 ** ((hodnotenie2 - hodnotenie1) / 400))
    EB = 1 / (1 + 10 ** ((hodnotenie1 - hodnotenie2) / 400))
    vysledok = random.choices(
        population=["1", "X", "2"], weights=[EA, 0.1, EB], k=1
    )[0]

    if vysledok == "1":
        goly_tim1 = random.randint(1, 5)
        goly_tim2 = random.randint(0, goly_tim1 - 1)
    elif vysledok == "2":
        goly_tim2 = random.randint(1, 5)
        goly_tim1 = random.randint(0, goly_tim2 - 1)
    else:
        goly_tim1 = goly_tim2 = random.randint(0, 3)
    
    return goly_tim1, goly_tim2


# Hlavný program
def hlavny_program():
    global konto
    timy = nacitaj_timy("Z:/2024-PI1-Python/Spameak_Casino/Betting/timy_sk.txt")
    tim1, tim2 = random.sample(timy, 2)
    nazov1, hodnotenie1 = tim1
    nazov2, hodnotenie2 = tim2
    
    kurz_1, kurz_X, kurz_2 = vypocitaj_kurzy(hodnotenie1, hodnotenie2)
    round(kurz_1, 2)
    round(kurz_2, 2)
    round(kurz_X, 2)
    
    # Výstup pre užívateľa
    print("\n---------------------------------------------------")
    print(f"Stav tvojho účtu je : {konto}€")
    print("                                                     ")
    print("\n---------------------------------------------------")
    print(f"{nazov1} : {nazov2}")
    print("                                                     ")
    print(f"1 (Vyhrá {nazov1}) = {kurz_1}")
    print(f"X (Remíza) = {kurz_X}")
    print(f"2 (Vyhrá {nazov2}) = {kurz_2}")
    print("---------------------------------------------------")
    
    # Používateľ zadá svoje tipy
    while True:
        tip_vysledok = input("Tipnite si víťaza (1, X alebo 2): ")
        if tip_vysledok in ["1", "X", "2"]:
            break
        else:
            print("Zadaj prosím 1, X alebo 2.")


    # Kontrola vstupu pre sumu
 
    while True:
        try:
            suma = float(input("Zadaj koľko € chceš vsadiť: "))
            if konto >= suma:
                break
            else:  
                print("---------------------------------------------------")
                print("Nemáš dostatok peňazí na takúto stávku")
                print("---------------------------------------------------")
        except ValueError:
            print("Prosím, zadaj platnú sumu (číslo).")

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
        konto -= suma
        vyhra = round(suma * (kurz_1 if vysledok == "1" else kurz_X if vysledok == "X" else kurz_2), 2)
        konto += vyhra
        round(konto, 2)
        print("----------------------------------------------------")
        print(f"Gratulujem! Vyhral/-a si {vyhra}€")
    else:
        konto -= suma
        round(konto, 2)
        print("----------------------------------------------------")
        print("Bohužiaľ, tvoja stávka nebola úspešná")
    print("----------------------------------------------------")
    print(f"Aktuálny zostatok na konte: {konto}€")
    print("----------------------------------------------------")

# Hra prebehne počet_kôl krát
for i in range(počet_kôl):
    print(f"\nKolo {i + 1} z {počet_kôl}:")
    hlavny_program()

# Skontroluj, či je konto prázdne
if konto <= 0:
    print("----------------------------------------------------")
    print("Tvoj zostatok na konte je 0€. Nemáš možnosť tipovať, pre reset, reštartuj program")
    print("----------------------------------------------------")

while True:
    odpoved = input(f"Konečný zostatok na účte : {konto}€, pre vypnutie zavri aplikáciu.").strip().lower()