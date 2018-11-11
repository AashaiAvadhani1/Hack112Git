import cv2 as cv
from PIL import Image
import numpy as np

################################################ Usable functions

def flip(listTups):
    newTups = []
    for tup in listTups:
        newTups.append((tup[1],tup[0]))
    return newTups

#For pictures without a well-defined black border
def generatePointsForPic(imPath,desSize,minThresh,maxThresh):
    img = cv.imread(imPath, 0)
    ratio = desSize / len(img)
    img = cv.resize(img, None, fx=ratio, fy=ratio)
    thing = cv.Canny(img, minThresh, maxThresh)
    # cv.imshow("thing"+str(minThresh)+str(maxThresh),thing)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    listPoints = []
    for i in range(len(thing)):
        for j in range(len(thing[0])):
            if thing[i][j] != 0:
                listPoints.append((i, j))
    return listPoints


#For pixel art and toons that have a clear black border, use processJPG and processPNG
def processJPG(imPath, wantWid = 20):
    img = Image.open(imPath)
    width = img.width
    height = img.height

    small = img.resize((wantWid, height // (width // wantWid)))
    bg = Image.new("RGB", small.size)
    for i in range(bg.width):
        for j in range(bg.height):
            if sum(bg.getpixel((i, j))) > 100:
                bg.putpixel((i, j), (255, 255, 255))
    # bg.show()
    listPoints = []
    for i in range(bg.width):
        for j in range(bg.height):
            if bg.getpixel((i,j)) != (255,255,255):
                listPoints.append((i, j))
    return listPoints

def processPNG(imPath,wantWid=20):
    img = Image.open(imPath)
    width = img.width
    height = img.height

    # print(wantWid)
    # print(height)
    # print(width)
    small = img.resize((wantWid, height // (width // wantWid)))
    bg = Image.new("RGB", small.size)
    for i in range(bg.width):
        for j in range(bg.height):
            replPix = small.getpixel((i, j))
            if replPix[-1] == 0:
                bg.putpixel((i, j), (255, 255, 255))
            else:
                bg.putpixel((i, j), small.getpixel((i, j))[:-1])

    for i in range(bg.width):
        for j in range(bg.height):
            if sum(bg.getpixel((i, j))) > 100:
                bg.putpixel((i, j), (255, 255, 255))
    # bg.show()
    listPoints = []
    for i in range(bg.width):
        for j in range(bg.height):
            if bg.getpixel((i,j)) != (255,255,255):
                listPoints.append((i, j))
    return flip(listPoints)


############################################### Test functions

wantedSize = 400
wantedMin = 100
wantedMax = 200
# generatePointsForPic("112.jpg",wantedSize,wantedMin,wantedMax)
# generatePointsForPic("assets/notme.jpg",wantedSize,wantedMin,wantedMax)

# print(processPNG("assets/heart.png"))

# for i in range(0,250,40):
#     for j in range(0,250,40):
#         generatePointsForPic("assets/face.jpg",50,i,j)

# for i in range(235,260,5):
#     for j in range(235,260,5):
#         generatePointsForPic("assets/face.jpg",50,i,j)