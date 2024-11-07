# SpameakGamba Beta v3.0 - [Copyright by SpameakGamba a.s. 2024 - Developed and Modified by @swobodaa08 - SpameakWear s.r.o. 2024] 



# Import
import tkinter as tk
okno = tk.Tk()
okno.attributes('-fullscreen', False)
okno.title("SpameakGamble")
okno.geometry("700x350")  # Zadám šírku a výšku strán
konto = 0

def my_upd():
    global konto
    konto = konto + 1
    b1.config(text=f"Počet žetónov : {konto+1}")

b1=tk.Button(okno,text=f"Počet žetónov : {konto}", width=16,
    command=lambda:my_upd(),bg="lime", font=('Helvetica', '20', 'bold'))
b1.grid(row=0,column=0,padx="200",pady="125")



tk.mainloop()