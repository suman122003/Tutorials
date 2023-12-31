# label, geometry, maxsize and minsize

# label - a widget  with that user can't interact (like buttons)

from tkinter import *

rootfn = Tk()

rootfn.geometry('644x434') # width x height
rootfn.minsize(300, 200) # width, height
rootfn.maxsize(1200, 988) # width, height

skpgui1 = Label(text='This is the 1st Label in GUI (using tkinter)')
skpgui1.pack()

rootfn.mainloop()