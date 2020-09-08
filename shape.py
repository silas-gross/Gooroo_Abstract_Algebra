#import matplot.lib as ml
#import numpy as np
import Tkinter as tk




top=tk.Tk()
def triangle(p1, p2, p3):
    w=tk.Canvas(top,  cursor="dot", height=500, width="500")
    tri=w.create_polygon(50, 425, 450, 425, 250, 83, fill='', outline="Black")
    label1=w.create_text(p2, text="2")
    label2=w.create_text(p3, text="3")
    label3=w.create_text(p1, text="1")
    dividing_line=w.create_line(250,83, 250,450, dash=(10,))
    w.pack()
p2=[40,430]
p3=[460, 430]
p1=[250,70]
def rf(p1, p2, p3):
    p4=p3
    p3=p2
    p2=p4
def ro(p1, p2, p3):
    p4=p1
    p1=p2
    p2=p3
    p3=p4
def buttons(p1, p2, p3):
    l=tk.Button(top, text="Rotate", command=ro(p1, p2, p3))
    k=tk.Button(top, text="Reflect", command=rf(p1, p2, p3))
    k.pack()
    l.pack()
    triangle(p1, p2, p3)
    print(p1)
buttons(p1, p2, p3)

top.mainloop()
