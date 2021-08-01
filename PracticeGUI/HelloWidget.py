from tkinter import *
from tkinter import ttk


class HelloApp:
    def __init__(self, master):
        self.label = ttk.Label(master, text="Hello, Tkinter!")  # child window of root(master), assign text to it
        self.label.grid(row=0, column=0, columnspan=2)  # put in label into proper place (column 0 > TOP RIGHT CORNER)

        ttk.Button(master, text="Texas", command=self.texas_hello).grid(row=1, column=0)    # command is used to call out assigned method
        ttk.Button(master, text="Hawaii", command=self.hawaii_hello).grid(row=1, column=1)

    def texas_hello(self):
        self.label.config(text="Howdy Tkinter!")   # changing label text

    def hawaii_hello(self):
        self.label.config(text='Aloha Tkinter!')



def main():
    root = Tk()     # top level window
    app = HelloApp(root)
    root.mainloop()

main()