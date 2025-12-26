# main.py
import cv2
import numpy as np
from utils.kalman import BallKalman
from inference.detect import BallDetector
from inference.track import write_csv
from inference.render import render
from utils.config import *

cap = cv2.VideoCapture(VIDEO_PATH)
detector = BallDetector(MODEL_PATH, CONF_THRESH)
kf = BallKalman()

rows = []
frame_idx = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    det = detector.detect(frame)

    if det is None:
        rows.append([frame_idx, -1, -1, 0])
    else:
        pred = kf.update(det)
        rows.append([frame_idx, pred[0], pred[1], 1])

    frame_idx += 1

cap.release()

write_csv(CSV_OUTPUT, rows)
render(VIDEO_PATH, VIDEO_OUTPUT, rows)
