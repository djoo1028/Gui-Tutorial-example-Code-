'''
------------------------
|----|-----|-----|-----|
|----|-----|-----|-----|
|----|-----|-----|-----|
|-----------------------

x, y coordinate
'''

import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()
root.title('Nami Sushi')
root.geometry('640x480')

# btn1 = Button(root, text = 'Button1')
# btn2 = Button(root, text = 'Button2')
#
# # btn1.pack(side = 'left')
# # btn2.pack(side = 'left')
#
# btn1.grid(row = 0, column = 0)
# btn2.grid(row = 1, column = 1)


#Top line
btnF16 = Button(root, text = 'F16',padx = 10, pady = 10)
btnF17 = Button(root, text = 'F17',padx = 10, pady = 10)
btnF18 = Button(root, text = 'F18',padx = 10, pady = 10)
btnF19 = Button(root, text = 'F19',width  = 5, height = 2)

btnF16.grid(row = 0, column = 0, sticky = N+E+W+S,padx = 3, pady = 3) # sticky will expand all direction
btnF17.grid(row = 0, column = 1, sticky = N+E+W+S,padx = 3, pady = 3)
btnF18.grid(row = 0, column = 2, sticky = N+E+W+S,padx = 3, pady = 3)
btnF19.grid(row = 0, column = 3, sticky = N+E+W+S,padx = 3, pady = 3)

#Second Line

btnClear = Button(root, text = 'clear',padx = 10, pady = 10)
btnequal = Button(root, text = '=',padx = 10, pady = 10)
btnDivision = Button(root, text = '/',padx = 10, pady = 10)
btnMultiplier = Button(root, text = '*',padx = 10, pady = 10)

btnClear.grid(row = 1, column = 0, sticky = N+E+W+S,padx = 3, pady = 3)
btnequal.grid(row = 1, column = 1, sticky = N+E+W+S,padx = 3, pady = 3)
btnDivision.grid(row = 1, column = 2, sticky = N+E+W+S,padx = 3, pady = 3)
btnMultiplier.grid(row = 1, column = 3, sticky = N+E+W+S,padx = 3, pady = 3)

#Third line
btn7 = Button(root, text = '7',padx = 10, pady = 10)
btn8 = Button(root, text = '8',padx = 10, pady = 10)
btn9= Button(root, text = '9',padx = 10, pady = 10)
btnMinus = Button(root, text = '-',padx = 10, pady = 10)

btn7.grid(row = 2, column = 0, sticky = N+E+W+S,padx = 3, pady = 3)
btn8.grid(row = 2, column = 1, sticky = N+E+W+S,padx = 3, pady = 3)
btn9.grid(row = 2, column = 2, sticky = N+E+W+S,padx = 3, pady = 3)
btnMinus.grid(row = 2, column = 3, sticky = N+E+W+S,padx = 3, pady = 3)

#Fourth line
btn4 = Button(root, text = '4',padx = 10, pady = 10)
btn5 = Button(root, text = '5',padx = 10, pady = 10)
btn6 = Button(root, text = '6',padx = 10, pady = 10)
btnPlus = Button(root, text = '+',padx = 10, pady = 10)

btn4.grid(row = 3, column = 0, sticky = N+E+W+S,padx = 3, pady = 3)
btn5.grid(row = 3, column = 1, sticky = N+E+W+S,padx = 3, pady = 3)
btn6.grid(row = 3, column = 2, sticky = N+E+W+S,padx = 3, pady = 3)
btnPlus.grid(row = 3, column = 3, sticky = N+E+W+S,padx = 3, pady = 3)

#Fifth line
btn1 = Button(root, text = '1',padx = 10, pady = 10)
btn2 = Button(root, text = '2',padx = 10, pady = 10)
btn3 = Button(root, text = '3',padx = 10, pady = 10)
btnEnter = Button(root, text = 'Enter',padx = 10, pady = 10)

btn1.grid(row = 4, column = 0, sticky = N+E+W+S,padx = 3, pady = 3)
btn2.grid(row = 4, column = 1, sticky = N+E+W+S,padx = 3, pady = 3)
btn3.grid(row = 4, column = 2, sticky = N+E+W+S,padx = 3, pady = 3)
btnEnter.grid(row = 4, column = 3, rowspan = 2, sticky = N+E+W+S,padx = 3, pady = 3) # Add couple rows from current location


#BottomLine
btn0 = Button(root, text = '0',padx = 10, pady = 10)
btnPeriod = Button(root, text = '.',padx = 10, pady = 10)

btn0.grid(row = 5, column = 0, columnspan = 2, sticky = N+E+W+S,padx = 3, pady = 3)
btnPeriod.grid(row = 5, column = 2, sticky = N+E+W+S,padx = 3, pady = 3)


root.mainloop()
