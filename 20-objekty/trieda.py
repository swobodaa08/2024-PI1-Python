class Trieda:
    def __init__(self, prezyvka, meno, vek):
        self.prezyvka = prezyvka
        self.meno = meno
        self.vek = vek

    def showcase(self):
        print(f"Ahoj, ja som {self.prezyvka} a volám sa {self.meno}. Mám {self.vek} rokov.")

slivka = Trieda("cigan", "Alex Slivka", "16")
sopor = Trieda("sopor", "David Sopor", "16")
sutek = Trieda("sutek", "Samuel Sutek", "16")
vrskovy = Trieda("kubo", "Jakub Vrskovy", "16")
pokorny = Trieda("danko", "Daniel Pokorny", "16")
svoboda = Trieda("svoboda", "Samuel Svoboda", "16")
mitka = Trieda("martin", "Martin Mitka", "16")

ziaci = [slivka, sopor, sutek, vrskovy, pokorny, svoboda, mitka]
hladam = input("\nKoho hladas z 1.AT z druhej skupiny?: \n")

nasiel = False
for ziak in ziaci:
    if ziak.meno.lower() == hladam.lower():
        print(f"{hladam} sa nachádza v 1.AT v druhej skupine")
        ziak.showcase()
        nasiel = True

if nasiel == False:
    print("Nikto taký v 1.AT v druhej skupine nie je!")