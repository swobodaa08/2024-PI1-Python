retazec = input("Zadaj retazec: ")

def vypis():
    dlzka = len(retazec)
    print(f"Dĺžka reťazca je {dlzka}")
    for znak in retazec:
        print(znak)
    print("")
    for a in range(dlzka, 0, -1):
        a = a - 1
        print(retazec[a])
    print("")
    for i in range(dlzka):
        for tri in range(3):
            print(retazec[i],end="")
        print()
        i += 1

vypis()

# print(dlzka)