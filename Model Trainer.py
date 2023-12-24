import cv2
import numpy as np
from PIL import Image
import os

path = 'samples'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



def Images_And_Labels(path):

    imagepaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples=[]
    ids = []

    for imagepath in imagepaths:

        gray_img = Image.open(imagepath).convert('L')
        img_arr = np.array(gray_img,'uint8')

        id = int(os.path.split(imagepath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print ("Training faces. It will take a few seconds. Wait ...")

faces,ids = Images_And_Labels(path)
recognizer.train(faces, np.array(ids))

recognizer.write('trainer/trainer.yml')

print("Model trained, Now we can recognize your face.")
