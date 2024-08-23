import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

pTime=0
cTime=0
wCam ,hCam = 648 ,480


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange()
#print(volRange)

minVol=volRange[0]
maxvol=volRange[1]
volBar=400
volPer=0
area=0
vol=0

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

detector =htm.handDetector(detectionCon=0.8)

while True :
    ret , img =cap.read()
    img=detector.findHands(img)
    lmlist,bbox = detector.findPosition(img,draw=False)
    if len(lmlist) !=0 :
        area =(bbox[2]-bbox[0])*(bbox[3]-bbox[1])/100
        #print(area)
        if 150<area<700 :
            #print(lmlist[4],lmlist[8])
            length ,img ,Lineinfo = detector.findDistance(4,8,img)
            #convet volume
            volBar = np.interp(length, [20, 230], [400, 150])
            volPer = np.interp(length, [20, 230], [0, 100])
            smoothness=5
            volPer= smoothness *round(volPer/smoothness)
            finguers=detector.fingersUp()
            #print(finguers)
            if not finguers[4]:
                volume.SetMasterVolumeLevelScalar(volPer/100,None)
                cv2.circle(img, (Lineinfo[4], Lineinfo[5]), 8, (0, 255, 0), cv2.FILLED)
                colorVol = (0, 255, 0)
            else:
                colorVol = (255, 0, 0)

    # if length < 40 :
           # cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

    #cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    #cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    #cv2.putText(img, f'{str(int(volPer))} %', (40, 80), cv2.FONT_ITALIC, 1,
               # (0, 0, 0), 3)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'FPS={ str(int(fps))}', (10, 50), cv2.FONT_ITALIC, 1,
                (0, 0, 0), 3)

    cv2.imshow('image',img)

    if cv2.waitKey(1)==ord('q') :
        break

cap.release()
cv2.destroyAllWindows()