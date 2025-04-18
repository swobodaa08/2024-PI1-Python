# SpameakCasino Beta v4.3 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] # SpameakGamba Beta v3.0 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] 



import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os
import random
import pygame

# Inicializácia konta
konto = 0
velkost = 24

# Direktoria prihlasenia
directory = os.path.join(os.getcwd(), "Home/Spameak_kody/Spameak_Casino/Progress")

# Funkcia na načítanie progresu podľa priezviska
def load_progress(priezvisko):
    file_name = os.path.join(directory, f"{priezvisko}_progress.pkl")
    if os.path.exists(file_name):
        with open(file_name, "rb") as f:
            return pickle.load(f)
    return 0  # Ak súbor neexistuje, začni s 0 €

# Funkcia na uloženie progresu podľa priezviska
def save_progress(priezvisko, progress):
    # Nastavenie cesty k priecinku a vytvorenie priecinka, ak neexistuje
    os.makedirs(directory, exist_ok=True)  # Vytvori priecinok, ak neexistuje

    # Nastavenie celej cesty k suboru
    file_name = os.path.join(directory, f"{priezvisko}_progress.pkl")
    
    # Ulozenie do suboru
    with open(file_name, "wb") as f:
        pickle.dump(progress, f)

# Funkcia na aktualizáciu žetónov
def my_upd():
    global konto, velkost
    konto += 1
    b1.config(text=f"Peňazí na účte : {konto}€")
    save_progress(priezvisko, konto)
    if konto > 999999:
        velkost = 24

# Funkcia na ukončenie programu
def exit_program():
    okno.quit()
    okno.destroy()

def add_secret():
    global konto
    if konto < 100000:
        konto = konto + 100000


# Funkcia na spustenie hry "SpameakGamba"
def start_gamba():
    okno.destroy()  # Zavrie hlavné okno SpameakGamble
    
    global konto
    počet_kôl = 0

    print("                                                       ")
    print("-------------------------------------------------------")
    print("Vitaj v hre SpameakGamba")
    print("Hra je veľmi jednoduchá, stačí tipnúť číslo od 1 do 5")
    print("Ak trafíš správne číslo, vyhrávaš trojnásobok vkladu.")
    print(f"Zostatok na účte: {konto}€")
    print("-------------------------------------------------------")

    # Kontrola vstupu pre počet kôl
    while True:
        try:
            počet_kôl = int(input("Zadaj počet kôl koľko chceš hrať? (Maximálne 20): "))
            if 0 < počet_kôl <= 20:
                break
            else:
                print("Počet kôl musí byť medzi 1 a 20.")
        except ValueError:
            print("Zadaj prosím platné číslo pre počet kôl.")

    # Princip hry
    for _ in range(počet_kôl):
        while True:
            try:
                suma = float(input("Zadaj koľko € chceš vsadiť: "))
                if suma <= konto and 10000 >= suma >= 0.50:
                    break
                else:
                    if suma >= konto:
                        print("Nemáš dostatok peňazí na túto stávku...")
                    else:
                        print("Stávka musí byť aspon 0.50€ a nemôže byť vyššia ako 10000€")
            except ValueError:
                print("Zadaj prosím platnú sumu (číslo).")

        while True:
            try:
                tip = int(input("Zadaj číslo od 1 do 5 ktore tipuješ: "))
                if 1 <= tip <= 5:
                    break
                else:
                    print("Zadaj číslo od 1 do 5.")
            except ValueError:
                print("Zadaj prosím platné číslo (1-5).")

        b = random.randint(1, 5)
        if tip == b:
            konto -= suma
            konto += (suma * 3)
            print(f"Vyhral/-a si! Výherné číslo bolo {b}. Tvoje konto je teraz {konto}€.")
            save_progress(priezvisko, konto)
        else:
            konto -= suma
            print(f"Prehral/-a si... Výherné číslo bolo {b}. Tvoje konto je teraz {konto}€.")
            save_progress(priezvisko, konto)

        if konto <= 0:
            print("Tvoje konto je 0€.")
            save_progress(priezvisko, 0)
            break

