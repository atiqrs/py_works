import cv2

print("Hello")

img = cv2.imread("../res/pic.png")

cv2.imshow("Viewer",img)
cv2.waitKey(0)