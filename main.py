import cv2

print("START")

imgon = cv2.imread("res/on.jpg")
imgoff = cv2.imread("res/off.jpg")

print("width: {} pixels".format(imgon.shape[1]))
print("height: {} pixels".format(imgon.shape[0]))
print("channels: {}".format(imgon.shape[2]))


cv2.imshow("Viewer 1",imgon)
cv2.imshow("Viewer 2",imgoff)

cv2.waitKey(0)

print("END")

# img = cv2.imread("res/pic.png")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # img_gray_mode = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#
# img_gray_mode = cv2.imread("res/pic.png", cv2.IMREAD_GRAYSCALE)
#
# cv2.imshow("Viewer 1",img)
# cv2.imshow("Viewer 2",img_gray)
# cv2.imshow("Viewer 3",img_gray_mode)