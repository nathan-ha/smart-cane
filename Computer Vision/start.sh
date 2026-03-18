#!/bin/bash

WRKDIR="/home/opencv/smart-cane/Computer Vision"


cd "${WRKDIR}"

if [ ! -d "${WRKDIR}/venv" ]; then
    echo "Virtual environment doesn't exist! Creating environment..."
    python3 -m venv --system-site-packages venv
    source venv/bin/activate
    pip install -r requirements.txt --no-cache-dir --only-binary :all:
    deactivate
fi
 
source venv/bin/activate

python3 object-recognition.py
