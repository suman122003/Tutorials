# lsitbox
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title('ListBox Tutorial')
root.geometry('700x400')

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, '1st of item our listbox')
def additem():
    global i
    lbx.insert(ACTIVE, f'{i}')
    i += 1
i=0
Button(root, text='Add item', command=additem).pack()

root.mainloop()