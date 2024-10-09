# Tic Tac Toe hra pre 2 hráčov

# Funkcia pre vytvorenie hracej plochy
def vytvor_hernu_plochu(pole):
    print(f"{pole[0]} | {pole[1]} | {pole[2]}")
    print("--+---+--")
    print(f"{pole[3]} | {pole[4]} | {pole[5]}")
    print("--+---+--")
    print(f"{pole[6]} | {pole[7]} | {pole[8]}")

# Funkcia na kontrolu víťaza
def kontrola_vitaza(pole, hrac):
    # Všetky možné výherné kombinácie
    vyherne_kombinacie = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # riadky
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # stĺpce
        [0, 4, 8], [2, 4, 6]  # diagonály
    ]
    
    for kombinacia in vyherne_kombinacie:
        if pole[kombinacia[0]] == pole[kombinacia[1]] == pole[kombinacia[2]] == hrac:
            return True
    return False

# Funkcia na kontrolu remízy
def kontrola_remizy(pole):
    return all(x in ['X', 'O'] for x in pole)

# Hlavná funkcia pre hru
def tic_tac_toe():
    pole = [' ' for _ in range(9)]  # Hraciu plocha inicializujeme prázdnymi poliami
    hrac = 'X'  # Začína hráč X

    while True:
        vytvor_hernu_plochu(pole)
        print(f"Hráč {hrac} je na ťahu.")
        
        try:
            tah = int(input("Vyber číslo od 1 do 9: ")) - 1
            if pole[tah] != ' ':
                print("Toto miesto je už obsadené. Skús znova.")
                continue
        except (ValueError, IndexError):
            print("Neplatná voľba. Vyber číslo od 1 do 9.")
            continue

        # Uložíme ťah hráča
        pole[tah] = hrac

        # Skontrolujeme, či daný hráč vyhral
        if kontrola_vitaza(pole, hrac):
            vytvor_hernu_plochu(pole)
            print(f"Hráč {hrac} vyhral!")
            break

        # Skontrolujeme remízu
        if kontrola_remizy(pole):
            vytvor_hernu_plochu(pole)
            print("Je to remíza!")
            break

        # Striedame hráča
        hrac = 'O' if hrac == 'X' else 'X'

# Spustíme hru
tic_tac_toe()
