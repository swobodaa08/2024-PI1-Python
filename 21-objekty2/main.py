import datetime

class Osoba: # triedy vzdy piseme velkym prvym pismenom
    def __init__(self, meno, priezvisko, rok): # konštruktor, zavola sa pri vzniku objektu
        self.meno = meno # atribut objektu (vlastnost)
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok

    def pozdrav(self): # metoda objektu (co vie objekt robit)
        print(f"Ahoj, ja som {self.meno} {self.priezvisko} a mám {self.vek} rokov.")

    def vypis_meno(self):
        print(self.meno, self.priezvisko)

    def vypis_vek(self):
        print(self.vek)
    
    def vypis_rok(self):
        print(self.rok)

class Student(Osoba):  # trieda student zdedí atributy a metody od triedy osoba
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok) # super - znamena, ze pouzije atributy z rodicovskej triedy Osoba
        # Osoba.__init__(meno, priezvisko, rok) 
        self.trieda = trieda
    
    def pozdrav(self):
        super().pozdrav()
        print(f"Som študenom {self.trieda} triedy.")
        # polymorfizmus - menime metodu pozdrav z rodicovskej triedy Osoba

# samo = Osoba("Samuel", "Svoboda", 2008) # vznikne objekt samo vytvoreny pomocou triedy Osoba
# samo.pozdrav() # volam metodu objektu pozdrav()
# samo.vypis_meno()
# samo.vypis_rok()
# samo.vypis_vek()
# fero = Osoba("František", "Tichý", 1978)
# fero.pozdrav()


student = Student("Samuel", "Svoboda", 2008, "1.AT")
student.pozdrav()