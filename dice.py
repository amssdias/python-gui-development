import tkinter as tk
import random

window = tk.Tk()
window.columnconfigure(0, weight=1, minsize=150)
window.rowconfigure([0, 1], weight=1, minsize=50)

def dice_random():
    lbl_dice['text'] = random.randint(1, 6)

btn_roll = tk.Button(text="Roll", height=3, command=dice_random)
btn_roll.grid(row=0, column=0, sticky="nsew")

lbl_dice = tk.Label(text="0", height=3)
lbl_dice.grid(row=1, column=0, sticky="nsew")

window.mainloop()