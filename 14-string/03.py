# range() - je funkcia ktora vygeneruje nejaku postupnost
# range(5) - postupnost 0,1,2,3,4
# range(od, pokial-1, krok)
# range moze mat aj klesajucu postupnost - range(5, 0, -1)

print(list(range(5)))
print(list(range(2, 5)))
print(list(range(2, 10, 2)))
print(list(range(5, 0, -1)))

ret = "Ahoj"
for i in range(len(ret)-1, -1, -1):
    print(ret[i])