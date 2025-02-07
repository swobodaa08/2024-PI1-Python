print("--------------------------------------------------------------------")
print("Vitaj v SpameakCalc 2024")
print("SpameakCalc ti vypočíta tvoj čistý príjem na základe zadaných údajov")
print("Staćí zadať hrubú mzdu a počet detí")
print("PLATÍ PRE ROK 2024 !!!")
print("--------------------------------------------------------------------")

hruba_mzda = float(input("Zadaj svoju hrubú mzdu v €: "))
pocet_deti_do18 = int(input("Máś nejaké deti do 18 rokov? Ak hej, koľko? (Ak nemáš, napíš nulu): "))

def vypocet():
    global cisty_prijem
    odvody_socialne_poistovne = (hruba_mzda / 100) * 9.4
    preddavky_do_zdravotnej_poistovne = (hruba_mzda / 100) * 4
    poistenie_zamestnavatela = odvody_socialne_poistovne + preddavky_do_zdravotnej_poistovne
    ciastkovy_zaklad_dane = hruba_mzda - poistenie_zamestnavatela
    nezdanitelna_cast = 470.54
    zaklad_dane = ciastkovy_zaklad_dane - nezdanitelna_cast
    preddavok_za_dan_z_prijmov = (zaklad_dane / 100) * 19
    bonus_za_deti = pocet_deti_do18 * 140
    cisty_prijem = hruba_mzda - poistenie_zamestnavatela - preddavok_za_dan_z_prijmov + bonus_za_deti

vypocet()

round(cisty_prijem, 2)

print(f"Tvoj čistý mesačný príjem je {cisty_prijem}€, parada")