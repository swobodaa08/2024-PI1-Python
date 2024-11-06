import tkinter  # Stiahnutie tkinter do kodu

canvas = tkinter.Canvas()   # vytvorenie platna a jeho priradenie do premennej canvas
canvas.pack()   # umiestnenie platna do okna

canvas.create_text(100, 75, text="Ahoj")
# vypise text "Ahoj" na pozicii x=100 y=100
# suradnice zadavame vzdy v poradi x, y
# x rastie smerom doprava
# y rastie smerom dole
canvas.create_rectangle(50, 50, 150, 100)
# vykreslenie stvorca (obdlznika)
# prve dve cisla urcuju poziciu zaciatocneho bodu
# dalsie dve cisla urcuju poziciu koncoveho bodu

canvas.create_oval(50, 50, 150, 100)
# vykreslenie kruhu (oválu)
# prve dve cisla urcuju poziciu zaciatocneho bodu
# dalsie dve cisla urcuju poziciu koncoveho bodu


tkinter.mainloop()  # aby zostalo okno otvorene, aby sa nezavrelo