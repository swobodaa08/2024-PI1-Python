# SpameakGamba Beta v3.2 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] # SpameakGamba Beta v3.0 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] 



# Import
import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os

konto = 0  # Počiatočná hodnota premennej eur

# Funkcia na načítanie progresu podľa priezviska
def load_progress(priezvisko):
    file_name = f"{priezvisko}_progress.pkl"
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)
    return 0  # Ak súbor neexistuje, začni s 0 eurami

# Funkcia na uloženie progresu podľa priezviska
def save_progress(priezvisko, progress):
    file_name = f"{priezvisko}_progress.pkl"
    with open(file_name, "wb") as f:
        pickle.dump(progress, f)

# Funkcia na aktualizáciu eur
def my_upd():
    global konto
    konto += 1
    b1.config(text=f"Máš : {konto}€")

# Funkcia na uloženie progresu po zadaní priezviska
def save_prompt():
    global konto
    priezvisko = simpledialog.askstring("Uložiť progres", "Zadajte svoje priezvisko:")
    if priezvisko:
        save_progress(priezvisko, konto)
        messagebox.showinfo("Uložené", f"Progres bol uložený pre priezvisko {priezvisko}!")

# Funkcia na ukončenie programu
def exit_program():
    okno.quit()
    okno.destroy()

# Získanie priezviska na začiatku
root = tk.Tk()
root.withdraw()  # Skryje hlavné okno počas zadávania priezviska
priezvisko = simpledialog.askstring("Prihlásenie", "Zadajte svoje priezvisko:")
root.deiconify()  # Znova zobrazí hlavné okno

if priezvisko:
    konto = load_progress(priezvisko)
    root.destroy()  # Zatvorí okno priezviska a inicializuje hlavné okno

    # Inicializácia hlavného okna
    okno = tk.Tk()
    okno.attributes('-fullscreen', True)
    okno.title("SpameakGamble")
    okno.geometry("1920x1080")

    # Tlačidlo na rátanie žetónov (zarovnané do stredu)
    b1 = tk.Button(okno, text=f"Počet žetónov : {konto}", width=20,
                   command=my_upd, bg="lime", font=('Helvetica', '20', 'bold'))
    b1.place(relx=0.5, rely=0.5, anchor='center')  # Centrálne umiestnenie

    # Tlačidlo na uloženie progresu (zarovnané do pravého horného rohu)
    save_button = tk.Button(okno, text="Save", command=save_prompt, bg="yellow", font=('Helvetica', '12', 'bold'))
    save_button.place(relx=0.95, rely=0.05, anchor='ne')  # Zarovná do pravého horného rohu

    # Tlačidlo na ukončenie programu (zarovnané do pravého dolného rohu)
    exit_button = tk.Button(okno, text="Koniec", command=exit_program, bg="red", font=('Helvetica', '12', 'bold'))
    exit_button.place(relx=0.95, rely=0.95, anchor='se')  # Zarovná do pravého dolného rohu

    okno.mainloop()
else:
    messagebox.showinfo("Chyba", "Nebolo zadané priezvisko. Program sa ukončí.")
