from tkinter import *   #importing all
from tkinter import ttk     #importing ttk module

root = Tk()  # top level window
button = ttk.Button(root, text='Button 1')    # creating instance for button widget
button.pack()   # placing button in root window

print(button['text'])
#   Changing the name of widget:
button['text'] = 'Change...'
button.config(text='Changing name')

label1 = ttk.Label(root, text='New label')
label1.pack()


#   SETTING WIDGETS ON PARTICULAR PLACES (Pack, Grid, Place)









root.mainloop()
