meno = input('Zadaj svoje meno: ')
priezvisko = input('Zadaj priezvisko: ')
rok = int(input('Zadaj rok narodenia: '))
vek = 2024 - rok
if vek < 18 :
    print("You cant open this website if you are under 18")
else:
    print('Ahoj', meno, priezvisko, 'tvoj vek je', vek, 'rokov.')