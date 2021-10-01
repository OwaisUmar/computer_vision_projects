import cv2
import numpy as np

img = cv2.imread("resources/optimus.jpg")
img = cv2.resize(img, (500,375))
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)  #thickens the line
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)  #thins the line

cv2.imshow("Optimus Prime", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dilated", imgDilation)
cv2.imshow("Eroded", imgEroded)
cv2.waitKey(0)
