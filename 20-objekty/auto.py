import random

class Auto:
    def __init__(self, vlastnik, znacka, farba):
        self.vlastnik = vlastnik
        self.znacka = znacka
        self.farba = farba
        self.cena = random.randint(12000, 160000)
    def showcase(self):
        print(f"\nAuto používateľa {self.vlastnik} je {self.znacka}, farba auta je {self.farba} a predávam ho za cenu {self.cena}€\n")

sutek_car = Auto("Samuel Sutek", "Ferrari", "ružová")
svoboda_car = Auto("Samuel Svoboda", "Lamborghini", "žltá")
sopor_car = Auto("David Sopor", "BMW", "čierna")
mitka_car = Auto("Martin Ritka", "Lietajúce auto", "krídelná")
vrskovy_car = Auto("Jakub Vrskovy", "Fiat Multipla", "fialová")
svoboda_car.showcase()
sutek_car.showcase()
sopor_car.showcase()
mitka_car.showcase()
vrskovy_car.showcase()