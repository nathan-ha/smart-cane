# Overview
The computer vision will be processed on a raspberry pi 4. The largest detected object will be written to a file called .detected_obj.

## CV Instructions
Requirements:
- Python3+
- Camera Plugged in

Upon first install, run:
```
pip install ultralytics opencv-python
```

If you get an error, run
```
python3 -m venv .venv
source .venv/bin/activate
```

To run object detection, do:
```
./object-recognition.py
```
