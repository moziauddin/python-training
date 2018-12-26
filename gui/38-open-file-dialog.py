from tkinter import *
from tkinter import filedialog

win1 = Tk()
win1.title('Open File Dialog Example')


def openfiledialog():
    fileloc = filedialog.askopenfile('r')  # Brings up file open dialogue. fileloc contains a TextIOWrapper
    print("Your pick was:", fileloc)
    label1 = Label(text=fileloc, fg='red').pack()  # Prints the file name to a label
    # Open and Read the File Contents
    filename = fileloc.name  # Gets file name from the TextIOWrapper
    fileopen = open(filename)  # Opens file as a String/Bytes
    label2 = Label(text=fileopen.read(), fg='blue').pack()


but = Button(text='Open File', width=30, bg='salmon', fg='red', command=openfiledialog)
but.pack()
win1.mainloop()
