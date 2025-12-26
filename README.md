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
├── results/             # Processed videos with trajectory overlay
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

Linux / macOS:
```bash
source venv/bin/activate
```

Windows:
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
- Supported format: `.mp4` (recommended for reproducibility)

Place the input video inside:

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

To run the full detection, tracking, and visualization pipeline:

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

- A colored dot indicates the current ball centroid
- A polyline shows the accumulated ball trajectory

---

## Model Details

- Detector: YOLOv8 (single-class: ball)
- Tracker: Kalman Filter with a constant velocity motion model

### Rationale

- YOLOv8 provides fast and accurate small-object detection
- Kalman filtering smooths frame-wise detection noise
- The approach is simple, interpretable, and aligned with industry practice

---

## Model Used in This Submission

For this submission, a **pre-trained YOLOv8 model (`best.pt`)** is used for cricket ball detection.

The model was trained externally on a cricket ball detection dataset and is included in the `models/` directory to ensure **full reproducibility of inference results**.

The training script is provided for completeness and future retraining, but **model training itself was not performed as part of this submission**.

---

## Handling Occlusions and Missed Detections

- The system does not hallucinate detections
- When the ball is not detected in a frame:
  - Coordinates are set to `-1, -1`
  - Visibility flag is set to `0`
- The Kalman filter maintains internal state to ensure smooth trajectory continuity

---

## Training the Model (Optional)

A training script is provided to allow retraining or fine-tuning of the detector:

```bash
python code/train/train_yolo.py
```

This step is optional and not required to reproduce the results in this repository, as a trained model (`models/best.pt`) is already provided.

---

## Common Issues and Fixes

False positives (e.g., shoes or gloves):
- Increase detection confidence threshold
- Use a domain-specific cricket ball dataset for training

MOV file issues on Windows:
- Convert `.mov` videos to `.mp4` using FFmpeg:
```bash
ffmpeg -i input.mov -c:v libx264 input/video.mp4
```

Output file errors:
- Output filenames are sanitized to avoid invalid filesystem paths

---

## Reproducibility

The complete pipeline can be reproduced using:

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
- Issues encountered and fixes applied
- Performance improvements and example outputs

---

## Conclusion

This project presents a robust, reproducible, and industry-aligned solution for cricket ball detection and tracking from a single static camera. By combining deep learning–based detection with classical filtering, the system achieves stable tracking performance while remaining interpretable and easy to reproduce.
