# Andrew ID: vvortega
# Name: Victoria Ortega



################################################ Usable functions
def convertCanvasPoints(lst, scale, height, width, city):
    coordinates = []
    for canvasPoint in lst:
        x = city[0] - ((canvasPoint[0] - width//2)*scale)
        y = city[1] + ((canvasPoint[1] - height//2)*scale)
        coordinates.append((round(x,6),round(y,6)))
    return coordinates

def makeURL(lst): #takes in result of convertCanvasPoints
    basic = "https://www.google.com/maps/dir/"
    for coord in lst:
        basic = basic + str(coord[0]) + "," + str(coord[1]) +"/"
    basic = basic[0:-1]
    return basic #+ str(lst[0][0])+","+str(lst[0][1])+"/"

# print(makeURL(convertCanvasPoints(list,.01,100,100,(40.4428,-79.9430))))