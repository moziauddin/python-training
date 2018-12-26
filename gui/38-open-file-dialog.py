from tkinter import *
from tkinter import filedialog

win1 = Tk()
win1.title('Open File Dialog Example')


def openFileDialog():
    fileLoc = filedialog.askopenfile('r')
    print("Your pick was:", fileLoc)
    label1 = Label(text=fileLoc, fg='red').pack()


but = Button(text='Open File', width=30, bg='salmon', fg='red', command=openFileDialog)
but.pack()
win1.mainloop()
