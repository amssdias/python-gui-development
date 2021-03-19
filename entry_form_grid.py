import tkinter as tk

window = tk.Tk()
window.rowconfigure(0, weight=1, minsize=70)
window.columnconfigure(0, weight=1, minsize=100)

main_frame = tk.Frame(master=window, relief=tk.SUNKEN ,borderwidth=3, padx=2, pady=2)
main_frame.grid(row=0, column=0)
main_frame.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)

entry_form = [
    'First Name:', 
    'Last Name:', 
    'Address Line1:', 
    'Address Line2:',
    'City:',
    'State/Province:',
    'Postal Code:',
    'Country']

labels = []

for count, form in enumerate(entry_form):
    label = {}
    label[form] = tk.Label(master=main_frame, text=form)
    label[form].grid(row=count, column=0, sticky="e")

    label['entry'] = tk.Entry(master=main_frame, width=50)
    label['entry'].grid(row=count, column=1)

    labels.append(label)


button_frame = tk.Frame(master=window, pady=8, padx=8)
button_frame.grid(row=1, column=0, sticky="e")

btn_submit = tk.Button(master=button_frame, text="Submit", padx=5)
btn_submit.pack(side=tk.RIGHT, fill=tk.X)

btn_clear = tk.Button(master=button_frame, text="Clear", padx=5)
btn_clear.pack(side=tk.RIGHT)

window.mainloop()