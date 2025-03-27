# uzivatel zada celu vetu a program vetu rozdeli na slova, ktore vypise nahodnou farbou na nahodnom mieste
# aj pismenka zo slov vypise nahodnymi farbami
# nastudovat retazce

import tkinter as tk

# canvas = tk.Canvas()
# canvas.pack()

def vypocet_medzier():
    pocet_medzier = 0
    for pismeno in veta:
        if pismeno == chr(32):
            pocet_medzier += 1
    return pocet_medzier

def jedno_slovo():
    slovo = ""
    dlzka_slova = 0
    for _ in range(vypocet_medzier()):
        for pismeno in (veta[dlzka_slova+1:]):
            dlzka_slova += 1
            if ord(pismeno) == 32:
                break
            else:
                slovo += pismeno
        print(slovo, dlzka_slova)

veta = input("Zadaj vetu: ")

for i in range(vypocet_medzier()+1):
    jedno_slovo()



# tk.mainloop()