import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Username setter")

def akcia():
    label.config(text = textbox.get())

label = tk.Label(root, text="unknown")
label.pack()

textbox = tk.Entry(root)
textbox.pack()

button = tk.Button(root, text="Set username", command=akcia)
button.pack()

root.mainloop()