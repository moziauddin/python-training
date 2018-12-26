from tkinter import *


def readdata():
    print("Clicked ReadData: You typed:", textval.get())

def removedata():
    print("Clicked RemoveData")


win1 = Tk()
win1.title("Read from Textbox using a Button")
win1.geometry("200x200+100+600")

# Button class is used to add a button to the window
# use command property of the Button class to add functionality
# Use Entry() class to create a textbox
# Use variables to store values from functions delared as below:
# var = StringVar()/IntVar()/DoubleVar()/BooleanVar()
# Then use textvariable property of Entry() class to assign value
# to variable delared earlier. Always declare vars after window initialization
# To read a variable from function use the varname.get() method
# Use font=## to manipulate the font sizes
# To print a value from var in a label use lab10 = Label(text=textval)

textval = StringVar()
lab1 = Label(text='Your Name:', fg='lemon chiffon', bg='saddle brown').grid(row=0, column=0)
but1 = Button(text='Read', bg='wheat', fg='brown', command=readdata).grid(row=3, column=0)
but2 = Button(text='Remove', bg='wheat', fg='brown', command=removedata).grid(row=3, column=1)
text1 = Entry(textvariable=textval).grid(row=0, column=1)


# To keep the window visible, use mainloop()
win1.mainloop()
