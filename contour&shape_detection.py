import cv2
import numpy as np


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255,255,100), thickness=3)
            peri = cv2.arcLength(cnt, True)
            #print(peri)
            corners = cv2.approxPolyDP(cnt, 0.02*peri, True)
            sides = len(corners)
            x, y, w, h = cv2.boundingRect(corners)
            if sides == 4:
                if w == h:
                    cv2.putText(imgContour, "Square", ((x+w//4), y+h//2),cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0), thickness=1)
                else:
                    cv2.putText(imgContour, "Rectangle", ((x+w//8), (y+h//2)), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0), thickness=1)
            elif sides == 3:
                cv2.putText(imgContour, "Triangle", ((x+w//4), (y+h//2)), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0), thickness=1)
            else:
                cv2.putText(imgContour, "Circle", ((x+w//4), (y+h//2)), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0), thickness=1)


img = cv2.resize(cv2.imread("resources/shapes.png"), (650,650))
#img = cv2.imread("resources/shapes.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)

imgCanny = cv2.Canny(imgBlur, 100, 100)
getContours(imgCanny)
imgBlank = np.zeros_like(img)
imgCanny = cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR)

'''
h1 = np.hstack([img, imgGray, imgBlur])
h2 = np.hstack([imgCanny, imgContour, imgBlank])
imgStack = np.vstack([h1,h2])'''


cv2.imshow("Outline", imgContour)

cv2.waitKey(0)