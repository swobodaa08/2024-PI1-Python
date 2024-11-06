# SpameakGamba v1.1 (Copyright by @AlexSlivka7 s.r.o. 2024)(Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024)


# Definícia
počet_kôl = int(input("Zadaj počet kôl koľko chceš hrať?(Maximálne 20): "))
konto = 0

# Ignor
import random

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
          konto = konto + suma
          print(f"Vyhral si tvoje konto je {konto}€ uhádol si správne číslo :)")
          print(f"Počet ostávajúcich pokusov: {počet_kôl}")
     else:
          konto = konto - suma
          print(f"Prehral si, tvoje konto je {konto}€ číslo bolo {b} skús ešte raz :)")
          print(f"Počet ostávajúcich pokusov: {počet_kôl}")

# Konecne konto
print(f"Celkovo si vyhral {konto}€ gratulujem") 