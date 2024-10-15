dnesny_datum_dni = int(input("Zadaj dnešný deň: ")) + (365 * 15) + (30 * 9)
euro_dni = 5766 - dnesny_datum_dni
dni = (dnesny_datum_dni - euro_dni)
hodiny = (dnesny_datum_dni * 24) - (euro_dni * 24)
sekundy = (dnesny_datum_dni * 24 * 60 * 60) - (euro_dni * 24 * 60 * 60)
print(f"Počet dní od zavedenia eura je {dni}")
print(f"Počet hodín od zavedenia eura je približne {hodiny}")
print(f"Počet sekúnd od zavedenia eura je približne {sekundy}")