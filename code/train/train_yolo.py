# train_yolo.py
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="ball.yaml",   # YOLO formatted dataset
    epochs=50,
    imgsz=640,
    batch=16,
    name="cricket_ball"
)
