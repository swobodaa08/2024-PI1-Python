subor = open("18-txt/subor2.txt", "w") # otvori subor na zapis a ak subor neexistuje tak sa vytvori "w", ak existuje, tak sa zmaze cely obsah
# subor.write("Ahoj\n")
# subor.write("ako\n")
# subor.write("sa\n")
# subor.write("mas?")
print("ahoj", file=subor)
print("ahoj", file=subor)

subor.close()