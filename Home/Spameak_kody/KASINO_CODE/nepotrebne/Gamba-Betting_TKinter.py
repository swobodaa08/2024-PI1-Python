# SpameakGamba Beta v4.0 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] # SpameakGamba Beta v3.0 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] 



import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os
import random

# Inicializácia konta
konto = 0

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
    global konto
    konto += 1
    b1.config(text=f"Počet žetónov : {konto}")
    save_progress(priezvisko, konto)

# Funkcia na ukončenie programu
def exit_program():
    okno.quit()
    okno.destroy()


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
    print(f"Počet žetónov: {konto} = {konto}€")
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
    for i in range(počet_kôl):
        while True:
            try:
                suma = float(input("Zadaj koľko € chceš vsadiť: "))
                if 10000 >= suma >= 0.50:
                    break
                else:
                    print("Vklad musí byť medzi 0.50€ a 10000€ na jednu hru.")
                if suma <= konto:
                    break
                else:
                    print("Nemáš dostatok peňazí na túto stávku...")
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
        return kurz_1, kurz_X, kurz_2

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
            goly_tim1 = random.randint(1, 6)
            goly_tim2 = random.randint(0, goly_tim1 - 1)
        elif vysledok == "2":
            goly_tim2 = random.randint(1, 6)
            goly_tim1 = random.randint(0, goly_tim2 - 1)
        else:
            goly_tim1 = goly_tim2 = random.randint(0, 3)
        
        return goly_tim1, goly_tim2


    # Hlavný program

    def hlavny_program():
        global konto
        timy = nacitaj_timy(relative_path)
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
    okno.attributes('-fullscreen', True)
    okno.title("SpameakGamble")
    okno.geometry("1920x1080")
    canvas = tk.Canvas(okno, width=1920, height=1080)
    canvas.pack(fill="both", expand=True)

    # Načítanie obrázka a jeho prispôsobenie veľkosti Canvasu
    image_path = "Spameak_Casino/Background.jpg"  # cesta k obrázku
    background_image = Image.open(image_path)
    background_image = background_image.resize((1920, 1080), Image.LANCZOS)  # zmenšenie na veľkosť Canvasu
    background_photo = ImageTk.PhotoImage(background_image)

    # Vložte obrázok na Canvas
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # Tlačidlo na rátanie žetónov (zarovnané do stredu)
    b1 = tk.Button(okno, text=f"Počet žetónov : {konto}", width=20,
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

    okno.mainloop()
else:
    messagebox.showinfo("Chyba", "Nebolo zadané priezvisko. Program sa ukončí.")
