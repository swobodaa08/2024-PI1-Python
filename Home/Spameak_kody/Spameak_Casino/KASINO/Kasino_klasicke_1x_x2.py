# SpameakCasino Beta v4.1 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] # SpameakGamba Beta v3.0 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] 



import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os
import random

# Inicializácia konta
konto = 0
velkost = 24

# Direktoria prihlasenia
directory = os.path.join(os.getcwd(), "Spameak_Casino/Progress")

# Funkcia na načítanie progresu podľa priezviska
def load_progress(priezvisko):
    file_name = os.path.join(directory, f"{priezvisko}_progress.pkl")
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)
    return 0  # Ak súbor neexistuje, začni s 0 €

# Funkcia na uloženie progresu podľa priezviska
def save_progress(priezvisko, progress):
    # Nastavenie cesty k priecinku a vytvorenie priecinka, ak neexistuje
    os.makedirs(directory, exist_ok=True)  # Vytvori priecinok, ak neexistuje

    # Nastavenie celej cesty k suboru
    file_name = os.path.join(directory, f"{priezvisko}_progress.pkl")
    
    # Ulozenie do suboru
    with open(file_name, "wb") as f:
        pickle.dump(progress, f)

# Funkcia na aktualizáciu žetónov
def my_upd():
    global konto, velkost
    konto += 1
    b1.config(text=f"Peňazí na účte : {konto}€")
    save_progress(priezvisko, konto)

# Funkcia na ukončenie programu
def exit_program():
    okno.quit()
    okno.destroy()

def add_secret():
    global konto
    if konto < 100000:
        konto = konto + 100000


# Funkcia na spustenie hry "SpameakGamba"
def start_gamba():
    okno.destroy()  # Zavrie hlavné okno SpameakGamble
    
    global konto
    počet_kôl = 0

    print("                                                       ")
    print("-------------------------------------------------------")
    print("Vitaj v hre SpameakGamba")
    print("Hra je veľmi jednoduchá, stačí tipnúť číslo od 1 do 5")
    print("Ak trafíš správne číslo, vyhrávaš trojnásobok vkladu.")
    print(f"Zostatok na účte: {konto}€")
    print("-------------------------------------------------------")

    # Kontrola vstupu pre počet kôl
    while True:
        try:
            počet_kôl = int(input("Zadaj počet kôl koľko chceš hrať? (Maximálne 20): "))
            if 0 < počet_kôl <= 20:
                break
            else:
                print("Počet kôl musí byť medzi 1 a 20.")
        except ValueError:
            print("Zadaj prosím platné číslo pre počet kôl.")

    # Princip hry
    for _ in range(počet_kôl):
        while True:
            try:
                suma = float(input("Zadaj koľko € chceš vsadiť: "))
                if suma <= konto and 10000 >= suma >= 0.50:
                    break
                else:
                    if suma >= konto:
                        print("Nemáš dostatok peňazí na túto stávku...")
                    else:
                        print("Stávka musí byť aspon 0.50€ a nemôže byť vyššia ako 10000€")
            except ValueError:
                print("Zadaj prosím platnú sumu (číslo).")

        while True:
            try:
                tip = int(input("Zadaj číslo od 1 do 5 ktore tipuješ: "))
                if 1 <= tip <= 5:
                    break
                else:
                    print("Zadaj číslo od 1 do 5.")
            except ValueError:
                print("Zadaj prosím platné číslo (1-5).")

        b = random.randint(1, 5)
        if tip == b:
            konto -= suma
            konto += (suma * 3)
            print(f"Vyhral/-a si! Výherné číslo bolo {b}. Tvoje konto je teraz {konto}€.")
            save_progress(priezvisko, konto)
        else:
            konto -= suma
            print(f"Prehral/-a si... Výherné číslo bolo {b}. Tvoje konto je teraz {konto}€.")
            save_progress(priezvisko, konto)

        if konto <= 0:
            print("Tvoje konto je 0€.")
            save_progress(priezvisko, 0)
            break


