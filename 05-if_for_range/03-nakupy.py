pocet = 0
celkova_suma = 0
for Suma in 1.50, 10.20, 5.30, 4.00, 5.50, 100:
    pocet = pocet + 1
    celkova_suma = celkova_suma + Suma
    print(f"Suma {pocet}. nákupu: {Suma}€")
print(f"Celkový počet nákupov: {pocet}")
print(f"Celková suma: {celkova_suma}€")