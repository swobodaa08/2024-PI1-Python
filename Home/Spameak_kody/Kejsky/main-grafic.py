import tkinter as tk
import random
import time
from threading import Thread

# Načítanie skinov zo súboru
def nacitaj_skiny(subor):
    try:
        with open(subor, 'r', encoding='utf-8') as f:
            return [riadok.strip() for riadok in f.readlines() if riadok.strip()]
    except FileNotFoundError:
        return ["Skiny sa nenašli"]

class CaseOpenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎁 Case Opener")
        self.root.geometry("600x300")
        self.root.resizable(False, False)

        self.skiny = nacitaj_skiny("skin_list.txt")

        # GUI prvky
        self.label = tk.Label(root, text="Stlač 'Otvoriť bedničku'", font=("Arial", 20), pady=20)
        self.label.pack()

        self.button = tk.Button(root, text="Otvoriť bedničku", font=("Arial", 16), command=self.spusti_otvaranie)
        self.button.pack()

        self.vyherny_label = tk.Label(root, text="", font=("Arial", 24, "bold"), fg="green")
        self.vyherny_label.pack(pady=20)

    def spusti_otvaranie(self):
        # Vypneme tlačidlo počas animácie
        self.button.config(state=tk.DISABLED)
        self.vyherny_label.config(text="")

        # Animácia v samostatnom vlákne (aby GUI nezamrzol)
        thread = Thread(target=self.animuj_otvaranie)
        thread.start()

    def animuj_otvaranie(self):
        for i in range(25):  # počet prechodov skinov
            skin = random.choice(self.skiny)
            self.label.config(text=f"➡️ {skin}")
            time.sleep(0.05 + i * 0.01)  # spomaľovanie efektu

        vyherny_skin = random.choice(self.skiny)
        self.label.config(text="🎉 Výhra:")
        self.vyherny_label.config(text=vyherny_skin)
        self.button.config(state=tk.NORMAL)

# Spustenie GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = CaseOpenerApp(root)
    root.mainloop()
