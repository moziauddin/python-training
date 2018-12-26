from tkinter import *

win1 = Tk()
win1.title('Checkboxes Examples')
win1.geometry('200x300+400+600')


def getstate():
    print("Var1: %d, Var2: %d, Var3: %d", var1.get(), var2.get(), var3.get())


def closenow():
    win1.destroy()



var1 = IntVar()
Checkbutton(win1, text='apples', variable=var1).pack(anchor=W)
var2 = IntVar()
Checkbutton(win1, text='oranges', variable=var2).pack(anchor=W)
var3 = IntVar()
Checkbutton(win1, text='grapes', variable=var3).pack(anchor=W)

print(var1.get(), var2.get(), var3.get())

Button(win1, text='Print State', bg='salmon', fg='blue', command=getstate).pack()
Button(win1, text='Close', bg='black', fg='white', command=closenow).pack()
win1.mainloop()
