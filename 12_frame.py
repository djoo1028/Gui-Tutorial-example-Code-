import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('640x480')


Label(root, text = 'Select Menu').pack(side = 'top')
Button(root, text = 'Order').pack(side = 'bottom')
#Meal Frame
frame_burger = Frame(root, relief = 'solid', bd = 1) #bd = edge line
frame_burger.pack(side = 'left', fill = 'both', expand = True)

Button(frame_burger, text = 'Hamburger').pack()
Button(frame_burger, text = 'Cheese burger').pack()
Button(frame_burger, text = 'Double burger').pack()


#Beverage Frame
frame_drink = LabelFrame(root, text= 'Beverage')
frame_drink.pack(side = 'right', fill = 'both', expand = True)
Button(frame_drink, text = 'Coke').pack()
Button(frame_drink, text = 'Sprite').pack()
root.mainloop()
