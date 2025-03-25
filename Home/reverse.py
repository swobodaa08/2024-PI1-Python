string = input("Zadaj hocijake slovo: ")
string2 = string[::-1]
output = ""
for pismeno in string2:
    output = output + pismeno
print(output)