import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# cascades: https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
glasses_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_mcs_mouth.xml')
#smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')
nose_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_mcs_nose.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

     # ย่อขนาดเฟรมเหลือ 1/4 ทำให้ face recognition ทำงานได้เร็วขึ้น

    # แปลงสีภาพจาก BGR (ถูกใช้ใน OpenCV) เป็นสีแบบ RGB (ถูกใช้ใน face_recognition)
    gray = img[:, :, ::-1]
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
            
        nose = nose_cascade.detectMultiScale(roi_gray)
        for(nx, ny, nw, nh) in nose:
            cv2.rectangle(roi_color, (nx,ny), (nx+nw,ny+nh), (255,0,255), 2)
        
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
        for(sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx,sy), (sx+sw,sy+sh), (0,0,255), 2)

    cv2.imshow('img', img)
    
    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
