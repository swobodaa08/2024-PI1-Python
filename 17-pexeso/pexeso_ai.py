import random
import os
import time

# Vygenerujeme páry kariet (8 párov pre 4x4)
def generate_board():
    symbols = list("A B C D E F G H".split()) * 2
    random.shuffle(symbols)
    return [symbols[i*4:(i+1)*4] for i in range(4)]

# Hracia plocha s odhalenými kartami
def create_mask():
    return [["*" for _ in range(4)] for _ in range(4)]

# Pomocná funkcia na zobrazenie stavu
def display(mask):
    print("   1  2  3  4")
    for i, row in enumerate(mask):
        print(chr(65+i), " ".join(f" {c}" for c in row))

# Prevod zadania ako "A1" na indexy
def parse_input(pos):
    row = ord(pos[0].upper()) - 65
    col = int(pos[1]) - 1
    return row, col

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Hlavná hra
def play():
    board = generate_board()
    mask = create_mask()
    found = 0

    while found < 8:
        clear_screen()
        display(mask)
        print("\nZadaj prvú kartu (napr. A1):")
        pos1 = input(" > ").strip()
        r1, c1 = parse_input(pos1)
        mask[r1][c1] = board[r1][c1]

        clear_screen()
        display(mask)
        print("\nZadaj druhú kartu (napr. B2):")
        pos2 = input(" > ").strip()
        r2, c2 = parse_input(pos2)
        mask[r2][c2] = board[r2][c2]

        clear_screen()
        display(mask)

        if board[r1][c1] == board[r2][c2] and (r1, c1) != (r2, c2):
            print("\n✔️  Správny pár!")
            found += 1
        else:
            print("\n❌ Nesprávny pár. Skúste znova.")
            time.sleep(2)
            mask[r1][c1] = "*"
            mask[r2][c2] = "*"

    print("\n🎉 Gratulujem, našiel si všetky páry!")

if __name__ == "__main__":
    play()