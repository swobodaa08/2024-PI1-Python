vstup = input('zadaj: ')
pocet = 0
retazec1 = retazec2 = ''
for znak in vstup:
    retazec1 = retazec1 + znak
    retazec2 = znak + retazec2
print('počet znakov reťazca =', len(vstup))
print('retazec1 =', retazec1)
print('retazec2 =', retazec2)