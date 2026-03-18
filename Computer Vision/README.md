# Overview
The computer vision will be processed on a raspberry pi 4. The largest detected object will be written to a file called .detected_obj.

## CV Instructions
Requirements:
- Python3+
- Camera Plugged in

Upon first install, run:
```
sudo ./init
```
Ensure you're running the init.sh script as a sudo user.

Once you run the init.sh script, run the start.sh script to run object detection, do:
```
./start.sh
```
