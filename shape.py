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
def text(p1, p2):
    tex=tk.Canvas(top, height=100, width=500)
    if p1==[250, 70] and p2==[40,430]:
        tex.create_text(50, 250, text="g=1")
    if p1==[250, 70] and p2==[460,430]:
        tex.create_text(50, 250, text="g=s")
    if p1==[460, 430] and p2==[40,430]:
        tex.create_text(50, 250, text="g=rs")
    if p1==[40, 430] and p2==[460,430]:
        tex.create_text(50, 250, text="g=r")
    if p1==[460, 430] and p2==[250,70]:
        tex.create_text(50, 250, text="g=r^2")
    if p1==[40, 430] and p2==[250,70]:
        tex.create_text(50, 250, text="g=r^2s")
    tex.pack()
def rf(p1, p2, p3):
    p4=p3
    p3=p2
    p2=p4
def ro(p1, p2, p3):
    p4=p1
    p1=p2
    p2=p3
    p3=p4
    print(p4)
def buttons(p1, p2, p3):
    l=tk.Button(top, text="Rotate", command=ro(p1, p2, p3))
    k=tk.Button(top, text="Reflect", command=rf(p1, p2, p3))
    triangle(p1, p2, p3)
    text(p1, p2)
    k.pack()
    l.pack()
buttons(p1, p2, p3)
top.mainloop()
