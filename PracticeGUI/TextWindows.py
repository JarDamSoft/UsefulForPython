from tkinter import *
from tkinter import ttk

root = Tk()

#   WINDOW FOR LOGIN etc.. (only one line of text)
entry = ttk.Entry(root, width=50)
entry.pack()
entry.get()
entry.delete(3, 4)  # remove characters (from, to)
entry.delete(2, END)
entry.insert(0, 'Enter login')
entry.config(show="*")  # replacing typed text with astrix
entry.state(['disabled'])
entry.state(['!disabled'])
entry.state(['readonly']) # user cant enter ant text, only read or copy
root.mainloop()