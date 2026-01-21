# pip install ultralytics opencv-python

from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Camera not working")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("balls", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    print("Hold 'q' on the window to exit.")

cap.release()
cv2.destroyAllWindows()
