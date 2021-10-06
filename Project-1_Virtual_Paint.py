import cv2
import numpy as np

cap = cv2.VideoCapture(0)

my_colors = [[0, 109, 154, 60, 255, 255], [0, 126, 135, 15, 229, 255]]
my_color_values = [[0, 255, 255], [0, 0, 255]]
myPoints = []  # [x,y,ColorId]


def getContours(maskimg):
    contours, hierarchy = cv2.findContours(maskimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -100, -100, -100, -100
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(img, cnt, -1, (255, 255, 100), thickness=3)
            peri = cv2.arcLength(cnt, True)
            corners = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            sides = len(corners)
            x, y, w, h = cv2.boundingRect(corners)
    return x + w // 2, y


def getColors():
    count = 0
    newPoints = []
    for i in my_colors:
        lower = np.array((i[:3]))
        upper = np.array((i[3:]))
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(img, (x, y), 20, my_color_values[count], cv2.FILLED)
        if x!=-100:
            newPoints.append((x,y,count))
        count += 1
    return newPoints


def drawOnCanvas(newPoints):
    for points in newPoints:
        cv2.circle(img, (points[0], points[1]), 7, my_color_values[points[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = getColors()
    if len(newPoints):
        for npts in newPoints:
            myPoints.append(npts)
    if len(myPoints):
        drawOnCanvas(myPoints)



    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
