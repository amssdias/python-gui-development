import tkinter as tk

window = tk.Tk()

frm_info = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frm_info.pack(fill=tk.BOTH, expand=True)

frm_btn = tk.Frame(master=window, padx=10, pady=8)
frm_btn.pack(fill=tk.BOTH)

btn_submit = tk.Button(master=frm_btn, text="Submit", padx=8, pady=3)
btn_clear = tk.Button(master=frm_btn, text="Clear", padx=8, pady=3)
btn_submit.pack(side=tk.RIGHT)
btn_clear.pack(side=tk.RIGHT)

entry_form = [
    'First Name:', 
    'Last Name:', 
    'Address Line1:', 
    'Address Line2:',
    'City:',
    'State/Province:',
    'Postal Code:',
    'Country']

frames = []

for i in range(8):
    frames.append(tk.Frame(master=frm_info))
    frames[i].pack()

labels = []

for count, label in enumerate(entry_form):
    lbl = {}

    lbl[label] = tk.Label(master=frames[count], text=label, width=15)
    lbl[label].pack(side=tk.LEFT, expand=True)

    lbl[f'entry{count}'] = tk.Entry(master=frames[count], width=50)
    lbl[f'entry{count}'].pack(side=tk.LEFT)

    labels.append(lbl)

print(labels)

window.mainloop()