import cv2 as cv

capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Unable To Open Webcam.")

while True:
    ret, frame = capture.read()
    
    cv.imshow("Cube Solver", frame)

    if cv.waitKey(1) == 27:
        break

capture.release()
cv.destroyAllWindows()

