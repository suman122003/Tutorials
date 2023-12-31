# menus and submenus
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title('Pycharm duplicate')
root.geometry('700x400')

def myfunc():
    print('It is a random functions.')
def newproj():
    print('A new project is created.')
def savefn():
    print('Your File is saved.')
def saveasfn():
    print('Select the location where the file will be saved.')
def printfn():
    print('It\'s the print option.')

def helpfn():
    tmsg.showinfo('Help', 'Mail me if you are having problems using this software.')

def rateus():
    yorn = tmsg.askquestion('Experience', 'Was your experience good?')
    print(yorn)
    if yorn == 'yes':
        msg = 'Great! Keep exploring. We will add more things in this software.'
    else:
        msg = 'Ok. Stay tuned. We are frequently updating this software.'
    tmsg.showinfo('Thanks for the response.', msg)

def kriti():
    ans = tmsg.askretrycancel('Kriti se dosti kar lo...', 
            'Sorry, Kriti nahi banegi aapki dost. Usse manane ke liye Retry karo.')
    if ans:
        rep = 'Retry karne pe bhi kuch nahi hoga. Zyada frank hua to thappad padega.'
    else:
        rep = 'Bahut badiya bhai can kar diya warna pitte.'
    tmsg.showinfo('Warning!', rep)

mymenu = Menu(root)
# mymenu.add_command(label='File', command=myfunc) # not drop down

m1 = Menu(mymenu, tearoff=0)
m1.add_command(label='New Project', command=newproj)
m1.add_command(label='Save', command=savefn)
m1.add_command(label='Save As', command=savefn)
m1.add_separator()
m1.add_command(label='Print', command=printfn)

mymenu.add_cascade(label='File', menu=m1)

m2 = Menu(mymenu, tearoff=0)
m2.add_command(label='Cut')
m2.add_command(label='Copy')
m2.add_command(label='Paste')
m2.add_separator()
m2.add_command(label='Find')
mymenu.add_cascade(label='Edit', menu=m2)

m3 = Menu(mymenu, tearoff=0)
m3.add_command(label='Help', command=helpfn)
m3.add_command(label='Rate Us', command=rateus)
m3.add_command(label='Befriend Kriti?', command=kriti)
mymenu.add_cascade(label='Help', menu=m3)

mymenu.add_command(label='Exit', command=quit)

root.config(menu=mymenu)

root.mainloop()
