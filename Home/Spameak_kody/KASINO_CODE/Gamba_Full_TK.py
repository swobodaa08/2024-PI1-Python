import tkinter as tk
import random
from PIL import Image, ImageTk, ImageEnhance

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
image_path = "Spameak_Casino/Gamba.jpg"  # cesta k obrázku
background_image = Image.open(image_path)
background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Inicializácia jasného obrázka na pozadí
enhancer = ImageEnhance.Brightness(background_image)
brightness_factor = 1.3  # Počiatočný jas
bright_background_image = enhancer.enhance(brightness_factor)
background_photo = ImageTk.PhotoImage(bright_background_image)

# Nastavenie obrázka ako pozadia na Canvas
canvas_image = canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Názov Hry na Canvas
canvas.create_rectangle ((screen_width / 2) - 325,32,(screen_width / 2) + 325,132, fill="cyan")
canvas.create_text(screen_width / 2, 75, text="Spameak Gamba", font=("Helvetica", "50", "bold"))


# Definícia tlačidiel
def pokracovat():
    pokracovat_button.destroy()
    global background_photo  # Aby sa aktualizovaný obrázok zobrazil správne
    brightness_factor = 0.3  # Nastavenie tmavšej verzie obrázka
    dark_background_image = enhancer.enhance(brightness_factor)
    background_photo = ImageTk.PhotoImage(dark_background_image)  # Aktualizovaný obrázok
    canvas.itemconfig(canvas_image, image=background_photo)  # Zmena obrázka na Canvas
    
    canvas.create_text(screen_width / 2, 255, text="Koľko kôl chceš hrať?", font=("Helvetica", "50", "bold"), fill="white")

    one_button = tk.Button(gamba, text=" 1 ", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    one_button.place(relx=0.20, rely=0.5, anchor='se')
        
    two_button = tk.Button(gamba, text=" 2 ", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    two_button.place(relx=0.27, rely=0.5, anchor='se')
        
    three_button = tk.Button(gamba, text=" 3 ", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    three_button.place(relx=0.34, rely=0.5, anchor='se')
        
    four_button = tk.Button(gamba, text=" 4 ", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    four_button.place(relx=0.41, rely=0.5, anchor='se')
        
    five_button = tk.Button(gamba, text=" 5 ", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    five_button.place(relx=0.48, rely=0.5, anchor='se')
        
    six_button = tk.Button(gamba, text=" 6 ", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    six_button.place(relx=0.55, rely=0.5, anchor='se')
        
    seven_button = tk.Button(gamba, text=" 7 ", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    seven_button.place(relx=0.62, rely=0.5, anchor='se')
        
    eight_button = tk.Button(gamba, text=" 8 ", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    eight_button.place(relx=0.69, rely=0.5, anchor='se')
     
    nine_button = tk.Button(gamba, text=" 9 ", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    nine_button.place(relx=0.76, rely=0.5, anchor='se')
        
    ten_button = tk.Button(gamba, text="10", command=click, bg="white", font=('Helvetica', '32', 'bold'))
    ten_button.place(relx=0.83, rely=0.5, anchor='se')

def click():
    # global počet_kôl
    

# def exit_program():
#     gamba.quit()
#     gamba.destroy()

# def spat():
#     gamba.quit
#     gamba.destroy()

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