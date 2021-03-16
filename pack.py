import tkinter as tk


root = tk.Tk()

root.title("Greeter")

tk.Label(root, text='Label 1', bg='green').pack(side='left', fill='y')
tk.Label(root, text='Label 2', bg='red').pack(side='left', fill='y')
tk.Label(root, text='Label 3', bg='blue').pack(side='top', fill='x', expand=True)
tk.Label(root, text='Label 4', bg='purple').pack(side='top', fill='x', expand=True)
 

root.mainloop()
