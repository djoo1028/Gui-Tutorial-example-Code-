from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('300x400+2000+0')
label1 = Label(root, text = "hello")
label1.pack()

photo = PhotoImage(file = 'img1.png')
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text = 'See you again')

    #garbage collection
    #If we do not set global, garbage collect remove photo2
    global photo2
    photo2 = PhotoImage(file='img2.png')
    label2.config(image=photo2)

btn = Button(root, text = 'click', command = change)
btn.pack()


btn1 = Button(root, text = 'Change Image', command = change)
btn1.pack()
root.mainloop()
