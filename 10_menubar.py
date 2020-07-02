from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('640x480')

def create_new_file():
    print('I am creating new file')


#File menu
menu = Menu(root)
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = 'New File', command = create_new_file)
menu_file.add_command(label = 'New Window')
menu_file.add_separator()
menu_file.add_command(label = 'Open File...')


menu_file.add_separator()
menu_file.add_command(label = 'Save All', state = 'disable')
menu_file.add_separator()
menu_file.add_command(label = 'Exit', command = root.quit)

menu.add_cascade(label = 'File', menu = menu_file)


#Edit menu
menu.add_cascade(label = 'Edit')

#language menu add
menu_lang = Menu(menu, tearoff = 0)
menu_lang.add_radiobutton(label = 'Python')
menu_lang.add_radiobutton(label = 'Java')
menu_lang.add_radiobutton(label = 'C++')
menu.add_cascade(label = 'Language', menu = menu_lang)

#check box
menu_view = Menu(menu, tearoff = 0)
menu_view.add_checkbutton(label = 'Show Minimap')
menu.add_cascade(label = 'View', menu = menu_view)


root.mainloop()
