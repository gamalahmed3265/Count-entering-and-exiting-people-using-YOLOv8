
from conter import *
from showClassInModel import showClass
from ultralytics import YOLO

def main():
    video="../peoplecount1.mp4"
    model="../yolov8s.pt"
    
    model=YOLO(model)
    # showClass(model.names)
    
    conter=Conter(video,model)
    conter()

if __name__ == "__main__":
    main()