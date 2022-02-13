import cv2
import numpy as np

karnel = np.ones((2,2),np.uint8)
# karnel = np.ones((20,20),np.uint8)
cir_count = 0

img = cv2.imread("res/fon.jpg",1)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(11,11),0)
imgEdge = cv2.Canny(imgBlur, 20,50)
imgDialation = cv2.dilate(imgEdge,karnel,iterations=1)

imagem = cv2.bitwise_not(imgDialation)

# cv2.imshow("img main", img)
# cv2.imshow("img Gray", imgGrey)
# cv2.imshow("img GaussianBlur", imgBlur)
# cv2.imshow("img Canny", imgEdge)
# cv2.imshow("img Canny", imgDialation)
# cv2.imshow("img Revert", imagem)

_, thrash = cv2.threshold(imagem, 240, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("img", img)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    # if len(approx) == 3:
    #     cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    if len(approx) == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
          cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    # elif len(approx) == 5:
    #     cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    # elif len(approx) == 10:
    #     cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cir_count += 1
        print(cir_count)
        str = "No ", cir_count, " Circle"
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


# cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()