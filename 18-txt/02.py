try:
    subor = open("18-txt/subor.txt", "r") 

    while True:
        riadok = subor.readline()
        if riadok == "":
            break
        print(riadok.strip()) # strip odstrani necitatelne znaky napr. \n, \t

    subor.close() # zatvori subor
except:
    print("subor neexistuje")