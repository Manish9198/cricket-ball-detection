# Cricket Ball Detection & Tracking (Single Camera)

A complete computer vision pipeline to detect, track, and visualize the trajectory of a cricket ball from a single static camera video.

The system detects the ball centroid per frame, handles occlusions, outputs structured annotations, and generates a processed video with trajectory overlay.

---

## Features

- Per-frame ball centroid detection
- Kalman Filter–based tracking for smooth trajectories
- Frame-wise annotation output (CSV)
- Processed video with centroid and trajectory overlay
- Graceful handling of missed detections and occlusions
- Fully reproducible end-to-end pipeline

---

## Repository Structure

```
cricket-ball-detection/
│
├── code/
│   ├── train/           # Model training scripts
│   ├── inference/       # Detection, tracking, rendering
│   ├── utils/           # Kalman filter, config, helpers
│   └── main.py          # End-to-end pipeline
│
├── annotations/         # Per-frame CSV outputs
├── results/             # Processed videos with trajectory
├── models/              # Trained YOLO model (.pt)
├── input/               # Input videos
│
├── README.md
├── requirements.txt
└── report.pdf
```

---

## Setup Instructions

### 1. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

Linux / macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Dependencies

- Python 3.8+
- ultralytics (YOLOv8)
- OpenCV
- NumPy
- Pandas
- FilterPy
- PyTorch

All dependencies are listed in `requirements.txt`.

---

## Input Format

- Single cricket video from a static camera
- Supported formats: `.mp4` (recommended)

Place input video inside:

```
input/
└── video.mp4
```

Update the video path in:

```
code/utils/config.py
```

---

## Running the Pipeline

```bash
python code/main.py
```

---

## Outputs

### 1. Annotation File (CSV)

Generated at:

```
annotations/output_<video_name>.csv
```

Format:

```csv
frame,x,y,visible
0,512.3,298.1,1
1,518.7,305.4,1
2,-1,-1,0
```

- `x, y` represent the ball centroid
- `visible = 1` indicates the ball is detected
- `visible = 0` indicates the ball is not visible or occluded

---

### 2. Processed Video

Generated at:

```
results/trajectory_<video_name>.mp4
```

- Red dot indicates the current ball centroid
- Blue line indicates the ball trajectory

---

## Model Details

- Detector: YOLOv8 (single-class: ball)
- Tracker: Kalman Filter (constant velocity model)

### Why This Approach?

- YOLO provides fast and accurate small-object detection
- Kalman filter smooths noisy detections and handles occlusions
- Simple, interpretable, and industry-aligned solution

---

## Handling Occlusions and Missed Detections

- No hallucinated detections are produced
- When the ball is not detected:
  - Coordinates are set to `-1, -1`
  - Visibility flag is set to `0`
- Kalman filter maintains internal state for smooth trajectory prediction

---

## Training the Model (Optional)

To train a custom cricket ball detector:

```bash
python code/train/train_yolo.py
```

After training, move the best model:

```bash
cp runs/detect/cricket_ball/weights/best.pt models/ball_yolo.pt
```

Update `MODEL_PATH` in `config.py` accordingly.

---

## Common Issues and Fixes

False Positives (Shoes, Gloves):

- Increase confidence threshold
- Train with a domain-specific cricket ball dataset

MOV File Issues on Windows:
Convert `.mov` to `.mp4` using FFmpeg:

```bash
ffmpeg -i input.mov -c:v libx264 input/video.mp4
```

Output File Errors:

- Output filenames are auto-sanitized to avoid invalid paths

---

## Reproducibility

The entire pipeline is reproducible using:

```bash
pip install -r requirements.txt
python code/main.py
```

---

## Report

A detailed technical report is provided in `report.pdf`, covering:

- Modelling decisions
- Fallback logic
- Assumptions
- Issues faced and fixes applied
- Performance improvements and example outputs

---

## Conclusion

This project demonstrates a robust, reproducible, and industry-aligned cricket ball tracking system using deep learning for detection and classical filtering for tracking. The pipeline is modular, interpretable, and suitable for real-world sports analytics scenarios.
