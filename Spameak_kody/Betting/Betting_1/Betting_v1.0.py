# SpameakBet v1.0 - [Copyright by SpameakBetting a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024]

import random


# Vymyslí random šance na kurzy
x1 = random.randint(1, 100)
x2 = random.randint(1, 100-x1)
xx = random.randint(1, 100-x1-x2)

# Premení čísla na názvy tímu
šanca1 = ['Real Madrid'] * x1
šancax = ['Remíza'] * xx
šanca2 = ['Barcelona'] * x2

# Zo šancí vytvorí kurzy
kurz1 = 100 / x1
kurzx = 100 / xx
kurz2 = 100 / x2

print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print(f"Real Madrid       Remíza       Barcelona")
print(f"   {round(kurz1, 2)}            {round(kurzx, 2)}            {round(kurz2, 2)}")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")

while True:
    try:
        tip = int(input("Na ktorý tím tipuješ?(1, 0, 2): "))
        if 0 <= tip <= 2:
            break
        else:
            print("Zadaj 1, 0 alebo 2")
    except ValueError:
        print("Zadaj platné číslo")



vysledok = random.choice(šanca1 + šancax + šanca2)

šanca1 = ['Real Madrid'] / x1
šancax = ['Remíza'] / xx
šanca2 = ['Barcelona'] / x2

if tip == 1:
    tip = šanca1
if tip == 0:
    tip = šancax
if tip == 2:
    tip = šanca2

if tip == vysledok:
    print(f"Zápas vyhral/-a {vysledok}, vyhral si")
else:
    if tip == šanca1:
        if vysledok == šancax:
            print(f"Zápas skončil remízou, prehrávaš stávku")
        else:
            print(f"Zápas vyhral/-a {šanca2}, prehrávaš stávku")
    if tip == šancax:
        if vysledok == šanca1:
            print(f"Zápas vyhral/-a {šanca1}, prehrávaš stávku")
        else:
            print(f"Zápas vyhral/-a {šanca2}, prehrávaš stávku")
    if tip == šanca2:
        if vysledok == šanca1:
            print(f"Zápas vyhral/-a {šanca1}, prehrávaš stávku")
        else:
            print(f"Zápas vyhral/-a {šancax}, prehrávaš stávku")