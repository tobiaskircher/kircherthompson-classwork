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
    print(rgb)

    
while True:
    ret, frame = capture.read()

    drawGrid(frame)
    
    cv.imshow("Cube Solver", frame)

    if cv.waitKey(1) == 27:
        break

capture.release()
cv.destroyAllWindows()