# Funkcia na spustenie hry "Automat - Slot"
def start_slot():
    okno.destroy()
    global konto

    # Initialize pygame
    pygame.init()

    # Screen settings
    WIDTH, HEIGHT = 400, 500
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Slot Machine")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    # Load fruit images
    SYMBOLS = ['ananas', 'apple', 'cherry', 'grape', 'strawberry']
    images = {symbol: pygame.image.load(f"{symbol}.png") for symbol in SYMBOLS}

    PAYOUTS = {
        ('ananas', 'ananas', 'ananas'): 5,
        ('apple', 'apple', 'apple'): 10,
        ('cherry', 'cherry', 'cherry'): 20,
        ('grape', 'grape', 'grape'): 50,
        ('strawberry', 'strawberry', 'strawberry'): 100,  # Jackpot
    }

    # Font
    font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 30)

    # Game variables
    bet = 5
    slots = [random.choice(SYMBOLS) for _ in range(3)]

    # Button positions
    spin_button = pygame.Rect(150, 400, 100, 50)
    increase_bet_button = pygame.Rect(270, 400, 50, 50)
    decrease_bet_button = pygame.Rect(80, 400, 50, 50)

    # Function to draw the slot machine
    def draw_machine():
        screen.fill(WHITE)
        balance_text = font.render(f"Balance: ${konto}", True, BLACK)
        bet_text = font.render(f"Bet: ${bet}", True, BLACK)
        screen.blit(balance_text, (10, 10))
        screen.blit(bet_text, (10, 50))
        
        for i, symbol in enumerate(slots):
            screen.blit(images[symbol], (80 + i * 100, 150))
        
        # Draw buttons
        pygame.draw.rect(screen, BLUE, spin_button)
        pygame.draw.rect(screen, GRAY, increase_bet_button)
        pygame.draw.rect(screen, GRAY, decrease_bet_button)
        
        spin_text = button_font.render("Spin", True, WHITE)
        plus_text = button_font.render("+", True, BLACK)
        minus_text = button_font.render("-", True, BLACK)
        
        screen.blit(spin_text, (spin_button.x + 25, spin_button.y + 10))
        screen.blit(plus_text, (increase_bet_button.x + 15, increase_bet_button.y + 10))
        screen.blit(minus_text, (decrease_bet_button.x + 15, decrease_bet_button.y + 10))
        
        pygame.display.flip()


    # Function to spin
    def spin():
        global slots, konto
        if konto < bet:
            return
        konto -= bet
        save_progress(priezvisko, konto)
        spin_animation()
        slots = [random.choice(SYMBOLS) for _ in range(3)]
        draw_machine()
        check_win()
    
    # Function for spinning animation
    def spin_animation():
        global slots
        for _ in range(10):
            slots = [random.choice(SYMBOLS) for _ in range(3)]
            draw_machine()
            pygame.time.delay(100)

    # Function to check for winnings
    def check_win():
        global konto
        if tuple(slots) in PAYOUTS:
            winnings = bet * PAYOUTS[tuple(slots)]
            konto += winnings
            save_progress(priezvisko, konto)
            highlight_win()
            pygame.time.delay(500)

    # Function to highlight winnings
    def highlight_win():
        pygame.draw.rect(screen, GREEN, (70, 140, 260, 100), 5)
        pygame.display.flip()
        pygame.time.delay(500)

    # Main loop
    running = True
    while running:
        draw_machine()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if spin_button.collidepoint(event.pos):
                    spin()
                elif increase_bet_button.collidepoint(event.pos) and bet < konto:
                    bet += 5
                elif decrease_bet_button.collidepoint(event.pos) and bet > 5:
                    bet -= 5

    pygame.quit()


