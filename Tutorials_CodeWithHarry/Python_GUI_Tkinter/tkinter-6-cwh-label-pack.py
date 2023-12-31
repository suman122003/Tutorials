from tkinter import *
root =  Tk()
root.geometry('500x400')

root.title('GUI by CodeWithHarry')

'''
Important Label options
text - adds the text
bg - background
fg - foreground
font - sets the font
1. font=('Comicsansns', 12, 'bold')
2. font = 'comicsansms 12 bold'
padx - x padding
pady - y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
'''

titlelbl = Label(text='''
GUI is used to make an interactive interface. 
The idea of learning it came to my mind after seeing the software in Ajoy Ghatak sir's quantum mechanics course.
This is the first attempt to learn GUI. Thanks to CodeWithHarry for making this course''',
bg='red', fg='white', padx=83, pady=16, 
font = 'comicsansms 12 bold', borderwidth=2.5, relief=SUNKEN)

'''
Important pack options
anchor = nw, ne
side = top (default), bottom left, right
fill
padx
pady
'''

titlelbl.pack(side='bottom', anchor='sw', fill=X, padx=30, pady=30)

root.mainloop()
