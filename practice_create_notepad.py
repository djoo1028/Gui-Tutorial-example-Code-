import os
from tkinter import *

root = Tk()
root.title('Untitled - Notepad')
root.geometry('640x480')
root.resizable(True, True)

filename = 'mynote.txt'

#Create Menu Frame
menu = Menu(root)

def open_file():
    # Check file existence
    if os.path.isfile(filename):
        with open(filename, 'r', encoding = 'utf8') as file: # 'r' :read
            txt.delete('1.0', END) # remove current context
            txt.insert(END, file.read()) # saved contents


def save_file():
    with open(filename, 'w', encoding='utf8') as file: # 'w' :write
        file.write(txt.get('1.0', END))


#Create menu options
menu_file = Menu(menu, tearoff = 0)

menu_file.add_command(label = 'Open', command = open_file)
menu_file.add_command(label = 'Save', command = save_file)
menu_file.add_separator()
menu_file.add_command(label = 'Exit', command = root.quit)
#Put menu in the menu bar(top)
menu.add_cascade(label = 'File', menu = menu_file)



menu.add_cascade(label = 'Edit')
menu.add_cascade(label = 'Format')
menu.add_cascade(label = 'View')
menu.add_cascade(label = 'Help')


#scroll bar(put it in the same frame)
scrollbar = Scrollbar(root)
scrollbar.pack(side = 'right', fill = 'y')

# Text box
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side = 'left', fill = 'both', expand =True)

#mapping to interact each other
scrollbar.config(command = txt.yview())


root.config(menu = menu)
root.mainloop()