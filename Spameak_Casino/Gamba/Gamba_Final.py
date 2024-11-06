# SpameakGamba Beta v2.3 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] 


# Import
import random

# Definícia
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("-------------------------------------------------------")
print("                                                       ")
print("Vitaj v hre SpameakGamba")
print("Hra je veľmi jednoduchá, stačí tipnúť číslo od 1 do 5")
print("Táto hra je stále v Beta verzii, ak si narazil na chybu, kontaktuj môj instagram : @swobodaa08")
print("Ak trafíš správne číslo, vyhrávaš Trojnásobok vkladu, ak vsadíš 50€ a trafíš číslo, vyhrávaš 150€")
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

konto = 0

# Princip hry
for i in range(počet_kôl):
    # Kontrola vstupu pre sumu
    while True:
        try:
            suma = float(input("Zadaj koľko € chceš vsadiť: "))
            if 10000 > suma >= 0.50:
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
    while True:
        try:
            tip = int(input("Zadaj číslo od 1 do 5 ktore tipuješ: "))
            if 1 <= tip <= 5:
                break
            else:
                print("-------------------------------------------------------------------------------------------------------------")
                print("Také číslo ani nebolo v možnostiach, zadaj číslo od 1 do 5, aby si neprišiel o svoj vklad bez šance vyhrať...")
                print("-------------------------------------------------------------------------------------------------------------")
                print("                                                       ")
        except ValueError:
            print("-------------------------------------------")
            print("ČISLOOOO! Zadaj prosím platnú sumu (číslo).")
            print("-------------------------------------------")
            print("                                                       ")
    b = random.randint(1, 5)
    počet_kôl -= 1
    if tip == b:
        konto += suma * 3
        if počet_kôl == 0:
            break
        else:
            print("                                                       ")
            print("                                                       ")
            print("                                                       ")
            print("                                                       ")
            print("                                                       ")
            print("-------------------------------------------------------------------------")
            print("                                                       ")
            print(f"Vyhral/-a si !!!!")
            print(f"Výherné číslo bolo {b}, perfektne")
            print(f"Počet zostávajúcich pokusov: {počet_kôl}")
            if konto > 0:
                print(f"Tvoj profit je zatiaľ {konto}€, ak budeš takto pokračovať zachvíľu z teba bude milionár :)")
            else:
                print(f"Avšak stále si už prehral/-a {konto * -1}€, ak chceš stále hrať, pokračuj")
            print("                                                       ")
            print("-------------------------------------------------------------------------")
    else:
        konto -= suma
        if počet_kôl == 0:
            break
        else:
            print("                                                       ")
            print("                                                       ")
            print("                                                       ")
            print("                                                       ")
            print("-------------------------------------------------------------------------")
            print("                                                       ")
            print(f"Prehral/-a si.....")
            print(f"Výherné číslo bolo {b}")
            print(f"Počet zostávajúcich pokusov: {počet_kôl}")
            if konto > 0:
                print(f"Avšak nezúfaj, zatial si stále v profite {konto}€")
            else:
                print(f"Zatiaľ si prehral/-a {konto * -1}€, ak chceš skončiť, vypni tento program.")
            print("                                                       ")
            print("-------------------------------------------------------------------------")

# Tkinter import
import tkinter as tk
okno = tk.Tk()
okno.attributes('-fullscreen', False)
okno.title("SpameakGamble")
canvas = tk.Canvas(width=1080, height=720)  # Zadám šírku a výšku strán
canvas.pack()

# Konecne konto
konto = round(konto, 2)
if konto < 0:
    canvas.create_oval(10, 280, 1070, 440, fill="red")
    canvas.create_text(540, 360, text=f"Dokopy si prehral {abs(konto)}€ nabudúce skús Poker alebo Respin Joker :3", font=('Helvetica', '20', 'bold'))
else:
    canvas.create_oval(235, 280, 835, 440, fill="lime")
    canvas.create_text(540, 360, text=f"Dokopy si v profite {konto}€ gratulujem :)", font=('Helvetica', '20', 'bold'))

# Okno Softveru
tk.mainloop()