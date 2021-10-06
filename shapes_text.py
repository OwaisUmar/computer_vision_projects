import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img[:]=[25,100,255]     #color
#cv2.imshow("Image", img)

cv2.rectangle(img, (128,128), (384,384), (255,255,255), 50)
cv2.circle(img, (255,255), 245, (255,255,255), 20)
cv2.line(img, (0,0), (512,512), (0,0,0), 50)
cv2.line(img, (512,0), (0,512), (0,0,0), 50)
cv2.putText(img, "OPEN CV", (182,72), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,255,255), 2)


cv2.imshow("Rectangle", img)



cv2.waitKey(0)
