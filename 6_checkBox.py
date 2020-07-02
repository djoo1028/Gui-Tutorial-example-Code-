from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('300x400+2000+0')

chkvar = IntVar() # We can store int type value in chkvar
chkbox = Checkbutton(root, text = 'Do Not show anymore today', variable = chkvar)
#chkbox.select()
#chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "Do not show this for a week", variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0: deselect, 1: selected
    print(chkvar2.get())
btn = Button(root, text = 'Click', command = btncmd)
btn.pack()
root.mainloop()
