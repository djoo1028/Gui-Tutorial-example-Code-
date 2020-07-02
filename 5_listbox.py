from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('300x400+2000+0')

# if height is 0 then show every element in listbox
# other integer will show that the number of element
listbox = Listbox(root, selectmode = 'extended', height = 0)
listbox.insert(0,'apple')
listbox.insert(1,'strawberry')
listbox.insert(2,'banana')
listbox.insert(END,'Watermelon')
listbox.insert(END,'Grape')
listbox.pack()

def btncmd():
    #delete element from last
    #listbox.delete(END)
    #delete element from beginning
    #listbox.delete(0)

    #Check the number of element
    #print('There is',listbox.size(),'elements')

    #element check
    #print('from beginning to three:', listbox.get(0,2))

    # selected element
    print('selected item:',listbox.curselection())
btn = Button(root, text = 'Click', command = btncmd)
btn.pack()
root.mainloop()
