import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(3) and 0xFF == ord('q'):
        break
    # if cv2.waitKey(2) and 0xFF == ord('s'):
    #     img.save('c:/Users/user/Downloads/myphoto.jpg', 'JPEG')