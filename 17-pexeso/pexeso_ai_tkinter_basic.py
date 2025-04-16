import tkinter as tk
import random
from math import ceil

# Globálne premenné
symbols = list("A B C D E F G H".split()) * 2
random.shuffle(symbols)
board = [symbols[i*4:(i+1)*4] for i in range(4)]

revealed = [[False for _ in range(4)] for _ in range(4)]
buttons = [[None for _ in range(4)] for _ in range(4)]
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
    if found_pairs[0] == 8:
        for row in buttons:
            for btn in row:
                btn.config(state="disabled")
        uspesnost = (8 / pokusy) * 100
        uspesnost = ceil(uspesnost)
        win_label = tk.Label(root, text=f"🎉 Vyhral si! \n Počet odokrytí : {pokusy} \n Úspešnosť odokrytí : {uspesnost}%", font=("Arial", 16), fg="green")
        win_label.grid(row=5, column=0, columnspan=4, pady=10)

# Vytvorenie GUI
root = tk.Tk()
root.title("Pexeso 4x4")

for r in range(4):
    for c in range(4):
        btn = tk.Button(root, text=" ", width=6, height=3,
                        font=("Arial", 16), bg="lightgray",
                        command=lambda r=r, c=c: on_click(r, c))
        btn.grid(row=r, column=c, padx=5, pady=5)
        buttons[r][c] = btn

root.mainloop()