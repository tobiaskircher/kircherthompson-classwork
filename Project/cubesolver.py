import cv2 as cv

WHITE = (255,255,255)
capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Unable To Open Webcam.")
    exit()

while True:
    ret, frame = capture.read()

    cv.rectangle(frame,(0,0),(100,100), WHITE,1)
    
    cv.imshow("Cube Solver", frame)

    if cv.waitKey(1) == 27:
        break

capture.release()
cv.destroyAllWindows()

