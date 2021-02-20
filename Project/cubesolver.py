import cv2 as cv

WHITE = (255,255,255)
capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Unable To Open Webcam.")
    exit()

else:
    ret, frame = capture.read()
    dimensions = frame.shape
    width = dimensions[0]
    height = dimensions[1]
    centre = [width//2, height//2]

#Colour Ranges
#colour = [[r_min,r_max],[g_min,g_max],[b_min,b_max], "colour_name"]
blue = [[180,220],[145,175],[80,110],"blue"]
orange = [[85,115],[135,165],[205,235],"orange"]
green = [[130,160],[170,200],[105,135],"green"]
red = [[125,155],[100,130],[200,230],"red"]
white = [[160,205],[165,205],[160,200],"white"]
yellow = [[100,130],[175,205],[160,200],"yellow"]
colours = [blue, orange, green, red, white, yellow]

def getColour(rgb_value):
    return_value = "none"
    for colour in colours:
        if colour[0][0] <= rgb_value[0] <= colour[0][1]:
            if colour[1][0] <= rgb_value[1] <= colour[1][1]:
                if colour[2][0] <= rgb_value[2] <= colour[2][1]:
                    return_value = colour[3]
                    break
    return return_value


def drawGrid(frame):
    rectWidth = 70
    halfRectWidth = rectWidth // 2
    gap = 15
    
    rows = [centre[0] - halfRectWidth - gap - rectWidth,
         centre[0] - halfRectWidth,
         centre[0] + halfRectWidth + gap]

    columns = [centre[1] - halfRectWidth - gap - rectWidth,
         centre[1] - halfRectWidth,
         centre[1] + halfRectWidth + gap]

    for x in columns:
        for y in rows:
            cv.rectangle(frame,(x,y),(x+rectWidth,y+rectWidth), WHITE,1)

            #region = frame[x:x+rectWidth, y:y+rectWidth]
            #mean = cv.mean(region)
            #print(mean)

    region = frame[centre[0]:centre[0]+rectWidth, centre[1]:centre[1]+rectWidth]
    mean = cv.mean(region)
    rgb = [int(mean[0]),int(mean[1]),int(mean[2])]
    #print(rgb)
    print(getColour(rgb))

    
while True:
    ret, frame = capture.read()

    frame = cv.flip(frame,1)

    drawGrid(frame)
    
    cv.imshow("Cube Solver", frame)

    if cv.waitKey(1) == 27:
        break

capture.release()
cv.destroyAllWindows()

