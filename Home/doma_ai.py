pokus = 0
if pokus == 5:
    print("Maximálny počet pokusov bol vyčerpaný...")
else:
    e = input("Zadaj svoj email: ")
    for pokus in range(5):
        if e == "svobodas2008@gmail.com":  # Zadaj celý email, ktorý sa očakáva
            heslo = "Poprad123"
            heslo2 = input("Zadaj svoje heslo: ")
        else:
            print("Nesprávny email.")
            pokus = pokus + 1

if heslo2 == heslo:
    print("Vitaj vo svojom profile!")
else:
    print("Nesprávne heslo, skús to znova.")