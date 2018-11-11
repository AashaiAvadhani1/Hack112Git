# Basic Animation Framework
# import connectingTheDots as ctd

import tkinter
import math
import random
import sys
from tkinter import *

#from image_util import *
import copy
####################################
# customize these functions
####################################


def init(data):
    # load data.xyz as appropriate
#    data.icon = PhotoImage("globe.gif")
#    data.iconCenters = []
#    data.iconWidth = data.icon.width()
#    data.iconHeight = data.icon.height()
    pass

def mousePressed(event, data):
    # use event.x and event.y
    pass

#returns as a string
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    # ctd.mapGraph(inputValue, 13, imType="pix", geoScale=.1)



def entryBox():
    root=Tk()
    def retrieve_input():
        inputValue=textBox.get("1.0","end-1c")
        print(inputValue)
    textBox=Text(root, height=10, width=50)
    textBox.pack()
    buttonCommit=Button(root, height=1, width=10, text="Enter",

                        command=lambda: retrieve_input())
    #command=lambda: retrieve_input() >>> just means do this when i press the button
    buttonCommit.pack()

    mainloop()

def getText():
    pass
def keyPressed(event, data):
    if(event.keysym == "T" or event.keysym == "t"):
        entryBox()
        runProgram()

    pass



def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)
#draw stuff

def drawText(canvas,data):
    #WorldArt

    #create the W
    canvas.create_text(145, data.height//2-100, text = "W", font = "Helvetica 100 bold", fill = "darkBlue")
    #create the O
    canvas.create_text(235, data.height//2-100, text = "O", font = "Helvetica 100 bold", fill = "darkRed")

    #create the R
    canvas.create_text(315, data.height//2-100, text = "R", font = "Helvetica 100 bold", fill = "darkGreen")

    #create the L
    yellow = rgbString(244, 194, 13)
    canvas.create_text(390, data.height//2-100, text = "L", font = "Helvetica 100 bold", fill = yellow)

    #create the D
    teal = rgbString(85, 156, 231)
    canvas.create_text(460, data.height//2-100, text = "D", font = "Helvetica 100 bold", fill = teal)


    #create the A
    canvas.create_text(230, data.height//2, text = "A", font = "ComicSansMS 100 bold", fill = "black")

    #create the R
    canvas.create_text(310, data.height//2, text = "R", font = "ComicSansMS 100 bold", fill = "black")

    #create the T
    canvas.create_text(385, data.height//2, text = "T", font = "ComicSansMS 100 bold", fill = "black")

    ##############THING#############
    canvas.create_text(data.width//2+10,data.height//2+125, text = "Press T to input your file name!",
                                                        font = "Arial 20 bold")
def redrawAll(canvas, data):
    drawText(canvas,data)
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)




mapGraph("assets/heart.png",13,imType="pix",geoScale=.1)