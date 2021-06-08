from __future__ import print_function
import argparse
import cv2

# Load
imgon = cv2.imread("res/on.jpg")

# Console Print
print("width: {} pixels".format(imgon.shape[1]))
print("height: {} pixels".format(imgon.shape[0]))
print("channels: {}".format(imgon.shape[2]))

# Display
cv2.imshow("Viewer 1",imgon)
cv2.waitKey(0)

# Save
cv2.imwrite("D:/image.jpg",imgon)