import tkinter as tk
from tkinter import simpledialog, messagebox

canvas = tk.Canvas(width=1920, height=1080)
canvas.pack()
click = 0
canvas.create_text(960, 450, text="Prvý click nefunguje :)", font=("Heltvica", "20", "bold"))
def kontrola_stlaceni():
    global click, input_uzivatela
    if click == input_uzivatela:
        canvas.quit
        canvas.destroy
    else:
        return click

while True:
    try:
        input_uzivatela = simpledialog.askinteger("Počet kliknutí", "Zadajte po koľkých kliknutiach sa má program vypnúť:")
        if 0 < input_uzivatela < 10000:
            break
        else:
            messagebox.showinfo("Chyba", "Počet kliknutí musí byť aspoň jedna ale nemôže byť viac ako 10000")
    except ValueError():
        messagebox.showinfo("Chyba", "Zadaj číslo")

def stlacenie():
    global click
    button.config(text=f"Button clicked: {click}")
    click = click + 1
    return click

button = tk.Button(canvas, width=20, text=f"Button clicked: {click}", command=stlacenie, bg="lime", font=('Helvetica', '40', 'bold'))
button.place(relx=0.5, rely=0.5, anchor='center')
kontrola_stlaceni()



tk.mainloop()