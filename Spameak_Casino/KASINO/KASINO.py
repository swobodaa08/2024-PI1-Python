# SpameakGamba Beta v4.0 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] # SpameakGamba Beta v3.0 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] 



import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os
import random

# Inicializácia konta
konto = 0

# Funkcia na načítanie progresu podľa priezviska
def load_progress(priezvisko):
    file_name = f"{priezvisko}_progress.pkl"
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)
    return 0  # Ak súbor neexistuje, začni s 0 €

# Funkcia na uloženie progresu podľa priezviska
def save_progress(priezvisko, progress):
    file_name = f"{priezvisko}_progress.pkl"
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

# Získanie priezviska na začiatku
root = tk.Tk()
root.withdraw()
priezvisko = simpledialog.askstring("Prihlásenie", "Zadajte svoje priezvisko:")
root.deiconify()

if priezvisko:
    konto = load_progress(priezvisko)
    root.destroy()

        # Inicializácia hlavného okna
    okno = tk.Tk()
    okno.attributes('-fullscreen', True)
    okno.title("SpameakGamble")
    okno.geometry("1920x1080")
    canvas = tk.Canvas()
    canvas.pack()

        # Pozadie farba
    canvas.create_rectangle

        # Tlačidlo na rátanie žetónov (zarovnané do stredu)
    b1 = tk.Button(okno, text=f"Počet žetónov : {konto}", width=20,
                    command=my_upd, bg="lime", font=('Helvetica', '20', 'bold'))
    b1.place(relx=0.5, rely=0.5, anchor='center')

        # Tlačidlo "Gamba" (v strede napravo)
    gamba_button = tk.Button(okno, text="Gamba", command=start_gamba, bg="magenta", font=('Helvetica', '12', 'bold'))
    gamba_button.place(relx=0.75, rely=0.5, anchor='center')

        # Tlačidlo na ukončenie programu (pravý dolný roh)
    exit_button = tk.Button(okno, text="Koniec", command=exit_program, bg="red", font=('Helvetica', '12', 'bold'))
    exit_button.place(relx=0.95, rely=0.95, anchor='se')

    okno.mainloop()
else:
    messagebox.showinfo("Chyba", "Nebolo zadané priezvisko. Program sa ukončí.")
