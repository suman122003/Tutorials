# frame in tkinter
from tkinter import *

root = Tk()
root.geometry('600x400')

f1 = Frame(root, bg='grey', borderwidth=5, relief=SUNKEN)
f1.pack(side=LEFT, fill='y')

l1 = Label(f1, text='Project Tkinter')
l1.pack(pady=40)

f2 = Frame(root, bg='blue', borderwidth=5, relief=SUNKEN)
f2.pack(side=TOP, fill='x')
l2 = Label(f2, text='Done in Visual Studio Code', font='helvetica 12 bold', 
           fg='white', bg='green')
l2.pack()

root.mainloop()