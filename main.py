
from conter import *
from ultralytics import YOLO

def main():
    video="../peoplecount1.mp4"
    model="../yolov8s.pt"
    
    model=YOLO(model)
    conter=Conter(video,model)
    conter()

if __name__ == "__main__":
    main()