# image - user cannot interact
# label, geometry, maxsize and minsize

# label - a widget  with that user can't interact (like buttons)

from tkinter import *
from PIL import Image, ImageTk

rootfn = Tk()

rootfn.geometry('644x434')  # width x height
rootfn.minsize(300, 200)    # width, height
rootfn.maxsize(1200, 988)   # width, height

image1 = Image.open('prism.png')
photo1 = ImageTk.PhotoImage(image=image1)

photo1label = Label(rootfn, image=photo1)
photo1label.pack()

rootfn.mainloop()

