# print(bin(255)) # vypise cislo v binarnej podobe
# print(hex(255)) # vypise cislo v hexadecimalnej podobe
# print(0b11111111) # vypise binarne cislo v desiatkovej podobe
# print(0xff) # vypise hexadecimalne cislo v desiatkovej podobe

def dec_bin(cislo):
    binarne = ""
    while cislo > 0:
        zvysok = cislo % 2
        binarne = str(zvysok) + binarne
        cislo = cislo // 2
    return binarne

def dec_hex(cislo):
    hexadecimalne = ""
    while cislo > 0:
        zvysok = cislo % 16
        if zvysok >= 10:
            hexadecimalne = chr(55 + zvysok) + hexadecimalne
        # if zvysok == 10:
        #     hexadecimalne = "A" + hexadecimalne
        # elif zvysok == 11:
        #     hexadecimalne = "B" + hexadecimalne
        # elif zvysok == 12:
        #     hexadecimalne = "C" + hexadecimalne
        # elif zvysok == 13:
        #     hexadecimalne = "D" + hexadecimalne
        # elif zvysok == 14:
        #     hexadecimalne = "E" + hexadecimalne
        # elif zvysok == 15:
        #     hexadecimalne = "F" + hexadecimalne
        else:
            hexadecimalne = str(zvysok) + hexadecimalne
        cislo = cislo // 16
    return hexadecimalne

def dec_oct(cislo):
    octanove = ""
    while cislo > 0:
        zvysok = cislo % 8
        if zvysok >= 10:
            octanove = chr(55 + zvysok) + octanove
        else:
            octanove = str(zvysok) + octanove
        cislo = cislo // 8
    return octanove

while True:
    print("[1] pre premenu na binarnu sustavu")
    print("[2] pre premenu na hexadecimalnu sustavu")
    print("[3] pre premenu na octanovu sustavu")

    choice = int(input("Vyber premenu ktoru chces pouzit: "))

    if choice == 1:
        cislo = int(input("Zadaj cislo (0-255): "))
        if -1 < cislo < 256:
            print("-----------------------------------------------------")
            print(f"Zadane cislo v binarnej sustave je: {dec_bin(cislo)}")
            print("-----------------------------------------------------")
            continue

    if choice == 2:
        cislo = int(input("Zadaj cislo (0-4294967295): "))
        if -1 < cislo < 4294967296:
            print("-----------------------------------------------------")
            print(f"Zadane cislo v binarnej sustave je: {dec_hex(cislo)}")
            print("-----------------------------------------------------")
            continue
    
    if choice == 3:
        cislo = int(input("Zadaj cislo (0-16777215): "))
        if -1 < cislo < 16777216:
            print("-----------------------------------------------------")
            print(f"Zadane cislo v osmickovej sustave je: {dec_oct(cislo)}")
            print("-----------------------------------------------------")
            continue
