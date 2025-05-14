import random

class Futbalista:
    def __init__(self, meno, timy, urovne):
        self.meno = meno
        self.klub = random.choice(timy)
        self.cena = random.choice(urovne) * random.randint(650, 945)
    def showcase(self):
        print(f"\n{self.meno} je futbalista za tím {self.klub}, jeho trhová hodnota je {self.cena}€\n")

timy = []
urovne = []
with open("Home/Spameak_kody/Spameak_Casino/timy_futbal.txt", "r") as f:
    for riadok in f:
        nazov, hodnotenie = riadok.strip().split(',')
        timy.append(nazov)
        timy.append(hodnotenie)
        urovne.append(int(hodnotenie))

sutek = Futbalista("Samuel Sutek", timy, urovne)
svoboda = Futbalista("Samuel Svoboda", timy, urovne)
sopor = Futbalista("David Sopor", timy, urovne)
mitka = Futbalista("Martin Mitka", timy, urovne)

svoboda.showcase()
sutek.showcase()
sopor.showcase()
mitka.showcase()