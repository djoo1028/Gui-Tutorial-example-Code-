import time
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('300x400+2000+0')

#progressbar = ttk.Progressbar(root, maximum = 100, mode = 'indeterminate')
# progressbar = ttk.Progressbar(root, maximum = 100, mode = 'determinate')
# progressbar.start(10)
# progressbar.pack()
#
# def btncmd():
#     progressbar.stop()
#
# btn = Button(root, text = 'stop', command = btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar2.pack()

# def btncmd():
#     progressbar.stop()
#

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)

        p_var2.set(i) # set progress bar
        progressbar2.update() # update progress bar
        print(p_var2.get())


btn = Button(root, text = 'Start', command = btncmd2)
btn.pack()

root.mainloop()
