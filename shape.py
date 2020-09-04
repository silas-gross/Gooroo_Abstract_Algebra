#import matplot.lib as ml
#import numpy as np
import Tkinter as tk

#def triangle:


top=tk.Tk()
w=tk.Canvas(top,  cursor="dot", height=500, width="500")
tri=w.create_polygon(50, 425, 450, 425, 250, 83, fill='', outline="Black")
label1=w.create_text(40, 430, text="2")
label2=w.create_text(460, 430, text="3")
label3=w.create_text(250, 75, text="1")
dividing_line=w.create_line(250,83, 250,450, dash=(10,))
w.pack()
top.mainloop()
