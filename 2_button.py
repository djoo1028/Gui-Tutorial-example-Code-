from tkinter import *


root = Tk()
root.title('Nami Sushi')

#button widget
bt1 = Button(root, text = 'Button1')
#If pack does not exist then it won't show up on the window frame
bt1.pack()

#padx, pady -> we can change size of the button
#If we do not have padx and pady then it will be default value
bt2 = Button(root, padx = 5, pady = 10, text = 'Button2')
bt2.pack()

bt3 = Button(root, padx = 10, pady = 5, text = 'Button3')
bt3.pack()

#If we write width and height then button size is fixed.
# There is possibility that button size does not fit on the button
# However padx and pady is changable
bt4 = Button(root, width = 10, height = 3, text = 'Button4')
bt4.pack()

bt5 = Button(root, fg ='red', bg = 'yellow', text = 'Button5')
bt5.pack()

#Create button with image but it does not work jpg extend
photo = PhotoImage(file = "img1.png")
bt6 = Button(root, image = photo)
bt6.pack()

def btncmd():
    print('You hit the button 7')

#button response
bt7 = Button(root, text = "response", command = btncmd)
bt7.pack()
root.mainloop()
