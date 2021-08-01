from tkinter import *
from tkinter import ttk
import time

root = Tk()
progressbar2 = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressbar2.pack()
progressbar2.config(mode='determinate', maximum=100)
label = ttk.Label(root, text="{}".format(progress_percent)).pack()


def increase_progress():
    for step in range(0, 100):
        progressbar2.step(1)
        label.config(text="{}".format(progress_percent))
        progress_percent = progress_percent + 1
        print("Test")
        root.update_idletasks()
        time.sleep(0.01)


Button(root, text='Download', command=increase_progress).pack()
# Button(root, text='Stop', command=break).pack()
mainloop()