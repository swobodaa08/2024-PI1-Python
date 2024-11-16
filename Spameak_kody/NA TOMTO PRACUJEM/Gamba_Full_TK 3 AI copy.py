import tkinter as tk
import random
from PIL import Image, ImageTk, ImageEnhance
from tkinter import simpledialog, messagebox

# Hlavne okno Gamba
gamba = tk.Tk()
# Zistenie rozlíšenia obrazovky
screen_width = gamba.winfo_screenwidth()
screen_height = gamba.winfo_screenheight()
gamba.attributes("-fullscreen", True)
gamba.title("SpameakGamba")
gamba.geometry(f"{screen_width}x{screen_height}")

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
tip = 0
konto = 1000

def pokracovat():
    pokracovat_button.destroy()
    global background_photo
    global suma
    global konto
    brightness_factor = 0.3
    dark_background_image = enhancer.enhance(brightness_factor)
    background_photo = ImageTk.PhotoImage(dark_background_image)
    canvas.itemconfig(canvas_image, image=background_photo)
    



    # ZADANIE POCET KOL





    # Otvoriť dialóg na výber počtu kôl
    kola = tk.Tk()
    kola.withdraw()
    while True:
        try:
            počet_kôl = simpledialog.askinteger("Počet Kôl", "Zadaj počet kôl, koľko chceš hrať:")
            if počet_kôl is not None and 1 <= počet_kôl <= 20:
                break
            else:
                messagebox.showinfo("Chyba", "Počet kôl musí byť od 1 do 20")
        except ValueError:
            messagebox.showinfo("Chyba", "Zadaj číslo od 1 do 20")
    



    # ZADANIE SUMY UZIVATELA





    # Dialóg pre zadanie sumy
    for _ in range(počet_kôl):
        peniaze = tk.Toplevel(gamba)  # Toplevel okno pre fullscreen
        peniaze.attributes("-topmost", True)  # Umiestnenie na stred
        peniaze.transient(gamba)  # Nastavenie ako dieťa hlavného okna
        peniaze.title("Zadaj sumu")

        # Výpočet stredu obrazovky
        x_offset = (screen_width - 400) // 2
        y_offset = (screen_height - 200) // 2
        peniaze.geometry(f"400x200+{x_offset}+{y_offset}")  # Nastavenie presnej pozície
        
        def submit_suma(event=None):
            global suma
            try:
                entered_value = float(entry_suma.get())
                if 0.50 <= entered_value <= 10000 and entered_value <= konto:
                    suma = entered_value
                    peniaze.destroy()  # Zatvorenie okna
                else:
                    show_error("Chyba", "Vklad musí byť medzi 0.50€ a 10000€ a taktiež musíš mať na vklad peniaze :)")
            except ValueError:
                show_error("Chyba", "Zadaj platnú sumu")

        def show_error(title, message):
            """Zobrazí chybové hlásenie pred oknom na zadávanie sumy."""
            error_window = tk.Toplevel(peniaze)
            error_window.title(title)
            error_window.geometry(f"400x200+{x_offset}+{y_offset}")  # Nastavenie presnej pozície
            error_window.transient(peniaze)  # Vytvoriť dieťa okna "peniaze"
            error_window.attributes("-topmost", True)  # Zobraziť na vrchu
            error_window.bind("<Return>", submit_suma)

            # Obsah chybového okna
            tk.Label(error_window, text=message, font=("Helvetica", 12)).pack(pady=20)
            # Definícia tlačidla "OK"
            ok_button = tk.Button(error_window, text="OK", command=error_window.destroy, font=("Helvetica", 12), bg="red")
            ok_button.pack(pady=10)
        
            # Väzba na Enter
            error_window.bind("<Return>", lambda event: error_window.destroy())

            # Fokus na tlačidlo "OK" (voliteľné, ak chcete prednastaviť tlačidlo na Enter)
            ok_button.focus_set()

            # Fokus na chybové okno
            error_window.grab_set()

        # Rám pre zarovnanie obsahu do stredu
        frame = tk.Frame(peniaze)
        frame.pack(expand=True)  # Expanduje do stredu vertikálne aj horizontálne

        # Obsah okna
        tk.Label(frame, text="Zadaj koľko € chceš vsadiť:", font=("Helvetica", 14)).pack(pady=10)
        entry_suma = tk.Entry(frame, font=("Helvetica", 14))
        entry_suma.pack(pady=10)
        entry_suma.bind("<Return>", submit_suma)  # Väzba na Enter
        entry_suma.focus()  # Automatické zameranie textového poľa
        submit_button = tk.Button(frame, text="Potvrdiť", command=submit_suma, font=("Helvetica", 14), bg="lime")
        submit_button.pack(pady=10)
        
        # Čakanie na zatvorenie okna
        peniaze.grab_set()
        gamba.wait_window(peniaze)






        # UZIVATELOV TIP






        # Dialóg pre zadanie tipovania
        tipovanie = tk.Toplevel(gamba)  # Toplevel okno pre fullscreen
        tipovanie.attributes("-topmost", True)  # Umiestnenie na stred
        tipovanie.transient(gamba)  # Nastavenie ako dieťa hlavného okna
        tipovanie.title("Zadaj svoj tip")
        tipovanie.geometry(f"400x200+{x_offset}+{y_offset}")  # Nastavenie presnej pozície
        # Nastavenie zamerania na okno
        tipovanie.lift()
        tipovanie.focus_force()  # Urobí okno aktívnym

        # Hra

        def submit_tip(event=None):
            global tip
            try:
                entered_guess = int(entry_guess.get())
                if 1 <= entered_guess <= 5:
                    tip = entered_guess
                    tipovanie.destroy()
                else:
                    show_error2("Chyba", "Tip musí byť číslo od 1 do 5")
            except ValueError:
                show_error2("Chyba", "Zadaj platný tip")


        def show_error2(title, message):
            """Zobrazí chybové hlásenie pred oknom na zadávanie sumy."""
            error_window2 = tk.Toplevel(tipovanie)
            error_window2.title(title)
            error_window2.geometry(f"400x200+{x_offset}+{y_offset}")  # Nastavenie presnej pozície
            error_window2.transient(tipovanie)  # Vytvoriť dieťa okna "tipovanie"
            error_window2.attributes("-topmost", True)  # Zobraziť na vrchu
            error_window2.bind("<Return>", submit_tip)

            # Obsah chybového okna
            tk.Label(error_window2, text=message, font=("Helvetica", 12)).pack(pady=20)
            # Definícia tlačidla "OK"
            ok2_button = tk.Button(error_window2, text="OK", command=error_window2.destroy, font=("Helvetica", 12), bg="red")
            ok2_button.pack(pady=10)
        
            # Väzba na Enter
            error_window2.bind("<Return>", lambda event: error_window2.destroy())

            # Fokus na tlačidlo "OK" (voliteľné, ak chcete prednastaviť tlačidlo na Enter)
            ok2_button.focus_set()

            # Fokus na chybové okno
            error_window2.grab_set()


        def pokracuj_na_dalsie_kolo():
            canvas.delete("all")  # Vymaže všetko z plátna
            canvas.create_image(0, 0, image=background_photo, anchor="nw")  # Obnoví pozadie
            continue_button.destroy()  # Zničí tlačidlo, aby sa nevytvárali duplicitné
            if počet_kôl > 0:
                pokracovat()  # Spustí ďalšie kolo
                continue_button.destroy()
            else:
                messagebox.showinfo("Koniec hry", "Hra skončila. Ďakujeme za hranie!")
                continue_button.destroy()

        # RÁM
        frame2 = tk.Frame(tipovanie)
        frame2.pack(expand=True)  # Expanduje do stredu vertikálne aj horizontálne

        # Obsah okna
        tk.Label(frame2, text="Zadaj číslo od 1 do 5:", font=("Helvetica", 14)).pack(pady=10)
        entry_guess = tk.Entry(frame2, font=("Helvetica", 14))
        entry_guess.pack(pady=10)
        entry_guess.bind("<Return>", submit_tip)  # Väzba na Enter
        entry_guess.focus()  # Automatické zameranie textového poľa
        submit_button2 = tk.Button(frame2, text="Potvrdiť", command=submit_tip, font=("Helvetica", 14), bg="lime")
        submit_button2.pack(pady=10)

        # Čakanie na zatvorenie okna
        tipovanie.grab_set()
        gamba.wait_window(tipovanie)


        cislo = random.randint(1, 5)
        konto = konto - suma

        počet_kôl -= 1
        if tip == cislo:
            konto += suma * 3
            canvas.create_text(500, 500, text="Vyhral/-a si !!!!", font=("Helvetica", "20", "bold"), fill="white")
            canvas.create_text(500, 600, text=f"Výherné číslo bolo {cislo}, perfektne", font=("Helvetica", "20", "bold"), fill="white")
            canvas.create_text(500, 700, text=f"Počet zostávajúcich pokusov: {počet_kôl}", font=("Helvetica", "20", "bold"), fill="white")
            if konto > 1000:
                canvas.create_text(500, 800, text=f"Tvoj profit je zatiaľ {konto}€, ak budeš takto pokračovať zachvíľu z teba bude milionár :)", font=("Helvetica", "20", "bold"), fill="white")
            else:
                canvas.create_text(500, 800, text=f"Máš {konto}€ na účte, ak chceš stále hrať, pokračuj", font=("Helvetica", "20", "bold"), fill="white")
        
        else:
            canvas.create_text(500, 500, text="Prehral/-a si....", font=("Helvetica", "20", "bold"), fill="white")
            canvas.create_text(500, 600, text=f"Výherné číslo bolo {cislo}", font=("Helvetica", "20", "bold"), fill="white")
            canvas.create_text(500, 700, text=f"Počet zostávajúcich pokusov: {počet_kôl}", font=("Helvetica", "20", "bold"), fill="white")
            if konto > 500:
                canvas.create_text(500, 800, text=f"Avšak nezúfaj, zatial máš stále {konto}€", font=("Helvetica", "20", "bold"), fill="white")
            else:
                canvas.create_text(500, 800, text=f"Už máš iba {konto}€ na účte, ak chceš skončiť, vypni tento program.", font=("Helvetica", "20", "bold"), fill="white")
        
        continue_button = tk.Button(gamba, text="Pokračovať", font=("Helvetica", 14), bg="blue", fg="white", command=pokracuj_na_dalsie_kolo)
        continue_button.place(relx=0.5, rely=0.5, anchor='se')


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