import cv2
from random import randrange

#importing trained data for matching
trained_face_data = cv2.CascadeClassifier('face.xml')

#This image can also be used
# img = cv2.imread('p.jpg')

#using webcam as source
webcam = cv2.VideoCapture(0)

while True:
    s_F_R, frame = webcam.read()
    
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cordinates = trained_face_data.detectMultiScale(frame)

    for(x, y, w, h) in cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(255), randrange(254)), 3)

    cv2.imshow('Face Detector', frame)

    key = cv2.waitKey(1)

    if key == 81 or key == 131:
        break;

