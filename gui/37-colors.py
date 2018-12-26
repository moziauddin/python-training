from tkinter import *
from tkinter import colorchooser

win1 = Tk()


def getcolor():
    palette = colorchooser.askcolor()  # Creates color palette
    cell = Label(text=palette, fg=palette[1])  # Creates a cell with label color code and fg color is chosen color
    cell.pack()
    print("Color is:", palette)


but = Button(text='Select Color', width=20, command=getcolor)  # Triggers the get color function
but.pack()
win1.mainloop()

