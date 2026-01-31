# pip install ultralytics opencv-python

from ultralytics import YOLO
import cv2
import time

# ===== CONFIG =====
SHOW_WINDOW = True
OUTPUT_FILE = ".detected_obj"
# ==================

model = YOLO("yolo26n.pt")

# open camera (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    input("Press enter to continue")
    raise RuntimeError()

print(f"SHOW_WINDOW is set to {SHOW_WINDOW}")
print(f"Output written to {OUTPUT_FILE}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    r = results[0]

    largest_obj = None
    largest_area = 0

    # iterate over detections
    if r.boxes is not None:
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            area = (x2 - x1) * (y2 - y1)

            if area > largest_area:
                largest_area = area
                cls_id = int(box.cls[0])
                class_name = model.names[cls_id]
                largest_obj = (class_name, float(area))

    # write biggest detected object to file
    if largest_obj:
        with open(OUTPUT_FILE, "w") as f:
            f.write(f"Object: {largest_obj[0]}\n")
            f.write(f"Area: {largest_obj[1]:.2f}\n")
            f.write(f"Timestamp: {time.time()}\n")

    # only show window if flag is set
    if SHOW_WINDOW:
        annotated_frame = r.plot()
        cv2.imshow("Object Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
