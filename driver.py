import numpy as np
import cv2

apple_cascade = cv2.CascadeClassifier("/home/csimmons155/Documents/CustomHaar2/data/mcdonalds_cascade.xml")

#face_cascade = cv2.CascadeClassifier('/home/csimmons155/OpenCV/opencv-2.4.13/data/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    apple_logo = apple_cascade.detectMultiScale(gray, 3, 3)


    for (x,y,w,h) in apple_logo:

        print "Rectangle: ", (x,y,w,h)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)



    cv2.imshow("img", img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()