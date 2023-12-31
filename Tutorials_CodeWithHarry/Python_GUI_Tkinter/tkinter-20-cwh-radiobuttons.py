# radiobuttons
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title('Radiobuttons tutorials')
root.geometry('700x400')

var = IntVar()

Label(root, text='Here are the dishes. What would you like to have sir?', 
        font='lucida 10 bold', justify=LEFT, padx= 14).pack()
radio1 = Radiobutton(root, text='1. Mixed Rice', padx=14, 
                variable=var, value=1).pack(anchor='w')
radio1 = Radiobutton(root, text='2. Paratha', padx=14, 
                variable=var, value=2).pack(anchor='w')
radio1 = Radiobutton(root, text='3. Idli', padx=14, 
                variable=var, value=3).pack(anchor='w')
radio1 = Radiobutton(root, text='4. Dosa', padx=14, 
                variable=var, value=4).pack(anchor='w')
def ordernow():
    tmsg.showinfo('Order Received', f'Your order for {var.get()} has been received.')
Button(text='Order Now', command=ordernow).pack()

root.mainloop()