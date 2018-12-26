from tkinter import *
win1 = Tk()
win1.title('Radio Button Example')

rb1 = Radiobutton(win1, text='yes', bg='olive', padx=33, pady=33).pack(anchor='w')
rb2 = Radiobutton(win1, text='no', fg='purple').pack(anchor='w')

def trigger():
    getval = int.get()
    if getval == 0:
        Label(text='Female Selected', fg='red').pack()
    elif getval == 1:
        Label(text='Male Selected', fg='red').pack()
    else:
        Label(text='Neutral Selected', fg='blue').pack()


int = IntVar()
int.set(10)
Label(text='------------------------', justify=LEFT).pack()
Label(text="Choose gender:", justify=LEFT).pack()
Radiobutton(text='Male', variable=int, value=1, command=trigger).pack(anchor=W)
Radiobutton(text='Female', variable=int, value=0, command=trigger).pack(anchor=W)

# Create radio buttons from a list
gender = [('Male', 1), ('Female', 0), ('neutral', 2)]
Label(text="Choose gender from List:", justify=LEFT).pack()

# Create radio buttons using for look
# indicatoron=0 is used to switch from circle to full button
for txt, val in gender:
    Radiobutton(win1, text=txt, value=val, indicatoron=0, command=trigger, variable=int).pack(anchor=W)

win1.mainloop()