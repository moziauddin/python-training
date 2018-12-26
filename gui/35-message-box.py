from tkinter import *
from tkinter import messagebox
win1 = Tk()
win1.title("Read from Textbox using a Button")
win1.geometry("200x200+100+600")


def readdata():
    print("Clicked ReadData: You typed:", textval.get())


def removedata():
    print("Clicked RemoveData")


def newfile():
    print("clicked on new file")


def mquit():
    print('Clicked on Quit')
    closeBool = messagebox.askyesnocancel(title='quit-gui', message='Are you sure, you want to quit')
    if closeBool == 1:
        win1.destroy()

def mclose():
    print('Clicked on Close')
    messagebox.showinfo(title='quit-gui', message='Are you sure, you want to close')

def mopen():
    print('Clicked on Open')

textval = StringVar()
lab1 = Label(text='Your Name:', fg='lemon chiffon', bg='saddle brown').grid(row=0, column=0)
but1 = Button(text='Read', bg='wheat', fg='brown', command=readdata, font=('Calibri', 11, 'normal')).grid(row=3, column=0)
but2 = Button(text='Remove', bg='wheat', fg='brown', command=removedata).grid(row=3, column=1)
text1 = Entry(textvariable=textval).grid(row=0, column=1)

menu1 = Menu()
list1 = Menu()
list2 = Menu()
list3 = Menu()
menu1.add_cascade(label='Main', menu=list1)
menu1.add_cascade(label='Settings', menu=list2)
menu1.add_cascade(label='Help', menu=list3)

list1.add_command(label='New', command=newfile)
list1.add_command(label='Open', command=mopen)
list1.add_checkbutton(label='Debug Mode')
list1.add_command(label='Close', command=mclose)
list1.add_command(label='Quit', command=mquit)

list2.add_command(label='Edit Settings')
list2.add_command(label='Read Settings')
list2.add_command(label='Reset All Settings')

list3.add_command(label='About')
list3.add_command(label='Get Help')

win1.config(menu=menu1)
win1.mainloop()
