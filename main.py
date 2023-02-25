import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface.xml")
path = 'venv/images'
#create a list for all the images that we will import
images = []
mylist=os.listdir(path)


for cl in mylist:
    currentimg=cv2.imread(f'{path}/{cl}')
    images.append(currentimg)

    for img in images:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray)

        for face in faces:
            x, y, w, h = face
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))
            img[y: y + h, x: x + w] = cv2.GaussianBlur(img[y: y + h, x: x + w], (29, 29), 0)

        cv2.imshow("Blur_Image", img)
        cv2.waitKey(2000)

