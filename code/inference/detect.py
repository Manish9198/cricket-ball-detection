# detect.py
from ultralytics import YOLO
import numpy as np

class BallDetector:
    def __init__(self, model_path, conf):
        self.model = YOLO(model_path)
        self.conf = conf

    def detect(self, frame):
        results = self.model(frame, conf=self.conf, verbose=False)
        boxes = results[0].boxes
        if boxes is None or len(boxes) == 0:
            return None

        box = boxes.xyxy[0].cpu().numpy()
        x1,y1,x2,y2 = box
        cx = (x1+x2)/2
        cy = (y1+y2)/2
        return np.array([cx, cy])
