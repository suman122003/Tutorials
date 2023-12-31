# solution of exercise 1 - newspaper gui
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Newpaper by Tkinter')
root.geometry('900x600')

texts = []
photos = []
for i in range(1, 4):
    with open(f'{i}.txt') as f:
        text = f.read()
        texts.append(text)
    
    image = Image.open(f'{i}.png')
    #TODO: resize the image
    photos.append(ImageTk.PhotoImage(image))


# debug it and then continue


root.mainloop()