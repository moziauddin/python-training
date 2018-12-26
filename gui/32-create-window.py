from tkinter import *

win1 = Tk()  # object of class Tk
win1.title("My First PyGUI Window")  # Adds title to the window
win1.geometry("400x400+100+600")
lab1 = Label(win1, text='Your Name:', fg='Navy', bg='Teal')
# lab1.pack()  # Places the element in the center of the window
# lab1.place(x=0, y=0)  # places the element wrt the left top corner
lab1.grid(row=0, column=0, sticky='w')  # Places in a grid ref by rows and columns
lab2 = Label(win1, text='Enter your Email:', fg='dark red', bg='coral')\
# lab2.pack()
# lab2.place(x=0, y=20)
lab2.grid(row=2, column=0, sticky='w')


# Creating Second Window
# Pass the object name of the window as a property to each element

win2 = Tk()
win2.title('My Second Window')
win2.geometry("400x400+600+600")
lab3 = Label(win2, text='Name: ', bg='coral', fg='dark red').place(x=0, y=0)
lab4 = Label(win2, text='Email: ', bg='coral', fg='dark red').place(x=0, y=20)

# To keep the window visible, use mainloop()
win1.mainloop()
# win2.mainloop()
