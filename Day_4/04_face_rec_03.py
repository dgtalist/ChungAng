import cv2
import numpy as np
import face_recognition

imgSin = face_recognition.load_image_file('picture/sinmina3.jpg')
imgSin = cv2.cvtColor(imgSin, cv2.COLOR_BGR2RGB)
#imgTest = face_recognition.load_image_file('picture/sinmina3.jpg')
imgTest = face_recognition.load_image_file('picture/kim2.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceTarget = face_recognition.face_locations(imgSin)[0]
encodeSin = face_recognition.face_encodings(imgSin)[0]
cv2.rectangle(imgSin,(faceTarget[3],faceTarget[0]),(faceTarget[1],faceTarget[2]),(255,0,255),2)

faceTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceTest[3],faceTest[0]),(faceTest[1],faceTest[2]),(255,0,255),2)

comp = face_recognition.compare_faces([encodeSin], encodeTest)
per = face_recognition.face_distance([encodeSin], encodeTest)
print(comp, per)

cv2.imshow('sinmina', imgSin)
cv2.imshow('sinmina_test', imgTest)
cv2.waitKey(0)
