# load_skinov = open("ALL_SKINS.txt", "r", encoding="UTF-8")

# for info in load_skinov:
#     skin, rarity, collection, date = (info.split(","))
#     print(skin)
#     print(rarity)
#     print(collection)
#     print(date)

import random
import time

# Načítanie skinov zo súboru
def nacitaj_skiny(subor):
    with open(subor, 'r', encoding='utf-8') as f:
        return [riadok.strip() for riadok in f.readlines() if riadok.strip()]

# Simulácia otvárania kejsy
def otvor_kejsku(skiny):
    print("🎁 Otváram bedničku...")
    time.sleep(1)

    # Simulácia prechádzania skinov (animácia)
    for _ in range(10):
        print("➡️ ", random.choice(skiny))
        time.sleep(0.1)

    vyhrany_skin = random.choice(skiny)
    print("\n🎉 Vyhral si:", vyhrany_skin)
    return vyhrany_skin

# Hlavný program
def main():
    skiny = nacitaj_skiny('ALL_Skins.txt')
    if not skiny:
        print("❌ Súbor je prázdny alebo chýba!")
        return

    while True:
        input("\nStlač Enter pre otvorenie bedničky...")
        otvor_kejsku(skiny)

        volba = input("\nChceš otvoriť ďalšiu bedničku? (áno/nie): ").lower()
        if volba != 'áno':
            print("👋 Zbohom!")
            break

if __name__ == '__main__':
    main()
