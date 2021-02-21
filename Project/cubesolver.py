import cv2 as cv

font = cv.FONT_HERSHEY_SIMPLEX
PUREBLACK = (0,0,0)
PUREWHITE = (255,255,255)
capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Unable To Open Webcam.")
    exit()

else:
    ret, frame = capture.read()
    dimensions = frame.shape
    height = dimensions[0]
    width = dimensions[1]
    centre = [width//2, height//2]

#Colour Ranges
#colour = [[r_min,r_max],[g_min,g_max],[b_min,b_max], "colour_name"]
blue = [[150,220],[145,185],[65,110],"blue"]
orange = [[0,115],[90,165],[205,255],"orange"]
green = [[75,149],[170,200],[85,135],"green"]
red = [[30,155],[45,130],[195,255],"red"]
white = [[125,220],[145,220],[145,220],"white"]
yellow = [[30,130],[170,215],[160,200],"yellow"]
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
    rectWidth = 50
    halfRectWidth = rectWidth // 2
    gap = 30
    
    rows = [centre[1] - halfRectWidth - gap - rectWidth,
         centre[1] - halfRectWidth,
         centre[1] + halfRectWidth + gap]

    columns = [centre[0] - halfRectWidth - gap - rectWidth,
         centre[0] - halfRectWidth,
         centre[0] + halfRectWidth + gap]

    for x in columns:
        for y in rows:
            
            region = frame[y:y+rectWidth, x:x+rectWidth] 
            mean = cv.mean(region)
            rgb = [int(mean[0]),int(mean[1]),int(mean[2])]

            rectColour = PUREBLACK
            get_colour = getColour(rgb)
            
            if get_colour != "none":
                rectColour = rgb

            cv.rectangle(frame,(x,y),(x+rectWidth,y+rectWidth), rectColour,1)
            if x == columns[1]:
                cv.putText(frame,''.join(str(rgb)),(x,y), font, 0.5,PUREWHITE,cv.LINE_4)

    
while True:
    ret, frame = capture.read()

    frame = cv.flip(frame,1)
    
    drawGrid(frame)
    
    cv.imshow("Cube Solver", frame)

    if cv.waitKey(1) == 27:
        break

capture.release()
cv.destroyAllWindows()

