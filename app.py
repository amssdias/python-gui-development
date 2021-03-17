import os
import tkinter as tk
from tkinter import ttk, filedialog


def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)
    notebook.add(text_area, text="Untitled")
    notebook.select(text_area)


def save_file():
    # Get the path of where the file will be saved
    file_path = filedialog.asksaveasfilename()

    try:
        filename = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select())
        content = text_widget.get("1.0", "end-1c")

        with open(file_path) as file_:
            file_.write(content)

    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return

    notebook.tab("current", text=filename)


root = tk.Tk()
root.title('Teclado Text Editor')
root.option_add("*tearOFF", False)

# main goes inside root
main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=50, pady=(4, 0))

# creating the menu bar
menubar = tk.Menu()
root.config(menu=menubar)

# Create element and put inside the menu bar
file_menu = tk.Menu(menubar)
menubar.add_cascade(menu=file_menu, label="File")

# Create the cascade for the element in the menu bar with commands
file_menu.add_command(label='New', command=create_file)
file_menu.add_command(label='Save', command=save_file)

# Create notebook and put it inside main
notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

root.mainloop()
