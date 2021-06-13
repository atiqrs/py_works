import cv2

print("START")
frameWidth = 40
frameHeight = 80
vid = cv2.VideoCapture("res/apps.mp4")
while True:
    succes, img = vid.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("If breked!")
        break
print("END")