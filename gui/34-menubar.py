from tkinter import *


def readdata():
    print("Clicked ReadData: You typed:", textval.get())


def removedata():
    print("Clicked RemoveData")


def newfile():
    print("clicked on new file")


win1 = Tk()
win1.title("Read from Textbox using a Button")
win1.geometry("200x200+100+600")

textval = StringVar()
lab1 = Label(text='Your Name:', fg='lemon chiffon', bg='saddle brown').grid(row=0, column=0)
but1 = Button(text='Read', bg='wheat', fg='brown', command=readdata, font=('Calibri', 11, 'normal')).grid(row=3, column=0)
but2 = Button(text='Remove', bg='wheat', fg='brown', command=removedata).grid(row=3, column=1)
text1 = Entry(textvariable=textval).grid(row=0, column=1)

# Use font=(name,size,style) Ex: font=('Calibri',11,'italic')
# Adding Menubar, menu and menu items
# Use Menu() class to create a nenu item
# Menu1 becomes the root or your menubar
# Then we add lists for each menu item using Menu() class
# add_cascade class adds a menu to the root menu
# You can pass the label, and the menu list you want to add to that menu
# add_command is used to add a label and functionality to the menu command
# Use .config method with the root menu as an argument

menu1 = Menu()  # Creates a menu object
list1 = Menu()  # Creates a menu list
list2 = Menu()
list3 = Menu()
menu1.add_cascade(label='Main', menu=list1)  # Adds menus to the menu bar and passes the list
menu1.add_cascade(label='Settings', menu=list2)
menu1.add_cascade(label='Help', menu=list3)

list1.add_command(label='New', command=newfile)  # Add commands to a list. Add command=name to add finctionality
list1.add_command(label='Open')
list1.add_command(label='Close')
list1.add_command(label='Quit')

list2.add_command(label='Edit Settings')
list2.add_command(label='Read Settings')
list2.add_command(label='Reset All Settings')

list3.add_command(label='About')
list3.add_command(label='Get Help')

win1.config(menu=menu1)  # Adds Menubar to the window

# To keep the window visible, use mainloop()
win1.mainloop()