# Funkcia na spustenie hry "SpameakBet"
def start_bet():
    okno.destroy()  # Zavrie hlavné okno SpameakGamble

    from pathlib import Path
    global konto
    počet_kôl = 0

    # Original absolute path
    absolute_path = Path("c:/2024-PI1-Python-1/Spameak_Casino/timy.txt")

    # Get the current working directory
    current_dir = Path.cwd()

    # Convert to relative path based on the current directory
    relative_path = absolute_path.relative_to(current_dir)

    # Original absolute path
    absolute_path2 = Path("c:/2024-PI1-Python-1/Spameak_Casino/vysledky.txt")

    # Get the current working directory
    current_dir2 = Path.cwd()

    # Convert to relative path based on the current directory
    relative_path2 = absolute_path2.relative_to(current_dir2)


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
        if kurz_1 > 150:
            kurz_1 = 150
        if kurz_2 > 150:
            kurz_2 = 150

        if kurz_1 <= 1.15:
            kurz_1x = 1.00
        else:
            if kurz_1 < 10:
                kurz_1x = (kurz_1 * 0.6)
            else:   
                kurz_1x = (kurz_1 * 0.9)

        if kurz_2 <= 1.15:
            kurz_x2 = 1.00
        else:
            if kurz_2 < 10:
                kurz_x2 = (kurz_2 * 0.6)
            else:   
                kurz_x2 = (kurz_2 * 0.9)
        
        if kurz_1 or kurz_2 <= 1.25:
            kurz_12 = 1.00
        else:
            if kurz_1 and kurz_2 == int:
                kurz_12 = random.randint(1, 1.35)
            else:
                kurz_12 = 1.00
        
        round(kurz_1x, 2)
        round(kurz_x2, 2)
        round(kurz_12, 2)
        
        return kurz_1, kurz_X, kurz_2, kurz_1x, kurz_x2, kurz_12
    

    # Funkcia na uloženie výsledku zápasu do súboru
    def uloz_vysledok(nazov1, goly_tim1, nazov2, goly_tim2):
        vysledok = f"{nazov1} {goly_tim1}:{goly_tim2} {nazov2}\n"
        with open(relative_path2, "a") as f:
            f.write(vysledok)

    # Funkcia na náhodné vyhodnotenie zápasu podľa pravdepodobností
    def vyhodnot_zapas(hodnotenie1, hodnotenie2):
        EA = 1 / (1 + 10 ** ((hodnotenie2 - hodnotenie1) / 400))
        EB = 1 / (1 + 10 ** ((hodnotenie1 - hodnotenie2) / 400))
        vysledok = random.choices(
            population=["1", "X", "2"], weights=[EA, 0.1, EB], k=1
        )[0]

        if vysledok == "1":
            goly_tim1 = random.randint(1, 4)
            goly_tim2 = random.randint(0, goly_tim1 - 1)
        elif vysledok == "2":
            goly_tim2 = random.randint(1, 4)
            goly_tim1 = random.randint(0, goly_tim2 - 1)
        else:
            goly_tim1 = goly_tim2 = random.randint(0, 2)
        
        return goly_tim1, goly_tim2


    # Hlavný program

    def hlavny_program():
        global konto
        timy = nacitaj_timy(relative_path)
        tim1, tim2 = random.sample(timy, 2)
        nazov1, hodnotenie1 = tim1
        nazov2, hodnotenie2 = tim2
        
        kurz_1, kurz_X, kurz_2, kurz_1x, kurz_12, kurz_x2 = vypocitaj_kurzy(hodnotenie1, hodnotenie2)
        round(kurz_1, 2)
        round(kurz_2, 2)
        round(kurz_X, 2)
        if kurz_1x and kurz_12 and kurz_x2 == int:
            round(kurz_1x, 2)
            round(kurz_x2, 2)
            round(kurz_12, 2)
        
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
        print("                                                     ")
        print(f"1X (Vyhrá {nazov1} alebo remíza) = {kurz_1x}")
        print(f"12 (Nebude remíza) = {kurz_12}")
        print(f"X2 (Vyhrá {nazov2} alebo remíza) = {kurz_x2}")
        print("---------------------------------------------------")
        
        # Používateľ zadá svoje tipy
        while True:
            try:
                tip_vysledok = input("Tipnite si víťaza (1, X, 2, 1x, 12, x2): ")
                if tip_vysledok in ["1", "X", "x", "2", "1x", "1X", "12", "X2", "x2"]:
                    break
                else:
                    print("Zadaj prosím 1, X, 2, alebo 1x, x2, 12.")
            except kurz_1x or kurz_12 or kurz_x2 == str:
                print("Vyzerá to, že tip, ktorý sa snažíš podať je zamknutý, podaj na kurz ktorý neni zamknutý")


        # Kontrola vstupu pre sumu
    
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

        # Vyhodnotenie zápasu
        goly_tim1, goly_tim2 = vyhodnot_zapas(hodnotenie1, hodnotenie2)
        if goly_tim1 > goly_tim2:
            vysledok = ["1", "1x", "1X", "12"]
        elif goly_tim2 > goly_tim1:
            vysledok = ["2", "X2", "x2", "12"]
        else:
            vysledok = ["X", "x", "1X", "1x", "x2", "X2"]
            
        # Výsledok zápasu a stávky
        print(f"\nKonečný výsledok: {nazov1} {goly_tim1}:{goly_tim2} {nazov2}")

        # Uloženie výsledku do súboru
        uloz_vysledok(nazov1, goly_tim1, nazov2, goly_tim2)
            
        # Vyhodnotenie stávky používateľa
        if tip_vysledok in vysledok:
            konto -= suma
            vyhra = round(suma * (kurz_1 if "1" in vysledok and tip_vysledok == "1" else kurz_X if "X" in vysledok and tip_vysledok in ["X", "x"] else kurz_2 if "2" in vysledok and tip_vysledok == "2" else kurz_1x if "1x" in vysledok and tip_vysledok.lower() == "1x" else kurz_x2 if "x2" in vysledok and tip_vysledok.lower() == "x2" else kurz_12), 2)
            konto += vyhra
            round(konto, 2)
            print("----------------------------------------------------")
            print(f"Gratulujem! Vyhral/-a si {vyhra}€")
            save_progress(priezvisko, konto)
        else:
            konto -= suma
            round(konto, 2)
            print("----------------------------------------------------")
            print("Bohužiaľ, tvoja stávka nebola úspešná")
            save_progress(priezvisko, konto)
        print("----------------------------------------------------")
        print(f"Aktuálny zostatok na konte: {konto}€")
        print("----------------------------------------------------")

    # Hra prebehne počet_kôl krát
    for i in range(počet_kôl):
        print(f"\nKolo {i + 1} z {počet_kôl}:")
        hlavny_program()

    # Skontroluj, či je konto prázdne
    if konto <= 0:
        save_progress(priezvisko, konto)
        print("----------------------------------------------------")
        print("Tvoj zostatok na konte je 0€. Nemáš možnosť tipovať, pre reset, reštartuj program")
        print("----------------------------------------------------")




