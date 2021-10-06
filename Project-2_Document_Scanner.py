import cv2
import numpy as np

img = cv2.imread("resources/doc2.jpg")
img = cv2.resize(img,(360,480))
width = img.shape[1]
height = img.shape[0]


def getContours(img):
    biggest = np.array([])
    maxarea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            #cv2.drawContours(imgContour, cnt, -1, (255,255,100), thickness=3)
            peri = cv2.arcLength(cnt, True)
            corners = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if len(corners)==4 and area>maxarea:
                biggest = corners
                maxarea = area
            sides = len(corners)
            x, y, w, h = cv2.boundingRect(corners)
    cv2.drawContours(imgContour, biggest, -1, (255, 255, 100), thickness=10)
    return biggest


def preProcessing(newimg):
    imgGray = cv2.cvtColor(newimg,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5,5), 1)
    imgCanny = cv2.Canny(imgBlur, 145,300)
    kernel = np.ones((5,5))
    imgDilate = cv2.dilate(imgCanny, kernel, iterations=2)
    imgErode = cv2.erode(imgDilate, kernel, iterations=1)
    return imgErode


def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2), np.int32)
    add = myPoints.sum(1)
    #print(myPoints)
    #print(add)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    print(myPointsNew)
    return  myPointsNew


def getWarp(img, biggest):
    #print(biggest.shape)
    biggest = reorder(biggest)
    print(biggest)
    cornerpts = np.float32(biggest)
    corner = np.float32([[0,0], [width, 0], [0,height], [width, height]])
    matrix = cv2.getPerspectiveTransform(cornerpts, corner)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    return imgOutput


imgContour = img.copy()
imgThres = preProcessing(img)
points = getContours(imgThres)
#print(biggest)
imgWarped = getWarp(imgContour, points)
imgWarped = cv2.resize(imgWarped, (360, 480))
cv2.imshow("Original", img)
cv2.imshow("Contours", imgContour)
cv2.imshow("Threshold", imgThres)
cv2.imshow("Warped", imgWarped)

cv2.waitKey(0)
