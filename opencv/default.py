import cv2

print("START")

imgon = cv2.imread("res/on.jpg")
imgoff = cv2.imread("res/off.jpg")
img = cv2.imread("res/pic.png")

print("width: {} pixels".format(imgon.shape[1]))
print("height: {} pixels".format(imgon.shape[0]))
print("channels: {}".format(imgon.shape[2]))
img2 = cv2.imread("res/pic2.png")

cv2.imshow("Viewer 1",img2)

img2 = cv2.imread("res/pic2.png",0)

# cv2.imshow("Viewer 1",imgon)
# cv2.imshow("Viewer 2",imgoff)
cv2.imshow("Viewer 2",img2)

cv2.waitKey(5000)

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


from __future__ import print_function
import argparse
import cv2

print("START")

ap = argparse.ArgumentParser()
ap.add_argument("-res", "/off.jpg", required = True,
help = "res/off.jpg")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,
g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r,
g, b))


corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)
image[0:100, 0:100] = (0, 255, 0)

cv2.imshow("Updated", image)
cv2.waitKey(5000)