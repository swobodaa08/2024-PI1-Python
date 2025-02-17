import tkinter as tk
import random
from PIL import Image, ImageTk, ImageEnhance
from tkinter import simpledialog, messagebox

# Hlavne okno Gamba
gamba = tk.Tk()
gamba.attributes("-fullscreen", True)
gamba.title("SpameakGamba")
gamba.geometry("1920x1080")

# Zistenie rozlíšenia obrazovky
screen_width = gamba.winfo_screenwidth()
screen_height = gamba.winfo_screenheight()

# Vytvorenie Canvasu
canvas = tk.Canvas(gamba, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)

# Načítanie a prispôsobenie obrázka
image_path = "Spameak_Casino/Gamba.jpg"
background_image = Image.open(image_path)
background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Inicializácia jasného obrázka na pozadí
enhancer = ImageEnhance.Brightness(background_image)
brightness_factor = 1.3
bright_background_image = enhancer.enhance(brightness_factor)
background_photo = ImageTk.PhotoImage(bright_background_image)

# Nastavenie obrázka ako pozadia na Canvas
canvas_image = canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Názov Hry na Canvas
canvas.create_rectangle ((screen_width / 2) - 325,32,(screen_width / 2) + 325,132, fill="cyan")
canvas.create_text(screen_width / 2, 75, text="Spameak Gamba", font=("Helvetica", "50", "bold"))


# Definícia tlačidiel

počet_kôl = 0
suma = 0

def pokracovat():
    pokracovat_button.destroy()
    global background_photo
    # global konto
    brightness_factor = 0.3
    dark_background_image = enhancer.enhance(brightness_factor)
    background_photo = ImageTk.PhotoImage(dark_background_image)
    canvas.itemconfig(canvas_image, image=background_photo)
    kola = tk.Tk()
    kola.withdraw()
    while True:
        try:
            počet_kôl = simpledialog.askinteger("Počet Kôl", "Zadaj počet kôl, koľko chceš hrať:")
            if 0 < počet_kôl < 21:
                break
            else:
                messagebox.showinfo("Chyba", "Počet kôl musí byť od 1 do 20")
        except ValueError:
            messagebox.showinfo("Chyba", "Zadaj číslo od 1 do 20")
    kola.deiconify()

    for _ in range(počet_kôl):
    # Kontrola vstupu pre sumu
        peniaze = tk.Tk()
        peniaze.withdraw()
        peniaze.attributes("-topmost", True)
    while True:
        try:
            suma = simpledialog.askfloat("Suma", "Zadaj koľko € chceš vsadiť:")
            if suma is not None and 10000 >= suma >= 0.50:
                break
            else:
                messagebox.showinfo("Chyba", "Vklad musí byť aspoň 0.50€ a nemôže byť vyšší ako 10000€ na jednu hru...")
        except ValueError:
            messagebox.showinfo("Chyba", "Zadaj platnú sumu")
        peniaze.deiconify()
    # while True:
    #     try:
    #         tip = int(input("Zadaj číslo od 1 do 5 ktore tipuješ: "))
    #         if 1 <= tip <= 5:
    #             break
    #         else:
    #             print("-------------------------------------------------------------------------------------------------------------")
    #             print("Také číslo ani nebolo v možnostiach, zadaj číslo od 1 do 5, aby si neprišiel o svoj vklad bez šance vyhrať...")
    #             print("-------------------------------------------------------------------------------------------------------------")
    #             print("                                                       ")
    #     except ValueError:
    #         print("-------------------------------------------")
    #         print("ČISLOOOO! Zadaj prosím platnú sumu (číslo).")
    #         print("-------------------------------------------")
    #         print("                                                       ")
    # b = random.randint(1, 5)
    # počet_kôl -= 1
    # if tip == b:
    #     konto += suma * 3
    #     if počet_kôl == 0:
    #         break
    #     else:
    #         print("                                                       ")
    #         print("                                                       ")
    #         print("                                                       ")
    #         print("                                                       ")
    #         print("                                                       ")
    #         print("-------------------------------------------------------------------------")
    #         print("                                                       ")
    #         print(f"Vyhral/-a si !!!!")
    #         print(f"Výherné číslo bolo {b}, perfektne")
    #         print(f"Počet zostávajúcich pokusov: {počet_kôl}")
    #         if konto > 0:
    #             print(f"Tvoj profit je zatiaľ {konto}€, ak budeš takto pokračovať zachvíľu z teba bude milionár :)")
    #         else:
    #             print(f"Avšak stále si už prehral/-a {konto * -1}€, ak chceš stále hrať, pokračuj")
    #         print("                                                       ")
    #         print("-------------------------------------------------------------------------")
    # else:
    #     konto -= suma
    #     if počet_kôl == 0:
    #         break
    #     else:
    #         print("                                                       ")
    #         print("                                                       ")
    #         print("                                                       ")
    #         print("                                                       ")
    #         print("-------------------------------------------------------------------------")
    #         print("                                                       ")
    #         print(f"Prehral/-a si.....")
    #         print(f"Výherné číslo bolo {b}")
    #         print(f"Počet zostávajúcich pokusov: {počet_kôl}")
    #         if konto > 0:
    #             print(f"Avšak nezúfaj, zatial si stále v profite {konto}€")
    #         else:
    #             print(f"Zatiaľ si prehral/-a {konto * -1}€, ak chceš skončiť, vypni tento program.")
    #         print("                                                       ")
    #         print("-------------------------------------------------------------------------")


def exit_program():
    gamba.quit()
    gamba.destroy()

def spat():
    gamba.quit
    gamba.destroy()

# Vytvorenie tlačidla "Pokračovať"
pokracovat_button = tk.Button(gamba, text="Pokračovať", command= pokracovat, bg="Lime", font=('Times New Roman', '36', 'bold'))
pokracovat_button.place(x=screen_width / 2, y=screen_height / 2, anchor="center")

# Vytvorenie tlačidla "Koniec" (pravý dolný roh)
exit_button = tk.Button(gamba, text="Koniec", command=exit_program, bg="red", font=('Helvetica', '25', 'bold'))
exit_button.place(relx=0.98, rely=0.98, anchor='se')

# Vytvorenie tlačidla "Koniec" (pravý dolný roh)
spat_button = tk.Button(gamba, text="Späť", command=spat, bg="white", font=('Helvetica', '25', 'bold'))
spat_button.place(relx=0.07, rely=0.98, anchor='se')

# Meno Pouzivatela
# canvas.create_rectangle(10,10,300,100, fill="Gold")
# canvas.create_text(155,55, text=f"{priezvisko}", font=("Helvetica", "20", "bold"))

# Spustenie hlavného cyklu
gamba.mainloop()