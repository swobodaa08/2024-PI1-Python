# Získanie vstupu
rok = int(input("Zadaj rok tvojho narodenia: "))
mesiac = input("Zadaj v ktorom mesiaci si sa narodil (v angličtine): ").lower()

# Mapa mesiacov do čísel
mesiace = {
    "january": 1, "february": 2, "march": 3, "april": 4,
    "may": 5, "june": 6, "july": 7, "august": 8,
    "september": 9, "october": 10, "november": 11, "december": 12
}

# Kontrola, či mesiac existuje v slovníku
if mesiac in mesiace:
    month = mesiace[mesiac]
else:
    print("Nesprávny názov mesiaca.")
    exit()

# Výpočet veku a mesiacov
aktualny_rok = 2024
aktualny_mesiac = 10  # Povedzme, že teraz je október 2024
vek_roku = aktualny_rok - rok

# Výpočet rozdielu v mesiacoch
if month > aktualny_mesiac:
    vypocet_mesiaca = month
    vek_roku -= 1
else:
    vypocet_mesiaca = aktualny_mesiac - month

# Výstup výsledku
print(f"Tvoj vek je {vek_roku} rokov a {vypocet_mesiaca} mesiacov")