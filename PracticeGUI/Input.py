from tkinter import *
from tkinter import ttk


def callback():
    print("Clicked!")


root = Tk()
button = ttk.Button(root, text='Nowy')
button.pack()   # adding button to root window
button.config(command=callback)
button.invoke()  # its allow to execute assigned method to
button.state(['disabled'])
bt = button.instate(['disabled'])    # checking if the currently is the same as state that was entered
print(bt)   # print out bool value of button state
button.state(['!disabled']) # changes button status to enable
bt1 = button.instate(['disabled'])
print(bt1)
button.config(compound=RIGHT)

#   BUTTON WITH LOGO IMAGE
logo = PhotoImage(file='C:\\Users\\JaremkoD\\Desktop\\ZF.png')
button1 = ttk.Button(root, text='Nowy 2')
button1.pack()
button1.config(image=logo, compound=RIGHT)
small_logo = logo.subsample(5, 5)
button1.config(image=small_logo)

root.mainloop()


