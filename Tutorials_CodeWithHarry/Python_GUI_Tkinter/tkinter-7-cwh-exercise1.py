# newspaper gui
from tkinter import *
from PIL import Image, ImageTk

rootb = Tk()
rootb.geometry('700x500')

img1 = Image.open('1.png')
image1 = ImageTk.PhotoImage(image=img1)

imglbl1 = Label(image=image1)
imglbl1.pack()

rootb.mainloop()
