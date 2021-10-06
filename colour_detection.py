import cv2
import numpy as np

def empty(a):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640,240)
cv2.createTrackbar("Hue Min", "Trackbars", 0,179,empty)
cv2.createTrackbar("Hue Max", "Trackbars", 174,179,empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0,255,empty)
cv2.createTrackbar("Sat Max", "Trackbars", 123,255,empty)
cv2.createTrackbar("Val Min", "Trackbars", 0,255,empty)
cv2.createTrackbar("Val Max", "Trackbars", 255,255,empty)

while True:
    img = cv2.imread("resources/car.jpg")
    img = cv2.resize(img, (480, 300))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    mask = cv2.bitwise_not(mask)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    h1 = np.hstack((img, imgHSV))
    h2 = np.hstack((img, imgResult))
    imgResult = np.vstack((h1, h2))

    #cv2.imshow("car", img)
    #cv2.imshow("HSV", imgHSV)
    #cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)

