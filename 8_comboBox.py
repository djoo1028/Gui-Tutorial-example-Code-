import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('300x400+2000+0')

values = [str(i) + 'day' for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 5, values = values)
combobox.pack()
combobox.set('Card payment')

readOnly_combobox = ttk.Combobox(root, height = 10, values = values, state = 'readonly')
readOnly_combobox.current(0)
readOnly_combobox.pack()
readOnly_combobox.set('Danggg')


def btncmd():
    print(combobox.get())
    print(readOnly_combobox.get())

btn = Button(root, text = 'Select', command = btncmd)
btn.pack()
root.mainloop()
