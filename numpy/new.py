import cv2
import numpy as np

print("START")

img = cv2.imread("res/off.jpg",1)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img1", img)
cv2.imshow("img2", imgGrey)

print("END")
cv2.waitKey(0)