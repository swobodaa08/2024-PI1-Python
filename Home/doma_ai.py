e = input("Zadaj svoj email: ")
if e == "svobodas2008@gmail.com":  # Zadaj celý email, ktorý sa očakáva
    heslo = "Poprad123"
    heslo2 = input("Zadaj svoje heslo: ")
    if heslo2 == heslo:
        print("Vitaj vo svojom profile!")
    else:
        print("Nesprávne heslo, skús to znova.")
else:
    print("Nesprávny email.")