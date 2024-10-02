r = float(input("Zadaj polomer: "))     # float je funkcia na prevod textu do desatinneho cisla
# udajove typy:
#               string = reťazec znakov (text)
#               int = celé čísla
#               float = desatinne cisla
O = 2 * 3.14 * r    # desatinne cislo uvadzame vzdy s bodkou!!!
S = 3.14 * (r * r)
print("Obvod kruhu je: ", round(O, 2))  # round zaokruhli cislo resp. premennu, v nasom pripade O je premenna a 2 je pocet desatinnych miest
print("Obsah kruhu je: ", round(S, 2))