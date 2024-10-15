from datetime import datetime

# Získanie dátumu od používateľa
dnesny_den = int(input("Zadaj dnešný deň v mesiaci: "))
dnesny_mesiac = int(input("Zadaj dnešný mesiac (1-12): "))
dnesny_rok = int(input("Zadaj dnešný rok: "))

# Dátum zavedenia eura - 1. január 2009
euro_datum = datetime(2009, 1, 1)

# Dátum zadaný používateľom
dnesny_datum = datetime(dnesny_rok, dnesny_mesiac, dnesny_den)

# Výpočet rozdielu medzi dátumami
rozdiel = dnesny_datum - euro_datum

# Prepočet na dni, hodiny, sekundy
dni = rozdiel.days
hodiny = dni * 24
sekundy = dni * 24 * 60 * 60

# Výstup
print(f"Počet dní od zavedenia eura je {dni}")
print(f"Počet hodín od zavedenia eura je približne {hodiny}")
print(f"Počet sekúnd od zavedenia eura je približne {sekundy}")