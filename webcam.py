import cv2

cap = cv2.VideoCapture(0)   #captures from webcam 0
cap.set(3, 640)
cap.set(4, 480)
cap.set(10,10000)

while True:
    success, img = cap.read()  #save image frame ----- success is boolean value
    cv2.imshow("Video", img)
    cv2.waitKey(0)

