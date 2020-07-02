import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('640x480')

frame = Frame(root)
frame.pack()


scrollbar = Scrollbar(frame)
scrollbar.pack(side = 'right', fill = 'y')

#if we do not have set then scroll go back to original location
listbox = Listbox(frame, selectmode = 'extend', height = 10, yscrollcommand = scrollbar.set)
for i in range(1,32):#1 ~ 31
    listbox.insert(END,'day ' + str(i))

listbox.pack(side = 'left')

scrollbar.config(command = listbox.yview)


root.mainloop()
