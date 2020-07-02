from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('300x400+2000+0')

label1 = Label(root, text = 'Select your meal')
label1.pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text = 'Hamburger', value = 1, variable = burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text = 'cheese burger', value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = 'chicken burger', value = 3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text = 'Please select beverage')

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = 'Coke', value = 'Coke',variable = drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text = 'Sprite', value = 'Sprite',variable = drink_var)
btn_drink3 = Radiobutton(root, text = 'Fanta', value = 'Fanta',variable = drink_var)


btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()
def btncmd():
    print(burger_var.get())
    print(drink_var.get())
btn = Button(root, text = 'Order', command = btncmd)
btn.pack()
root.mainloop()
