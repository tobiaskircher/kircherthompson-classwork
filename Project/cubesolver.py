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
    print("Dimensions: ", dimensions)
    print("Height: ", height)
    print("Width: ", width)
    
while True:
    ret, frame = capture.read()

    cv.rectangle(frame,(0,0),(100,100), WHITE,1)
    
    cv.imshow("Cube Solver", frame)

    if cv.waitKey(1) == 27:
        break

capture.release()
cv.destroyAllWindows()

