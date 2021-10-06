import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)

#for yellow: [[0,109,154], [60,255,255]]
#for red: [[0,126,135], [15,229,255]]

def empty(a):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640,240)
cv2.createTrackbar("Hue Min", "Trackbars", 0,179,empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179,179,empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0,255,empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255,255,empty)
cv2.createTrackbar("Val Min", "Trackbars", 0,255,empty)
cv2.createTrackbar("Val Max", "Trackbars", 255,255,empty)

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array((h_min, s_min, v_min))
    upper = np.array((h_max, s_max, v_max))
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hstack = np.hstack([img, mask, imgResult])
    cv2.imshow("Result", imgResult)
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

