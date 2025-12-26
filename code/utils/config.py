# config.py
import os

VIDEO_PATH = "input/15.mov"
MODEL_PATH = "models/best.pt"

CONF_THRESH = 0.25
IOU_THRESH = 0.4

# Extract safe filename
video_name = os.path.splitext(os.path.basename(VIDEO_PATH))[0]

CSV_OUTPUT = f"annotations/output_{video_name}.csv"
VIDEO_OUTPUT = f"results/trajectory_{video_name}.mp4"
