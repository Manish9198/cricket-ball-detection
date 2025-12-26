# Cricket Ball Detection & Tracking (Single Camera)

This repository contains a complete computer vision pipeline to detect, track, and visualize the trajectory of a cricket ball from a single static camera video.

The system detects the ball centroid in each frame where it is visible, handles missed detections and occlusions, outputs structured per-frame annotations, and generates a processed video with trajectory overlay.

---

## Features

- Per-frame ball centroid detection
- Kalman Filter–based tracking for smooth trajectories
- Frame-wise annotation output (CSV format)
- Processed video with centroid and trajectory overlay
- Graceful handling of occlusions and missed detections
- Fully reproducible end-to-end inference pipeline

---

## Repository Structure

cricket-ball-detection/
├── code/
│   ├── train/           # Model training scripts
│   ├── inference/       # Detection, tracking, rendering
│   ├── utils/           # Kalman filter, config, helpers
│   └── main.py          # End-to-end pipeline
├── annotations/         # Per-frame CSV outputs
├── results/             # Processed videos with trajectory overlay
├── models/              # Trained YOLO model (.pt)
├── input/               # Input videos
├── README.md
├── requirements.txt
└── report.pdf

---

## System Requirements

- Python 3.11 (supported and recommended)
- Windows / Linux / macOS
- Git

Note: This project is tested and supported on Python 3.11 for stable PyTorch and Ultralytics compatibility.

---

## Clone the Repository

git clone https://github.com/Manish9198/cricket-ball-detection.git  
cd cricket-ball-detection

---

## Install Dependencies (No Virtual Environment)

This project runs directly using system Python (Python 3.11).

pip install -r requirements.txt

---

## Dependencies

- Python 3.11
- ultralytics (YOLOv8)
- OpenCV
- NumPy
- Pandas
- FilterPy
- PyTorch

All dependencies are listed in requirements.txt.

---

## Input Format

- Single cricket video from a static camera
- Supported format: .mp4

Place the input video inside:

input/video.mp4

Update the video path in:

code/utils/config.py

Example:

VIDEO_PATH = "input/video.mp4"

---

## Running the Pipeline

python code/main.py

This performs:
- YOLOv8-based ball detection
- Kalman Filter–based tracking
- CSV annotation generation
- Trajectory video rendering

---

## Outputs

Annotation CSV:
annotations/output_<video_name>.csv

CSV format:
frame,x,y,visible
0,512.3,298.1,1
1,518.7,305.4,1
2,-1,-1,0

Processed video:
results/trajectory_<video_name>.mp4

---

## Model Details

- Detector: YOLOv8 (single-class: cricket ball)
- Tracker: Kalman Filter with constant velocity motion model

Rationale:
- YOLOv8 provides fast and accurate small-object detection
- Kalman filtering smooths frame-wise noise
- Simple, interpretable, industry-aligned approach

---

## Model Used

A pre-trained YOLOv8 model (best.pt) is included in the models directory.

- Trained externally on a cricket ball dataset
- Included to ensure full reproducibility
- Training is not required to run inference

---

## Handling Occlusions and Missed Detections

- No hallucinated detections
- When the ball is not detected:
  - Coordinates set to -1, -1
  - Visibility set to 0
- Kalman filter maintains smooth trajectory continuity

---

## Training (Optional)

python code/train/train_yolo.py

Training is optional and not required to reproduce results.

---

## Common Issues

False positives:
- Increase detection confidence threshold
- Use a domain-specific cricket ball dataset

MOV files on Windows:
ffmpeg -i input.mov -c:v libx264 input/video.mp4

Output file issues:
- Filenames are sanitized to avoid invalid paths

---

## Reproducibility

pip install -r requirements.txt  
python code/main.py

---

## Report

See report.pdf for:
- Modelling decisions
- Fallback logic
- Assumptions
- Issues and fixes
- Performance analysis

---

## Conclusion

This project provides a robust and reproducible cricket ball detection and tracking pipeline using Python 3.11, YOLOv8, and Kalman filtering, suitable for industry-aligned computer vision workflows.
