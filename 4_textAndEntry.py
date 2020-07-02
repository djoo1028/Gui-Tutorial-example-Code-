from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('300x400+2000+0')

txt = Text(root, width = 30, height = 5)
txt.pack()

txt.insert(END, 'type a word')


# Entry => just one line
e = Entry(root, width = 30)

e.pack()
e.insert(0, 'Just one line')

def btncmd():
    # print letters
    print(txt.get('1.0', END)) # meaning of 1.0 -> 1: first line 0:zero column
    print(e.get())

    # Delete letters
    txt.delete('1.0', END)
    e.delete(0, END)
btn = Button(root, text = 'Click', command = btncmd)
btn.pack()
root.mainloop()
