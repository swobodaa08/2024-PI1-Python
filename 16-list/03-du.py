# min a max teplota v ktorom dni


import random
import math

teploty = []
pocet_dni = 15

for i in range(pocet_dni):
    # teploty[i] = random.randint(10, 30) # vrati chybu, lebo prvky este neexistuju
    teploty.append(random.randint(-30, 40))


def biggest(teploty):
    najvacsie = teploty[0]
    for cislo in teploty:
        if cislo > najvacsie: najvacsie = cislo
    return najvacsie

def smallest(teploty):
    najmensie = teploty[0]
    for cislo in teploty:
        if cislo < najmensie: najmensie = cislo
    return najmensie

print(teploty)
print(max(teploty))
print(biggest(teploty))
print(smallest(teploty))
print(min(teploty))