# Získanie priezviska na začiatku
root = tk.Tk()
root.withdraw()
priezvisko = simpledialog.askstring("Prihlásenie", "Zadajte svoje priezvisko:")
root.deiconify()

if priezvisko:
    konto = load_progress(priezvisko)
    root.destroy()

    # Inicializácia hlavného okna
    from PIL import Image, ImageTk
    okno = tk.Tk()
    # Obrazovka
    screen_width = okno.winfo_screenwidth()
    screen_height = okno.winfo_screenheight()
    okno.attributes('-fullscreen', True)
    okno.title("SpameakGamble")
    okno.geometry(f"{screen_width}x{screen_height}")
    canvas = tk.Canvas(okno, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)

    # Načítanie obrázka a jeho prispôsobenie veľkosti Canvasu
    image_path = "Spameak_Casino/Background.jpg"  # cesta k obrázku
    background_image = Image.open(image_path)
    background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)  # zmenšenie na veľkosť Canvasu
    background_photo = ImageTk.PhotoImage(background_image)

    # Vložte obrázok na Canvas
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # Meno používateľa
    canvas.create_rectangle(10,10,300,100, fill="Gold")
    canvas.create_text(155,55, text=f"{priezvisko}", font=("Helvetica", "20", "bold"))

    # Tlačidlo na rátanie žetónov (zarovnané do stredu)
    b1 = tk.Button(okno, text=f"Peňazí na účte : {konto}€", width=velkost,
                    command=my_upd, bg="lime", font=('Helvetica', '40', 'bold'))
    b1.place(relx=0.5, rely=0.5, anchor='center')

    # Tlačidlo "Gamba" (v strede napravo)
    gamba_button = tk.Button(okno, text="Gamba", command=start_gamba, bg="magenta", font=('Helvetica', '25', 'bold'))
    gamba_button.place(relx=0.08, rely=0.98, anchor='se')

    # Tlačidlo "Bet" (hore napravo)
    bet_button = tk.Button(okno, text="Betting", command=start_bet, bg="cyan", font=('Helvetica', '25', 'bold'))
    bet_button.place(relx=0.5328, rely=0.98, anchor='se')

    # Tlačidlo na ukončenie programu (pravý dolný roh)
    exit_button = tk.Button(okno, text="Koniec", command=exit_program, bg="red", font=('Helvetica', '25', 'bold'))
    exit_button.place(relx=0.98, rely=0.98, anchor='se')

    # Tlačidlo na ukončenie programu (pravý dolný roh)
    secret_button = tk.Button(okno, text="-", command=add_secret, bg="black", font=('Helvetica', '5', 'bold'))
    secret_button.place(relx=0.55, rely=0.285, anchor='se')

    okno.mainloop()
else:
    messagebox.showinfo("Chyba", "Nebolo zadané priezvisko. Program sa ukončí.")
