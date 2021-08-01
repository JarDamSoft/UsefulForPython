from tkinter import *
from tkinter import ttk    # Themed tk


root = Tk()
label_1 = ttk.Label(root, text='Test')
label_1.pack()
label_1.config(text='Nowy test. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBB'
                    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAAA')


label_1.config(wraplength=300)
label_1.config(justify=CENTER)
label_1.config(background='black')
label_1.config(foreground='white')
label_1.config(font=('Arial', 18, 'bold'))

# logo = PhotoImage(file='path')
# label_1.config(image=logo)

label_1.config(compound='text')     # displaying text over the logo




root.mainloop()
