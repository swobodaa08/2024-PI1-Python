# uzivatel zada celu vetu a program vetu rozdeli na slova, ktore vypise nahodnou farbou na nahodnom mieste
# aj pismenka zo slov vypise nahodnymi farbami
# nastudovat retazce

import tkinter as tk
import random

# canvas = tk.Canvas()
# canvas.pack()

def vypocet_slov():
    pocet_medzier = 0
    for pismeno in veta:
        if pismeno == chr(32):
            pocet_medzier += 1
    return pocet_medzier

def jedno_slovo():
    global dlzka_slova, slovo
    for pismeno in (veta[dlzka_slova::]):
        if ord(pismeno) == 32:
            break
        else:
            slovo += pismeno
            dlzka_slova += 1
    print(slovo, dlzka_slova)

veta = input("Zadaj vetu: ")
dlzka_slova = 0
slovo = ""

for i in range(vypocet_slov()+1):
    jedno_slovo()



# tk.mainloop()