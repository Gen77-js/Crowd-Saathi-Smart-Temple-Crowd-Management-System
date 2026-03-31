from ultralytics import YOLO
import cv2
from tracker import CentroidTracker

model = YOLO("models/yolov8n.pt")
tracker = CentroidTracker()

def detect_and_track(frame):
    results = model(frame, conf=0.4, classes=[0])
    rects = []

    for r in results:
        if r.boxes is not None:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                rects.append((x1, y1, x2, y2))

    objects = tracker.update(rects)

    for objectID, centroid in objects.items():
        cv2.putText(frame, f"ID {objectID}",
                    (centroid[0]-10, centroid[1]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0,255,0), 2)
        cv2.circle(frame, tuple(centroid), 4, (0,255,0), -1)

    return frame, objects
