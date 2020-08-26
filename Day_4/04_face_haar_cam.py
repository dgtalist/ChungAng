import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2,
    minNeighbors=5, minSize=(20, 20))
    for (x, y, w, h) in faces :
        cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
        roi_gray=gray[y:y+h, x:x+w]

    cv2.imshow('video', img)
    k=cv2.waitKey(30)&0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllwindows()
