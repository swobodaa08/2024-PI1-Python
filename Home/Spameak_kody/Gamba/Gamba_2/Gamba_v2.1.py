# SpameakGamba v2.1 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024]


# Import
import random


# Definícia
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("-------------------------------------------------------")
print("                                                       ")
print("Vitaj v hre SpameakGamba")
print("Táto hra je stále v Beta verzii, ak si narazil na chybu, kontaktuj môj instagram : @swobodaa08")
print("Ak trafíš správne číslo, vyhrávaš Trojnásobok vkladu, ak vsadíš 50€ a trafíš číslo, vyhrávaš 150€")
print("Uži si Gamble <33333333")
print("                                                       ")
print("-------------------------------------------------------")
print("                                                       ")
print("                                                       ")
print("                                                       ")
počet_kôl = int(input("Zadaj počet kôl koľko chceš hrať?(Maximálne 20): "))
konto = 0


# Chybny počet kôl
if počet_kôl == 0:
    print("Zadal si počet kôl 0 zadaj aspoň jedno kolo!!!!")


# Princip hry
for i in range(počet_kôl):
    suma = int(input("Zadaj koľko € chceš vsadiť: "))
    tip = int(input("Zadaj číslo od 1 do 5 ktore tipuješ: "))
    b = (random.randint(1,5))
    počet_kôl = počet_kôl - 1
    if tip == b:
        konto = konto + (suma * 3)
        print(f"Vyhral si tvoje konto je {konto}€ uhádol si správne číslo :)")
        print(f"Počet ostávajúcich pokusov: {počet_kôl}")
    else:
        konto = konto - suma
        print(f"Prehral si, tvoje konto je {konto}€ číslo bolo {b} skús ešte raz :)")
        print(f"Počet ostávajúcich pokusov: {počet_kôl}")


# Tkinter import
import tkinter as tk
okno = tk.Tk()
okno.attributes('-fullscreen', False)
okno.title("SpameakGamble")
canvas = tk.Canvas(width=1080, height=720) # Zadám šírku a výšku strán
canvas.pack()

# Konecne konto
if konto < 0:
    canvas.create_text(540,360, text=f"Dokopy si prehral {konto}€ nabudúce skús Poker alebo Respin Joker :3", font=('Helvetica','25','bold'))
else:
    canvas.create_text(540,360, text=f"Dokopy si vyhral {konto}€ gratulujem :)", font=('Helvetica','25','bold'))

# Okno Softveru
tk.mainloop()