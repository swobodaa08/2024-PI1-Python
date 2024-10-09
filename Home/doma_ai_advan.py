pokus = 0
max_pokusov = 5
spravny_email = "svobodas2008@gmail.com"
spravne_heslo = "Poprad123"

while pokus < max_pokusov:
    e = input("Zadaj svoj email: ")

    if e == spravny_email:
        heslo2 = input("Zadaj svoje heslo: ")
        if heslo2 == spravne_heslo:
            print("Vitaj vo svojom profile!")
            break  # Zastaví cyklus, pokud je heslo správné
        else:
            print("Nesprávne heslo, skús to znova.")
            pokus += 1
    else:
        print("Nesprávny email.")
        pokus += 1

    if pokus == max_pokusov:
        print("Maximálny počet pokusov bol vyčerpaný...")