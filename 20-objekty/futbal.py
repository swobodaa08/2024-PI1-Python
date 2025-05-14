import random

class Futbalista:
    def __init__(self, meno, priezvisko, rocnik, timy, urovne):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rocnik = rocnik
        self.klub = random.choice(timy)
        self.cena = random.choice(urovne) * random.randint(650, 945)
    def showcase(self):
        print(f"\n{self.meno} {self.priezvisko} je odteraz futbalista za tím {self.klub}, narodil sa v roku {self.rocnik} a jeho trhová hodnota bude {self.cena}€")

timy = []
urovne = []
with open("Home/Spameak_kody/Spameak_Casino/timy_futbal.txt", "r") as f:
    for riadok in f:
        nazov, hodnotenie = riadok.strip().split(',')
        timy.append(nazov)
        urovne.append(int(hodnotenie))

while True:
    meno = input("\n--- Pridanie nového hráča do systému ---\nZadaj meno: ")
    priezvisko = input("Zadaj priezvisko: ")
    rocnik = int(input("Zadaj rok narodenia: "))
    novy_hrac = Futbalista(meno, priezvisko, rocnik, timy, urovne)

    novy_hrac.showcase()

    subor = open("20-objekty/hraci.txt", "a", encoding="UTF-8")
    subor.write(f"{meno} {priezvisko}, {rocnik}, {novy_hrac.klub}, {novy_hrac.cena}€\n")
    subor.close()