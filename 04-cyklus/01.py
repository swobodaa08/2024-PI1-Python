# for je prikaz cyklu s pevnym poctom opakovani (pocet opakovani je nam vopred znamy)
# premenna i je riadiaca premenna cyklu, ktora sa pri kazdom opakovani zvysuje o 1, kym je mensia ako "n"
# pociatocna hodnota i je 0
# ak bude n = 5, tak i bude postupne : (0,1,2,3,4)

n = 5
for i in range(n):
    print(i+1, "Ahoj Svet!")