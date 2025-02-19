import tkinter as tk
import random

balance = 0
profit = 0
disprofit = 0

def klik(zarabanie):
    global balance, profit, disprofit
    random_suma = random.randint(-108,75)
    balance += random_suma
    x = 200
    y = 150
    canvas.delete("all")
    if random_suma > 0:
        canvas.create_text(x, y, text=f"+{random_suma}€", fill="limegreen", font=("Heltvica", "12", "bold"))
        profit += 1
    elif random_suma > 1000:
        canvas.create_text(x, y, text=f"+{random_suma}€", fill="purple", font=("Heltvica", "35", "bold"))
    elif random_suma < 0:
        canvas.create_text(x, y, text=f"{random_suma}€", fill="red", font=("Heltvica", "12", "bold"))
        disprofit += 1
    else:
        canvas.create_text(x, y, text=f"{random_suma}€", fill="black", font=("Heltvica", "12", "bold"))
    
    if balance > 0:
        canvas.create_text(200, 20, text=f"Balance : {balance}€", fill="limegreen", font=("Heltvica", "20", "bold"))
    elif balance < 0:
        canvas.create_text(200, 20, text=f"Balance : {balance}€", fill="red", font=("Heltvica", "20", "bold"))
    else:
        canvas.create_text(200, 20, text=f"Balance : {balance}€", fill="black", font=("Heltvica", "20", "bold"))

    canvas.create_text(100, 90, text=f"Profits: {profit}", fill="limegreen", font=("Heltvica", "14", "bold"))
    canvas.create_text(280, 90, text=f"Disprofits: {disprofit}", fill="red", font=("Heltvica", "14", "bold"))

    print(balance)

okno = tk.Tk()
okno.title("Mitka - simulator")
canvas = tk.Canvas(okno)
canvas.pack()
canvas.bind_all("<Return>", klik)
canvas.bind("<ButtonPress>", klik)


tk.mainloop()