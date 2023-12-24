import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4,480)


detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


face_id = input("Enter a Numeric user ID here: ")


print("Taking samples, look at camera ....... ")
count = 0

while True:

    ret, img = cam.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1



        cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h,x:x+w])


        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >=10:
        break

print("Samples taken now closing the program....")
cam.release()
cv2.destroyAllWindows()