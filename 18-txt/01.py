subor = open("18-txt\subor.txt", "r") 
# open otvori subor txt na citanie, pre zapis je "w" - ak subor neexistuje, program vypise chybu
# subor = open("subor.txt", "r") = relative path
# subor = open("Z:\2024-PI1-Python\2024-PI1-Python\18-txt\subor.txt", "r") = absolute path
# subor = open("../16-list/subor.txt", "r") .. je o priecinok vyssie

# for _ in range(4):
#     riadok = subor.readline() # readline precita cely riadok (odkial sa prave nachadza) zo suboru a ulozi do premennej (riadok)
#     print(riadok)

# riadok = subor.readline()
# while riadok != '':
#     print(riadok)
#     riadok = subor.readline()

while True:
    riadok = subor.readline()
    if riadok == "":
        break
    print(riadok.strip()) # strip odstrani necitatelne znaky napr. \n, \t

subor.close() # zatvori subor