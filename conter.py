import os
import numpy as np
import cv2 as cv
from showClassInModel import showDatainFile
from tracker import *



    
area1=[(312,388),(289,390),(474,469),(497,462)]

area2=[(279,392),(250,397),(423,477),(454,469)]


def RGB(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
class Conter:
    def __init__(self,video,model):
        self.video=video
        self.model=model
        self.classList=showDatainFile()

            

    def readVideo(self):
        cv.namedWindow('RGB')
        cv.setMouseCallback('RGB',RGB)
        
        print(self.classList)
        cap=cv.VideoCapture(self.video)
        while cap.isOpened():
            rat,frame=cap.read()
            if rat==False:
                break
            
            frame=cv.resize(frame,(1020,500))
            
            
            cv.imshow("RGB",frame)
            if cv.waitKey(1) & 0xFF ==ord("q"):
                break
        cap.release()
        cv.destroyAllWindows()
    
    def __call__(self):
        self.readVideo()