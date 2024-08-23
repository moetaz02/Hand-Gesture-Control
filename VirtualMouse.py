import cv2
import numpy
import numpy as np

import HandTrackingModule as htm
import time
import autopy
pTime=0
cTime=0
wCam ,hCam = 648 ,480
wScr,hScr = autopy.screen.size()
framR=80
smoothening=2.1
plocX,plocY=0,0
clocX,clocY=0,0

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
detctor=htm.handDetector(maxHands=1)

while True :
    ret , img =cap.read()
    ing=detctor.findHands(img)
    cv2.rectangle(img, (framR, framR), (wCam - framR, hCam - framR), (255, 0, 255), 2)
    lmlist ,bbox = detctor.findPosition(img,draw=False)
    if len (lmlist) !=0 :
        x1,y1 =lmlist[8][1:]
        x2,y2 = lmlist[12][1:]
        fingers= detctor.fingersUp()
        #print(fingers)
        if fingers[1]==1 and fingers[2]==0 :

            x3= np.interp(x1,(framR,wCam-framR),(0,wScr))
            y3 = np.interp(y1, (framR, hCam-framR), (0, hScr))
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            autopy.mouse.move(wScr - clocX, clocY)
            plocX, plocY = clocX, clocY
        if fingers[1] == 1 and fingers[2] == 1:
            length,img,lineinfo=detctor.findDistance(8,12,img,draw=False)
            #print(length)
            if length <20 :
                autopy.mouse.click()


    cv2.imshow('image',img)

    if cv2.waitKey(1)==ord('q') :
        break

cap.release()
cv2.destroyAllWindows()