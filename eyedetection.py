import numpy as np
import cv2


cap = cv2.VideoCapture(0)
gray=cv2.cvtColor(cap,cvtColor.RGB2GRAY)
while(True):
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
    cv2.imshow("Frame",frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

path = "haarcascade_eye.xml"

print("path: ", path)
eye_cascade = cv2.CascadeClassifier(path)

eyes = eye_cascade.detectMultiScale(cap, scaleFactor=1.02,minNeighbors=20,minSize=(10,10))
print(len(eyes))

for (x, y, w, h) in eyes:
	xc = (x + x+w)/2
	yc = (y + y+h)/2
	radius = w/2
	cv2.circle(cap, (int(xc),int(yc)), int(radius), (255,0,0), 2)
cv2.imshow("Eyes",cap)
cv2.waitKey(0)
cv2.destroyAllWindows()
