from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title('User Experience')
root.geometry('500x200')
t1 = '''Thanks for exploring the website. Please give your feedback here.
What do you rate out of 100 for this website?'''
Label(root, text=t1).pack()
sl = Scale(root, from_=0, to=100, orient=HORIZONTAL)
sl.set(60)
sl.pack()
def userexp():
    tmsg.showinfo('Feedback', 'Thanks for the feedback.')
Button(root, text='Submit', command=userexp).pack()
root.mainloop()