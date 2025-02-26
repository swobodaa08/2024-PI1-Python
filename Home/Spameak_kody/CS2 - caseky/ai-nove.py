import tkinter as tk
from tkinter import PhotoImage
import random
import time
from PIL import Image, ImageTk

class CaseOpener:
    def __init__(self, root):
        self.root = root
        self.root.title("CS2 Case Opener")
        self.root.geometry("600x500")
        
        # Nastavenie obrázkov skinov
        self.skins = [
            "skin1.jpg",
            "skin2.jpg",
            "skin3.jpg",  # Tieto obrázky musíš nahradiť správnymi obrázkami, ktoré máš.
            "skin4.jpg",
            "skin5.jpg"
        ]
        
        self.case_image = Image.open("case.jpg")  # Predstavuje obrázok bedne
        self.case_image = self.case_image.resize((200, 200))  # Zmenšíme obrázok na požiadanu veľkosť
        self.case_image_tk = ImageTk.PhotoImage(self.case_image)

        # Vytvorte widgety
        self.case_label = tk.Label(self.root, image=self.case_image_tk)
        self.case_label.pack(pady=20)
        
        self.open_button = tk.Button(self.root, text="Otvoriť Bednu", command=self.open_case)
        self.open_button.pack(pady=10)
        
        self.skin_label = tk.Label(self.root)
        self.skin_label.pack(pady=20)

    def open_case(self):
        # Pre animáciu otvárania bedne
        for i in range(5):
            self.case_label.config(image="")
            self.root.update()
            time.sleep(0.1)
            self.case_label.config(image=self.case_image_tk)
            self.root.update()
            time.sleep(0.1)

        # Po animácii zobraziť náhodný skin
        chosen_skin = random.choice(self.skins)
        skin_image = Image.open(chosen_skin)
        skin_image = skin_image.resize((300, 300))  # Nastaviť rozmer pre zobrazenie
        skin_image_tk = ImageTk.PhotoImage(skin_image)
        
        self.skin_label.config(image=skin_image_tk)
        self.skin_label.image = skin_image_tk  # Uchováme referenciu na obrázok

# Vytvorenie hlavného okna
root = tk.Tk()
case_opener = CaseOpener(root)
root.mainloop()
