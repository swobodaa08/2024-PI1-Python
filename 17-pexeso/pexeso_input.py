import tkinter as tk
import random
import math

# Globálne premenné

try:
    vstup = int(input("Zadaj, koľko na párov chceš hrať?: "))
    if vstup == 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16:
        pass
    else:
        print("Zadaj počet párov od 4 do 16 !!")
except ValueError:
    print("Zadaj číslo")

symbols = list("A B C D E F G H".split()) * 2
random.shuffle(symbols)
board = [symbols[i*(vstup/2):(i+1)*(vstup/2)] for i in range((vstup))]

revealed = [[False for _ in range((vstup/2))] for _ in range((vstup/2))]
buttons = [[None for _ in range((vstup/2))] for _ in range((vstup/2))]
first_click = [None]  # uložené ako zoznam kvôli mutácii v rámci funkcie
locked = [False]
found_pairs = [0]
pokusy = 0

def on_click(r, c):
    global pokusy
    if locked[0] or revealed[r][c]:
        return

    buttons[r][c].config(text=board[r][c], bg="white")

    if first_click[0] is None:
        first_click[0] = (r, c)
    else:
        r1, c1 = first_click[0]
        r2, c2 = r, c

        if (r1, c1) == (r2, c2):
            return  # rovnaké kliknutie

        locked[0] = True
        if board[r1][c1] == board[r2][c2]:
            buttons[r1][c1].config(bg="lime")
            buttons[r][c].config(bg="lime")
            revealed[r1][c1] = True
            revealed[r2][c2] = True
            found_pairs[0] += 1
            root.after(500, check_win)
        else:
            root.after(1000, lambda: hide_cards(r1, c1, r2, c2))

        first_click[0] = None
        pokusy += 1

def hide_cards(r1, c1, r2, c2):
    buttons[r1][c1].config(text=" ", bg="lightgray")
    buttons[r2][c2].config(text=" ", bg="lightgray")
    locked[0] = False

def check_win():
    locked[0] = False
    if found_pairs[0] == vstup:
        for row in buttons:
            for btn in row:
                btn.config(state="disabled")
        uspesnost = (vstup / pokusy) * 100
        uspesnost = math.ceil(uspesnost)
        win_label = tk.Label(root, text=f"🎉 Vyhral si! \n Počet odokrytí : {pokusy} \n Úspešnosť odokrytí : {uspesnost}%", font=("Arial", 16), fg="green")
        win_label.grid(row=5, column=0, columnspan=4, pady=10)

# Vytvorenie GUI
root = tk.Tk()
root.title(f"Pexeso {vstup/2}x{vstup/2}")

for r in range((vstup/2)):
    for c in range((vstup/2)):
        btn = tk.Button(root, text=" ", width=6, height=3,
                        font=("Arial", 16), bg="lightgray",
                        command=lambda r=r, c=c: on_click(r, c))
        btn.grid(row=r, column=c, padx=5, pady=5)
        buttons[r][c] = btn

root.mainloop()