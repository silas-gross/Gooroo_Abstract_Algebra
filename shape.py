import tkinter as tk
import tkinter.font as tkFont
import math
import time

root = tk.Tk()
id = lambda p: p

currentRotation = tk.IntVar(root, value=0)
currentReflection = tk.IntVar(root, value=1)
currentTransLabel = tk.StringVar(root, value="g = I")

fontSize = tkFont.Font(family="Arial", size=12)
colors = ['IndianRed1', 'SpringGreen2', 'cornflower blue', 'peach puff', 'LightGoldenrod1', 'SkyBlue3', 'MediumPurple1', 'LightCyan2', 'Orange', 'turquoise']

def createText(target, x, y, n):
	text = target.create_text(x, y, text = str(n+1), tag = "l." + str(n), font = ("Arial", 12))
	rect = target.create_rectangle(target.bbox(text), fill = colors[n%len(colors)], tag = "l.r." + str(n))
	target.tag_lower(rect, text)


def relocateText(target, x, y, n):
	if len(target.find_withtag("l." + str(n))) == 0:
		return

	target.coords("l." + str(n), x, y)
	bbox = target.bbox("l." + str(n))
	bbox = (bbox[0]-4, bbox[1]-4, bbox[2]+4, bbox[3]+4)
	target.coords("l.r." + str(n), bbox)


# Translates in polar to rotate the figure
def polarTrans(p):
	return (p[0] + currentRotation.get(), p[1])

# Translates in cartesian to center and reflect
def cartTrans(p):
	return (currentReflection.get() * p[0] + 250, p[1] + 250)


################################################################################
##
##               Button callback functions
##
###############################################################################

# Removes a point
# Changes the label, animates down by one point, and remove the extra label
def subPoint():
	global currentPoints, currentPointsLabel, canvas, polyId
	if currentPoints.get() == 3:
		return
	reset()

	currentPoints.set(currentPoints.get()-1)
	currentPointsLabel.set(str(currentPoints.get()))

	# Remove the extra label
	canvas.delete("l." + currentPointsLabel.get())
	canvas.delete("l.r." + currentPointsLabel.get())

	plotToPolygon(canvas, polyId, currentPoints.get()+1, 200, -1, 10, .1, interp=quadInterp)


# Adds a point
# Changes the label, animates up by a point, and adds an extra point label
def addPoint():
	global currentPoints, currentPointsLabel, canvas, polyId
	if currentPoints.get() == 20:
		return
	reset()

	# Add a new label
	createText(canvas, 0, 0, currentPoints.get())

	currentPoints.set(currentPoints.get()+1)
	currentPointsLabel.set(str(currentPoints.get()))

	plotToPolygon(canvas, polyId, currentPoints.get(), 200, 1, 10, .1, interp=quadInterp)


# Changes the trans identity and rotation variable
def rotate():
	global currentRotation, currentTransLabel
	currentRotation.set(currentRotation.get() + 360/currentPoints.get())
	currentTransLabel.set(currentTransLabel.get() + " * s")

	plotPolygon(canvas, polyId, currentPoints.get(), 200)


# Changes the trans identity and reflection variable
def reflect():
	global currentReflection, currentTransLabel
	currentReflection.set(currentReflection.get() * -1)
	currentTransLabel.set(currentTransLabel.get() + " * r")

	plotPolygon(canvas, polyId, currentPoints.get(), 200)


# Brings all trans, rotation, and reflection back to initial
def reset():
	global currentRotation, currentReflection, currentTransLabel
	currentRotation.set(0)
	currentReflection.set(1)
	currentTransLabel.set("g = I")

	plotPolygon(canvas, polyId, currentPoints.get(), 200)


######################################################################
##
##             Build functions, one for each pane
##
######################################################################

def buildNCounter():
	global currentPoints, currentPointsLabel

	nCounter = tk.Frame(root, pady=5)
	nCounter.pack(side=tk.TOP)

	# Initialize as a triangle
	currentPoints = tk.IntVar(root, value = 3)
	currentPointsLabel = tk.StringVar(root, "3")

	tk.Button(root, text = "-", command = subPoint).pack(in_=nCounter, side=tk.LEFT)
	tk.Label(root, textvariable=currentPointsLabel, padx=10, font=fontSize).pack(in_=nCounter, side=tk.LEFT)
	tk.Button(root, text = "+", command = addPoint).pack(in_=nCounter, side=tk.LEFT)


