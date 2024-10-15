pocet = int(input("Zadaj počet bajtov: "))
pamat = 256 ** pocet - 1
if pocet == 0:
    pamat = 0
print(f"Maximálna hodnota je {pamat}")