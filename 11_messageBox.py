import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('640x480')
def info():
    msgbox.showinfo('notice', 'You are good ')
btn = Button(root, command = info, text = 'warning')
btn.pack()

def warn():
    msgbox.showwarning('Warning', 'There is no seat')

btn1 = Button(root, command = warn, text = 'warning')
btn1.pack()

def error():
    msgbox.showerror('Error', 'It did not work')

btn2 = Button(root, command = error, text = 'error')
btn2.pack()

def okcancel():
    msgbox.askokcancel('y/n', 'Do you want to book a ticket?')

btn3 = Button(root, command = okcancel, text = 'ask')
btn3.pack()


def retrycancel():
    msgbox.askretrycancel('y/n', 'Do you want to book a ticket?')


btn4 = Button(root, command = retrycancel, text = 'ask one more time')
btn4.pack()

def retrycancel():
    msgbox.askretrycancel('y/n', 'Do you want to book a ticket?')

def yesOrNo():
    msgbox.askyesno('y/n', 'Not good')
btn5 = Button(root, command = yesOrNo, text = 'yes & No?')
btn5.pack()

def yesOrNocancel():
    response = msgbox.askyesnocancel(title = None, message='It is not stored')
    #yes = save and terminate
    #no = terminate without saving
    #cancel = terminate
    print(response) #True = 1,false = 0, None
    if response == 1:
        print('yesr')
    elif response == 0:
        print('No')
    else:
        print('cancel')
btn6 = Button(root, command = yesOrNocancel, text = 'yes & No & cancel')
btn6.pack()


root.mainloop()
