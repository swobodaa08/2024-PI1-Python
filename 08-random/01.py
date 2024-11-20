import random # kniznica ktora sluzi na generovanie nahodnych hodnot


for _ in range(10):
    x = 1
    y = 50
    nahodne_cislo = random.randint (x, y) # vygeneruje nahodne cele cislo
    nahodna_farba = random.choice(["red", "green", "blue"]) # vygeneruje nahodnu hodnotu zo zoznamu hodnot, zoznam ohranicime []
    nahodne_pismeno = random.choice("aeiouy") # vygeneruje nahodnu samohlasku
    print(nahodne_cislo)
    print(nahodna_farba)
    print(nahodne_pismeno)
    x =+ 100
    y =+ 100
