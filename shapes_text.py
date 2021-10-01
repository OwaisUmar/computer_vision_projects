import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img[:]=[25,100,255]     #color
#cv2.imshow("Image", img)

Line = cv2.line(img, (0,0), (512,512), (0,0,0), 50)
Line = cv2.line(Line, (512,0), (256,256), (0,0,0), 50)
Rect = cv2.rectangle()


cv2.imshow("Line", Line)


cv2.waitKey(0)
