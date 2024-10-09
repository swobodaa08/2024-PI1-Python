n = int(input("Zadaj n: "))
fak = 1
for i in range(n):
    fak = fak * (i+1) # sucet + (i+1) je vyraz, najskor sa vypocita vyraz a vysledna hodnota sa priradi do premennej sucet
    # print(i, i+1, sucet)
print(f"{n}! = {fak}") # {} napiseme pravym (pravy alt + B) alebo (pravy alt + 123)