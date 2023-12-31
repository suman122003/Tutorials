# buttons
from tkinter import *

def hellotkb():
    print('hello tkinter buttons')
def tutorialdt():
    print('This is the 9th video in the tkinter tutorial series by CodeWithHarry.')

root = Tk()
root.geometry('600x400')

f1 = Frame(root, borderwidth=5, bg='grey', relief='sunken')
f1.pack(side=LEFT, anchor='nw')

b1 = Button(f1, fg='red', text='Print now 1', command=hellotkb)
b1.pack(side=RIGHT, anchor='ne')
b2 = Button(f1, fg='red', text='Print now 2', command=tutorialdt)
b2.pack(side=RIGHT, anchor='ne')
b3 = Button(f1, fg='red', text='Print now 3')
b3.pack(side=RIGHT, anchor='ne')
b4 = Button(f1, fg='red', text='Print now 4')
b4.pack(side=RIGHT, anchor='ne')

root.mainloop()