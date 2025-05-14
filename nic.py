def sirka(meno_suboru):
    dlžka_max = 0
    with open(meno_suboru, 'r') as subor:
        for riadok in subor:
            dlžka = len(riadok)
            if dlžka > dlžka_max:
                dlžka_max = dlžka
    return dlžka_max

print(sirka("text1.txt"))
print(sirka("text2.txt"))