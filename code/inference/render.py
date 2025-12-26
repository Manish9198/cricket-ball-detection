# render.py
import cv2

def render(video_path, output_path, tracks):
    cap = cv2.VideoCapture(video_path)
    w,h = int(cap.get(3)), int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (w,h)
    )

    idx = 0
    trajectory = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if tracks[idx][3] == 1:
            x,y = int(tracks[idx][1]), int(tracks[idx][2])
            trajectory.append((x,y))
            cv2.circle(frame,(x,y),5,(0,0,255),-1)

        for i in range(1,len(trajectory)):
            cv2.line(frame, trajectory[i-1], trajectory[i], (255,0,0),2)

        out.write(frame)
        idx += 1

    cap.release()
    out.release()
