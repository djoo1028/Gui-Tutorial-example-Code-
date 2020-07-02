from tkinter import *


root = Tk()
root.title('Nami Sushi')

#default size
#width x height + (x location) + (y location)
#root.geometry('640x480+200+300')
root.geometry('640x480')


#Size changable (X, Y)
#If we set (False, False) x and y both are not changable
root.resizable(False, False)

#button widget

root.mainloop()
