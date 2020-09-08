#import matplot.lib as ml
#import numpy as np
import Tkinter as tk




top=tk.Tk()
p2=[40,430]
p3=[460, 430]
p1=[250,70]
tracker="g=1"
w=tk.Canvas(top,  cursor="dot", height=500, width="500")

def triangle(px1, px2, px3):
#    w=tk.Canvas(top,  cursor="dot", height=500, width="500")
    tri=w.create_polygon(50, 425, 450, 425, 250, 83, fill='', outline="Black")
    label1=w.create_text(px2, text="2")
    label2=w.create_text(px3, text="3")
    label3=w.create_text(px1, text="1")
    dividing_line=w.create_line(250,83, 250,450, dash=(10,))
    w.pack()
def text(px1, px2):
    global tracker
    #tex=tk.Canvas(top, height=100, width=500)
    if px1==[250, 70] and px2==[40,430]:
        w.create_text(250, 470, text="g=1")
    if px1==[250, 70] and px2==[460,430]:
        w.create_text(250, 470, text="g=s")
    if px1==[460, 430] and px2==[40,430]:
        w.create_text( 250,470, text="g=r*r*s")
    if px1==[40, 430] and px2==[460,430]:
        w.create_text(250, 470, text="g=r*r")
    if px1==[460, 430] and px2==[250,70]:
        w.create_text(250,470, text="g=r")
    if px1==[40, 430] and px2==[250,70]:
        w.create_text(250,470, text="g=r*s")
    w.create_text(250, 485, text=tracker)
def rf():
    global p1, p2, p3, tracker
    w.delete('all')
    p1, p2, p3= p1, p3, p2
    triangle(p1, p2, p3)
    #text(p1, p2)
    tracker=tracker+"*s"
    text(p1, p2)
def ro():
    global p1, p2, p3, tracker
    w.delete('all')
    p1, p2, p3= p2, p3, p1
    triangle(p1, p2, p3)
    tracker=tracker+"*r"
    text(p1, p2)
def buttons():
    l=tk.Button(top, text="Rotate", command=ro)
    k=tk.Button(top, text="Reflect", command=rf)
    triangle(p1, p2, p3)
    k.pack()
    l.pack()
buttons()
top.mainloop()
