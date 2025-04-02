import random

teploty = []
pocet_dni = 30
suma = 0

# naplni list teploty nahodnymi teplotnymi z rozsahu od 10 do 30

for i in range(pocet_dni):
    # teploty[i] = random.randint(10, 30) # vrati chybu, lebo prvky este neexistuju
    teploty.append(random.randint(10, 30))

for i in range(pocet_dni):
    print(f"{i+1}.deň - {teploty[i]}°C")

# priemerna = sum(teploty) / pocet_dni 

for i in range(pocet_dni):
    suma += teploty[i]

priemerna = suma / pocet_dni
podpriemerna = []

for teplota in teploty:
    if teplota < priemerna:
        podpriemerna.append(f"{teplota+1}.deň - {teplota}°C")

print(f"Priemerná teplota za {pocet_dni} dní je : {priemerna:.2f}°C") #:.2f naformatuje vystup float na dve desatinne miesta

print(f"Dni s podpriemernou teplotou: {podpriemerna}")