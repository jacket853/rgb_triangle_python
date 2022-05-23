from graphics import *
import math

def drawUI(win, centPoint, R, G, B):

    # Triangle BCG
    BGClst = [B, centPoint, G]
    BGC = Polygon(BGClst)
    BGC.setFill("red")
    BGC.draw(win)

    # Triangle RCB
    RCBlst = [R, centPoint, B]
    RCB = Polygon(RCBlst)
    RCB.setFill("lime green")
    RCB.draw(win)

    # Triangle RCG
    RCGlst = [R, centPoint, G]
    RCG = Polygon(RCGlst)
    RCG.setFill("blue")
    RCG.draw(win)

    # Create point labels for triangle
    Rlabel = Text(Point(150, 85), "R")
    Rlabel.setSize(24)
    Rlabel.setTextColor("red")
    Rlabel.draw(win)

    Glabel = Text(Point(165 + (125 * math.sqrt(3)), 225), "G")
    Glabel.setSize(24)
    Glabel.setTextColor("green")
    Glabel.draw(win)

    Blabel = Text(Point(150, 365), "B")
    Blabel.setSize(24)
    Blabel.setTextColor("blue")
    Blabel.draw(win)

    # No return val - this function purely draws

def writeText(win):
    # On-start UI text - simple instructions for user
    startText = Text(Point(285, 50), "This program helps you find out what color corresponds with any point inside the Exeter RGB triangle.")
    startText.setTextColor("black")
    startText.setSize(9)
    startText.draw(win)
    directions = Text(Point(250, 430), "Click inside the triangle to move the point - the box shows the resulting color.\nClick on the black exit circle to end the program.")
    directions.setTextColor("black")
    directions.setSize(11)
    directions.draw(win)

def getCentroid(p1, p2, p3):
    # Get x and y values for each vertex on the triangle
    X1 = p1.getX()
    X2 = p2.getX()
    X3 = p3.getX()

    Y1 = p1.getY()
    Y2 = p2.getY()
    Y3 = p3.getY()

    # Average of the x and y values is the centroid
    cX = (X1 + X2 + X3) / 3
    cY = (Y1 + Y2 + Y3) / 3
    centroid = Point(cX, cY)

    return centroid

def drawExit(win):
    exPoint = Point(550, 450)
    exitCircle = Circle(exPoint, 30) # Creating circle and text
    exitCircle.setFill("black")
    exitCircle.draw(win)

    exitText = Text(exPoint, "click to exit")
    exitText.setSize(9)
    exitText.setTextColor("white")
    exitText.draw(win)
    return exitCircle

def pointChoice(win, exit):
    # Waits for mouseclick, gets attributes of clicked point
    newPoint = win.getMouse()
    xPos = newPoint.getX()
    yPos = newPoint.getY()

    # Gets attributes of circle - you must click on this circle to exit
    cent = exit.getCenter()
    centX = cent.getX()
    centY = cent.getY()
    r = exit.getRadius()

    # If the point is between edes of circle
    if (xPos - r <= centX <= xPos + r) and (yPos + r >= centY >= yPos - r):
        return True # The user clicked the circle
    else:
        return newPoint # Returns point to b e used later as new "centroid"

