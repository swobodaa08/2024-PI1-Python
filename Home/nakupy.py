pocet_nakupov = 0
koniec = 0
vypocet = 0
while koniec == 0:
    vypocet = vypocet + float(input("Zadaj hodnotu tvojho nákupu: "))
    pocet_nakupov = pocet_nakupov + 1
    if pocet_nakupov > 19:
        koniec = koniec + 1
        print(f"Počet nákupov je {pocet_nakupov} a výsledná cena je {vypocet}€")