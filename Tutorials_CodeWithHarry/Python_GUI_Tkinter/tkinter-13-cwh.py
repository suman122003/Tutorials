# canvas widget
from tkinter import *

root = Tk()
canvas_width = 1000
canvas_height = 700
root.geometry(f'{canvas_width}x{canvas_height}')
root.title('Tutorial 13 by CodeWithHarry')

canvaswidget = Canvas(root, width=canvas_width, height=canvas_height)
canvaswidget.pack()
# line from (x1, y1) to (x2, y2)
canvaswidget.create_line(0, 0, 900, 600, fill='red')
canvaswidget.create_line(0, 600, 900, 0, fill='red')
# top left point to bottom right coordinates
canvaswidget.create_rectangle(3, 5, 700, 400, fill='green')
# give coordinate like rectangle which will fit the oval
canvaswidget.create_oval(30, 50, 650, 350, fill='grey')
# coordinate of center of text
canvaswidget.create_text(200, 200, text='Created in Python GUI - Tkinter\n\t Using Canvas', 
                        fill='red')

root.mainloop()