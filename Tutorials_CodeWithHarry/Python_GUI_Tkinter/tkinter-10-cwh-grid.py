# widget and grid layout
from tkinter import *

root = Tk()
root.geometry('700x400')

usr = Label(root, text='Username')
pas = Label(root, text='Password')
usr.grid()
pas.grid(row=1)

# Variables in tkinter - BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

def getvals():
    print(f'Username: {uservalue.get()}')
    print(f'Password: {passvalue.get()}')

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text='Submit', command=getvals).grid()

root.mainloop()
