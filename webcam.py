import cv2

cap = cv2.VideoCapture(0)   #captures from webcam 0

while True:
    success, img = cap.read()  #save image frame ----- success is boolean value
    cv2.imshow("Video", img)   #show every frame
    if cv2.waitKey(1) & 0xFF==ord('q'):  #close if q is pressed
        break