def buildRRR():
	rrrControls = tk.Frame(root, pady=5)
	rrrControls.pack(side=tk.TOP)

	tk.Button(root, text = "Rotate", command = rotate).pack(in_=rrrControls, side=tk.LEFT, padx=5)
	tk.Button(root, text = "Reflect", command = reflect).pack(in_=rrrControls, side=tk.LEFT, padx=5)
	tk.Button(root, text = "Reset", command = reset).pack(in_=rrrControls, side=tk.LEFT, padx=5)


def buildCanvas():
	global canvas, polyId

	drawPane = tk.Frame(root, pady=10)
	drawPane.pack(side=tk.TOP)
	canvas = tk.Canvas(root, height=500, width=500)

	# Create a blank polygon to get an id and 3 initial labels
	polyId = canvas.create_polygon(0, 0, outline='black', fill='')
	createText(canvas, 0, 0, 0)
	createText(canvas, 0, 0, 1)
	createText(canvas, 0, 0, 2)

	plotPolygon(canvas, polyId, currentPoints.get(), 200)

	# Dotted line
	xc, yc = polarToCart([(0, 0)])[0]
	canvas.create_line(xc, yc-250, xc, yc+250, dash=(10,))

	canvas.pack(in_=drawPane)


def buildCurrentTrans():
	bottom = tk.Frame(root, pady=5)
	bottom.pack(side=tk.TOP)
	tk.Label(root, textvariable=currentTransLabel, font=fontSize).pack(in_=bottom)


def build():
	buildNCounter()
	buildCanvas()
	buildCurrentTrans()
	buildRRR()


###########################################################################
##
##          Interpolators
##
###########################################################################

def linearInterp(start, stop, progress):
	return start + (stop-start) * progress

def quadInterp(start, stop, x):
	mult = 8 * x * x * x * x if x < 0.5 else 1 - math.pow(-2 * x + 2, 4) / 2;
	return start + (stop-start)*mult


# Computes the polar points of a regular n-gon based on its radius and number of sides
# A simple point generator function essentially
def computeNgonPolar(n, r):
	alpha = 360.0 / n
	points = []
	angle = -90 if n%2 == 1 else alpha/2-90
	for c in range(n):
		points.append((angle%360, r))
		angle += alpha
	return points


# Computes the too n-gon point sets
# Generates a set of starting points and a set of ending points, then uniformly interpolates
# Direction function impacts if they interpolate start to end (forward, 1) or end to start (backwards, -1)
def computeToNgon(n, r, direction, steps, interp=linearInterp):
	alpha0 = 360.0 / (n-1)
	alpha1 = 360.0 / n

	pointStarts = polarToCart(computeNgonPolar(n-1, r))
	pointStarts.append(pointStarts[0])
	pointEnds = polarToCart(computeNgonPolar(n, r))

	points = []
	for step in range(steps):
		pointSet = []

		progress = step / (steps-1)
		for c in range(n):
			x1, y1 = pointStarts[c]
			x2, y2 = pointEnds[c]
			if direction > 0:
				pointSet.append((interp(x1, x2, progress), interp(y1, y2, progress)))
			else:
				pointSet.append((interp(x2, x1, progress), interp(y2, y1, progress)))

		points.append(pointSet)

	return points


# Acts on a list converting each point from polar to cartesian
def polarToCart(points):
	cart = []
	for p in points:
		a, r = polarTrans(p)
		rads = math.radians(a%360)
		cp = cartTrans((r*math.cos(rads), r*math.sin(rads)))
		cart.append(cp)
	return cart


# Plots a list of cartesian points
# A utility method for flattening and handling canvas operations
def plotCartesianPoints(target, polyId, points, xc, yc, gap=15):
	flat = []
	for x, y in points:
		flat.append(x)
		flat.append(y)
	target.coords(polyId, *flat)

	n = 0
	for x, y in points:
		x += gap if x > xc else -gap
		y += gap if y > yc else -gap
		relocateText(target, x, y, n)
		n += 1


# The most accessible polygon plotting function
# Takes care of all required math to make a side length and radius turn into a canvas plot
def plotPolygon(target, polyId, n, r, gap=15):
	points = computeNgonPolar(n, r)
	xc, yc = polarToCart([(0, 0)])[0]

	cartPoints = polarToCart(points)

	plotCartesianPoints(target, polyId, cartPoints, xc, yc, gap)


# An animation that plots each frame of the interpolation between shapes
def plotToPolygon(target, polyId, n, r, direction, steps, delay, interp=linearInterp, gap=15):
	points = computeToNgon(n, r, direction, steps, interp)
	xc, yc = polarToCart([(0, 0)])[0]
	for pointSet in points:
		plotCartesianPoints(target, polyId, pointSet, xc, yc, gap)
		root.update()
		time.sleep(delay)

build()
root.mainloop()

