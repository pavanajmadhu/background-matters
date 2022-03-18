import cv2
import numpy as np

cap=cv2.VideoCapture(0)
img=cv2.imread("bg.jpg")

while True:

    read,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    img=cv2.resize(img,(640,480))

    upper_b=np.array([104,153,70])
    lower_b=np.array([30,30,0])

    mask=cv2.inRange(frame,lower_b,upper_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    f=frame-res
    f=np.where(f==0,img,f)

    cv2.imshow("cap",frame)
    cv2.imshow("mask",f)

    if cv2.waitKey(1) & 0xff==ord("q") :
        break

cap.release()
cv2.destroyAllWindows()

