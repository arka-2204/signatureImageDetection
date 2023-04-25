import cv2
import numpy
from main import *
import os



# image = cv2.imread("souro.jpeg")

def generate(file_path):
    file =cv2.imread(f"{file_path}")
    bigger = cv2.resize(file, dsize=(128,128)) #dynamic resize
    gray =cv2.cvtColor(bigger, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    


    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    face_len=len(faces)
    if face_len ==0:
        print("No faces",file_path)
        return False
    else:
        for (x, y, w, h) in faces:
            
            cv2.rectangle(bigger, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print("its a face")
        return True

    # detection(gray)

    cv2.imshow('frame', bigger)
    # # cv2.waitKey(0)


path ="images/"
for file in os.listdir(path):
    file_path = path + str(file)

    if generate(file_path)== True:
        print("Face detected")
    else:
        print("signature")