# Funkcia na spustenie hry "SpameakBet"
def start_bet():
    okno.destroy()  # Zavrie hlavné okno SpameakGamble

    from pathlib import Path
    global konto
    počet_kôl = 0

    # Original absolute path
    absolute_path = Path("Z:/2024-PI1-Python/2024-PI1-Python/Spameak_Casino/timy.txt")

    # Get the current working directory
    current_dir = Path.cwd()

    # Convert to relative path based on the current directory
    relative_path = absolute_path.relative_to(current_dir)

    # Original absolute path
    absolute_path2 = Path("Z:/2024-PI1-Python/2024-PI1-Python/Spameak_Casino/vysledky.txt")

    # Get the current working directory
    current_dir2 = Path.cwd()

    # Convert to relative path based on the current directory
    relative_path2 = absolute_path2.relative_to(current_dir2)


    print("                                                       ")
    print("                                                       ")
    print("                                                       ")
    print("-------------------------------------------------------")
    print("                                                       ")
    print("Vitaj v hre SpameakBetting")
    print("Hra je veľmi jednoduchá, stačí tipnúť tím ktorý vyhrá")
    print("Táto hra je stále v Beta verzii, ak si narazil na chybu, kontaktuj môj instagram : @swobodaa08")
    print("Ak trafíš správne tím, ktorý vyhrá, tvoj vklad sa vynásobí kurzom vypísaným pred stávkou")
    print("Uži si Gamble <33333333")
    print("                                                       ")
    print("-------------------------------------------------------")
    print("                                                       ")
    print("                                                       ")
    print("                                                       ")


    # Kontrola vstupu pre počet kôl
    while True:
        try:
            počet_kôl = int(input("Zadaj počet kôl koľko chceš hrať? (Maximálne 20): "))
            if 0 < počet_kôl <= 20:
                break
            else:
                print("-----------------------------------------------------------------------------------------------------")
                print("Počet hraných hier nemôže byť vyšší ako 20, taktiež nie menší ako 1! Zadaj prosím číslo medzi 1 a 20.")
                print("-----------------------------------------------------------------------------------------------------")
                print("                                                       ")
        except ValueError:
            print("-------------------------------------------------------")
            print("Neplatný vstup! Zadaj prosím číslo.")
            print("-------------------------------------------------------")
            print("                                                       ")

    round(konto, 2)

    # Funkcia na načítanie tímov zo súboru
    def nacitaj_timy(subor):
        timy = []
        with open(subor, "r") as f:
            for riadok in f:
                nazov, hodnotenie = riadok.strip().split(',')
                timy.append((nazov, int(hodnotenie)))
        return timy

    # Funkcia na výpočet kurzov na základe hodnotenia
    def vypocitaj_kurzy(hodnotenie1, hodnotenie2):
        EA = 1 / (1 + 10 ** ((hodnotenie2 - hodnotenie1) / 400))
        EB = 1 / (1 + 10 ** ((hodnotenie1 - hodnotenie2) / 400))
        kurz_1 = round(1 / EA, 2)
        kurz_2 = round(1 / EB, 2)
        if kurz_1 > 150:
            kurz_1 = 150
        if kurz_2 > 150:
            kurz_2 = 150
        kurz_X = round((kurz_1 + kurz_2) / 2, 2)
        return kurz_1, kurz_X, kurz_2

    # Funkcia na uloženie výsledku zápasu do súboru
    def uloz_vysledok(nazov1, goly_tim1, nazov2, goly_tim2):
        vysledok = f"{nazov1} {goly_tim1}:{goly_tim2} {nazov2}\n"
        with open(relative_path2, "a") as f:
            f.write(vysledok)

    # Funkcia na náhodné vyhodnotenie zápasu podľa pravdepodobností
    def vyhodnot_zapas(hodnotenie1, hodnotenie2):
        EA = 1 / (1 + 10 ** ((hodnotenie2 - hodnotenie1) / 400))
        EB = 1 / (1 + 10 ** ((hodnotenie1 - hodnotenie2) / 400))
        vysledok = random.choices(
            population=["1", "X", "2"], weights=[EA, 0.1, EB], k=1
        )[0]

        if vysledok == "1":
            goly_tim1 = random.randint(1, 4)
            goly_tim2 = random.randint(0, goly_tim1 - 1)
        elif vysledok == "2":
            goly_tim2 = random.randint(1, 4)
            goly_tim1 = random.randint(0, goly_tim2 - 1)
        else:
            goly_tim1 = goly_tim2 = random.randint(0, 2)
        
        return goly_tim1, goly_tim2


    # Hlavný program

    def hlavny_program():
        global konto
        timy = nacitaj_timy(relative_path)
        tim1, tim2 = random.sample(timy, 2)
        nazov1, hodnotenie1 = tim1
        nazov2, hodnotenie2 = tim2
        
        kurz_1, kurz_X, kurz_2 = vypocitaj_kurzy(hodnotenie1, hodnotenie2)
        round(kurz_1, 2)
        round(kurz_2, 2)
        round(kurz_X, 2)
        
        # Výstup pre užívateľa
        print("\n---------------------------------------------------")
        print(f"Stav tvojho účtu je : {konto}€")
        print("                                                     ")
        print("\n---------------------------------------------------")
        print(f"{nazov1} : {nazov2}")
        print("                                                     ")
        print(f"1 (Vyhrá {nazov1}) = {kurz_1}")
        print(f"X (Remíza) = {kurz_X}")
        print(f"2 (Vyhrá {nazov2}) = {kurz_2}")
        print("---------------------------------------------------")
        
        # Používateľ zadá svoje tipy
        while True:
            tip_vysledok = input("Tipnite si víťaza (1, X alebo 2): ")
            if tip_vysledok in ["1", "X", "x", "2"]:
                break
            else:
                print("Zadaj prosím 1, X alebo 2.")


        # Kontrola vstupu pre sumu
    
        while True:
            try:
                suma = float(input("Zadaj koľko € chceš vsadiť: "))
                if konto >= suma and 0.50 <= suma <= 10000:
                    break
                else:  
                    print("---------------------------------------------------")
                    print("Nieje možné vytvoriť stávku.. Uisti sa či je suma aspoň 50 centov, či nepresahuje 10000€ a či máš na stávku peniaze!")
                    print("---------------------------------------------------")
            except ValueError:
                print("Prosím, zadaj platnú sumu (číslo).")

        # Vyhodnotenie zápasu
        goly_tim1, goly_tim2 = vyhodnot_zapas(hodnotenie1, hodnotenie2)
        vysledok = "1" if goly_tim1 > goly_tim2 else "2" if goly_tim2 > goly_tim1 else "X" and "x"
            
        # Výsledok zápasu a stávky
        print(f"\nKonečný výsledok: {nazov1} {goly_tim1}:{goly_tim2} {nazov2}")
        print(f"Výsledok zápasu: {vysledok}")

        # Uloženie výsledku do súboru
        uloz_vysledok(nazov1, goly_tim1, nazov2, goly_tim2)
            
        # Vyhodnotenie stávky používateľa
        if tip_vysledok == vysledok:
            konto -= suma
            vyhra = round(suma * (kurz_1 if vysledok == "1" else kurz_X if vysledok == "X" and "x" else kurz_2), 2)
            konto += vyhra
            round(konto, 2)
            print("----------------------------------------------------")
            print(f"Gratulujem! Vyhral/-a si {vyhra}€")
            save_progress(priezvisko, konto)
        else:
            konto -= suma
            round(konto, 2)
            print("----------------------------------------------------")
            print("Bohužiaľ, tvoja stávka nebola úspešná")
            save_progress(priezvisko, konto)
        print("----------------------------------------------------")
        print(f"Aktuálny zostatok na konte: {konto}€")
        print("----------------------------------------------------")

    # Hra prebehne počet_kôl krát
    for i in range(počet_kôl):
        print(f"\nKolo {i + 1} z {počet_kôl}:")
        hlavny_program()

    # Skontroluj, či je konto prázdne
    if konto <= 0:
        save_progress(priezvisko, konto)
        print("----------------------------------------------------")
        print("Tvoj zostatok na konte je 0€. Nemáš možnosť tipovať, pre reset, reštartuj program")
        print("----------------------------------------------------")




