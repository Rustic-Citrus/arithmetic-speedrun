import tkinter as tk
from tkinter import ttk

def submit():
    print("You entered:", entry.get())
    entry.delete(0, tk.END)

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
label = ttk.Label(frm, text="8 * 7 = ?")
label.pack()
# button = ttk.Button(frm, text="Quit", command=root.destroy)
# button.pack()
entry = ttk.Entry(frm)
entry.pack()
entry.bind("<Return>", lambda event: submit())
root.mainloop()
