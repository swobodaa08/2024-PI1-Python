import tkinter as tk
import random
from functools import partial

class Pexeso:
    def __init__(self, root):
        self.root = root
        self.root.title("Pexeso 4x4")

        self.symbols = list("R E G I N S < 3".split()) * 2
        random.shuffle(self.symbols)
        self.board = [self.symbols[i*4:(i+1)*4] for i in range(4)]

        self.buttons = [[None for _ in range(4)] for _ in range(4)]
        self.revealed = [[False for _ in range(4)] for _ in range(4)]

        self.first_click = None
        self.locked = False
        self.found_pairs = 0

        self.create_widgets()

    def create_widgets(self):
        for r in range(4):
            for c in range(4):
                btn = tk.Button(self.root, text=" ", width=6, height=3,
                                command=partial(self.on_click, r, c),
                                font=("Arial", 16), bg="lightgray")
                btn.grid(row=r, column=c, padx=5, pady=5)
                self.buttons[r][c] = btn

    def on_click(self, r, c):
        if self.locked or self.revealed[r][c]:
            return

        self.buttons[r][c].config(text=self.board[r][c], bg="white")
        if not self.first_click:
            self.first_click = (r, c)
        else:
            r1, c1 = self.first_click
            r2, c2 = r, c

            if (r1, c1) == (r2, c2):
                return  # same card clicked twice

            self.locked = True
            if self.board[r1][c1] == self.board[r2][c2]:
                self.revealed[r1][c1] = True
                self.revealed[r2][c2] = True
                self.found_pairs += 1
                self.root.after(500, self.check_win)
            else:
                self.root.after(1000, lambda: self.hide_cards(r1, c1, r2, c2))

            self.first_click = None

    def hide_cards(self, r1, c1, r2, c2):
        self.buttons[r1][c1].config(text=" ", bg="lightgray")
        self.buttons[r2][c2].config(text=" ", bg="lightgray")
        self.locked = False

    def check_win(self):
        self.locked = False
        if self.found_pairs == 8:
            for row in self.buttons:
                for btn in row:
                    btn.config(state="disabled")
            win_label = tk.Label(self.root, text="🎉 Výhra! Našiel si všetky páry!", font=("Arial", 16), fg="green")
            win_label.grid(row=5, column=0, columnspan=4, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = Pexeso(root)
    root.mainloop()