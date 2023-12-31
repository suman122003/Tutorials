# sliders
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title('Tutorial 19 - Sliders')
root.geometry('700x400')

myslider = Scale(root, from_=0, to=100)
myslider.pack()
Label(root, text='How many dollars do you want?').pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
myslider2.set(24)
myslider2.pack()
def getdollar():
    a = f'We have credited {myslider2.get()} Dollars in your account.'
    tmsg.showinfo('Congratulations', a)
Button(root, text='Get Dollars!', command=getdollar).pack()

root.mainloop()