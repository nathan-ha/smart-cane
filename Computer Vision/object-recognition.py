from ultralytics import YOLO
from picamera2 import Picamera2
import cv2
import pyttsx3

SHOW_WINDOW = False
tts = pyttsx3.init()

model = YOLO("yolo26n.pt")

# open camera (0 = default camera)
picam2 = Picamera2()

config = picam2.create_preview_configuration(main={"format": "RGB888"})

picam2.configure(config)

picam2.start()

print(f"SHOW_WINDOW is set to {SHOW_WINDOW}")

while True:
    frame = picam2.capture_array()

    if frame is None:
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

    # speak largest object
    if largest_obj:
        tts.say(largest_obj[0])
        tts.runAndWait()
        print(f"DEBUG {largest_obj[0]}")

    # only show window if flag is set
    if SHOW_WINDOW:
        annotated_frame = r.plot()
        cv2.imshow("Object Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

picam2.stop()
cv2.destroyAllWindows()
