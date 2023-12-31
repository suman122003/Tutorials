# Events
from tkinter import *
root = Tk()
root.geometry('700x400')
root.title('Tutorial 14 - Events in Tkinter')

wd = Button(root, text='Click Here')
wd.pack()

# see events in the documentation

def print1(event):
    print(f'You clicked on the button at {event.x}, {event.y}')

wd.bind('<Button-1>', print1)
wd.bind('<Double-1>', quit)   # double click to quit

root.mainloop()