def colorOutput(win, r, g, b, full): # Pass areas through function for proportions
    # Compare smaller areas to area of big triangle, calculate color amounts
    # If the user clicked closer to a vertex than a side
    if r > ((2/3) * full) or g > ((2/3) * full) or b > ((2/3) * full):
        BNGred = int(255 * (r / full))
        RNBgreen = int(255 * (g / full))
        RNGblue = int(255 * (b / full))
    elif r < ((1/3) * full): # If it is mostly blue and green
        BNGred = int(255 * (r / full))
        RNBgreen = int(255 * ((b + g) / full))
        RNGblue = int(255 * ((g + b) / full))
    elif g < ((1/3) * full): # If it is mostly blue and red
        BNGred = int(255 * ((r + b) / full))
        RNBgreen = int(255 * (g / full))
        RNGblue = int(255 * ((b + r) / full))
    elif b < ((1/3) * full): # If it is mostly red and green
        BNGred = int(255 * ((g + r) / full))
        RNBgreen = int(255 * ((r + g) / full))
        RNGblue = int(255 * (b / full))
    else: # If the user clicked perfectly in the center, the color is white
        BNGred = 255
        RNBgreen = 255
        RNGblue = 255

    # Using color_rgb function - if tuple does not correspond, nearest hex val
    color = color_rgb(BNGred, RNBgreen, RNGblue)
    # hexRGB = (R * 65536) + (G * 265) + B
    return color

def drawBox(win, color):
    box1 = Point(450, 150)
    box2 = Point(500, 200)
    colorBox = Rectangle(box1,box2)
    colorBox.draw(win)
    # Set the color of fill using func above
    colorBox.setFill(color)

def boxLabel(win, color):
    # Hexadecimal value for any color passed through func
    hexLab = Text(Point(475, 210), color)
    hexLab.setSize(11)
    hexLab.setTextColor("black")
    hexLab.draw(win)

    return hexLab # Returns text obj so it can be undrawn later

def triangleArea(p1, p2, p3):
    # Using the getX/getY funcs to find coordinates for point on graphwin
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    x3 = p3.getX()
    y3 = p3.getY()

    # Area of a triangle, cross product
    A = abs((0.5 * ((y1 * (x3 - x2)) + (y2 * (x1 - x3)) + (y3 * (x2 - x1)))))
    return A

def main():
    win = GraphWin("RGB Triangle Visualization", 600, 500) # Create window
    win.setBackground("white")
    writeText(win) # Draw write-up text for problem (long problem)

    # Creating 3 congruent triangles which create one equilateral triangle
    R = Point(150,100)
    B = Point(150,350)
    # Given two points of an equilateral triangle, the third point is
    # (sqrt(3)/2 * side length) away from the midpoint of those two points
    G = Point(150 + (125 * math.sqrt(3)), 225)
    centroid = getCentroid(R, G, B) # Use getCentroid to find third point for triangles

    # Calling the drawUI function; also draw the centroid's circle obj, for
    # use in mouseClickPoint function
    drawUI(win, centroid, R, G, B)
    # Find and draw starting manipulative point using centroid
    startCircle = Circle(centroid, 5)
    startCircle.setFill("black")
    startCircle.draw(win)

    # Find new "centroid" for triangles, redraw UI within exit loop below
    # If user clicks exit circle, the program ends
    exitCircle = drawExit(win) # Call function to var to draw exit circle

    # Empty string text so that future text can be undrawn without throwing error
    hexVal = boxLabel(win, "")

    while True:
        newPoint = pointChoice(win, exitCircle)
        startCircle.undraw()
        hexVal.undraw()
        if newPoint == True: # If the user clicked the exit button
            win.close()
            break # Break statement to avoid passing a boolean through func call

        # Areas of each smaller triangle and the big, outer triangle
        areaBNG = triangleArea(B, newPoint, G)
        areaRNB = triangleArea(R, newPoint, B)
        areaRNG = triangleArea(R, newPoint, G)
        triArea = triangleArea(R, B, G)
        # If the user clicked out of the triangle, the three small triangles
        # formed would have greater area than the main (RGB) triangle
        if (areaBNG + areaRNB + areaRNG) <= triArea: # If click is in triangle
            boxColor = colorOutput(win, areaBNG, areaRNB, areaRNG, triArea)
            drawBox(win, boxColor)
            hexVal = boxLabel(win, boxColor)
            drawUI(win, newPoint, R, G, B)
            # Draw the point to be dragged again
            startCircle = Circle(newPoint, 5)
            startCircle.setFill("black")
            startCircle.draw(win)

main()
