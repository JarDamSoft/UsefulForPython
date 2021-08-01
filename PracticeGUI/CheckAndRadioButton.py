from tkinter import *
from tkinter import ttk

root = Tk()
button1 = ttk.Checkbutton(root, text='Button 1')
button1.pack()

#   VARIABLE CLASSES: BooleanVar, DoubleVar, IntVar, StringVar
test = StringVar()
test.set('TEST')
test.get()  # Checks current value of variable test

button1.config(variable=test, onvalue='IS SELECTED', offvalue="NOT SELECTED")   # Checks whether button is selected, and prints out assigned value to it
print(test.get())

root.mainloop()