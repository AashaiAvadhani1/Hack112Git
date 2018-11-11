import cvProcess as parse
import connectPoints as order
import createURL as map
import webLaunch as web
import cv2 as cv

def mapGraph(imPath,ptsToScaleDownTo,imType="pic",geoScale=.2, minVal = 100, maxVal =200,startcoords=(40.434921, -79.99501)):
        # Uses edge-detection and opencv to process pictures into the list of tuples
        # describing their shape with individual pixels.
        # points = parse.processPNG("assets/heart.png",13) # scale = .1 Generates roadmap as well
        # points = parse.generatePointsForPic("assets/hack112.png",ptsToScaleDownTo,minVal,maxVal)
    if imType == "pix":
        # points = parse.processPNG(imPath, ptsToScaleDownTo)
        try:
            points = parse.processPNG(imPath,ptsToScaleDownTo)
        except:
            points = parse.processJPG(imPath,ptsToScaleDownTo)
    else:
        points = parse.generatePointsForPic(imPath,ptsToScaleDownTo,minVal,maxVal)

        # Arrange points by finding each point's nearest neighbor and adding it to
        # a new list (default ordering is by row, but shapes can be arcs and cross
        # rows sometimes.
    orderedPoints = order.connectPoints(points)

    img = cv.imread(imPath)
    ratio = ptsToScaleDownTo/len(img)
    width = len(img)*ratio
    height = len(img[0])*ratio


    # cv.imshow("inputPic", height)
        # convertCanvasPoints(lst, scale, height, width, city)
        # Turns the pixel mappings into actual longitude and latitude coordinates.
    coordinates = map.convertCanvasPoints(orderedPoints,geoScale,height,width,startcoords)

    print(len(coordinates)) # ~358 point graphing limit. Any more and the map won't load

        # Then we turn the longitude and latitude tuples into a Google Maps/Earth URL
        # that can be launched to show the picture on the earth/on any city you want.
    url = map.makeURL(coordinates)

    # Launch the final URL we got from our program
    web.goTo(url)




# def mapGraph(imPath,scaleDownTo,(minVal=100,maxVal=200), geoScale):
# mapGraph("assets/heart.png",13,imType="pix",geoScale=.1)
# mapGraph("assets/kriface.jpg",50)
mapGraph("assets/face.jpg",53,geoScale=.1,minVal=230,maxVal=250)
# mapGraph("assets/farnum.png",38,geoScale=.1,minVal=100,maxVal=200)
# mapGraph("assets/face.jpg",53,geoScale=.1,minVal=230,maxVal=250)

# mapGraph("assets/dog.jpg", 30, geoScale=.1)













