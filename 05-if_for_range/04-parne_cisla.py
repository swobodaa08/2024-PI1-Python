cislo = int(input("Zadaj číslo: "))
# vypis parnych cisel
print(f"Párne čísla do {cislo}:")
for i in range(2, cislo+1, 2):
    print(i)
# vypis neparnych cisel
print(f"Nepárne čísla do {cislo}:")
for i in range(1, cislo+1, 2):
    print(i)
if cislo == 0:
    print("Tvoje číslo je 0")
else:
    if cislo % 2 == 0:
        print(f"Číslo {cislo} je párne")
    else:
        print(f"Číslo {cislo} je nepárne")