# Získanie priezviska na začiatku
root = tk.Tk()
root.withdraw()
priezvisko = simpledialog.askstring("Prihlásenie", "Zadajte svoje priezvisko:")
root.deiconify()

if priezvisko:
    konto = load_progress(priezvisko)
    root.destroy()

    # Inicializácia hlavného okna
    from PIL import Image, ImageTk
    okno = tk.Tk()
    # Obrazovka
    screen_width = okno.winfo_screenwidth()
    screen_height = okno.winfo_screenheight()
    okno.attributes('-fullscreen', True)
    okno.title("SpameakGamble")
    okno.geometry(f"{screen_width}x{screen_height}")
    canvas = tk.Canvas(okno, width=screen_width, height=screen_height)
    canvas.pack(fill="both", expand=True)

    # Načítanie obrázka a jeho prispôsobenie veľkosti Canvasu
    image_path = "Home/Spameak_kody/Spameak_Casino/Background.jpg"  # cesta k obrázku
    background_image = Image.open(image_path)
    background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)  # zmenšenie na veľkosť Canvasu
    background_photo = ImageTk.PhotoImage(background_image)

    # Vložte obrázok na Canvas
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    # Meno používateľa
    canvas.create_rectangle(10,10,300,100, fill="Gold")
    canvas.create_text(155,55, text=f"{priezvisko}", font=("Helvetica", "20", "bold"))

    # Tlačidlo na rátanie žetónov (zarovnané do stredu)
    b1 = tk.Button(okno, text=f"Peňazí na účte : {konto}€", width=velkost,
                    command=my_upd, bg="lime", font=('Helvetica', '40', 'bold'))
    b1.place(relx=0.5, rely=0.5, anchor='center')

    # Tlačidlo "Gamba" (v strede napravo)
    gamba_button = tk.Button(okno, text="Gamba", command=start_gamba, bg="magenta", font=('Helvetica', '25', 'bold'))
    gamba_button.place(relx=0.08, rely=0.98, anchor='se')

    # Tlačidlo "Slot" 
    slot_button = tk.Button(okno, text="Slot", command=start_slot, bg="lime", font=("Heltvica", "25", "bold"))
    slot_button.place(relx=0.30, rely=0.98, anchor="se")

    # Tlačidlo "Bet" (hore napravo)
    bet_button = tk.Button(okno, text="Betting", command=start_bet, bg="cyan", font=('Helvetica', '25', 'bold'))
    bet_button.place(relx=0.5328, rely=0.98, anchor='se')


    # Tlačidlo na ukončenie programu (pravý dolný roh)
    exit_button = tk.Button(okno, text="Koniec", command=exit_program, bg="red", font=('Helvetica', '25', 'bold'))
    exit_button.place(relx=0.98, rely=0.98, anchor='se')

    # Tlačidlo na ukončenie programu (pravý dolný roh)
    secret_button = tk.Button(okno, text="-", command=add_secret, bg="black", font=('Helvetica', '5', 'bold'))
    secret_button.place(relx=0.55, rely=0.285, anchor='se')

    okno.mainloop()
else:
    messagebox.showinfo("Chyba", "Nebolo zadané priezvisko. Program sa ukončí.")