from tkinter import *
from tkinter import ttk

root = Tk()

#   DROP DOWN LIST/BOX (Combobox)
days = StringVar()
drop_box = ttk.Combobox(root, textvariable=days)
drop_box.pack()
drop_box.config(values=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
days.get()
days.set('Choose day...')
drop_box.state(['readonly'])

#   SPINBOX (
years = StringVar()
Spinbox(root, from_=1900, to=2019, textvariable=years).pack()
root.mainloop()