rok = int(input("Zadaj rok tvojho narodenia: "))
mesiac = input("Zadaj v ktorom mesiaci si sa narodil: ")
if mesiac == "january":
    month = 1
if mesiac == "february":
    month = 2
if mesiac == "march":
    month = 3
if mesiac == "april":
    month = 4
if mesiac == "may":
    month = 5
if mesiac == "june":
    month = 6
if mesiac == "july":
    month = 7
if mesiac == "august":
    month = 8
if mesiac == "september":
    month = 9
if mesiac == "october":
    month = 10
if mesiac == "november":
    month = 11
if mesiac == "december":
    month = 12
vek_roku = 2024 - rok
if (month > 10):
    vypocet_mesiaca = month
else:
    vypocet_mesiaca = 10 - month

if (month > 10):
    print(f"Tvoj vek je {vek_roku - 1} rokov a {vypocet_mesiaca} mesiacov")
else:
    print(f"Tvoj vek je {vek_roku} rokov a {vypocet_mesiaca} mesiacov")