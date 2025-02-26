import random
import time

# Predmety v bedni (môžeš pridať vlastné)
items = [
    "P90 | Asiimov",
    "AK-47 | Redline",
    "AWP | Dragon Lore",
    "M4A4 | Howl",
    "Desert Eagle | Blaze",
    "USP-S | Orion",
    "Glock-18 | Water Elemental",
    "No item (Unlucky)"
]

# Funkcia na simulovanie otvárania bedne
def open_case():
    print("Otvaram bednu... prosím čakaj!")
    time.sleep(2)  # Pauza na simuláciu otvárania bedne
    # Náhodne vyberieme predmet zo zoznamu
    item = random.choice(items)
    
    # Efekt zobrazenia predmetu
    if item == "No item (Unlucky)":
        print("Nezískal si žiadny vzácny predmet. Skús to znova.")
    else:
        print(f"Gratulujeme! Získal si: {item}")

# Hlavný program
def main():
    print("Vitaj v simulácii otvárania bední!")
    while True:
        input("Stlač Enter na otvorenie bedne...")
        open_case()
        again = input("Chceš otvoriť ďalšiu bedňu? (áno/nie): ").strip().lower()
        if again != "áno":
            print("Ďakujeme za hranie! Uvidíme sa nabudúce!")
            break

if __name__ == "__main__":
    main()