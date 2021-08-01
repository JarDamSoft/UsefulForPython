from tkinter import *
from tkinter import ttk
import time


def increase_progress():
    progressbar2 = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
    progressbar2.pack()
    progressbar2.config(mode='determinate', maximum=100)
    for step in range(0, 9):
        progressbar2.step(1)
        print("Test")
        root.update_idletasks()
        time.sleep(1)


root = Tk()
progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)  # orient can be set also in VERTICAL mode
progressbar.pack()

'''There are two modes that the progress bar can use. DETERMINATE and INDETERMINATE. 
If you know how many steps the operation you're tracking will take and can calculate it's progress then using the determinate mode will allow you to 
manually update the value of the progress bar to represent how many steps are left. If you cannot determine how much more time might remain for an operation then you
should use the indeterminate mode where the progress bar will just show the activity as still taking place without specifying the time that remains. '''

progressbar.config(mode='indeterminate')
progressbar.start()
progressbar.stop()

progressbar.config(mode='determinate', maximum=100.0, value=50.0)     # progress bar will be filled in 50%
progressbar.config(value=75.0)  # progress bar will be filled in 3/4
progressbar.step(25)    # progress bar will jumps 25 steps forward

# PROGRESS BAR WITH SCALE
progressbar.config(mode='determinate')
progress_value = DoubleVar()
progressbar.config(variable=progress_value)
scale = ttk.Scale(root, orient=HORIZONTAL, length=200, variable=progress_value, from_=0.0, to=100.0)
scale.pack()

increase_progress()

root.mainloop()

