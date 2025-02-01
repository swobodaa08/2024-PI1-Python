import tkinter as tk
import random
from tkinter import messagebox
import time

# Slot symbols
SYMBOLS = ['🍒', '🍋', '🍉', '⭐', '💰']
PAYOUTS = {
    ('🍒', '🍒', '🍒'): 5,
    ('🍋', '🍋', '🍋'): 10,
    ('🍉', '🍉', '🍉'): 20,
    ('⭐', '⭐', '⭐'): 50,
    ('💰', '💰', '💰'): 100,  # Jackpot
}

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")
        
        self.balance = 100  # Starting balance
        self.bet = 5  # Default bet

        # Labels for balance and bet
        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance}", font=("Arial", 14))
        self.balance_label.pack()
        
        self.bet_label = tk.Label(root, text=f"Bet: ${self.bet}", font=("Arial", 12))
        self.bet_label.pack()
        
        # Slot reels
        self.reel_labels = []
        self.reel_frames = []
        
        for i in range(3):
            frame = tk.Frame(root, width=80, height=80)
            frame.pack(side=tk.LEFT, padx=10)
            label = tk.Label(frame, text=random.choice(SYMBOLS), font=("Arial", 40))
            label.pack()
            self.reel_frames.append(frame)
            self.reel_labels.append(label)
        
        # Spin button
        self.spin_button = tk.Button(root, text="Spin", command=self.spin, font=("Arial", 14))
        self.spin_button.pack()
        
        # Bet adjustment buttons
        self.increase_bet = tk.Button(root, text="+", command=self.increase_bet, font=("Arial", 12))
        self.increase_bet.pack(side=tk.LEFT)
        self.decrease_bet = tk.Button(root, text="-", command=self.decrease_bet, font=("Arial", 12))
        self.decrease_bet.pack(side=tk.LEFT)
    
    def spin(self):
        if self.balance < self.bet:
            messagebox.showerror("Error", "Not enough balance!")
            return
        
        self.balance -= self.bet
        
        # Spinning animation with downward scrolling effect
        for _ in range(15):
            for label in self.reel_labels:
                label.config(text=random.choice(SYMBOLS))
            self.root.update()
            time.sleep(0.05)
        
        # Final spin result
        results = [random.choice(SYMBOLS) for _ in range(3)]
        for i in range(3):
            self.reel_labels[i].config(text=results[i])
        
        self.check_win(tuple(results))
        self.balance_label.config(text=f"Balance: ${self.balance}")
    
    def check_win(self, results):
        if results in PAYOUTS:
            winnings = self.bet * PAYOUTS[results]
            self.balance += winnings
            self.balance_label.config(text=f"Balance: ${self.balance}")
            messagebox.showinfo("You Win!", f"You won ${winnings}!")
    
    def increase_bet(self):
        if self.bet < self.balance:
            self.bet += 5
            self.bet_label.config(text=f"Bet: ${self.bet}")
    
    def decrease_bet(self):
        if self.bet > 5:
            self.bet -= 5
            self.bet_label.config(text=f"Bet: ${self.bet}")

if __name__ == "__main__":
    root = tk.Tk()
    game = SlotMachine(root)
    root.mainloop()