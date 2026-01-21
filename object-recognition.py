# pip install ultralytics opencv-python

from ultralytics import YOLO
import cv2
import time

# model
model = YOLO("yolov8n.pt")

# open camera (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Camera not working")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Object Detection", annotated_frame)

    print("Hold 'q' on the window to exit.")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # time.sleep(0.5)

cap.release()
cv2.destroyAllWindows()
