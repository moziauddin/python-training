from tkinter import *

win1 = Tk()
win1.title('Entry Class Example')
win1.geometry('300x400+300+600')

# Write function to print form
def clearform():
    print("Clearing Form")
    text1.delete(0,END)
    text2.delete(0, END)
    text3.delete(0, END)
    text4.delete(0, END)
    text5.delete(0, END)


def printform():
    print("Printing details:")
    print(text1.get(), text2.get(), text3.get(), text4.get(), text5.get())


# Create Text Boxes
text1 = Entry(win1)
text2 = Entry(win1)
text3 = Entry(win1)
text4 = Entry(win1)
text5 = Entry(win1)

# Create Labels to prepend the textboxes
lab1 = Label(win1, text='First Name: ')
lab2 = Label(win1, text='Last Name: ')
lab3 = Label(win1, text='Mobile: ')
lab4 = Label(win1, text='Email: ')
lab5 = Label(win1, text='Address: ')

# Place textboxes and labels in a grid with indexes
lab1.grid(row=0, column=0)
text1.grid(row=0, column=1)
lab2.grid(row=1, column=0)
text2.grid(row=1, column=1)
lab3.grid(row=2, column=0)
text3.grid(row=2, column=1)
lab4.grid(row=3, column=0)
text4.grid(row=3, column=1)
lab5.grid(row=4, column=0)
text5.grid(row=4, column=1)

# Declare a variable
phone = '0410 119 009'

# Insert default values for when the form loads
text1.insert(0, 'Mo')
text2.insert(0, 'Ziauddin')
text3.insert(0, phone)
text4.insert(0, 'myemailaddress@gmail.com')
text5.insert(0, '118 Robinson Crescent, Phillip, ACT 2600')

# Create Button to Print all values
Button(win1, text='Clear Form', bg='black', fg='white', command=clearform).grid(row=10, column=0)
Button(win1, text='Print Form', bg='black', fg='white', command=printform).grid(row=10, column=1)

win1.mainloop()
