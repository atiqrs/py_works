import cv2
import numpy as np

karnel = np.ones((20,20),np.uint8)

img = cv2.imread("res/off.png",1)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(11,11),0)
imgEdge = cv2.Canny(imgBlur, 20,50)
imgDialation = cv2.dilate(imgEdge,karnel,iterations=1)

imagem = cv2.bitwise_not(imgDialation)

cv2.imshow("img main", img)
cv2.imshow("img Gray", imgGrey)
cv2.imshow("img GaussianBlur", imgBlur)
cv2.imshow("img Canny", imgEdge)
cv2.imshow("img Canny", imgDialation)
cv2.imshow("img Revert", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()