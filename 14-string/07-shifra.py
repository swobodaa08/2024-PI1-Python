import random

list = [-4, -3, -2, -1, 1, 2, 3, 4]

while True:
    cislo = random.choice(list)
    text = input("Zadaj input: ")
    zasifrovane = ""
    
    for i in text:
        zasifrovane += chr(ord(i) + cislo)
    
    print(zasifrovane)
    if cislo > 0:
        print(f"Zašifrovali sme každý znak o {cislo} znaky dopredu")
    else:
        print(f"Zašifrovali sme každý znak o {cislo} znaky dozadu")

# print(ord("d"))
# print(ord("u"))
# print(ord("s"))
# print(ord("a"))
# print(ord("n"))
# print(ord("e"))
# print(ord("v"))
# print(ord("t"))
# print(ord("b"))
# print(ord("o"))