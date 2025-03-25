import random

list = [-4, -3, -2, -1, 1, 2, 3, 4]

# while True:
#     cislo = random.choice(list)
#     text = input("Zadaj input: ")
#     zasifrovane = ""
    
#     for i in text:
#         zasifrovane += chr(ord(i) + cislo)
    
#     print(zasifrovane)
#     if cislo > 0:
#         print(f"Zašifrovali sme každý znak o {cislo} znaky dopredu")
#     else:
#         print(f"Zašifrovali sme každý znak o {cislo} znaky dozadu")

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


while True:
    print("[1] pre zasifrovanie")
    print("[2] pre rozsifrovanie")
    print("[3] pre ukoncenie")
    print("[4] pre generator nahodneho hesla")

    choice = int(input("Vyber cislo: "))
    text2 = ""

    if choice == 1:
        text = input("Zadaj text: ")
        text = text.lower()
        for i in text:
            char = ord(i)+1
            if char == 123:
                char = 97
            text2 += chr(char)
        print("Zasifrovany text: ",text2)
        print("----------------")

    elif choice == 2:
        text = input("Zadaj text: ")
        text = text.lower()
        for i in text:
            char = ord(i)-1
            if char == 96:
                char = 122
            text2 += chr(char)
        print("Rozsifrovany text:",text2)
        print("----------------")
        
    elif choice == 3:
        break

    elif choice == 4:
        for i in range(random.randint(8,16)):
            text2 += chr(random.randint(1,390))
        print(f"Random heslo : {text2}")
        print("----------------")
    else:
        print("zla volba")
        print("----------------")