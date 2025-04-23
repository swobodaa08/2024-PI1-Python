# skombinovať mena a priezviska postupne 

fmena = open("18-txt/mena.txt", "r", encoding="UTF-8")
fpriezviska = open("18-txt/priezviska.txt", "r", encoding="UTF-8")
fmena_priezviska = open("18-txt/menaapriezviska.txt", "w", encoding="UTF-8")

for meno in fmena:
    priezvisko = fpriezviska.readline()
    print(f"{meno.strip()} {priezvisko.strip()}")
    fmena_priezviska.write(f"{meno} {priezvisko}")

fmena.close()
fpriezviska.close()
fmena_priezviska.close()