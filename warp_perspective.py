import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")

width, height = 500, 700
cornerpts = np.float32([[367, 137], [493, 163], [415, 325], [274, 294]])
corner = np.float32([[0,0], [width, 0], [width, height], [0,height]])
matrix = cv2.getPerspectiveTransform(cornerpts, corner)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("Image", img)
cv2.imshow("Warped Image", imgOutput)
cv2.waitKey(0)