import cv2
import numpy as np

img = cv2.imread("resources/igi.jpg")
img2 = cv2.imread("resources/cards.jpg")

img = cv2.resize(img, (200,200))
img2 = cv2.resize(img2, (300,200))

horizontal = np.hstack((img,img,img2))
vertical = np.vstack((horizontal,horizontal,horizontal))

cv2.imshow("I.G.I.", img)
cv2.imshow("Horizontal", horizontal)
cv2.imshow("Vertical", vertical)

cv2.waitKey(0)