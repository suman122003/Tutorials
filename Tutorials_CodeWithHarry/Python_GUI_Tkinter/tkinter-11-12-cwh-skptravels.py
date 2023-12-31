# travels from checkbuttons and entry widget
from tkinter import *

root = Tk()
root.geometry('600x400')

Label(root, text='SKP travels', font='comicsansms 12 bold', pady=14).grid(row=0, column=5)

names = Label(root, text='Name')
phno = Label(root, text='Phone no.')
addr = Label(root, text='Address')
emrgc = Label(root, text='Emergency Contact')
pmnt = Label(root, text='Payment Mode')

names.grid(row=1, column=3)
phno.grid(row=2, column=3)
addr.grid(row=3, column=3)
emrgc.grid(row=4, column=3)
pmnt.grid(row=5, column=3)

namesvalue = StringVar()
phnovalue = StringVar()
addrvalue = StringVar()
emrgcvalue = StringVar()
pmntvalue = StringVar()
foodservice = StringVar()

namesentry = Entry(root, textvariable=namesvalue)
phnoentry = Entry(root, textvariable=phnovalue)
addrentry = Entry(root, textvariable=addrvalue)
emrgcentry = Entry(root, textvariable=emrgcvalue)
pmntentry = Entry(root, textvariable=pmntvalue)

def getvals():
    print('Submitting details...')
    print(f'{namesvalue.get()}, {phnovalue.get()}, {addrvalue.get()}, {emrgcvalue.get()}, {pmntvalue.get()}.')
    with open('skp travels records.txt', 'w') as f:
        f.write(f'{namesvalue.get()}, {phnovalue.get()}, {addrvalue.get()}, {emrgcvalue.get()}, {pmntvalue.get()}.')
    print('Your details are submitted.')

namesentry.grid(row=1, column=5)
phnoentry.grid(row=2, column=5)
addrentry.grid(row=3, column=5)
emrgcentry.grid(row=4, column=5)
pmntentry.grid(row=5, column=5)

foodservicecb = Checkbutton(text='Want to prebook your meals?', variable=foodservice)
foodservicecb.grid(row=6, column=5)

Button(text='Submit', command=getvals).grid(row=7, column=5)

root.mainloop()