#import matplot.lib as ml
import numpy as np
import tkinter as tk
import math 



top=tk.Tk()
p2=[40,430]
p3=[460, 430]
p1=[250,70]
tracker="g=1"
w=tk.Canvas(top,  cursor="dot", height=500, width="500")
pf1, pf2, pf3, traf=p1, p2, p3, tracker
def makepoints(angle, side, nsides): # this actually splits the plane to create the points
    #This method just uses the sidelenghts as a method of getting the points, uses the angle for verification after the fact
    #Choose the first point as the center of the top and then go from there
    startingpoint=[250, 100] #kind of arbitrary, based on what looks nice from the triangle
    ns=int(nsides/2)
    stepsize=np.zeros(2)
    stepsizetrue=500/ns
    center_angle=2*np.Pi/nsides
    stepsize[0]=int(math.sqrt(side*side- stepsizetrue*stepsizetrue))
    stepsize[1]=int(stepsizetrue)
    x, y= np.zeros[nsides], np.zeros[nsides]
    for i in range(nsides):
        #need to choose a maximum range of y, then fix the step length for y and correct x 
        #going to choose y:100->600
        #so then just do a bit of math here
        #we take the centeral angle to just be 2*pi/n
        #Then the angle between any two points must be that 
        #so if we take the first point, and write the traingle as a side with length s
        #then it is a isocoles triangle.
        #we take that the total change in y must be in that range
        #we have fixed delta x and fixed delta y in the assumption that we alway change the coordinates such that we have the central line in the y direction
        #This takes the transform of y->y cos a +x sin a
        #Then 
        if i==0: 
            x[i]=startingpoint[0]
            y[i]=startingpoint[1]
        if i==1:
            x[i]=startingpoint[0]+stepsize[0]
            y[i]=startingpoint[1]+stepzize[1]
        else:
            y[i]=y[i-1]+int(s*(np.sin(angle/2)*np.pow(np.sin(center_angle), i)+ np.cos(angle/2)*np.pow(np.cos(center_angle),i))) 
            x[i]=x[i-1]+int(s*(np.cos(angle/2)*np.pow(np.sin(center_angle), i)+ np.sin(angle/2)*np.pow(np.cos(center_angle),i)))

                #I think this should work but I actually am not certian of my calculations here.
    return x, y

def nsidedpolygon(npoints): #takes in a number of sides and draws a polygon
    angle=(180*(npoints-2))/npoints #measure of each angle
    slength=1200/npoints #side length with a fixed perimeter. maybe try (n-1)^2 scaling?? or just (n-2) scaling??, lets see how fixed lenght works. may make more sense to do n/n^2 type scaling
    xpoints=np.zeros(npoints)
    ypoints=np.zeros(npoints)
    # create the array of points, that will then be brought together into a single array 
    #this may actually work better in mathematica, but I have no idea how to properly work with this sort of GUI in mathematica--want to use a functional paradigm, can that be done here?
    xpoints, ypoints=makepoints(angle, slength, npoints)
    points=np.zeros(2*npoints)
    for i in range(npoints):
        points[2*i]=xpoints[i]
        points[2*i+1]=ypoints[i]
    return points

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
        w.create_text(250, 470, text="g=r")
    if px1==[460, 430] and px2==[250,70]:
        w.create_text(250,470, text="g=r*r")
    if px1==[40, 430] and px2==[250,70]:
        w.create_text(250,470, text="g=r*s")
    w.create_text(250, 485, text=tracker)
def rf():
    global p1, p2, p3, tracker
    w.delete('all')
    if p1==[250, 70]:
        p1, p2, p3= p1, p3, p2
    if p2==[250, 70]:
        p1, p2, p3=p3, p2, p1
    if p3==[250, 70]:
        p1, p2, p3=p2, p1, p3
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
def rs():
    global p1, p2, p3, tracker, pf1, pf2, pf3, traf
    w.delete('all')
    p1, p2, p3, tracker=pf1, pf2, pf3, traf
    triangle(p1, p2, p3)
    text(p1, p2)
def buttons():
    l=tk.Button(top, text="Rotate", command=ro)
    k=tk.Button(top, text="Reflect", command=rf)
    m=tk.Button(top, text="Reset", command=rs)
    triangle(p1, p2, p3)
    k.pack()
    l.pack()
    m.pack()
buttons()
top.mainloop()
