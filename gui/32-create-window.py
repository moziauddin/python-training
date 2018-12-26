from tkinter import *

win1 = Tk()  # object of class Tk
win1.title("My First PyGUI Window")  # Adds title to the window
win1.geometry("400x400+100+600")
lab1 = Label(text='Name: ', fg='Navy', bg='Teal')
lab1.pack()
lab1 = Label(text='Email: ', fg='Navy', bg='Teal').pack()
# To keep the window visible, use mainloop()
win1.mainloop()
