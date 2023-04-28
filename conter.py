import os
import numpy as np
import cv2 as cv
from showClassInModel import showDatainFile
from tracker import *
import pandas as pd


    
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
        self.tracker=Tracker()
        
        self.font=cv.FONT_HERSHEY_COMPLEX
        
        self.people_entering = {}
        self.entering=set()
        
        self.people_exiting = {}
        self.exiting = set()

    def drawTowPolylines(self,frame):
        cv.polylines(frame,[np.array(area1,np.int32)],True,(255,0,0),2)
        cv.putText(frame,str('1'),(504,471),self.font,(1),(0,0,0),2)

        cv.polylines(frame,[np.array(area2,np.int32)],True,(255,0,0),2)
        cv.putText(frame,str('2'),(466,485),self.font,(1),(0,0,0),2)
        
        i = len(self.entering)
        o = len(self.exiting)
        cv.putText(frame,'Number of entering people= '+str(i),(20,44),self.font,(1),(0,255,0),2)
        cv.putText(frame,'Number of exiting people= '+str(o),(20,82),self.font,(1),(0,0,255),2)
    
    def peopleEntering(self,frame,x3,y3,x4,y4,id,c):
        results = cv.pointPolygonTest(np.array(area2,np.int32) ,((x4,y4)) , False )
        if results >=0:
            self.people_entering[id] = (x4,y4)
            cv.rectangle(frame,(x3,y3),(x4,y4),(0,0,255),2)
            
        if id in self.people_entering:
            results1 = cv.pointPolygonTest(np.array(area1,np.int32) ,((x4,y4)) , False )
            if results1 >=0:
                cv.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),2)
                cv.circle(frame , (x4,y4) , 4 , (255,0,255),-1)
                cv.putText(frame,str(c),(x3,y3-10),self.font,(0.5),(255,255,255),1)
                cv.putText(frame,str(id),(x3+65,y3-10),self.font,(0.5),(255,0,255),1)
                self.entering.add(id)
    
    def peopleExiting(self,frame,x3,y3,x4,y4,id,c):
        results2 = cv.pointPolygonTest(np.array(area1,np.int32) ,((x4,y4)) , False )
        if results2 >=0:
            self.people_exiting[id] = (x4,y4)
            cv.rectangle(frame,(x3,y3),(x4,y4),(0,255,0),2)
        if id in self.people_exiting:
            results3 = cv.pointPolygonTest(np.array(area2,np.int32) ,((x4,y4)) , False )
            if results3 >=0:
                cv.rectangle(frame,(x3,y3),(x4,y4),(0,0,255),2)
                cv.circle(frame , (x4,y4) , 4 , (255,0,255),-1)
                cv.putText(frame,str(c),(x3,y3-10),self.font,(0.5),(255,255,255),1)
                cv.putText(frame,str(id),(x3+55,y3-10),self.font,(0.5),(255,0,255),1)
                self.exiting.add(id)
                
    def predictModel(self,frame):
        results=self.model.predict(frame)
        #print('results',results[0])
        a=results[0].boxes.data
        #print("a",a)
        px=pd.DataFrame(a).astype("float")
        #print(px)
        list=[]
                
        for index,row in px.iterrows():
            #print(row)
    
            x1=int(row[0])
            y1=int(row[1])
            x2=int(row[2])
            y2=int(row[3])
            d=int(row[5])
            c=self.classList[d]
            
            if 'person' in c:
                list.append([x1,y1,x2,y2])  
            
        bbox_id = self.tracker.update(list)
        
        for bbox in bbox_id:
            x3,y3,x4,y4,id = bbox    
            self.peopleEntering(frame,x3,y3,x4,y4,id,c)
            self.peopleExiting(frame,x3,y3,x4,y4,id,c)
            
    def readVideo(self):
        # cv.namedWindow('RGB')
        # cv.setMouseCallback('RGB',RGB)
        
        # print(self.classList)
        
        cap=cv.VideoCapture(self.video)
        while cap.isOpened():
            rat,frame=cap.read()
            if rat==False:
                break
            
            frame=cv.resize(frame,(1020,500))
            
            self.predictModel(frame)
            self.drawTowPolylines(frame)
            
            cv.imshow("RGB",frame)
            if cv.waitKey(1) & 0xFF ==ord("q"):
                break
        cap.release()
        cv.destroyAllWindows()
    
    def __call__(self):
        self.readVideo()