from tkinter import *

counter = 0


def counterDisplay(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()


win1 = Tk()
win1.title("Simple Counter")
win1.geometry("50x110+300+600")
display = Label(win1, font=('Verdana', 44, 'bold'))
display.pack()
stopButton = Button(win1, command=win1.destroy, text='Stop', bg='wheat', fg='brown').pack()
counterDisplay(display)

win1.mainloop()


'''
Notes:

If you use display = Label(win1, font=('Verdana', 44, 'bold')).pack() 
in one statement, then it will result in the below error:
---------------------------------------
AttributeError: 'NoneType' object has no attribute 'config'
---------------------------------------

'''
